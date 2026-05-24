# Actividad 1 - Asistentes Conversacionales de IA

Objetivo

Explorar y comparar asistentes conversacionales de Inteligencia Artificial para analizar diferencias en precisión, claridad, multimodalidad y utilidad académica.
# Herramientas utilizadas
- ChatGPT
- Gemini
- Grok

# Pregunta realizada
Explica el linaje de datos como si fueras un científico de datos y dibuja un esquema simple.

# Resultados obtenidos
# Comparación de asistentes conversacionales IA

Durante la actividad se compararon las respuestas generadas por ChatGPT, Gemini y Grok sobre el concepto de linaje de datos (Data Lineage).

ChatGPT proporcionó una explicación académica y estructurada, orientada al contexto de Ciencia de Datos, gobierno de datos y Machine Learning. La respuesta destacó por su claridad conceptual y enfoque profesional, siendo especialmente útil para fines universitarios y de documentación técnica.

Gemini presentó una explicación más intuitiva y didáctica, utilizando analogías y lenguaje sencillo para facilitar la comprensión del concepto. La herramienta destacó por su capacidad pedagógica y facilidad para usuarios principiantes.

Por otro lado, Grok mostró una orientación más técnica y especializada en ingeniería de datos moderna. Introdujo conceptos avanzados relacionados con arquitecturas de datos, pipelines ETL/ELT, zonas Bronze/Silver/Gold y herramientas empresariales utilizadas en entornos Big Data.

En términos generales:
- ChatGPT fue el más equilibrado entre claridad y profundidad.
- Gemini fue el más fácil de comprender.
- Grok fue el más técnico y orientado a escenarios reales de ingeniería de datos.

La actividad permitió evidenciar que las herramientas de Inteligencia Artificial poseen fortalezas diferentes dependiendo del contexto de uso, el nivel técnico requerido y el tipo de usuario.

# Ejemplos generados de esquema simple
# ChatGPT
 ┌─────────────────┐
 │ Sistema Origen  │
 │ (Banco / CRM)   │
 └────────┬────────┘
          │
          ▼
 ┌─────────────────┐
 │ Base de Datos   │
 │   SQL / Cloud   │
 └────────┬────────┘
          │
          ▼
 ┌─────────────────┐
 │ Limpieza y ETL  │
 │ Python / Spark  │
 └────────┬────────┘
          │
          ▼
 ┌─────────────────┐
 │ Dataset Final   │
 │ Datos Curados   │
 └────────┬────────┘
          │
          ▼
 ┌─────────────────┐
 │ Modelo IA / BI  │
 │ Dashboard       │
 └─────────────────┘

 # Gemini
 FUENTES DE ORIGEN             ZONA DE PROCESAMIENTO (ETL)             DESTINO FINAL
+------------------+         +-----------------------------+         +-----------------+
|  Base de Datos   | ------> |      Limpieza de Datos      | ------> |    Tablero de   |
|  de Clientes     |         |  (Eliminar nulos, duplicados) |         |     Control     |
+------------------+         +-----------------------------+         +-----------------+
                                            |                                |
+------------------+                        v                                v
|  Logs de la App  | ------> |     Agregación / Cruce      | ------> |    Modelo de    |
|  (Clics/Ventas)  |         | (Unir clientes con compras) |         |  Predicción ML  |
+------------------+         +-----------------------------+         +-----------------+
        ^                                   ^                                ^
        |                                   |                                |
  [Fase: Origen]                  [Fase: Transformación]              [Fase: Consumo]

  # Grok
  <img width="811" height="537" alt="image" src="https://github.com/user-attachments/assets/3ca304cc-6976-44ce-90ad-daa06f16ce23" />


# Reflexión crítica

Las herramientas de Inteligencia Artificial representan un apoyo importante para el aprendizaje y análisis de conceptos complejos en Ciencia de Datos. Sin embargo, cada asistente presenta diferencias significativas en profundidad, claridad, estilo y orientación técnica.

Aunque las respuestas fueron útiles, ninguna herramienta debe considerarse como fuente absoluta de verdad. La validación mediante bibliografía científica, documentación oficial y criterio profesional sigue siendo indispensable.

Asimismo, se evidenció que la IA puede adaptarse a distintos perfiles de usuario:
- Gemini facilita el aprendizaje inicial,
- ChatGPT favorece el análisis académico,
- Grok se enfoca en escenarios técnicos y arquitecturas reales.

Esto demuestra que la selección de herramientas de IA debe alinearse con el objetivo del proyecto y el nivel de especialización requerido.

Frente a una pregunta más moral como la de si es ético clonar mascotas. Las tres no asumen una posición clara, arrojan resultados de posibles beneficios sin embargo la dejan abierta para que sea el usuario desde su posición personal adopte una postura frente al tema.
