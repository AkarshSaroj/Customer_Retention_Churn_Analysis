import pandas as pd
import matplotlib.pyplot as plt

# Load and clean data
df = pd.read_csv("churn_data.csv")
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Prepare data
churn_by_subscription = df.groupby("subscription_type")["churn"].value_counts(normalize=True).unstack().fillna(0)

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
colors = ['#4C72B0', '#DD8452']  # Modern blue & orange

churn_by_subscription.plot(kind="bar", stacked=True, color=colors, ax=ax)

# Add labels inside bars
for i, col in enumerate(churn_by_subscription.columns):
    for j, value in enumerate(churn_by_subscription[col]):
        if value > 0:
            ax.text(j, churn_by_subscription.iloc[j, :i+1].sum() - value/2,
                    f'{value*100:.1f}%', color='white', ha='center', fontsize=10)

# Style
ax.set_title("Customer Churn Distribution by Subscription Type", fontsize=14, weight='bold')
ax.set_ylabel("Proportion of Customers")
ax.set_xlabel("Subscription Type")
ax.set_ylim(0, 1.05)
ax.legend(title="Churn", loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2)
ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig("churn_by_subscription.png", dpi=300)
plt.show()
