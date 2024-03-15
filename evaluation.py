# Evaluation

import numpy as np
from scipy import stats
from math import sqrt 
from sklearn.metrics import confusion_matrix, f1_score, roc_auc_score, accuracy_score

def binary_sensitivity(c_matrix):
    """
    Calculate the true positives, false negatives, and sensitivity from confusion matrix

    Parameters
    ----------
    c_matrix: matrix 
        Confusion matrix

    Returns
    ----------
    - TP: Number of true positives in confusion matrix
    - FN: Number of false negatives in confusion matrix
    - sen: Sensitivity score     
    """
    TP = c_matrix[1, 1]
    FN = c_matrix[1,0]

    sen = TP / (TP + FN)

    return TP, FN, sen


def calculate_acc_ci(accuracy, n, confidence=0.95):
    """
    Calculate the confidence interval for a classification accuracy.

    Parameters:
    accuracy: float 
        The observed accuracy (proportion of correct classifications).
    n: int 
        The total number of predictions made (sample size).
    confidence: float 
        The desired confidence level.

    Returns:
    A tuple containing the lower and upper bounds of the confidence interval.
    """
    # Calculate the z-score for the desired confidence level
    z = np.abs(stats.norm.ppf((1 - confidence) / 2))
    
    # Calculate the margin of error
    margin_of_error = z * np.sqrt((accuracy * (1 - accuracy)) / n)
    
    # Calculate the confidence interval
    ci_lower = accuracy - margin_of_error
    ci_upper = accuracy + margin_of_error
    
    return ci_lower, ci_upper


def calculate_sensitivity_confidence_interval(TP, FN, confidence_level=0.95):
    """
    Calculate the confidence interval for sensitivity (true positive rate).
    
    Parameters:
    TP: int 
        Number of true positives.
    FN: int
        Number of false negatives.
    confidence_level: float
        Desired confidence level for the interval.
    
    Returns:
    A tuple containing the lower and upper bounds of the confidence interval.
    """
    # Calculate the point estimate of sensitivity
    sensitivity = TP / (TP + FN)
    
    # Calculate the standard error
    n = TP + FN
    standard_error = sqrt(sensitivity * (1 - sensitivity) / n)
    
    # Find the z-score for the confidence level
    z_score = norm.ppf((1 + confidence_level) / 2)
    
    # Calculate the margin of error
    margin_of_error = z_score * standard_error
    
    # Calculate the confidence interval
    ci_lower = sensitivity - margin_of_error
    ci_upper = sensitivity + margin_of_error
    
    return ci_lower, ci_upper


def evaluation_metrics(pred, pred_proba, cm, X_test, y_test):
    """
    Calculate accuracy, sensitivity, F1 score, and AUC-ROC

    Parameters: 
    pred: list 
        Predictions made on the test set
    pred_proba: list
        Probability predictions made on the test set
    cm: matrix
        Confusion matrix 
    X_test: dataframe 
        Features from the test dataset
    y_test: dataframe
        Labels from the test dataset

    Returns:
    acc: float
        Accuracy score
    sen: float
         Sensitivity score
    f1: float
        F1 score
    auc_roc: float 
        Area under the curve receiving operator curve score 
    """
    acc = accuracy_score(y_test, pred)
    _, _, sen = binary_sensitivity(cm)
    f1 = f1_score(y_test, pred)
    auc_roc = roc_auc_score(y_test, pred_proba)
    return acc, sen, f1, auc_roc
