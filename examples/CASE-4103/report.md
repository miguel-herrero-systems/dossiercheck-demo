# DossierCheck

Expediente: CASE-4103
Referencia esperada: CASE-4103
Estado: **INCONSISTENT**

Este resultado sólo evalúa consistencia conforme al esquema; no acredita autenticidad, veracidad, validez jurídica ni aprobación.

## Documentos

| Archivo | Tipo | Páginas | SHA-256 | Incidencia |
|---|---|---:|---|---|
| application.pdf | application | 1 | `47b1fa9e8b721b522c0564bd725b782d6b7e397217f52052c2e2a6a7ddb02bf6` | - |
| certificate.pdf | certificate | 1 | `6c24b29f2f7f73b86cc56691d7279155501ba4edbcbf954b6e8b277b2a4c5318` | - |
| contract.pdf | contract | 2 | `284c9a07353cb0bd04fa9f8b8cb9da302ecb863e542760b87189a52f75eb73eb` | - |

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
| same_total_amount | FAIL | Values conflict |
| guarantee_if_advance | NOT_APPLICABLE | Condition is verifiably false |

## Evidencias

- **case_ref**, application.pdf, página 1: «Case Reference: CASE-4103» → `CASE-4103` (aceptada: sí).
- **case_ref**, certificate.pdf, página 1: «Case Reference: CASE-4103» → `CASE-4103` (aceptada: sí).
- **case_ref**, contract.pdf, página 1: «Case Reference: CASE-4103» → `CASE-4103` (aceptada: sí).
- **applicant_id**, application.pdf, página 1: «Applicant ID: ID-4103» → `ID-4103` (aceptada: sí).
- **applicant_id**, contract.pdf, página 1: «Applicant ID: ID-4103» → `ID-4103` (aceptada: sí).
- **applicant_id**, certificate.pdf, página 1: «Applicant ID: ID-4103» → `ID-4103` (aceptada: sí).
- **applicant_name**, application.pdf, página 1: «Applicant Name: Nuño Verdalto Ejemplo» → `nuño verdalto ejemplo` (aceptada: sí).
- **applicant_name**, contract.pdf, página 1: «Applicant Name: Nuño Verdalto Ejemplo» → `nuño verdalto ejemplo` (aceptada: sí).
- **applicant_name**, certificate.pdf, página 1: «Applicant Name: Nuño Verdalto Ejemplo» → `nuño verdalto ejemplo` (aceptada: sí).
- **total_amount**, application.pdf, página 1: «Total Amount: 98.750,00 EUR» → `98750.00 EUR` (aceptada: sí).
- **total_amount**, contract.pdf, página 2: «Total Amount: 111.250,00 EUR» → `111250.00 EUR` (aceptada: sí).
- **advance_payment**, application.pdf, página 1: «Advance Payment: 0,00 EUR» → `0.00 EUR` (aceptada: sí).

La decisión final corresponde siempre a una persona.
