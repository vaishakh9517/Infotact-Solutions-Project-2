#Importing Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

#Importing raw dataset
file_path = "D:/Git/Infotact-Solutions-Project-2/Data/Raw/Online Retail.csv"
df = pd.read_csv(file_path, encoding='latin1')

#Initial Check
print("Shape : ", df.shape)
print(df.head())
df.info()
print("Missing Values Count : ", df.isnull().sum())

#Data Cleaning and Preprocessing
# - Removing Invoice numbers that starts with 'C' (Cancelled orders)
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]

# - Removing negative quantities and unit prices
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

# - Converting InvoiceDate to DateTime format
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors = 'coerce')
print("Total null values in Date : ", df['InvoiceDate'].isna().sum())

# - Handling missing values
df = df.dropna(subset = ['CustomerID'])
df = df.dropna(subset = ['InvoiceDate'])

# Adding Total Sales Column
df['Sales' ] = df['Quantity'] * df['UnitPrice']

# Rechecking the dataset
df.info()

# Feature Engineering
# - RFM - Recency, Frequency, Monetary for each customer
snapshot_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)
rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x : (snapshot_date - x.max()).days, #Recency
    'InvoiceNo' : 'nunique',                                  #Frequency
    'Sales' : 'sum'                                           #Monetary
}).reset_index()

rfm.columns = ['CustomerID', 'Recency', 'Frequency', 'Monetary']

# - Adding Average Purchase Inside RFM
rfm['AveragePurchase'] = rfm['Monetary'] / rfm['Frequency']

# Data Scaling
features = ['Recency', 'Frequency', 'Monetary', 'AveragePurchase']
scaler = RobustScaler()

print(rfm.isnull().sum())

rfm[features] = rfm[features].replace([np.inf, -np.inf], np.nan)
rfm.dropna(subset=features, inplace=True)
rfm_scaled = scaler.fit_transform(rfm[features])

print("After removing null and infinite values from Recency\n", rfm.isnull().sum())

scaled_df = pd.DataFrame(rfm_scaled, columns=features)

print("No of Null Values in Scaled Dataframe : \n", scaled_df.isnull().sum())

# Determining optimal number of clusters
wcss = []
silhouette_scores = []
for k in range (2, 11):
    km = KMeans(n_clusters = k, random_state= 42)
    km.fit(scaled_df)

    # Elbow Method
    wcss.append(km.inertia_)

    # Silhouette Score
    score = silhouette_score(scaled_df, km.labels_)
    silhouette_scores.append(score)

#Plotting Elbow Method Graph
plt.figure()
plt.plot(range(2, 11), wcss, marker = 'o')
plt.title("Elblow Method for Optimal K")
plt.xlabel("No. of Clusters")
plt.ylabel("WCSS")
plt.grid(True)
plt.show()

#Calculating Silhouette Score
plt.figure()
plt.plot(range(2, 11), silhouette_scores, marker = 'o')
plt.title("Silhouette Scores for each K")
plt.xlabel("No of Clusters (K)")
plt.ylabel("Silhouette Score")
plt.grid(True)
plt.show()

# Fit KMeans with Chose K (K=4)
k_optimal = 4
kmeans = KMeans(n_clusters = k_optimal, random_state = 42)
cluster_labels = kmeans.fit_predict(scaled_df)
rfm['Cluster'] = cluster_labels

# PCA for visualization
pca = PCA(n_components = 2)
pca_components = pca.fit_transform(scaled_df)
rfm['PCA1'] = pca_components[: , 0]
rfm['PCA2'] = pca_components[: , 1]

plt.figure()
sns.scatterplot(data = rfm, x = 'PCA1', y = 'PCA2', hue = 'Cluster', palette = 'Set1', legend = 'full')
plt.title('Customer Segments PCA 2D')
plt.show()

# Profiling Clusters
cluster_summary = rfm.groupby('Cluster')[features].mean()
cluster_summary['Count'] = rfm.groupby('Cluster')['CustomerID'].count()
print(cluster_summary)

# Saving resulting dataset
rfm.to_csv('D:/Git/Infotact-Solutions-Project-2/Data/Cleaned/Customer_Segments.csv', index = False)
df.to_csv('D:/Git/Infotact-Solutions-Project-2/Data/Cleaned/Cleaned_BrightNest.csv', index = False)

