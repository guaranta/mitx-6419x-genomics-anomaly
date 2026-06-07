# mitx-6419x-genomics-anomaly

**MITx 6.419x — Data Analysis: Statistical Modeling and Computation in Applications**

Modelagem estatística em dados de alta dimensão: do genoma aos logs de infraestrutura (NOC/SOC).

| Módulo | Conteúdo | Comando |
|--------|----------|---------|
| `count-models/` | PMF binomial → contagem de incidentes | `python count-models/run.py` |
| `pca-anomaly/` | PCA + k-means → detecção de anomalias | `python pca-anomaly/run.py` |
| `regression/` | Correlação e regressão de KPIs | `python regression/run.py` |

## Setup

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python count-models/run.py
```

## Origem acadêmica

Inspirado no curso **6.419x** (exercise12 binomial, slides genomics/correlation). Pipeline reescrito para observabilidade e SOC.

## Portfólio

- [Portfolio AI Engineer / CTO](https://portfolio-ai-cto-guaranta.netlify.app)
- [Ponte genômica → observabilidade](docs/portfolio-link.md)

## Autor

**Guarantã Almeida** — [github.com/guaranta](https://github.com/guaranta)
