# Modelo conceptual y límite de confianza

La unidad de trabajo es un **expediente definido**, no una carpeta arbitraria de archivos. Un esquema configura los tipos de documento esperados, campos, etiquetas y reglas sencillas. La referencia prevista del expediente se proporciona por separado; el nombre de la carpeta no acredita que un documento pertenezca al caso.

```text
Caso configurado + PDF de origen
          ↓
Inventario y SHA-256 de cada archivo
          ↓
Extracción de texto → valores candidatos
          ↓
Verificación de evidencia (documento, página, cita, etiqueta)
          ↓
Normalización → motor de reglas determinista
          ↓
manifest.json → report.md → revisión humana
```

Extracción, aceptación de evidencia y validación son pasos distintos. En `extract-and-check`, un modelo puede proponer un valor, pero no conceder un `PASS`. En `deterministic-test` se proporcionan candidatos y evidencias prefijados sin usar ningún modelo. Los dos modos convergen en el mismo motor de reglas y contrato de manifest.

**Invariante:** ninguna regla puede devolver `PASS` utilizando un campo cuya evidencia no se haya aceptado. Las ausencias, duplicados, documentos ilegibles y ambigüedades deben quedar visibles como fallo o necesidad de revisión, según el caso. `READY_FOR_HUMAN_REVIEW` no equivale a aprobación automática.

Los tres casos publicados son **resultados registrados** de una candidata privada 0.1.2, acompañados de PDF ficticios. Este repositorio no incluye su implementación. `scripts/inspect_samples.py` solo comprueba que los PDF publicados coinciden con los hashes del manifest; no vuelve a extraer candidatos, verificar citas y páginas ni calcular las reglas.

El enfoque puede ser útil cuando se conocen de antemano el formulario de destino y los documentos de apoyo. Una posible aplicación futura sería preparar un formulario oficial interactivo a partir de los PDF aportados, con conciliación y cumplimentación final por una persona. Ese procedimiento administrativo concreto **todavía no está construido ni validado**.
