# 🏥 Healthcare Insurance Cost Prediction App

A clean, modern **Streamlit-based web application** that predicts **health insurance costs** using a trained **Machine Learning regression model**. The project focuses on **good UX/UI**, **data-driven predictions**, and **simple user interaction**.

---

## 🚀 Features

* 🔮 **Machine Learning–based prediction** using real insurance data
* 🧮 Automatic **BMI calculation** from height & weight
* 🎨 Clean, modern UI with custom styling (no default Streamlit look)
* ⚡ Instant predictions
* 📱 Responsive layout
* 🧠 Model loaded efficiently using caching

---

## 🧩 Pages Overview

### 🏠 Home Page

* Hero section with project introduction
* Clear CTA to start prediction
* How-it-works explanation
* Key features summary

### 📊 Insurance Predictor Page

* Structured input form
* Clean two-column layout
* BMI calculated automatically
* Prediction result displayed in a highlighted card
* Disclaimer for transparency

---

## 🛠 Tech Stack

* **Frontend / App Framework**: Streamlit
* **Machine Learning**: Scikit-learn (Regression model)
* **Model Persistence**: Joblib
* **Data Handling**: Pandas, NumPy
* **Styling**: Custom CSS (embedded via `st.markdown`)

---

## 📂 Project Structure

```text
.
├── app.py                  # Main app entry point
├── pages/
│   ├── home.py              # Home page UI
│   └── predictor.py         # Insurance predictor page
├── model/
│   └── model.joblib         # Trained ML model
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 📥 Input Parameters

The prediction model uses the following inputs:

| Feature  | Description              |
| -------- | ------------------------ |
| Age      | User age (years)         |
| Gender   | Male / Female            |
| Height   | In centimeters           |
| Weight   | In kilograms             |
| BMI      | Calculated automatically |
| Smoker   | Yes / No                 |
| Children | Number of dependents     |
| Region   | Residential region       |

---

## 📈 Output

* **Estimated Insurance Cost (₹)**
* Displayed prominently after form submission
* Includes a disclaimer noting prediction variability

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd insurance-cost-predictor
```

### 2️⃣ Create virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the app

```bash
streamlit run app.py
```

---

## 🧠 Model Notes

* The ML model is trained on historical healthcare insurance data
* Uses regression to estimate insurance charges
* Model is loaded using `@st.cache_resource` for performance

---

## 🎨 UI / UX Design Principles

* CTA buttons are visually prominent
* Input fields keep native usability
* Gradients are used sparingly
* White space for readability
* Consistent font (Inter)

---

## ⚠️ Disclaimer

> This application provides **estimates only**. Actual insurance costs may vary depending on provider policies, location, medical history, and other real-world factors.

---

## 📌 Future Improvements

* Add model confidence range
* Support more regions
* User authentication
* Save prediction history
* Deploy on cloud (Streamlit Cloud / AWS / GCP)

---

## 👨‍💻 Author

Built with ❤️ using Streamlit & Machine Learning

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to contribute!
