import pandas as pd

df = pd.read_csv("upi_transactions.csv")

print(df.head())
print(df.info())

print(df.isnull().sum())

df = df.dropna()

df = df.drop_duplicates()

df["DateTime"] = pd.to_datetime(df["DateTime"])

df["Year"] = df["DateTime"].dt.year
df["Month_Number"] = df["DateTime"].dt.month
df["Month"] = df["DateTime"].dt.month_name()
df["Quarter"] = df["DateTime"].dt.quarter
df["Day"] = df["DateTime"].dt.day
df["Weekday"] = df["DateTime"].dt.day_name()
df["Hour"] = df["DateTime"].dt.hour
df["Week"] = df["DateTime"].dt.isocalendar().week

df["Amount"] = pd.to_numeric(df["Amount"])

def amount_category(x):
    if x < 500:
        return "Low"
    elif x < 2000:
        return "Medium"
    elif x < 10000:
        return "High"
    else:
        return "Very High"

df["Amount_Category"] = df["Amount"].apply(amount_category)

def transaction_time(hour):
    if 5 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 17:
        return "Afternoon"
    elif 17 <= hour < 22:
        return "Evening"
    else:
        return "Night"

df["Time_Slot"] = df["Hour"].apply(transaction_time)

df["Success_Flag"] = df["Status"].apply(lambda x: 1 if x == "Success" else 0)
df["Failure_Flag"] = df["Status"].apply(lambda x: 1 if x == "Failed" else 0)
df["Fraud"] = df["Fraud_Flag"].map({"Yes": 1, "No": 0})

df.to_csv("cleaned_upi_transactions.csv", index=False)

print("\nData Cleaning Completed Successfully!")
print(f"Total Rows: {len(df)}")
print(f"Total Columns: {len(df.columns)}")