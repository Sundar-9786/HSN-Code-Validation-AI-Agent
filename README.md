# 🧠 HSN Code Validation Agent (Deployed with Flask + Dialogflow)

This project is an AI-powered agent built using Google Dialogflow and a Flask backend. It validates HSN (Harmonized System of Nomenclature) codes against a master dataset.

## 🚀 Live URL

- API Endpoint: [https://sundar9786.pythonanywhere.com/webhook](https://sundar9786.pythonanywhere.com/webhook)
- Health Check: [https://sundar9786.pythonanywhere.com/](https://sundar9786.pythonanywhere.com/)

## 🧱 Technologies Used

- 🔹 Google Dialogflow (NLP)
- 🔹 Python Flask (backend webhook)
- 🔹 Pandas for data processing
- 🔹 PythonAnywhere (web hosting)
- 🔹 Excel (`HSN_SAC.xlsx`) as master data source

## 🧠 Features

- Validates **single or multiple HSN codes**
- Checks:
  - ✅ Format (2–8 digit numbers)
  - ✅ Existence in master data
  - ✅ Hierarchical fallback (parent categories)
- Returns:
  - Descriptions for valid codes
  - Friendly error messages for invalid codes

## 🗂️ Project Structure

