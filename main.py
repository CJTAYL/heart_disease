# Main script
import pickle 
import evaluation as eval 
from sklearn.linear_model import LogisticRegressionCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

def main(): 
    with open('mydata.pkl', 'rb') as f:
        X_encoded_scaled, y = pickle.load(f)
    
    ### Best Model ###

    # Test/Train Split 
    X_train, X_test, y_train, y_test = train_test_split(X_encoded_scaled, y, test_size=.40, random_state=0)
    print(f'Training Set Size: {X_train.shape}, {y_train.shape}')
    print(f'Testing Set Size: {X_test.shape}, {y_test.shape}')

    # Logistic Regression 
    lr = LogisticRegressionCV(cv=5, random_state=1, solver='liblinear')
    lr.fit(X_train, y_train)

    lr_pred = lr.predict(X_test)
    lr_scores = lr.predict_proba(X_test)[:, 1]
    lr_cm = confusion_matrix(y_test, lr_pred)

    lr_acc, lr_sen, lr_f1_score, lr_auc_roc = eval.evaluation_metrics(lr_pred, lr_scores, lr_cm, X_test, y_test)

    print(f'LR Acc. Score: {lr_acc:.2f}')
    print(f'LR Sen. Score: {lr_sen:.2f}')
    print(f'LR F1 Score: {lr_f1_score:.2f}')
    print(f'LR AUC-ROC: {lr_auc_roc:.2f}')    



if __name__ == "__main__":
    main()