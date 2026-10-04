# Salary Prediction Project

[![Python](https://img.shields.io/badge/Python-3.13%2B-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Model-orange.svg)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)

This repository contains a machine learning regression project designed to predict employee salaries based on professional experience and demographic attributes[cite: 6]. Multiple algorithms were evaluated, and the Gradient Boosting Regressor was selected for final deployment[cite: 6].

---

## Dataset Notice
*Note: The dataset used in this project (`Salary_Data.csv`)[cite: 6] can be easily obtained from Kaggle by searching for employee salary datasets.*

---

## Dataset Features
The raw dataset contains the following attributes[cite: 6]:
* **Age**: Employee age[cite: 6].
* **Gender**: Male or Female[cite: 6].
* **Education Level**: Bachelor's, Master's, PhD, etc[cite: 6].
* **Job Title**: Professional role[cite: 6].
* **Years of Experience**: Number of years worked[cite: 6].
* **Salary**: Target variable (Annual salary)[cite: 6].

---

## Project Workflow
1. **Data Cleaning**: Handling missing values (`dropna`)[cite: 6].
2. **Model Comparison**: Benchmarking various regression algorithms (Linear Regression, Ridge, Lasso, Decision Tree, Gradient Boosting, XGBoost, etc.) using an automated testing function[cite: 6].
3. **Model Training**: Training the optimal model (`GradientBoostingRegressor`)[cite: 6].
4. **Evaluation**: Assessing performance metrics including R-Squared (~0.75), RMSE, and MAE[cite: 6].
5. **Model Persistence**: Saving the trained model using `joblib` into `salary_prediction_model.pkl`[cite: 6].
6. **Web Application**: Interactive deployment interface built with Streamlit.

---

## Getting Started & Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/salary-prediction.git](https://github.com/YOUR_USERNAME/salary-prediction.git)
   cd salary-prediction
