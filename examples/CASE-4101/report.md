# DossierCheck

Expediente: CASE-4101
Referencia esperada: CASE-4101
Estado: **READY_FOR_HUMAN_REVIEW**

Este resultado sólo evalúa consistencia conforme al esquema; no acredita autenticidad, veracidad, validez jurídica ni aprobación.

## Documentos

| Archivo | Tipo | Páginas | SHA-256 | Incidencia |
|---|---|---:|---|---|
| application.pdf | application | 2 | `91c86b4a0794f681624d6785308af134da50d27712b0bf36bf0972902f07d1d5` | - |
| certificate.pdf | certificate | 1 | `2f0f3b4fdfacb4758313bc982eb6c901e4b3168635c4648d4ef0e2e2e94909f6` | - |
| contract.pdf | contract | 1 | `1c35b3bce03a2e2ac61c939a2d40199c2097b4f93bc55f303b8f26beb08c3e66` | - |

## Comprobaciones

| Regla | Resultado | Motivo |
|---|---|---|
| case_anchor:application.pdf | PASS | Matches external case reference |
| case_anchor:certificate.pdf | PASS | Matches external case reference |
| case_anchor:contract.pdf | PASS | Matches external case reference |
| application_present | PASS | Document count is 1; expected exactly 1 |
| contract_present | PASS | Document count is 1; expected exactly 1 |
| certificate_present | PASS | Document count is 1; expected exactly 1 |
| same_case_ref | PASS | All configured values match |
| same_applicant_id | PASS | All configured values match |
| same_applicant_name | PASS | All configured values match |
| same_total_amount | PASS | All configured values match |
| guarantee_if_advance | NOT_APPLICABLE | Condition is verifiably false |

## Evidencias

- **case_ref**, application.pdf, página 1: «Case Reference: CASE-4101» → `CASE-4101` (aceptada: sí).
- **case_ref**, certificate.pdf, página 1: «Case Reference: CASE-4101» → `CASE-4101` (aceptada: sí).
- **case_ref**, contract.pdf, página 1: «Case Reference: CASE-4101» → `CASE-4101` (aceptada: sí).
- **applicant_id**, application.pdf, página 1: «Applicant ID: ID-4101» → `ID-4101` (aceptada: sí).
- **applicant_id**, contract.pdf, página 1: «Applicant ID: ID-4101» → `ID-4101` (aceptada: sí).
- **applicant_id**, certificate.pdf, página 1: «Applicant ID: ID-4101» → `ID-4101` (aceptada: sí).
- **applicant_name**, application.pdf, página 1: «Applicant Name: Iria Zorvanto Prueba» → `iria zorvanto prueba` (aceptada: sí).
- **applicant_name**, contract.pdf, página 1: «Applicant Name: Iria Zorvanto Prueba» → `iria zorvanto prueba` (aceptada: sí).
- **applicant_name**, certificate.pdf, página 1: «Applicant Name: Iria Zorvanto Prueba» → `iria zorvanto prueba` (aceptada: sí).
- **total_amount**, application.pdf, página 2: «Total Amount: 186.450,00 EUR» → `186450.00 EUR` (aceptada: sí).
- **total_amount**, contract.pdf, página 1: «Total Amount: 186.450,00 EUR» → `186450.00 EUR` (aceptada: sí).
- **advance_payment**, application.pdf, página 2: «Advance Payment: 0,00 EUR» → `0.00 EUR` (aceptada: sí).

La decisión final corresponde siempre a una persona.
