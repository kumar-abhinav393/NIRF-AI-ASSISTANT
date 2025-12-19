import pandas as pd
import joblib

MODEL_PATH = "model/gms_model.pkl"

_model = None

def load_model():
    global _model
    if _model is None:
        _model = joblib.load(MODEL_PATH)
    return _model

def predict_gms(
    ug4_ms_21, ug4_ms_22, ug4_ms_23,
    ug5_ms_21, ug5_ms_22, ug5_ms_23,
    pg2_ms_21, pg2_ms_22, pg2_ms_23,
    pg3_ms_21, pg3_ms_22, pg3_ms_23,
    pg5_ms_21, pg5_ms_22, pg5_ms_23
):
    model = load_model()
    data = {
        "UG4_PLACED_MEDIAN_SALARY_2021-22": ug4_ms_21,
        "UG4_PLACED_MEDIAN_SALARY_2022-23": ug4_ms_22,
        "UG4_PLACED_MEDIAN_SALARY_2023-24": ug4_ms_23,

        "UG5_PLACED_MEDIAN_SALARY_2021-22": ug5_ms_21,
        "UG5_PLACED_MEDIAN_SALARY_2022-23": ug5_ms_22,
        "UG5_PLACED_MEDIAN_SALARY_2023-24": ug5_ms_23,

        "PG2_PLACED_MEDIAN_SALARY_2021-22": pg2_ms_21,
        "PG2_PLACED_MEDIAN_SALARY_2022-23": pg2_ms_22,
        "PG2_PLACED_MEDIAN_SALARY_2023-24": pg2_ms_23,

        "PG3_PLACED_MEDIAN_SALARY_2021-22": pg3_ms_21,
        "PG3_PLACED_MEDIAN_SALARY_2022-23": pg3_ms_22,
        "PG3_PLACED_MEDIAN_SALARY_2023-24": pg3_ms_23,

        "PG5_PLACED_MEDIAN_SALARY_2021-22": pg5_ms_21,
        "PG5_PLACED_MEDIAN_SALARY_2022-23": pg5_ms_22,
        "PG5_PLACED_MEDIAN_SALARY_2023-24": pg5_ms_23,
    }
    
    df_input = pd.DataFrame([data])
    score = model.predict(df_input)[0]
    
    return round(float(score), 2)