# Diversity Matters: Perceived Inclusion and Discrimination by Brazilian Tech Professionals

This repository contains all the codes, data, ICFs and resources used in the study.

[![DOI](https://zenodo.org/badge/823398782.svg)](https://doi.org/10.5281/zenodo.15885217)

Access the full paper [here](results/Diversity4SEBR.pdf)

## Abstract

This study investigates perceived inclusion and discrimination by Brazilian tech professionals. Through a survey of 220 participants across Brazil, placed on Google Forms, we examine the challenges faced by underrepresented groups, the strategies companies employ, and the gaps in current practices.

## Repository Structure

- /data: Contains raw and processed data collected from the survey.
- /scripts: Includes all scripts used for data analysis and visualization and a `requirements.txt` file that lists the libraries required to reproduce the project environment.
- /survey: The survey questionnaire used in the study and the ICF. Available versions: Portuguese and English.
- /results: Analysis results, including charts, tables, summaries, and full characterization of the 220 survey respondants. Also includes the full paper in pdf version.

## Reproducing the Study

### Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- [Git](https://git-scm.com)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/aisepucrio/Diversity4BRSE.git
   cd Diversity4BRSE
   ```

2. **Install dependencies**
   ```bash
   pip install -r scripts/requirements.txt
   ```

3. **Run the scripts according to the analysis you aim to visualize on your terminal:**

    - `python scripts/coding.py`
    - `python scripts/company.py`
    - `python scripts/leaders.py`
    - `python scripts/profile.py`
    - `python scripts/teams.py`

## Contributing

We welcome contributions from the community! Here's how you can help:

- 📝 **Participate in our survey**: [Survey (PT)](https://forms.gle/n9wLZbP2Nd2nRhUD9) | [Survey (EN)](https://forms.gle/21LsnDiqJqDLoihW8)
- 🐛 **Report issues**: Open an issue if you find bugs or have suggestions
- 🔧 **Submit improvements**: Create a pull request with your enhancements

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as permitted under the terms of this license.

## Citation

If you use this repository or its data, please cite:

**APA Format:**
```
Sousa, Theo; Azevedo, Júlia; Ribas, Jessica; Uchôa, Anderson; Rocha, Larissa; and Alves Pereira, Juliana. Diversity Matters: Perceived Inclusion and Discrimination by Brazilian Tech Professionals. In Brazilian Symposium on Software Engineering (SBES). September 2025.
```

**BibTeX:**
```bibtex
@inproceedings{sousaDiversity4BRSE,
  author    = {Canuto, Theo and Azevedo, Júlia and Ribas, Jessica and 
               Uchôa, Anderson and Rocha, Larissa and Alves Pereira, Juliana},
  title     = {Diversity Matters: Perceived Inclusion and Discrimination 
               by Brazilian Tech Professionals},
  year      = {2025}
}
```
