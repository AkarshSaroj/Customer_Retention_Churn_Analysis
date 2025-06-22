import pandas as pd
import matplotlib.pyplot as plt

# Load and clean data
df = pd.read_csv("churn_data.csv")
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

colors = ['#4C72B0', '#DD8452']  # Blue for 'No', Orange for 'Yes'

# 1. Churn by Subscription Type
churn_by_subscription = df.groupby("subscription_type")["churn"].value_counts(normalize=True).unstack().fillna(0)

fig1, ax1 = plt.subplots(figsize=(10, 6))
churn_by_subscription.plot(kind="bar", stacked=True, color=colors, ax=ax1)
for i, col in enumerate(churn_by_subscription.columns):
    for j, value in enumerate(churn_by_subscription[col]):
        if value > 0:
            ax1.text(j, churn_by_subscription.iloc[j, :i+1].sum() - value/2,
                     f'{value*100:.1f}%', color='white', ha='center', fontsize=10)
ax1.set_title("Customer Churn Distribution by Subscription Type", fontsize=14, weight='bold')
ax1.set_ylabel("Proportion of Customers")
ax1.set_xlabel("Subscription Type")
ax1.set_ylim(0, 1.05)
ax1.legend(title="Churn", loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2)
ax1.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("churn_by_subscription.png", dpi=300)

# 2. Churn by Gender
churn_by_gender = df.groupby("gender")["churn"].value_counts(normalize=True).unstack().fillna(0)

fig2, ax2 = plt.subplots(figsize=(10, 6))
churn_by_gender.plot(kind="bar", stacked=True, color=colors, ax=ax2)
for i, col in enumerate(churn_by_gender.columns):
    for j, value in enumerate(churn_by_gender[col]):
        if value > 0:
            ax2.text(j, churn_by_gender.iloc[j, :i+1].sum() - value/2,
                     f'{value*100:.1f}%', color='white', ha='center', fontsize=10)
ax2.set_title("Customer Churn Distribution by Gender", fontsize=14, weight='bold')
ax2.set_ylabel("Proportion of Customers")
ax2.set_xlabel("Gender")
ax2.set_ylim(0, 1.05)
ax2.legend(title="Churn", loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2)
ax2.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("churn_by_gender.png", dpi=300)

# 3. Churn by Last Login Bins (0–5, 6–10, ..., 56–60)
df['login_bin'] = pd.cut(df['last_login_days'], bins=range(0, 66, 5), right=False)

churn_by_bin = df.groupby(['login_bin', 'churn']).size().unstack().fillna(0)

fig3, ax3 = plt.subplots(figsize=(12, 6))
churn_by_bin.plot(kind='bar', stacked=True, color=colors, ax=ax3)
ax3.set_title("Customer Churn Distribution by Last Login (Grouped)", fontsize=14, weight='bold')
ax3.set_ylabel("Number of Customers")
ax3.set_xlabel("Days Since Last Login (Grouped)")
ax3.legend(title="Churn", loc='upper right')
ax3.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("churn_by_last_login.png", dpi=300)

