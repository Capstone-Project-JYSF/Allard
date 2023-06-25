import pandas as pd
import numpy as np
import eli5
from scipy.stats import lognorm, loguniform, randint
from sklearn.model_selection import (
    RandomizedSearchCV,
    cross_val_score,
    cross_validate,
    train_test_split,
)
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler
from sklearn.compose import (
    ColumnTransformer,
    TransformedTargetRegressor,
    make_column_transformer,
)
import joblib

df = pd.read_csv('../data/cleaned_data_v2.csv')
df.info()

train_df, test_df = train_test_split(df, test_size=0.2, random_state=123)
X_train, y_train = train_df.drop(columns = ["What was the outcome of the case?"]), train_df["What was the outcome of the case?"]
X_test, y_test = test_df.drop(columns = ["What was the outcome of the case?"]), test_df["What was the outcome of the case?"]
print("train set:", train_df.shape)
print("test set:", test_df.shape)
train_df.head()

loaded_model = joblib.load('../models/stacking_model.sav')
print(loaded_model.predict_proba(X_test))
