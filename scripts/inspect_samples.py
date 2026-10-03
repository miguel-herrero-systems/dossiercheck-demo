"""Inspect published synthetic snapshots; this is not the DossierCheck engine."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1] / "examples"
EXPECTED = {
    "CASE-4101": "READY_FOR_HUMAN_REVIEW",
    "CASE-4103": "INCONSISTENT",
    "CASE-4107": "REVIEW_REQUIRED",
}


def main() -> int:
    problems: list[str] = []
    for case_id, expected_status in EXPECTED.items():
        case_dir = ROOT / case_id
        manifest = json.loads((case_dir / "result-manifest.json").read_text(encoding="utf-8"))
        if manifest.get("case_id") != case_id:
            problems.append(f"{case_id}: case ID differs from the folder name")
        if manifest.get("status") != expected_status:
            problems.append(f"{case_id}: recorded status differs from the published example")

        documents = manifest.get("documents", [])
        names = {document.get("filename") for document in documents}
        if names != {"application.pdf", "contract.pdf", "certificate.pdf"}:
            problems.append(f"{case_id}: unexpected document inventory")

        for document in documents:
            filename = document.get("filename")
            if filename not in {"application.pdf", "contract.pdf", "certificate.pdf"}:
                continue
            actual_sha256 = hashlib.sha256((case_dir / filename).read_bytes()).hexdigest()
            if actual_sha256 != document.get("sha256"):
                problems.append(f"{case_id}/{filename}: SHA-256 does not match the manifest")

        counts = {status: 0 for status in ("PASS", "FAIL", "REVIEW_REQUIRED", "NOT_APPLICABLE")}
        for check in manifest.get("checks", []):
            status = check.get("status")
            if status in counts:
                counts[status] += 1
        print(f"{case_id}: {expected_status} · " + ", ".join(f"{count} {status}" for status, count in counts.items() if count))

    if problems:
        for problem in problems:
            print(f"ERROR: {problem}")
        return 1
    print("Published PDF bytes match their recorded SHA-256 hashes. Rule outcomes were not recalculated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
