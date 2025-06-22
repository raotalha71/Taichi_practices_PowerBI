Taichi Exercise Effectiveness Prediction
This project investigates the mental health benefits of Taichi exercises among secondary school students in China using machine learning. By analyzing psychological data from the SCL-90 questionnaire, we predict distress levels to evaluate Taichi’s effectiveness. The pipeline includes data preprocessing, feature engineering, model training with Random Forest and XGBoost, and visualization of results.
Objectives 

Assess mental health benefits (e.g., reduced distress) of Taichi using SCL-90 scores.
Preprocess data from student surveys, including demographic and exercise details.
Select and train machine learning models to predict Taichi’s effectiveness.
Evaluate model performance using accuracy, precision, recall, and F1-score.
Identify key factors (e.g., Taichi practice, frequency) influencing outcomes.
Provide recommendations for integrating Taichi into school health programs.

Setup Instructions


Clone the repository:git clone <repository-url>
cd taichi-effectiveness


Create a virtual environment:python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies (see below).
Place the datasets (Psychological Questionnaire Survey.xlsx and second dataset) in the data/ folder.
Run the pipeline script:python main.py



Dependencies
Install the required Python packages using pip:
pip install pandas==2.2.3
pip install numpy==2.1.1
pip install scikit-learn==1.5.2
pip install imbalanced-learn==0.12.3
pip install xgboost==2.1.1
pip install matplotlib==3.9.2
pip install seaborn==0.13.2
pip install openpyxl==3.1.5

Data Preprocessing

Dataset 1: Psychological Questionnaire Survey.xlsx
Columns: Gender, Age, martial arts type (e.g., Neijia Quan for Taichi), frequency, duration, 90 SCL-90 questions.
Steps:
Remove Chinese text from column names and values.
Create Is_Taichi (1 = Taichi, 0 = non-Taichi).
Sum SCL-90 scores (columns 7–96) to create total_scl90.
Binarize to distress (<median = 0, ≥median = 1).




Dataset 2: (Placeholder, e.g., Second_Dataset.xlsx)
Assumed: Physical fitness (balance, flexibility), academic performance, or lifestyle data.
Merge with Dataset 1 using a common identifier (e.g., Serial Number).


Output: Processed_Dataset.xlsx with cleaned and merged data.

Model Training

Target: distress (binary: 0 = low distress, 1 = high distress).
Features: Is_Taichi, Gender, Age, frequency, duration.
Models: Random Forest, XGBoost.
Steps:
Encode categorical features (e.g., one-hot encoding).
Normalize Age.
Balance classes using SMOTE.
Train and evaluate models.



Usage

Ensure datasets are in data/.
Run main.py to preprocess data, train models, and generate visualizations:python main.py


Outputs:
Processed_Dataset.xlsx: Cleaned dataset.
model_metrics.txt: Accuracy, precision, recall, F1-score.
plots/: Visualizations (e.g., distress by Taichi practice).



Deliverables

Cleaned dataset with derived features.
Trained models with performance metrics.
Visualizations (bar plots, feature importance) for PowerBI or Python.
Report sections with insights and recommendations.

Notes

Update Second_Dataset.xlsx path and merge logic based on its contents.
Adjust distress threshold if needed (e.g., median of total_scl90).
Contact for support: [Your Email].

