# Market Intelligence Research Agent | Udacity + AWS QuickSuite

**Portfolio evidence — Nordic EV Charging Operations Software (2027 pilot decision)**

**Question:** If a small B2B software team considers a Nordic charging-operations pilot in 2027, where should it validate demand first — Denmark, Sweden, Finland or Norway?

During Udacity's **AWS Agentic AI Business Professional** project (3 Nov 2026), I used Amazon QuickSuite Quick Research, a dataset-backed comparison, source checking, decision-oriented synthesis and a separate insight reliability evaluation. The deliverable was a leadership brief with confidence levels, assumptions and next actions.

### Business recommendation
**Conditional pilot discovery in Denmark, with Sweden as a strong alternative.** Sweden scored 21/25 versus Denmark 20/25 in the course's assessment; Denmark-first was a *strategic judgement*, not an empirical finding or validated business opportunity. Before building a product, interview 10–15 charge-point operators, verify pricing and switching costs, and validate demand.

### Evidence and analysis
- [Executive brief](docs/executive-brief.md): five insights, recommendations and what is not established.
- [Reliability register](docs/reliability-register.md): confidence and explicit data-definition conflicts.
- [Selected historical indicators](data/iea-selected-2020-2023.csv): transcribed from the course's IEA/Kaggle analysis (not the full IEA dataset).
- [Reproducible checks](analysis/check_indicators.py) and [tests](tests/test_indicators.py): post-course independent verification of selected arithmetic.
- [Evidence checklist](docs/evidence-checklist.md): which native QuickSuite screenshots and exports need attaching.

### Quick checks
```bash
python -m unittest discover -s tests -v
python analysis/check_indicators.py data/iea-selected-2020-2023.csv
```

**Boundaries:** The historical dataset ends in 2023. 2027 market entry is a forward-looking scenario. Secondary research alone does not prove commercial viability. Claims about EU law should be checked against the regulation itself; AFIR does not mandate OCPP 2.0.1 by name. A source discrepancy concerning Denmark's 2023 EV sales share (36% versus 46%, likely different BEV/total EV definitions) is unresolved.

The applicant completed the course work; this repository packages evidence and an additional reproducible skills demonstration. **Do not mistake Udacity training for an AWS-issued certification.**
