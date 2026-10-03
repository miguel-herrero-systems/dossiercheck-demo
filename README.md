# DossierCheck — synthetic public demonstration

DossierCheck is a configurable workflow for checking consistency across a known set of PDF documents. It is designed to make discrepancies and their source evidence visible **before a person makes a decision**. It does not establish that a document is authentic, that a statement is true, or that a dossier has legal approval.

This repository is a **public conceptual showcase**, not the DossierCheck engine, an installable plugin, a document-upload service, or a promise that arbitrary PDFs can be checked. It contains three fictional PDF dossiers and the recorded results produced previously by the private DossierCheck 0.1.2 candidate. Opening the files here does not run AI or re-run the checks.

- [Explore the live English demonstration](https://hrevn.com/en/dossiercheck/)
- [How the model works](docs/model.md)

## Three inspectable cases

| Case | What to inspect | Recorded outcome |
| --- | --- | --- |
| [`CASE-4101`](examples/CASE-4101/) | The configured values agree across the PDFs. | `READY_FOR_HUMAN_REVIEW` |
| [`CASE-4103`](examples/CASE-4103/) | One amount differs across documents. | `INCONSISTENT` |
| [`CASE-4107`](examples/CASE-4107/) | A source contains competing values for the same configured field. | `REVIEW_REQUIRED` |

Each case includes `application.pdf`, `contract.pdf`, `certificate.pdf`, a `result-manifest.json`, and a human-readable `report.md`. All names, references, amounts and documents are fictional. The PDF files and recorded results are the same bytes used by the public HREVN demonstration.

Run `python3 scripts/inspect_samples.py` to check that the included PDFs match the SHA-256 hashes recorded in their manifests and to display the recorded status of each case. This script verifies the **published sample files**, not the correctness of DossierCheck's extraction or rule decisions.

## The model in one line

**Extract candidate values → verify their source evidence → normalize → apply configured rules → produce a manifest → send exceptions to human review.**

The central invariant is: **no rule may return `PASS` using a field whose evidence has not been accepted**. A passing consistency check means only that the configured comparison passed on accepted evidence. It is not an approval of the dossier.

## Boundaries

- The current DossierCheck candidate targets configured document types and text-bearing PDFs. It does not provide OCR or general understanding of arbitrary layouts.
- The displayed results are frozen synthetic examples, not a live analysis service.
- A real `extract-and-check` run can use a model to propose candidates; that is separate from the deterministic rule engine. The public examples do not send documents to a model when viewed.
- The underlying private engine, plugin package, API keys, real customer dossiers and generated private outputs are **not** in this repository.
- The three examples are illustrations, not a measured real-world accuracy claim.

No open-source license has been selected for this showcase. For questions about a configured workflow, use the [HREVN contact page](https://hrevn.com/en/contact/).
