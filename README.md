# 🧠 SmartMed Dashboard – A Sales Intelligence Tool for Pharmacy Distributors 💊

Welcome to **SmartMed Dashboard**, a sleek and intelligent sales analytics tool designed for the pharmacy and medical distribution industry. This dashboard transforms `.xlsx` or `.csv` reports into streamlined business insights — no coding or manual formatting required.

[🔗 Try the Live App](https://smartmed-llp.streamlit.app/)

---

## 🌟 Key Features

* 📁 Upload `.xlsx` or `.csv` sales reports
* 🧹 Automatic data cleaning and preprocessing
* 📊 Visualize trends in sales, discounts, and expiry timelines
* 🧠 Deep dive into customer and product-level insights
* 📅 Identify stock nearing expiration
* 🧾 Export filtered data directly as CSV
* 🎨 Gradient UI with animated logo support

---

## 🧰 Tech Stack

| Component     | Technology       |
| ------------- | ---------------- |
| Frontend      | Streamlit        |
| Data Handling | Pandas, OpenPyXL |
| Visualization | Plotly Express   |
| Styling       | Custom CSS       |
| Hosting       | Streamlit Cloud  |

---

## 📂 Directory Structure

```bash
SmartMed/
├── app.py                  # Main application file
├── requirements.txt        # Python dependencies
├── utils/
│   └── data_cleaning.py    # Data cleaning logic
├── assets/
│   └── logo.gif            # Animated sidebar logo
├── styles/
│   └── custom.css          # Custom visual styling
├── sample_data/
│   └── dummy_sales.xlsx    # Example input file
```

---

## 📊 Dashboard Sections

| Section           | Description                                        |
| ----------------- | -------------------------------------------------- |
| Sales Overview    | Key metrics: Total Sales, Quantity, Avg. Discount  |
| Monthly Trends    | Line/bar chart of monthly sales performance        |
| Customer Insights | Top customers, avg. spend, region-wise performance |
| Product Insights  | Top-selling products, revenue generators           |
| Scheme Analysis   | Discounts vs sales relationship                    |
| Expiry Tracker    | Products/batches nearing expiry and their value    |

---

## 🔧 How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/yourusername/smartmed-dashboard.git
cd smartmed-dashboard
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Launch the dashboard:

```bash
streamlit run app.py
```

4. Upload a sales Excel or CSV file, or use the provided dummy data.

---

## 📌 Licensing

This project is licensed under the MIT License. Use it, customize it, extend it. Just don’t sell expired meds, alright? 😎

---

## ✍️ Developed by

**Sujit Hulule** – Created as part of an internship simulation and dashboard design initiative.

---
