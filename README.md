# Diversity Matters: Perceived Inclusion and Discrimination by Brazilian Tech Professionals

This repository contains all the codes, data, ICFs and resources used in the study.

Access the full paper [here](results/Diversity4SEBR.pdf)

### Abstract

This study investigates perceived inclusion and discrimination by Brazilian tech professionals. Through a survey of 220 participants across Brazil, placed on Google Forms, we examine the challenges faced by underrepresented groups, the strategies companies employ, and the gaps in current practices.

### Repository Structure

- /data: Contains raw and processed data collected from the survey and a `requirements.txt` file that lists the libraries required to reproduce the project environment.
- /scripts: Includes all scripts used for data analysis and visualization.
- /survey: The survey questionnaire used in the study and the ICF. Available versions: Portuguese and English.
- /results: Analysis results, including charts, tables, summaries, and full characterization of the 220 survey respondants. Also includes the full paper in pdf version.

### Reproducing the Study

- 1. Install dependencies

    ```bash
   pip install -r scripts/requirements.txt
   ```

- 2. Run the scripts according to the analysis you aim to visualize:

    - `scripts/coding.py`
    - `scripts/company.py`
    - `scripts/leadership_roles.py`
    - `scripts/profile.py`
    - `scripts/teams.py`

### Contributing

We welcome contributions from the community. If you have any suggestions or improvements, please submit a pull request or open an issue. We also value your input! Please participate in our survey to help us gather valuable data for our research here: [Survey [PT]](https://forms.gle/n9wLZbP2Nd2nRhUD9) or [Survey [EN]](https://forms.gle/21LsnDiqJqDLoihW8)

### License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).  
Feel free to use, modify, and distribute it as permitted under the terms of this license.