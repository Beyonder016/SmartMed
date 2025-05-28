# 🧠 SmartMed Dashboard – A Sales Intelligence Tool for Pharmacy Distributors 💊

Welcome to **SmartMed Dashboard**, a sleek, powerful, and intelligent sales analytics tool tailor-built for the pharmacy and medical distribution industry. This dashboard isn’t just another spreadsheet viewer — it transforms boring `.xlsx` or `.csv` reports into streamlined business insights.

Upload. Analyze. Visualize. All in seconds.

---

## 🚀 Live Demo

> 📁 *Coming Soon on Streamlit Cloud*
> Stay tuned for the live hosted version!

---

## 🌟 Features

* 📁 **Excel/CSV Upload** – drag & drop simplicity
* 🧹 **Automated Data Cleaning** – date parsing, header fixing, NaN handling
* 📊 **Interactive Dashboards** – sales KPIs, trends, expiry tracking, discount analysis
* 🧠 **Customer & Product Insights** – top earners, top sellers
* 🗓️ **Expiry Alerts** – batches nearing expiry in 90 days
* 🌈 **Styled UI** – animated logo, gradient themes, custom CSS
* 📄 **Export Filtered Reports** – download instantly as CSV
* 🧪 **Built-in Sample Data** – test it even without real files

---

## 🪠 Tech Stack Breakdown

| Layer          | Tool/Lib                    |
| -------------- | --------------------------- |
| Web Framework  | Streamlit                   |
| Data Wrangling | pandas, openpyxl            |
| Charts         | plotly.express              |
| Styling        | Custom CSS, gradient themes |
| Deployment     | Streamlit Cloud-ready       |

---

## 📦 Folder Structure

```bash
SmartMed/
├── app.py                  # Main app
├── requirements.txt        # Dependencies
├── utils/
│   └── data_cleaning.py    # Reusable cleaning functions
├── assets/
│   └── logo.gif            # Sidebar animation
├── styles/
│   └── custom.css          # Full UI theming
├── sample_data/
│   └── dummy_sales.xlsx    # Test input
```

---

## 📊 How It Works

1. **Upload** your `.xlsx` or `.csv` sales report
2. SmartMed **cleans** the data (headers, dates, NaNs, etc.)
3. You **filter** by date, customer, product
4. It shows:

   * 📈 Monthly sales trend
   * 🧐 Top customers & products
   * 🌟 Discount performance
   * ⏳ Stock near expiry
5. **Download** the filtered view as a ready-to-go CSV

---

## 📸 UI Preview

> *Insert screenshots or GIFs of dashboard here*

---

## 🎨 UI Highlights

* 💻 Dark mode with vibrant gradients
* 🔄 Animated `.gif` logo in sidebar
* 🔸 Gradient navbar, sidebar, and background
* 📆 Responsive layout using columns & expanders
* 🪤 Translucent card-style panels with subtle shadows

---

## 🔮 Sample Use Cases

* Evaluate batch expiry risk for the quarter
* Identify low-performing high-discount products
* Generate instant customer leaderboard
* Pre-process reports for business reviews
* Present insights in stakeholder meetings

---

## 🔧 Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/smartmed-dashboard.git
cd smartmed-dashboard
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run locally**

```bash
streamlit run app.py
```

4. **Upload your `.xlsx` or use the dummy data**

---

## ☁️ Deploy on Streamlit Cloud

* Push the repo to GitHub
* Go to [Streamlit Cloud](https://share.streamlit.io/)
* Paste your repo link
* Done. It builds automatically using `requirements.txt`

---

## 🫀 Behind the Name

> “SmartMed” = Smart + Medicine
> It’s all about delivering **actionable insights** in a medical sales context.

---

## 🧳 Roadmap

* 🔐 Login & user sessions
* 📄 PDF export
* 🧠 AI-based sales forecasting
* 🌍 Geo-visualization by region
* 🗓 Date picker with toggles

---

## ❤️ Credits

Created by **Sujit Hulule** for an internal-use, demonstration-focused internship simulation project.

---

## 📜 License

MIT — use it, remix it, deploy it. Just don’t sell expired meds, alright? 😎
