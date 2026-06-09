import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler, OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np


# ========== Paths ==========
# عدّل المسار لو ملفك في مكان مختلف
DATA_PATH = r"C:\Users\dell\Desktop\advanced_db_project\cleaned_ebay_laptop_data.csv"

# هنحفظ الموديل هنا عشان FastAPI يستخدمه
MODEL_OUT_PATH = os.path.join("backend", "models", "model.pkl")
os.makedirs(os.path.dirname(MODEL_OUT_PATH), exist_ok=True)


def main():
    df = pd.read_csv(DATA_PATH)

    target = "Price"
    if target not in df.columns:
        raise ValueError(f"Target column '{target}' not found in CSV. Available: {df.columns.tolist()}")

    # نفس الأعمدة اللي في الـ notebook
    num_cols = [
        "RAM_GB", "Storage_GB", "Screen_Size_Inch", "Shipping_Cost",
        "Seller_Score", "Seller_Reviews"
    ]
    cat_cols = ["Processor", "Condition", "Country", "Listing_Type_Cat"]

    # تأكد الأعمدة موجودة
    missing = [c for c in (num_cols + cat_cols + [target]) if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns in CSV: {missing}")

    # Drop rows without target
    df = df.dropna(subset=[target])

    X = df[num_cols + cat_cols]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # ===== Preprocessor (exactly like notebook) =====
    numeric_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", RobustScaler()),
    ])

    categorical_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="constant", fill_value="missing")),
        ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
    ])

    preprocessor = ColumnTransformer(transformers=[
        ("num", numeric_transformer, num_cols),
        ("cat", categorical_transformer, cat_cols),
    ])

    rf_pipe = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("model", RandomForestRegressor(random_state=42)),
    ])

    # نفس فكرة البحث العشوائي (بس ممكن توسّعها بعدين)
    param_grid = {
        "model__n_estimators": [200, 400, 600],
        "model__max_depth": [10, 20, None],
        "model__min_samples_split": [2, 5, 10],
        "model__min_samples_leaf": [1, 2, 4],
    }

    search = RandomizedSearchCV(
        rf_pipe,
        param_distributions=param_grid,
        n_iter=8,
        cv=3,
        scoring="neg_mean_squared_error",
        random_state=42,
        n_jobs=-1,
        verbose=1
    )

    search.fit(X_train, y_train)
    best_model = search.best_estimator_

    # ===== Evaluate =====
    preds = best_model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    mae = mean_absolute_error(y_test, preds)
    r2 = r2_score(y_test, preds)

    print("\n===== Best Params =====")
    print(search.best_params_)
    print("\n===== Test Metrics =====")
    print(f"RMSE: {rmse:.2f}")
    print(f"MAE : {mae:.2f}")
    print(f"R2  : {r2:.4f}")

    # ===== Save Model (Pipeline) =====
    joblib.dump(best_model, MODEL_OUT_PATH)
    print(f"\n✅ Model saved to: {MODEL_OUT_PATH}")


if __name__ == "__main__":
    main()
