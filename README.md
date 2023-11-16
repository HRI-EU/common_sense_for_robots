<div align="center">

  <a href="">[![Static Badge](https://img.shields.io/badge/arXiv-2311.08412-B31B1B?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2311.08412)</a>

</div>

<h1 align="center">
  🧠🤖 common_sense_for_robots
</h1>

<div align="center">
  Supplemental material for the paper "Exploring Large Language Models as a Source of Common-Sense Knowledge for Robots"
</div>


## Contents
* `action_patterns_ground_truth.json` - ground truth for action patterns
* `prompts.py` - prompts used for extractings parts of action patterns and entire ones from LLMs
* `action_pattern_ontology_creation.py` - minimal script for setting up a TBox for action patterns and populating it with action patterns, e.g., extracted from LLMs
* `action_patterns_example.json` - example input for the ontology creation


## Citation
For scientific use, please cite as follows:
```
@inproceedings{ocker2023commonsense,
    author = {Ocker, Felix and Deigmöller, Jörg and Eggert, Julian},
    booktitle = {ISWC 2023 Posters and Demos: 22nd International Semantic Web Conference},
    title = {Exploring Large Language Models as a Source of Common-Sense Knowledge for Robots},
    year = {2023},
    publisher={CEUR-WS}
}
```
