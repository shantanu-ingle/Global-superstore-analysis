# 🧮 Retail Analytics Dashboard (Streamlit)

An interactive web dashboard built using **Streamlit**, **Pandas**, and **Seaborn**, based on the *Global Superstore* dataset. It helps visualize key business metrics like sales trends, return rates, regional performance, and top-performing sales reps.


---
## 📊 Features

✅ Filter by **Region** and **Category**  
✅ View **Monthly Sales Trends** (line chart)  
✅ Analyze **Sales & Return Rates by Region**  
✅ Identify **Top 5 Sales Reps by Profit**  
✅ View **Top Returned Products**  
✅ Download **filtered data as CSV**  
✅ Fully **interactive and mobile-friendly** layout

---

## 🛠️ Technologies Used

| Tool          | Purpose                        |
|---------------|---------------------------------|
| Streamlit     | Frontend for the dashboard      |
| Pandas        | Data cleaning & manipulation    |
| Matplotlib    | Data visualization              |
| Seaborn       | Styled charts                   |
| OpenPyXL      | Excel file support              |

---

## 📥 Installation

### 1. Clone the repository

```bash
git https://github.com/shantanu-ingle/Global-superstore-analysis.git
cd Global-superstore-analysis
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the Streamlit app
```bash
streamlit run dashboard.py
```