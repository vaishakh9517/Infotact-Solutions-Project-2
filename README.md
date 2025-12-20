# Customer-Segmentation-Analysis-Using-RFM-and-KMeans

This repository contains an end-to-end Customer Segmentation Analysis project focused on identifying meaningful customer groups using RFM analysis and K-Means clustering.
The project simulates a real-world retail analytics use case, transforming raw transactional data into actionable customer segments to support targeted marketing, retention strategies, and revenue optimization.

📁 Project Structure

/Customer-Segmentation-Analysis/
│
├── data/
│ ├── raw/
│ │ └── Online Retail.csv
│ ├── cleaned/
│ │ ├── Cleaned_BrightNest.csv
│ │ └── Customer_Segments.csv
│
├── notebooks/
│ └── Customer_Segmentation_RFM_KMeans.ipynb
│
├── visuals/
│ ├── Elbow_Method.png
│ ├── Silhouette_Scores.png
│ └── PCA_Clusters.png
│
└── README.md

📊 Project Overview: Customer Segmentation (Retail Analytics)
🔍 Objective

Segment customers based on purchasing behavior to enable personalized marketing, customer retention, and data-driven business decisions.

🧮 Data Summary

Source: Public retail transaction dataset

Time Period: 2 years of transactional data

Key Features:

InvoiceNo

InvoiceDate

CustomerID

Quantity

UnitPrice

Derived: Sales

🛠️ Methodology
1️⃣ Data Cleaning & Preparation

Removed cancelled invoices and return transactions.

Filtered negative quantities and prices.

Handled missing CustomerID and invalid timestamps.

Created a transaction-level Sales metric.

2️⃣ Feature Engineering (RFM)

Recency: Days since last purchase.

Frequency: Number of unique purchase invoices.

Monetary: Total customer spend.

Average Purchase Value: Monetary / Frequency.

3️⃣ Data Scaling

Applied RobustScaler to reduce the impact of outliers common in retail data.

4️⃣ Clustering & Model Selection

Used Elbow Method (WCSS) and Silhouette Score to determine optimal clusters.

Finalized K = 4 for balanced interpretability and statistical validity.

Applied K-Means clustering.

5️⃣ Dimensionality Reduction

Used PCA (2 components) for cluster visualization and validation.

📈 Segmentation Results

The analysis identified four distinct customer segments:

Cluster	Segment Description
Cluster 0	Low-value, infrequent, long-inactive customers
Cluster 1	Ultra-high value statistical outlier
Cluster 2	Moderately active repeat customers
Cluster 3	Highly loyal, high-value customers
Key Observations

A small percentage of customers contribute disproportionately to revenue.

Majority of customers fall into low-engagement segments, indicating reactivation opportunities.

Clear separation between high-value loyal customers and inactive buyers.

💡 Business Insights & Recommendations

High-value loyal customers should be prioritized for retention and loyalty programs.

Mid-value active customers represent strong upsell and growth potential.

Inactive customers require targeted re-engagement strategies.

Segment-level insights enable cost-efficient marketing and better ROI.

✅ Skills Demonstrated

Data Cleaning & Preprocessing (Python, Pandas)

Feature Engineering (RFM Analysis)

Machine Learning (K-Means Clustering)

Model Evaluation (Elbow Method, Silhouette Score)

Dimensionality Reduction (PCA)

Business Insight Generation

Retail & Customer Analytics

📌 Conclusion

This project demonstrates how machine learning and statistical analysis can be applied to real-world retail data to uncover actionable customer insights.
The resulting segmentation framework enables organizations to move from generic marketing to precision-driven, customer-centric strategies.

📎 License

This project is intended for educational and portfolio purposes only.

## 🙋‍♂️ About Me

**Vaishakh K**  
Data Analyst | Excel | MySQL | Python | Tableau | Power BI
[LinkedIn](https://www.linkedin.com/in/vaishakh-k-0b2bb8202/) • [Portfolio](https://github.com/vaishakh9517)

📎 License

This project is intended for educational and portfolio purposes only.
