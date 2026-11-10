# Reliability register / source validation

Research scope: Nordic B2B charge-point management software (CPMS), 2027 scenario.

| Finding | Confidence | Evidence base | Important limitation |
|---|---|---|---|
| AFIR obligations | HIGH (law) | EU Regulation 2023/1804 and later instruments | Do not turn technical preference for OCPP 2.0.1 into legal requirement |
| Market size & fragmentation | MEDIUM | Secondary industry reports in course Quick Research | Single-source numbers cannot support investment modelling |
| Underserved segments | MEDIUM/LOW | Non-Nordic survey/secondary inference | Unvalidated willingness to pay in Nordic countries |
| Denmark / Sweden historical infrastructure growth | HIGH for stated dataset values; source recheck pending | Curated 2020–2023 IEA/Kaggle figures | Not contemporary infrastructure counts |
| Denmark-first recommendation | MEDIUM | Multi-criterion subjective framework | Sweden scored 21/25 vs Denmark 20/25 |
| Consolidation-driven switching | MEDIUM | Company transaction reports + inference | M&A events do not guarantee software migration |

## Outstanding data-definition conflicts
- **Denmark 2023 EV sales share:** 46% combined EV vs 36% purported BEV-only. May reflect different numerator definitions; the difference is **not independently reconciled**.
- **Sweden charger network:** course analysis reported 34,500 chargers in 2023 compared with 62,012 in a secondary mid-2025 source; different dates make direct comparison invalid without source verification.
- **AFIR vs OCPP:** legislation and technical interoperability guidance are different categories of source.

## Explicit method
Collect research question and constraints → inspect historical dataset → use Quick Research for regulatory and competitive signals → cross-check critical numbers → classify evidence as verified fact, forecast or analyst judgement → issue leadership recommendations and risk register.

## Source hierarchy
1. Primary law: [AFIR](https://eur-lex.europa.eu/eli/reg/2023/1804/oj)
2. Quantitative historical data: [IEA Global EV Data](https://www.iea.org/data-and-statistics/data-tools/global-ev-data-explorer) (course working copy was Kaggle-hosted)
3. Official company filings, announcements and national transport/energy agencies for specific current claims
4. Industry consultancies and secondary media for triangulation only

The curated CSV is a transcription of counts cited in the course deliverables, **not** a direct export of raw IEA observations. A raw-dataset validation remains necessary.
