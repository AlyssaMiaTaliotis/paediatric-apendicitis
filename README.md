# Paediatric Appendicitis Diagnosis – Concept Bottleneck Models

## Team Members:
Ioana-Andreea Cristescu, Alissia Di Maria, Jonas Raedler, Alyssa Mia Taliotis

## Project Overview
**Providing Visual Interpretations in Concept-Bottleneck Models to Assist in Paediatric Appendicitis Diagnosis**  

## Environment Setup 
This guide will walk you through setting up the environment.

### First Time Setup 
For the first time, you need to install the required dependencies and set up the Python environment. Follow these steps:

1. Create virtual environment: `python3 -m venv venv`
2. Activates the virtual environment so you can install and run packages within it: `source venv/bin/activate`
3. Installs all the necessary Python packages into the virtual environment: `pip install -r requirements.txt` 

### After the First Time
Once the environment is set up, you only need to activate the virtual environment to start working on the project:

1. Activate the virtual environment: `source venv/bin/activate`
2. If dependencies change (e.g., after a repository update), update them: `pip install -r requirements.txt`

## Data 
To replicate our results, the original dataset can be accessed from this [Zenodo link](https://zenodo.org/records/7669442).

The dataset includes abdominal ultrasound images and clinical metadata from a retrospective study of pediatric patients with abdominal pain at Children’s Hospital St. Hedwig in Regensburg, Germany. Each subject has multiple ultrasound images (1–15 views) showing various abdominal regions, along with corresponding clinical scores, lab tests, physical examination findings, and final diagnostic labels (appendicitis status, management decision, and severity level).

### How to Prepare the Data:
1. Download and extract `US_Pictures.zip`, and place the extracted folder at the root of the repository.
2. Download `app_data.xlsx`, save the first sheet as a CSV file, and place it in the `data/` folder as `app_data.csv`.`
