import pandas as pd
import joblib
import numpy as np
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

# Load dataset
df = pd.read_excel("data/Engineering/MasterData_GPH.xlsx")

X = df[["Np", "Nhs"]]
y = df["GPH"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = XGBRegressor(
    n_estimators=200,
    learning_rate=0.1,
    max_depth=3,
    objective="reg:squarederror",
    random_state=42
)

model.fit(X_train, y_train)

preds = model.predict(X_test)

print("R2 Score:", r2_score(y_test, preds))

rmse = np.sqrt(mean_squared_error(y_test, preds))
print("RMSE:", rmse)

joblib.dump(model, "model/train_gph_model.pkl")
print("✅ Model saved as gph_xgb_model.pkl")
