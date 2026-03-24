import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("student_small.csv")

# Drop id
df = df.drop(columns=["id"])

X = df.drop("burnout", axis=1)
y = df["burnout"]

# Save feature names
joblib.dump(X.columns.tolist(), "features.pkl")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, "model.pkl")

print("✅ Model trained successfully")