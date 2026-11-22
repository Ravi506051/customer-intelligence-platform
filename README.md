# Customer Intelligence Platform

A Streamlit dashboard for exploring customer spend, order frequency, purchase recency, and simple customer segments.

## What it shows

- Starts with deterministic synthetic sample data (1,200 records, seed 42) or accepts a customer CSV.
- Calculates average order value and divides customers into spend-based quartiles.
- Shows customer count, total spend, and customers with more than 180 days since purchase.
- Compares spend by segment and recency by region.
- Exports the enriched customer table as CSV.

## Input data

For an uploaded CSV, provide numeric `spend`, `orders`, and `recency_days` columns plus a `region` column. The app derives average order value and spend quartile labels. The segment labels are exploratory spend groups; they are not a full RFM model.

## Run locally

```bash
python -m venv .venv
pip install -r requirements.txt
streamlit run app.py
```

## Scope

The built-in dataset is synthetic. Uploaded data is summarized in the app session and exported by the user; review the data before sharing the CSV. This dashboard is an analytics demo, not a customer-level decision system.

## Maintainer

Ravi Kumar Rao · [GitHub](https://github.com/Ravi506051)
