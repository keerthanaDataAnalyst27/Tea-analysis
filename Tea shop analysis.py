import pandas as pd
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv(r"C:\Users\ELCOT\Documents\coffee_sales.csv")

# Revenue
df["revenue"] = df["transaction_qty"] * df["unit_price"]

# Dashboard Layout
fig, axes = plt.subplots(2, 2, figsize=(14, 8))

fig.suptitle(
    "TEA SHOP SALES ANALYSIS DASHBOARD",
    fontsize=18,
    fontweight="bold"
)

# -------------------------
# Chart 1 - Product Revenue
# -------------------------

product_sales = df.groupby(
    "product_category"
)["revenue"].sum()

axes[0,0].bar(
    product_sales.index,
    product_sales.values,
    color=["red","blue","green","orange","purple"]
)

axes[0,0].set_title("Product Wise Revenue")
axes[0,0].set_ylabel("Revenue")
axes[0,0].tick_params(axis="x", rotation=45)

# -------------------------
# Chart 2 - Monthly Revenue
# -------------------------

df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

df["month"] = df["transaction_date"].dt.strftime("%b")

month_sales = df.groupby(
    "month"
)["revenue"].sum()

axes[0,1].plot(
    month_sales.index,
    month_sales.values,
    marker="o",
    linewidth=3
)

axes[0,1].set_title("Monthly Revenue Trend")
axes[0,1].set_ylabel("Revenue")

# -------------------------
# Chart 3 - Store Revenue
# -------------------------

store_sales = df.groupby(
    "store_location"
)["revenue"].sum()

axes[1,0].pie(
    store_sales.values,
    labels=store_sales.index,
    autopct="%1.1f%%"
)

axes[1,0].set_title("Store Revenue Share")

# -------------------------
# Chart 4 - Hour Revenue
# -------------------------

df["hour"] = pd.to_datetime(
    df["transaction_time"],
    format="%H:%M:%S"
).dt.hour

hour_sales = df.groupby(
    "hour"
)["revenue"].sum()

axes[1,1].bar(
    hour_sales.index,
    hour_sales.values,
    color="skyblue"
)

axes[1,1].set_title("Hourly Revenue")
axes[1,1].set_xlabel("Hour")
axes[1,1].set_ylabel("Revenue")

plt.tight_layout()

plt.show()
