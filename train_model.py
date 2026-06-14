import pandas as pd
import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

# ==========================================
# LOAD DATASET
# ==========================================

print("Loading dataset...")

data = pd.read_csv("dataset.csv")

print("Dataset Loaded Successfully")
print("Total Records:", len(data))

# ==========================================
# FEATURES
# ==========================================

X = data[[
    "Study_Time",
    "Attention_Span",
    "Revision_Count",
    "Mistakes",
    "Sleep_Hours",
    "Attendance",
    "Math_Score",
    "Physics_Score",
    "Chemistry_Score",
    "English_Score",
    "CS_Score"
]]

# ==========================================
# TARGET
# ==========================================

y = data["Performance_Level"]

# ==========================================
# LABEL ENCODING
# ==========================================

encoder = LabelEncoder()

y_encoded = encoder.fit_transform(y)

print("\nClasses Found:")
print(encoder.classes_)

# ==========================================
# TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.20,
    random_state=42,
    stratify=y_encoded
)

print("\nTraining Records :", len(X_train))
print("Testing Records  :", len(X_test))

# ==========================================
# RANDOM FOREST MODEL
# ==========================================

model = RandomForestClassifier(
    n_estimators=300,
    max_depth=10,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42
)

print("\nTraining Model...")

model.fit(X_train, y_train)

print("Training Completed Successfully")

# ==========================================
# MODEL EVALUATION
# ==========================================

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print("\n===================================")
print("MODEL ACCURACY")
print("===================================")

print(
    round(accuracy * 100, 2),
    "%"
)

print("\n===================================")
print("CLASSIFICATION REPORT")
print("===================================")

print(
    classification_report(
        y_test,
        predictions,
        target_names=encoder.classes_
    )
)

# ==========================================
# FEATURE IMPORTANCE
# ==========================================

feature_names = [

    "Study_Time",
    "Attention_Span",
    "Revision_Count",
    "Mistakes",
    "Sleep_Hours",
    "Attendance",
    "Math_Score",
    "Physics_Score",
    "Chemistry_Score",
    "English_Score",
    "CS_Score"
]

importance = model.feature_importances_

feature_df = pd.DataFrame({

    "Feature": feature_names,
    "Importance": importance

})

feature_df = feature_df.sort_values(
    by="Importance",
    ascending=False
)

print("\n===================================")
print("FEATURE IMPORTANCE")
print("===================================")

print(feature_df)

# ==========================================
# SAVE MODEL
# ==========================================

pickle.dump(
    model,
    open("model.pkl", "wb")
)

pickle.dump(
    encoder,
    open("encoder.pkl", "wb")
)

print("\n===================================")
print("FILES SAVED SUCCESSFULLY")
print("===================================")

print("✓ model.pkl")
print("✓ encoder.pkl")

# ==========================================
# SAMPLE TEST
# ==========================================

sample_student = [[

    5,      # Study Time
    40,     # Attention Span
    3,      # Revision Count
    5,      # Mistakes
    7,      # Sleep Hours
    85,     # Attendance
    75,     # Math
    80,     # Physics
    70,     # Chemistry
    85,     # English
    90      # CS

]]

prediction = model.predict(
    sample_student
)

result = encoder.inverse_transform(
    prediction
)

print("\n===================================")
print("SAMPLE STUDENT PREDICTION")
print("===================================")

print(
    "Predicted Performance :",
    result[0]
)

print("\nTraining Finished Successfully!")