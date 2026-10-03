# DossierCheck — demostración pública con datos sintéticos

DossierCheck plantea una revisión de **coherencia entre documentos PDF de un expediente conocido y configurado**. Señala discrepancias y muestra de qué página procede la evidencia para que una persona revise el caso. No acredita autenticidad, veracidad, validez jurídica ni aprobación.

Este repositorio es una **presentación conceptual pública**: no contiene el motor privado ni un complemento instalable y no permite subir documentos. Incluye tres expedientes ficticios y resultados que la candidata privada DossierCheck 0.1.2 generó anteriormente. Consultar estos archivos no vuelve a ejecutar IA ni las reglas.

- [Demostración en español](https://hrevn.com/dossiercheck/)
- [Demonstration in English](https://hrevn.com/en/dossiercheck/)
- [Explicación del modelo](docs/model.es.md)

| Caso | Qué muestra | Resultado registrado |
| --- | --- | --- |
| [`CASE-4101`](examples/CASE-4101/) | Coinciden los valores configurados. | `READY_FOR_HUMAN_REVIEW` |
| [`CASE-4103`](examples/CASE-4103/) | Hay una cifra contradictoria. | `INCONSISTENT` |
| [`CASE-4107`](examples/CASE-4107/) | Una fuente contiene dos valores posibles para el mismo campo. | `REVIEW_REQUIRED` |

Cada carpeta tiene tres PDF, el `result-manifest.json` y un `report.md`. Todo es ficticio. Para comprobar que los PDF coinciden con los hashes SHA-256 del manifest y ver los resultados registrados, ejecuta `python3 scripts/inspect_samples.py`. Ese script **no** verifica que el análisis de DossierCheck sea correcto.

La regla central es: **ninguna comprobación puede devolver `PASS` usando un campo cuya evidencia no haya sido aceptada**. Incluso un expediente sin discrepancias requiere revisión humana. La candidata actual trabaja con PDFs con texto y tipos documentales configurados; no incorpora OCR ni comprende cualquier formato arbitrario.

No hay una licencia de código abierto elegida para este repositorio. Para estudiar un procedimiento concreto, [contacta con HREVN](https://hrevn.com/contacto/).
