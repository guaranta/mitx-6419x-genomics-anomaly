# mitx-6419x-genomics-anomaly

**MITx 6.419x — Data Analysis: Statistical Modeling and Computation in Applications**

Pipeline estatístico de alta dimensão: modelos de contagem (binomial), redução dimensional (PCA) e detecção de anomalias — do contexto genômico ao monitoramento NOC/SOC.

---

## Objetivos de estudo

O 6.419x ensina modelagem estatística em dados de **alta dimensão e baixo sinal** — exatamente o perfil de genômica e, por analogia, de logs de infraestrutura. Este repositório cobre três competências: **(1)** modelar eventos raros com distribuição binomial e definir thresholds de alerta; **(2)** reduzir dimensionalidade com PCA e segmentar comportamento via clustering; **(3)** quantificar relações entre KPIs operacionais com correlação e regressão. O estudante deve entender não só o algoritmo, mas **quando** cada ferramenta é apropriada e como calibrar falsos positivos.

---

## Resultados em destaque

| Módulo | Métrica | Valor |
|--------|---------|-------|
| `count-models` | E[X] para Binomial(63, 0.00203) | **0.128** eventos/janela |
| `pca-anomaly` | Anomalias detectadas (210 amostras, 5%) | **17** pontos flagged |
| `regression` | MTTR → Downtime | **R² = 0.909**, r = 0.954 |

---

## Figuras e interpretação

### Modelo de contagem — incidentes raros (SOC)

![PMF binomial para eventos raros](docs/figures/binomial_pmf.png)

As barras mostram a probabilidade de observar 0, 1, 2… incidentes em uma janela de 63 observações com taxa base de 0.2%. A massa concentra-se em 0 — eventos são **raros por definição**. A linha vermelha marca o threshold de alerta (1 evento, α=1%): cruzar esse limiar merece investigação. No SOC, calibrar esse threshold equilibra **detecção precoce** vs **fadiga de alertas**.

### PCA + detecção de anomalias

![Projeção PCA com pontos anômalos em vermelho](docs/figures/pca_anomaly.png)

Pontos azuis são tráfego normal projetado em 2 componentes principais; vermelhos são anomalias injetadas (média deslocada). O algoritmo usa distância ao centróide k-means no espaço PCA — anomalias **distantes do cluster dominante** são flagged. Em produção, substitua features sintéticas por vetores de logs (frequência de endpoints, bytes, status codes) para detecção em NDR/SIEM.

### Regressão de KPIs operacionais

![Scatter MTTR vs downtime com reta OLS](docs/figures/kpi_regression.png)

Cada ponto é um incidente; o eixo X é tempo de resposta (MTTR) e Y é downtime total. A inclinação ~2.0 significa que cada minuto adicional de MTTR custa ~2 minutos de indisponibilidade acumulada. R²=0.91 indica que MTTR explica a maior parte da variação — argumento forte para investir em **automação SOAR** e runbooks.

---

## Módulos

| Módulo | Técnica | Comando |
|--------|---------|---------|
| `count-models/` | PMF binomial, threshold | `python count-models/run.py` |
| `pca-anomaly/` | PCA + k-means + distância | `python pca-anomaly/run.py` |
| `regression/` | Pearson + OLS | `python regression/run.py` |

## Setup

```bash
pip install -r requirements.txt
python docs/generate_figures.py
```

---

## Aprendizados e aplicação no mercado

A genômica ensina que **sinal raro em alta dimensão** exige modelos de contagem e redução dimensional — o mesmo framework serve para cybersecurity (eventos raros em milhares de features de log) e observabilidade (KPIs correlacionados em NOC). Binomial → alertas SOC; PCA → segmentação de tráfego e detecção de anomalias; regressão → justificar investimento em MTTR. Para CTO, este repositório demonstra que estatística aplicada não é acadêmica: é a base quantitativa de **SLAs, runbooks e priorização de backlog de segurança**.

---

## Autor

**Guarantã Almeida** — [github.com/guaranta](https://github.com/guaranta)
