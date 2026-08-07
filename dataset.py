import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# -------------------------------
# Configuration
# -------------------------------

NUM_RECORDS = 100000
random.seed(42)
np.random.seed(42)

# -------------------------------
# Master Data
# -------------------------------

banks = [
    "SBI",
    "HDFC",
    "ICICI",
    "Axis",
    "Kotak",
    "PNB",
    "Canara",
    "Bank of Baroda",
    "Union Bank",
    "IndusInd"
]

states = {
    "Maharashtra": ["Mumbai", "Pune", "Nagpur"],
    "Karnataka": ["Bengaluru", "Mysuru", "Hubli"],
    "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai"],
    "Delhi": ["New Delhi"],
    "West Bengal": ["Kolkata", "Durgapur", "Siliguri"],
    "Gujarat": ["Ahmedabad", "Surat", "Vadodara"],
    "Uttar Pradesh": ["Lucknow", "Kanpur", "Noida"],
    "Telangana": ["Hyderabad", "Warangal"],
    "Rajasthan": ["Jaipur", "Jodhpur"],
    "Kerala": ["Kochi", "Trivandrum"]
}

merchant_categories = [
    "Grocery",
    "Food",
    "Shopping",
    "Fuel",
    "Recharge",
    "Travel",
    "Healthcare",
    "Education",
    "Entertainment",
    "Utilities"
]

payment_methods = [
    "QR Code",
    "UPI ID",
    "Phone Number",
    "Intent",
    "Collect Request"
]

device_types = [
    "Android",
    "iPhone"
]

customer_types = [
    "New",
    "Existing"
]

age_groups = [
    "18-25",
    "26-35",
    "36-45",
    "46-60",
    "60+"
]

status = [
    "Success",
    "Failed",
    "Pending"
]

status_weights = [
    0.92,
    0.06,
    0.02
]

# -------------------------------
# Random Date Function
# -------------------------------

start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)

def random_date():
    delta = end_date - start_date
    seconds = random.randint(0, int(delta.total_seconds()))
    return start_date + timedelta(seconds=seconds)

# -------------------------------
# Generate Dataset
# -------------------------------

data = []

for i in range(NUM_RECORDS):

    state = random.choice(list(states.keys()))
    city = random.choice(states[state])

    amount = round(np.random.exponential(scale=800), 2)

    amount = max(10, min(amount, 50000))

    row = {
        "Transaction_ID": f"TXN{i+1:07d}",
        "DateTime": random_date(),
        "State": state,
        "City": city,
        "Sender_Bank": random.choice(banks),
        "Receiver_Bank": random.choice(banks),
        "Merchant_Category": random.choice(merchant_categories),
        "Payment_Method": random.choice(payment_methods),
        "Amount": amount,
        "Status": random.choices(status, weights=status_weights)[0],
        "Device_Type": random.choice(device_types),
        "Customer_Type": random.choice(customer_types),
        "Age_Group": random.choice(age_groups),
        "Fraud_Flag": np.random.choice(
            ["Yes", "No"],
            p=[0.01, 0.99]
        )
    }

    data.append(row)

# -------------------------------
# Create DataFrame
# -------------------------------

df = pd.DataFrame(data)

# Sort by date
df = df.sort_values("DateTime")

# Save CSV
df.to_csv("upi_transactions.csv", index=False)

print("Dataset Created Successfully!")
print(df.head())
print(f"\nTotal Records: {len(df)}")