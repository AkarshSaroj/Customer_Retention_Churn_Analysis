import pandas as pd
import random

# Set seed for reproducibility
random.seed(42)

# Number of records
n = 1000

# Generate synthetic data
data = {
    "customer_id": [f"C{str(i).zfill(4)}" for i in range(1, n + 1)],
    "age": [random.randint(18, 65) for _ in range(n)],
    "gender": [random.choice(["Male", "Female", "Other"]) for _ in range(n)],
    "subscription_type": [random.choice(["Free", "Basic", "Premium"]) for _ in range(n)],
    "last_login_days": [random.randint(0, 60) for _ in range(n)],
}

# Define logic for churn probability
def determine_churn(days, sub_type):
    if days > 30:
        return "Yes" if random.random() < 0.7 else "No"
    elif sub_type == "Free":
        return "Yes" if random.random() < 0.4 else "No"
    else:
        return "Yes" if random.random() < 0.2 else "No"

# Add churn column based on logic
data["churn"] = [
    determine_churn(days, sub)
    for days, sub in zip(data["last_login_days"], data["subscription_type"])
]

# Create DataFrame and export
df = pd.DataFrame(data)
df.to_csv("churn_data.csv", index=False)

print("✅ churn_data.csv has been generated with", n, "records.")
