# DossierCheck

Expediente: CASE-4107
Referencia esperada: CASE-4107
Estado: **REVIEW_REQUIRED**

Este resultado sólo evalúa consistencia conforme al esquema; no acredita autenticidad, veracidad, validez jurídica ni aprobación.

## Documentos

| Archivo | Tipo | Páginas | SHA-256 | Incidencia |
|---|---|---:|---|---|
| application.pdf | application | 1 | `e36c949dd79b0b461d5193b68169689b1ee465548b5614081c9949f5b1834d8a` | - |
| certificate.pdf | certificate | 1 | `42c2f1f2ffcb5ca70d09197ee882098d46cf6649c396a755578b3698ff8d926f` | - |
| contract.pdf | contract | 3 | `0405146542e757053e985928c1bf764551e863c63589de2cab5b135afbc4e264` | - |

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
| same_total_amount | REVIEW_REQUIRED | contract: Field is missing, ambiguous or unreadable |
| guarantee_if_advance | NOT_APPLICABLE | Condition is verifiably false |

## Evidencias

- **case_ref**, application.pdf, página 1: «Case Reference: CASE-4107» → `CASE-4107` (aceptada: sí).
- **case_ref**, certificate.pdf, página 1: «Case Reference: CASE-4107» → `CASE-4107` (aceptada: sí).
- **case_ref**, contract.pdf, página 1: «Case Reference: CASE-4107» → `CASE-4107` (aceptada: sí).
- **applicant_id**, application.pdf, página 1: «Applicant ID: ID-4107» → `ID-4107` (aceptada: sí).
- **applicant_id**, contract.pdf, página 1: «Applicant ID: ID-4107» → `ID-4107` (aceptada: sí).
- **applicant_id**, certificate.pdf, página 1: «Applicant ID: ID-4107» → `ID-4107` (aceptada: sí).
- **applicant_name**, application.pdf, página 1: «Applicant Name: Teo Brindavel Prueba» → `teo brindavel prueba` (aceptada: sí).
- **applicant_name**, contract.pdf, página 1: «Applicant Name: Teo Brindavel Prueba» → `teo brindavel prueba` (aceptada: sí).
- **applicant_name**, certificate.pdf, página 1: «Applicant Name: Teo Brindavel Prueba» → `teo brindavel prueba` (aceptada: sí).
- **advance_payment**, application.pdf, página 1: «Advance Payment: 0,00 EUR» → `0.00 EUR` (aceptada: sí).

### Candidatos pendientes de revisión

Estos valores tienen evidencia textual aceptada, pero **no son valores validados** ni resuelven la comprobación pendiente.

- **total_amount**: candidato no validado «459.900,00 EUR» — contract.pdf, página 1.
- **total_amount**: candidato no validado «451.000,00 EUR» — contract.pdf, página 3.

La decisión final corresponde siempre a una persona.
