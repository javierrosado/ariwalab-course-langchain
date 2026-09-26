# Inventario global y mapa pedagógico

## Alcance verificado

Commit GitHub main `27c24090f1662f9473b673d2020e7bffee04490b`: 407 archivos en cuatro módulos principales; preparación S0, once sesiones lectivas S1–S11 y bonus Foundry. También hay `comun/`, simulador, datasets, laboratorios por cuatro tracks, soluciones, guías docentes y archivos de decisiones. El catálogo visual usa los README de sesión, el plan, los laboratorios incrementales, las decisiones y la definición de los cuatro tracks.

| Etapa | Sesiones / laboratorio | Aprende y practica | Requiere | Próximo uso |
|---|---|---|---|---|
| Preparación | S0 | Tokens, variación, embeddings, alucinación; entorno y cuentas | Python, REST | S1–S2 y RAG |
| Módulo 1 | S1–S3 / L1–L3 | Agente, prompts, contrato tipado, primera tool externa | S0 | Tools, estado y seguridad |
| Módulo 2 | S4–S7 / L4–L7 | Catálogo de cuatro tools, MCP, memoria, RAG, guardrails y pruebas | S1–S3 | Operación y evaluación |
| Módulo 3 | S8–S11 / L8–L11 | API desplegada, Langfuse, evaluación, demo final | S1–S7 | Bonus y operación posterior |
| Módulo 4 | Bonus opcional / L12 | Switch de proveedor y hosted agent en Foundry | Agente L11 + Azure | Curso 2 |

## Dependencias y cautelas

- S2 introduce el estado sin atribuir memoria persistente al modelo; S5 implementa estado conversacional mediante thread_id.
- S3 separa tool call y ejecución; S4 introduce elección entre cuatro herramientas y MCP.
- S5 utiliza Qdrant Cloud y un modelo base compartido; no representar modelos afinados por industria.
- S6 exige guardrails en código; S9 aplica sanitización también a trazas; S10 verifica sobre golden dataset.
- Foundry es bonus asíncrono tras S11. El switch de proveedor conserva el código del agente, pero `host/main.py` advierte que ciertos guardrails no portan sin cambios al hosted agent.

## Inconsistencias editoriales detectadas

- `README.md` raíz y `PLAN-CURRICULAR.md` siguen anunciando 12 sesiones/72 h, mientras D07 y D17 y las carpetas de sesión concretan 11 lectivas más bonus asíncrono. Evitar representar el bonus como sesión lectiva 12.
- `README.md` raíz dice que las carpetas están vacías; el árbol contiene materiales, código y soluciones.
- El bonus dice «sin tocar una línea del código del agente» para cambiar el proveedor, pero documenta una excepción concreta al envolverlo como hosted agent: guardrails del L6 como función Python requieren adaptación.

## Recomendaciones docentes

Presentar S1, S3, S5, S6, S9 y S11 como evoluciones del mismo agente. Proyectar cada PNG con sus notas, ejecutar inmediatamente la demo o lab asociado y pedir al alumno que identifique qué paso observaría en una traza o evaluaría con un test.
