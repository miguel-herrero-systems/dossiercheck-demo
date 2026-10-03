# Conceptual model and trust boundary

The useful unit is a **defined dossier**, not an arbitrary folder of files. A case schema names expected document types, fields, labels and simple comparison rules. A separately supplied expected case reference anchors the membership of the documents; a folder name does not.

```text
Configured case + source PDFs
          ↓
Inventory and SHA-256 of each file
          ↓
PDF text extraction → candidate values
          ↓
Evidence verification (document, page, quote, configured anchor)
          ↓
Normalization → deterministic rule engine
          ↓
manifest.json → report.md → human review
```

Extraction, evidence acceptance and validation are separate decisions. A model may propose a candidate in `extract-and-check`, but it cannot grant `PASS`. A `deterministic-test` can supply prefixed candidates and evidence without any model; both modes converge on the same rule engine and manifest contract.

**Invariant:** No rule may return `PASS` using a field whose evidence has not been accepted. Missing, duplicated, unreadable or ambiguous material must remain visible as a failure or a request for review, according to the configured rule and case state. `READY_FOR_HUMAN_REVIEW` is not automatic approval.

The three committed cases are **recorded output snapshots** from a private 0.1.2 candidate, shown alongside their fictional source PDFs. This repository does not ship that candidate's implementation. `scripts/inspect_samples.py` only verifies that the published PDFs match the hashes in the recorded manifests. It does not re-run candidate extraction, verify quote/page grounding, or recalculate rule outcomes.

The proposed workflow is valuable where the destination form and supporting document set are known in advance. One possible future application is preparing an official interactive form from supporting PDFs, then having a person reconcile and complete it. That particular administrative procedure has **not** been built or validated; this repository does not claim otherwise.
