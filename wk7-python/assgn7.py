import pandas as pd
import matplotlib.pyplot as plt
import os

# File path
file_path = "C:\\Users\\dell\\desktop\\CODING PROJECTS\\PLP CODES\\PYTHON PROG\\ASSGNS\\wk7-python\\makeup_sales.csv"

# Initialize the DataFrame (this is a safety check)
df = None

# Task 1: Load and Explore the Dataset
if os.path.exists(file_path):
    try:
        # Load the dataset
        df = pd.read_csv(file_path)
        print("✅ Data loaded successfully!\n")
        print("📌 First 5 rows:")
        print(df.head())

        # Explore the structure of the dataset (data types and missing values)
        print("\n🔍 Dataset Info:")
        print(df.info())  # Get data types and non-null counts

        print("\n📊 Checking for missing values:")
        print(df.isnull().sum())  # Check for any missing values

        # Clean the dataset by filling or dropping missing values (example of dropping missing)
        df.dropna(inplace=True)  # Or df.fillna(method='ffill', inplace=True) if you want to fill

    except Exception as e:  # Handle any error while loading the file
        print(f"❌ An error occurred: {e}")
else:
    print("🚫 File not found. Make sure 'makeup_sales.csv' is in the same folder as your .py file.")

# Task 2: Basic Data Analysis
if df is not None:
    print("\n🔍 Basic Statistics:")
    print(df.describe())  # Basic stats for numerical columns

    # Example of groupings on a categorical column (e.g., 'Product' column)
    print("\n📊 Average Sales per Product:")
    print(df.groupby('Product')['Units_Sold'].mean())  # Mean units sold per product

# Task 3: Data Visualization
if df is not None:
    # Line chart showing trends (assuming you have a 'Date' column)
    plt.figure(figsize=(10, 6))
    # If there's a 'Date' column, use it for plotting
    # df['Date'] = pd.to_datetime(df['Date'])  # Uncomment if you have a 'Date' column
    # df.plot(x='Date', y='Units_Sold', kind='line')  # Replace with actual columns
    plt.title('Sales Trends Over Time')
    plt.xlabel('Date')
    plt.ylabel('Units Sold')
    plt.tight_layout()
    plt.show()

    # Bar chart for total units sold per product
    plt.figure(figsize=(10, 6))
    df.groupby('Product')['Units_Sold'].sum().plot(kind='bar', color='skyblue')
    plt.title('Total Units Sold per Product')
    plt.xlabel('Product')
    plt.ylabel('Total Units Sold')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Histogram for the distribution of 'Units Sold'
    plt.figure(figsize=(10, 6))
    df['Units_Sold'].plot(kind='hist', color='lightgreen', bins=15)
    plt.title('Distribution of Units Sold')
    plt.xlabel('Units Sold')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

    # Scatter plot for the relationship between two numerical columns (e.g., 'Price' vs. 'Units Sold')
    plt.figure(figsize=(10, 6))
    df.plot(kind='scatter', x='Price', y='Units_Sold', color='orange')
    plt.title('Price vs Units Sold')
    plt.xlabel('Price')
    plt.ylabel('Units Sold')
    plt.tight_layout()
    plt.show()

else:
    print("⚠️ Data analysis and visualization skipped due to file load error.")
