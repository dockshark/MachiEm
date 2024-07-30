from sklearn.linear_model import LogisticRegression
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
import numpy as np

def hybrid_model(data, labels):
    # Train a logistic regression model
    classical_model = LogisticRegression()
    classical_model.fit(data, labels)

    # Combine classical and quantum features
    classical_predictions = classical_model.predict_proba(data)[:, 1]
    combined_features = np.column_stack((data, classical_predictions))

    # Train a deep learning model on combined features
    model = Sequential([
        Dense(128, activation='relu', input_shape=(combined_features.shape[1],)),
        Dropout(0.2),
        Dense(64, activation='relu'),
        Dropout(0.2),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(combined_features, labels, epochs=10, batch_size=32, validation_split=0.2)
    return model
