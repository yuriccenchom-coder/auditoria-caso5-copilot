# Auditoría Ética y Forense: Caso GitHub Copilot y Licencias Open Source

**Materia:** Ética en Tecnologías de la Información / Computación Científica  
**Caso de Estudio:** Caso 5 — Plagio Algorítmico y Reutilización no Autorizada de Código Abierto (*GitHub Copilot / OpenAI Codex*)  
**Integrantes:** [Nombres de los integrantes del equipo]  

---

## 1. Contexto Técnico
El objeto de la auditoría es el sistema de generación de código **GitHub Copilot**, soportado por modelos de lenguaje autoregresivos de gran escala (LLMs) como **OpenAI Codex** (basado en la arquitectura Transformer).

* **Parámetros del Dataset de Entrenamiento:** El corpus de datos estuvo compuesto por terabytes de texto fuente extraídos de repositorios públicos en GitHub. Este dataset incluyó código bajo licencias permisivas (MIT, Apache 2.0) y licencias recíprocas o copyleft (GNU GPL v2/v3).
* **Mecanismo Estadístico del Algoritmo:** El modelo tokeniza las secuencias de código $X = (x_1, x_2, \dots, x_n)$ para estimar la probabilidad condicional de ocurrencia del siguiente token mediante la función de distribución:

$$P(x_t \mid x_1, x_2, \dots, x_{t-1}) = \text{softmax}(W \cdot h_t)$$

Donde $h_t$ representa el estado oculto del Transformer. El modelo utiliza la atención probabilística para predecir y reconstruir bloques enteros de código basándose en el contexto del programador.

---

## 2. Diagnóstico de la Infracción Ética
**Clasificación Formal de la Falta:** Plagio Algorítmico, Omisión Sistemática de Atribución e Infracción de Licencias de Software (*Mala Conducta en Computación Científica*).

* **Violación de Normativa MIT (Atribución Obligatoria):** La licencia MIT exige formalmente que cualquier reproducción parcial o total del código incluya el aviso original de *copyright*.
* **Violación de Normativa GPL (Reciprocidad / Heredabilidad):** Exige que toda obra derivada mantenga el carácter abierto (*Copyleft*) y se distribuya bajo los mismos términos.
* **Fallo Ético Interno:** El procesamiento del modelo remueve los metadatos de autoría y los encabezados de licencias (*Copyright Management Information - CMI*) durante la etapa de tokenización. Esto genera un "lavado de derechos de autor" (*copyright laundering*), entregando respuestas como si fueran contenido libre de restricciones o de autoría propia de la herramienta.

---

## 3. Evidencia Forense Cuantitativa
Para evidenciar objetivamente la falta técnica, la auditoría analiza las métricas de memorización no estocástica y duplicación literal (*verbatim extraction*):

* **Métrica de Similitud Jaccard:** Se evalúa la intersección de tokens entre la salida del modelo $G$ y el repositorio original $D$:

$$J(G, D) = \frac{|G \cap D|}{|G \cup D|}$$

* **Fallo Detectado (Porcentaje de Salida Literal):** Se halló que entre un **1% y 3%** de las salidas generadas por el modelo no correspondían a generalizaciones estadísticas, sino a memorización directa (secuencias continuas idénticas de más de **150 caracteres consecutivos**).
* **Caso Testigo (Raíz Cuadrada Inversa de Quake III):** Al ingresar como *prompt* las primeras líneas de la función de renderizado, el modelo devolvió la implementación entera *verbatim*, habiendo **mutilado la cabecera de la licencia GPL** de Id Software que regía legalmente dicha función.

---

## 4. Consecuencias Reales e Impacto
* **Contaminación de Software Comercial e Investigación:** La integración de código memorizado bajo licencia GPL en software propietario o proyectos de investigación científica expone a las organizaciones a litigios legales por ruptura de licencias.
* **Apropiación Injusta de Bienes Comunes (*Commons*):** Comercialización de un modelo de suscripción pagado por parte de corporaciones ($10–$20 USD/mes) utilizando como insumo primario el trabajo no remunerado de millones de desarrolladores de software libre.
* **Riesgos de Seguridad (*CVEs*):** El modelo replica fragmentos de código que contienen vulnerabilidades de seguridad conocidas o parches descontinuados, reinsertándolos en entornos de producción actuales.

---

## 5. Solución Metodológica bajo Buenas Prácticas Científicas (BPC)
* **Trazabilidad y Filtrado en el Data Pipeline:** Exclusión automatizada de código con licencias restrictivas (GPL/AGPL) en el dataset de entrenamiento y retención de metadatos mediante *vector embeddings*.
* **Mecanismos de Inferencia y Verificación (Filtro Anti-Plagio):** Verificación por similitud en tiempo real (métrica de MinHash / Levenshtein con umbral $\theta > 0.80$) para bloquear o citar automáticamente la fuente original.
* **Modelos Éticos (Open Benchmarks / Preregistro):** Adopción de la norma de publicación *Data Sheets for Datasets* y mecanismos de *Opt-In*.
