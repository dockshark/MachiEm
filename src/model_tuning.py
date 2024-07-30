# src/model_tuning.py

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

def tune_logistic_regression(data, labels):
    param_grid = {
        'C': [0.01, 0.1, 1, 10, 100],
        'solver': ['newton-cg', 'lbfgs', 'liblinear']
    }
    grid_search = GridSearchCV(LogisticRegression(), param_grid, cv=5, scoring='accuracy')
    grid_search.fit(data, labels)
    best_params = grid_search.best_params_
    best_score = grid_search.best_score_
    print(f'Best Parameters: {best_params}')
    print(f'Best Cross-Validation Accuracy: {best_score * 100:.2f}%')
    return grid_search.best_estimator_
