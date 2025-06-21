import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Load the trained model
#your project path may vary, ensure the model path is correct
model = joblib.load("D:/Projects/FYP_Martial_Arts_15000/psych_wellness_rf_model.pkl")

st.title("Psychological Distress Prediction After Tai Chi")

st.markdown("---")

# User inputs
st.header("Enter Participant Information")

gender = st.selectbox("Gender", ["Male", "Female"])
age = st.slider("Age", 10, 80, 25)
martial_freq = st.slider("Martial Arts Sessions per Week", 0, 7, 3)
duration = st.selectbox("Daily Exercise Duration", ["<30 min", "30-60 min", ">60 min"])
taichi = st.selectbox("Practiced Tai Chi?", ["Yes", "No"])

# Questionnaire (1: Very Positive - 5: Very Negative)
st.markdown("### Questionnaire (1: Very Positive - 5: Very Negative)")
question_cols = [
    'Nervousness or shakiness inside',
    'Pains in heart or chest',
    'Feeling low in energy or slowed down',
    'Blaming yourself for things',
    'Feeling blocked in getting things done',
    'Worrying too much about things',
    'Trouble falling asleep',
    'Trouble concentrating',
    'Feeling tense or keyed up',
    'Feeling everything is an effort',
    'The idea that something is wrong with your mind'
]
qs = []
for i, q in enumerate(question_cols, 1):
    val = st.slider(f"Q{i}: {q}", 1, 5, 3)
    qs.append(val)

# Encode categorical inputs to match model training
gender_val = 1 if gender == "Male" else 0
duration_map = {"<30 min": 0, "30-60 min": 1, ">60 min": 2}
duration_val = duration_map[duration]
taichi_val = 1 if taichi == "Yes" else 0

# Create input DataFrame with correct column order
input_data = pd.DataFrame([[gender_val, age, martial_freq, duration_val, taichi_val] + qs],
    columns=[
        'Gender', 'Age',
        'The number of times you are martial arts active in a week',
        'The duration of each of your exercises',
        'taichi'
    ] + question_cols
)

# Prediction
if st.button("Predict Psychological State"):
    prediction = model.predict(input_data)[0]
    label_map = {0: "Good", 1: "Moderate", 2: "Poor"}
    label = label_map.get(prediction, "Unknown")
    st.success(f"Predicted Psychological State: {label}")

    st.markdown("---")
    st.header("Tai Chi vs Non-Tai Chi Psychological Score Distribution (Multiple Aspects)")

    try:
        df = pd.read_csv("D:/Projects/FYP_Martial_Arts_15000/processed_martial_arts_data.csv")
        chart_types = [
            ("Boxplot", sns.boxplot),
            ("Violinplot", sns.violinplot),
            ("Swarmplot", sns.swarmplot),
            ("Stripplot", sns.stripplot),
            ("Barplot", sns.barplot),
            ("Pointplot", sns.pointplot),
            ("Boxenplot", sns.boxenplot),
            ("Histogram", None),  # Will use plt.hist
            ("KDEplot", None),    # Will use sns.kdeplot
            ("ECDFplot", None)    # Will use sns.ecdfplot
        ]
        for i, (chart_name, chart_func) in enumerate(chart_types):
            q_col = question_cols[i % len(question_cols)]
            st.subheader(f"{chart_name} for: {q_col}")
            fig, ax = plt.subplots(figsize=(7, 4))
            if chart_name == "Histogram":
                for val, label in zip([0, 1], ["No Tai Chi", "Tai Chi"]):
                    ax.hist(df[df["taichi"] == val][q_col], bins=5, alpha=0.5, label=label)
                ax.legend()
                ax.set_xlabel(q_col)
                ax.set_ylabel("Count")
            elif chart_name == "KDEplot":
                for val, label in zip([0, 1], ["No Tai Chi", "Tai Chi"]):
                    sns.kdeplot(df[df["taichi"] == val][q_col], ax=ax, label=label, fill=True)
                ax.set_xlabel(q_col)
                ax.set_ylabel("Density")
                ax.legend()
            elif chart_name == "ECDFplot":
                for val, label in zip([0, 1], ["No Tai Chi", "Tai Chi"]):
                    sns.ecdfplot(df[df["taichi"] == val][q_col], ax=ax, label=label)
                ax.set_xlabel(q_col)
                ax.set_ylabel("ECDF")
                ax.legend()
            else:
                chart_func(x="taichi", y=q_col, data=df, ax=ax)
                ax.set_xticklabels(["No Tai Chi", "Tai Chi"])
            ax.set_title(f"{chart_name} of '{q_col}' by Tai Chi Practice")
            st.pyplot(fig)
    except Exception as e:
        st.warning("Could not load dataset for visualization.")
        st.error(str(e))
