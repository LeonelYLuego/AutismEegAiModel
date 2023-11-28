import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
from tsfresh.feature_extraction.feature_calculators import (
    mean,
    kurtosis,
    skewness,
    abs_energy,
    standard_deviation,
)


def extract_data(jsons):
    data = pd.DataFrame(jsons)

    relevant_columns = [
        "channel3",
        "channel12",
    ]

    data = data[relevant_columns]
    data = data.drop(range(1538))
    data[relevant_columns] = data[relevant_columns].apply(
        pd.to_numeric, errors="coerce"
    )
    data = data.dropna()

    summary_statistics = {
        "Mean": data.apply(mean),
        "Kurtosis": data.apply(kurtosis),
        "Skewness": data.apply(skewness),
        "Abs Energy": data.apply(abs_energy),
        "Standard Deviation": data.apply(standard_deviation),
    }

    summary_statistics = pd.DataFrame(summary_statistics)
    return summary_statistics.mean(axis=0).values


def get_result(jsons):
    standard_scaler = joblib.load("app/static/scaler.joblib")
    data = [extract_data(jsons)]
    data_pred = standard_scaler.transform(data)

    # TODO: Averiguar como obtener el path de la carpeta app
    svm_regression = joblib.load("app/static/model.joblib")
    result = svm_regression.predict(data_pred)
    print(result)
    return result[0]
