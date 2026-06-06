import pandas as pd
import matplotlib.pyplot as plt

# =========================
# LOAD DATA
# =========================

df = pd.read_csv(
    r"C:\Users\ELCOT\Documents\coffee_sales.csv"
)

# Revenue Column
df["revenue"] = (
    df["transaction_qty"] *
    df["unit_price"]
)

# Date Conversion
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

df["month"] = (
    df["transaction_date"]
    .dt.month
)

df["day"] = (
    df["transaction_date"]
    .dt.day_name()
)

# =========================
# KPI VALUES
# =========================

total_revenue = df["revenue"].sum()

total_products = (
    df["product_category"]
    .nunique()
)

total_stores = (
    df["store_location"]
    .nunique()
)

# =========================
# AGGREGATIONS
# =========================

product_sales = (
    df.groupby("product_category")
    ["revenue"]
    .sum()
)

store_sales = (
    df.groupby("store_location")
    ["revenue"]
    .sum()
)

monthly_sales = (
    df.groupby("month")
    ["revenue"]
    .sum()
)

daily_sales = (
    df.groupby("day")
    ["revenue"]
    .sum()
)

# =========================
# COLORS
# =========================

BG = "#14081d"
CARD = "#251133"

PINK = "#ff4da6"
LIGHT_PINK = "#ff99cc"
PURPLE = "#c44dff"

plt.style.use("dark_background")

# =========================
# DASHBOARD
# =========================

fig, axes = plt.subplots(
    3,
    2,
    figsize=(16,12)
)

fig.patch.set_facecolor(BG)

for row in axes:
    for ax in row:
        ax.set_facecolor(CARD)

# =========================
# CHART 1
# PRODUCT REVENUE
# =========================

axes[0,0].bar(
    product_sales.index,
    product_sales.values,
    color=PINK
)

axes[0,0].set_title(
    "Product Revenue",
    color="white",
    fontsize=14
)

axes[0,0].tick_params(
    axis="x",
    rotation=45
)

# =========================
# CHART 2
# STORE PIE
# =========================

axes[0,1].pie(
    store_sales.values,
    labels=store_sales.index,
    autopct="%1.1f%%",
    colors=[
        PINK,
        PURPLE,
        LIGHT_PINK
    ]
)

axes[0,1].set_title(
    "Store Revenue Share"
)

# =========================
# CHART 3
# MONTHLY LINE
# =========================

axes[1,0].plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o",
    linewidth=3,
    color=LIGHT_PINK
)

axes[1,0].set_title(
    "Monthly Revenue"
)

# =========================
# CHART 4
# DAILY BARH
# =========================

axes[1,1].barh(
    daily_sales.index,
    daily_sales.values,
    color=PURPLE
)

axes[1,1].set_title(
    "Daily Revenue"
)

# =========================
# CHART 5
# AREA CHART
# =========================

axes[2,0].fill_between(
    range(len(product_sales)),
    product_sales.values,
    color=PINK,
    alpha=0.7
)

axes[2,0].set_xticks(
    range(len(product_sales))
)

axes[2,0].set_xticklabels(
    product_sales.index,
    rotation=45
)

axes[2,0].set_title(
    "Revenue Area Chart"
)

# =========================
# CHART 6
# DONUT CHART
# =========================

axes[2,1].pie(
    product_sales.values,
    labels=product_sales.index,
    autopct="%1.1f%%",
    colors=[
        PINK,
        PURPLE,
        LIGHT_PINK
    ]
)

centre_circle = plt.Circle(
    (0,0),
    0.65,
    fc=CARD
)

axes[2,1].add_artist(
    centre_circle
)

axes[2,1].set_title(
    "Top Products"
)

# =========================
# TITLE
# =========================

fig.suptitle(
    "COFFEE SHOP SALES DASHBOARD",
    fontsize=22,
    color=PINK,
    fontweight="bold"
)

# =========================
# KPI CARDS
# =========================

fig.text(
    0.12,
    0.92,
    f"Revenue\n{total_revenue:,.0f}",
    fontsize=14,
    bbox=dict(
        facecolor=PINK,
        alpha=0.5
    )
)

fig.text(
    0.42,
    0.92,
    f"Products\n{total_products}",
    fontsize=14,
    bbox=dict(
        facecolor=PURPLE,
        alpha=0.5
    )
)

fig.text(
    0.72,
    0.92,
    f"Stores\n{total_stores}",
    fontsize=14,
    bbox=dict(
        facecolor=LIGHT_PINK,
        alpha=0.5
    )
)

plt.tight_layout()
plt.show()
