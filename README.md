# Predicting Heart Disease Using Machine Learning Algorithms 

<img src='https://github.com/CJTAYL/heart_disease/assets/64110892/1047f551-bfda-4bc5-b8fc-63ebc2230f96' width='400' height='400' />

## Executive Summary 
Four machine learning algorithms were used to predict heart disease in a set of patients. The algorithms used were (a) Logistic regression, (b) Random forest, (d) Support-vector machine, and (e) k-Nearest neighbor. All models were built with Scikit-learn. The models were evaluated using accuracy, sensitivity, F1 score, and Area Under the Curve - Receiver Operating Characteristic (AUC-ROC). The results of the project indicated that logistic regression was the best performing algorithm. 

## Abstract
According to the Centers for Disease Control and Prevention (CDC), heart or coronary disease (CD) is the leading cause of death in the United States. However, with early diagnosis, current therapies are capable of significantly improving patient outcomes. One way to facilitate early diagnosis is through increased screenings. By providing medical professionals with easy-to-use tools, targeted screening could be implemented more frequently, which should facilitate the onset of therapy. The purpose of this research project was to demonstrate how a screening tool for CD can be built using basic data mining methods and publicly available datasets.

## Introduction
In 2021, the CDC determined that CD caused more deaths than accidents, strokes, Alzheimer's disease, and diabetes combined. Although this figure is worrisome, early diagnosis and treatment of CD can significantly improve a person's health outcomes. One strategy that can aid in the early diagnosis of CD is providing physicians access to machine learning (ML) algorithms that can act as screening tools.

### Related Work 
Akella and Akella (2021) evaluated the performance of six machine learning algorithms using the "Cleveland" data set from the "University of California Irvine Heart Disease Dataset". The six algorithms were (a) Logistic regression, (b) Decision tree, (c) Random forest, (d) Support-vector machine, (e) Neural network, and (f) k-Nearest neighbor.

To evaluate the performance of the algorithms, the researchers used accuracy, sensitivity, F1 score, and Area Under the Curve–Receiver Operating Characteristic (AUC-ROC). Additionally, the mean of the metrics (excluding accuracy) was calculated to provide a single measure to describe the performance of each algorithm. A description of the metrics can be found below. 

- Accuracy: Percent of predictions the model classified correctly.
- Sensitivity: Percent of positive instances the model classified correctly.
- F1 Score: Harmonic mean of recall and precision. Recall refers to the percentage of true positives that were identified correctly. Precision refers to the proportion of positive identifications that were correct
- AUC-ROC: Probability that the model ranks a random positive data point more highly compared to a random negative data point.

The results of the study demonstrated that across three test-train ratios each algorithm had an accuracy greater than 80 percent. The Neural network performed the best across all models. The full list of performance metrics can be found in the table below.

<img width="400" alt="image" src="https://github.com/CJTAYL/heart_disease/assets/64110892/1fa97bd2-71cc-4bf4-a640-79f50ae966ae">

Based on the results of the study, the authors determined that the Neural network algorithm was best suited for the “Cleveland” dataset.
Although the work of Akella and Akella was beneficial to the medical and data science communities, their study used one relatively small dataset (i.e., approximately 300 patients). To expand upon their work, their procedures should be replicated using other, larger datasets. 

## Proposed Work
The current project was a partial replication of the procedures used by Akella and Akella using a larger dataset. Specifically, the “Hungary” dataset from the “University of California Irvine Heart Disease Dataset” was combined with the “Cleveland” dataset to create a subject pool of 596 unique patients. The combined dataset was evaluated using four ML algorithms: Logistic Regression, Random Forest, Support-Vector Machines, and k-Nearest neighbor.

### Tools
The analysis used the Python programming language and the following packages: (a) Pandas, (b) NumPy, (c) Matplotlib, (d) Seaborn, (e) Scikit-learn, and (f) SciPy.

### Exploratory Data Analysis
Prior to combining the “Cleveland” and “Hungary” datasets, duplicate rows were removed, and missing values were replaced with column medians. After combining the datasets, the numeric variables were normalized, and the target variable (presence/absence of CD) was converted from a 5-level factor (0-4) to a 2-level factor (0, 1).

Correlations between the variables were examined using a heatmap, which is displayed below. 

<img width="400" alt="image" src="https://github.com/CJTAYL/heart_disease/assets/64110892/5632b348-4caa-434e-9e22-979cf1c1d10c">





