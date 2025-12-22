import joblib
import numpy as np

MODEL_PATH = "model/gph_model.pkl"
_model = None

def load_model():
    global _model
    if _model is None:
        _model = joblib.load(MODEL_PATH)
    return _model

def predict_gph(Np, Nhs):
    model = load_model()
    
    X_new = np.array([[Np, Nhs]])
    gph = model.predict(X_new)[0]
    return round(gph, 2)