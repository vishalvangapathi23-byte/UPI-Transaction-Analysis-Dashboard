import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------
# Load Dataset
# ---------------------------------------

df = pd.read_csv("cleaned_upi_transactions.csv")

plt.style.use("ggplot")

print("=" * 60)
print("UPI TRANSACTION ANALYSIS")
print("=" * 60)

print("\nDataset Shape")
print(df.shape)

print("\nColumns")
print(df.columns)

print("\nFirst Five Records")
print(df.head())

print("\nDataset Information")
print(df.info())

print("\nStatistical Summary")
print(df.describe())

# ---------------------------------------
# Total Transactions
# ---------------------------------------

total_transactions = len(df)

print("\nTotal Transactions :", total_transactions)

# ---------------------------------------
# Total Amount
# ---------------------------------------

total_amount = df["Amount"].sum()

print("Total Transaction Amount : ₹{:,.2f}".format(total_amount))

# ---------------------------------------
# Average Amount
# ---------------------------------------

average_amount = df["Amount"].mean()

print("Average Transaction Amount : ₹{:.2f}".format(average_amount))

# ---------------------------------------
# Highest Transaction
# ---------------------------------------

highest_amount = df["Amount"].max()

print("Highest Transaction : ₹{}".format(highest_amount))

# ---------------------------------------
# Lowest Transaction
# ---------------------------------------

lowest_amount = df["Amount"].min()

print("Lowest Transaction : ₹{}".format(lowest_amount))

# ---------------------------------------
# Transaction Status
# ---------------------------------------

status = df["Status"].value_counts()

print("\nTransaction Status")
print(status)

plt.figure(figsize=(7,5))
status.plot(kind="bar")

plt.title("Transaction Status")
plt.xlabel("Status")
plt.ylabel("Count")

plt.tight_layout()
plt.show()

# ---------------------------------------
# Monthly Transactions
# ---------------------------------------

monthly = df.groupby("Month")["Amount"].sum()

month_order = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

monthly = monthly.reindex(month_order)

plt.figure(figsize=(12,5))

monthly.plot(marker="o")

plt.title("Monthly Transaction Amount")

plt.xlabel("Month")

plt.ylabel("Amount")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()

# ---------------------------------------
# Bank Performance
# ---------------------------------------

bank = df.groupby("Sender_Bank")["Amount"].sum()

bank = bank.sort_values(ascending=False)

print("\nTop Banks")

print(bank)

plt.figure(figsize=(10,5))

bank.plot(kind="bar")

plt.title("Bank-wise Transaction Amount")

plt.xlabel("Bank")

plt.ylabel("Amount")

plt.tight_layout()

plt.show()

# ---------------------------------------
# Merchant Category
# ---------------------------------------

merchant = df.groupby("Merchant_Category")["Amount"].sum()

merchant = merchant.sort_values()

plt.figure(figsize=(8,5))

merchant.plot(kind="barh")

plt.title("Merchant Category Performance")

plt.xlabel("Amount")

plt.tight_layout()

plt.show()

# ---------------------------------------
# Payment Methods
# ---------------------------------------

payment = df["Payment_Method"].value_counts()

plt.figure(figsize=(7,7))

payment.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")

plt.title("Payment Method Distribution")

plt.tight_layout()

plt.show()

# ---------------------------------------
# State Analysis
# ---------------------------------------

state = df.groupby("State")["Amount"].sum()

state = state.sort_values()

plt.figure(figsize=(9,6))

state.plot(kind="barh")

plt.title("State-wise Transaction Amount")

plt.tight_layout()

plt.show()

# ---------------------------------------
# City Analysis
# ---------------------------------------

city = df.groupby("City")["Amount"].sum()

city = city.sort_values(ascending=False)

print("\nTop Cities")

print(city.head(10))

plt.figure(figsize=(10,6))

city.head(10).plot(kind="bar")

plt.title("Top 10 Cities")

plt.ylabel("Amount")

plt.tight_layout()

plt.show()

# ---------------------------------------
# Hourly Transactions
# ---------------------------------------

hour = df.groupby("Hour")["Transaction_ID"].count()

plt.figure(figsize=(12,5))

hour.plot(marker="o")

plt.title("Transactions by Hour")

plt.xlabel("Hour")

plt.ylabel("Transactions")

plt.grid(True)

plt.tight_layout()

plt.show()

# ---------------------------------------
# Weekday Analysis
# ---------------------------------------

weekday = df.groupby("Weekday")["Amount"].sum()

weekday = weekday.reindex([
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
])

plt.figure(figsize=(10,5))

weekday.plot(kind="bar")

plt.title("Weekday Transaction Amount")

plt.tight_layout()

plt.show()

# ---------------------------------------
# Device Analysis
# ---------------------------------------

device = df["Device_Type"].value_counts()

plt.figure(figsize=(6,6))

device.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Device Usage")

plt.ylabel("")

plt.tight_layout()

plt.show()

# ---------------------------------------
# Customer Type
# ---------------------------------------

customer = df["Customer_Type"].value_counts()

plt.figure(figsize=(6,4))

customer.plot(kind="bar")

plt.title("Customer Type")

plt.tight_layout()

plt.show()

# ---------------------------------------
# Amount Category
# ---------------------------------------

amount_category = df["Amount_Category"].value_counts()

plt.figure(figsize=(7,5))

amount_category.plot(kind="bar")

plt.title("Amount Categories")

plt.tight_layout()

plt.show()

# ---------------------------------------
# Time Slot
# ---------------------------------------

slot = df.groupby("Time_Slot")["Amount"].sum()

slot = slot.reindex([
    "Morning",
    "Afternoon",
    "Evening",
    "Night"
])

plt.figure(figsize=(8,5))

slot.plot(kind="bar")

plt.title("Time Slot Transaction Amount")

plt.tight_layout()

plt.show()

# ---------------------------------------
# Fraud Analysis
# ---------------------------------------

fraud = df["Fraud_Flag"].value_counts()

print("\nFraud Cases")

print(fraud)

plt.figure(figsize=(6,4))

fraud.plot(kind="bar")

plt.title("Fraud Transactions")

plt.tight_layout()

plt.show()

# ---------------------------------------
# Success Rate
# ---------------------------------------

success = (df["Status"] == "Success").sum()

failed = (df["Status"] == "Failed").sum()

pending = (df["Status"] == "Pending").sum()

success_rate = (success / total_transactions) * 100

failure_rate = (failed / total_transactions) * 100

print("\nSuccess Rate : {:.2f}%".format(success_rate))

print("Failure Rate : {:.2f}%".format(failure_rate))

# ---------------------------------------
# Top Merchant Categories
# ---------------------------------------

print("\nTop Merchant Categories")

print(df["Merchant_Category"].value_counts())

# ---------------------------------------
# Top Payment Methods
# ---------------------------------------

print("\nPayment Methods")

print(df["Payment_Method"].value_counts())

# ---------------------------------------
# Summary Report
# ---------------------------------------

summary = pd.DataFrame({

    "Metric":[

        "Total Transactions",

        "Total Amount",

        "Average Amount",

        "Highest Amount",

        "Lowest Amount",

        "Successful Transactions",

        "Failed Transactions",

        "Pending Transactions",

        "Success Rate",

        "Failure Rate",

        "Fraud Cases"

    ],

    "Value":[

        total_transactions,

        total_amount,

        average_amount,

        highest_amount,

        lowest_amount,

        success,

        failed,

        pending,

        round(success_rate,2),

        round(failure_rate,2),

        (df["Fraud_Flag"]=="Yes").sum()

    ]

})

summary.to_csv("summary_report.csv", index=False)

print("\nSummary Report Saved Successfully!")

print(summary)

print("\nEDA Completed Successfully!")