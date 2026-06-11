import pandas as pd
import numpy as np
import random

random.seed(42)
np.random.seed(42)

vendors = [
    "Accenture", "Deloitte", "IBM", "Wipro", "Oracle Corp",
    "Amazon Web Services", "KPMG", "McKinsey & Co",
    "Tata Consultancy", "Infosys", "HCL Technologies",
    "Cognizant", "Microsoft", "Google Cloud", "Cisco Systems",
    "Salesforce", "ServiceNow", "Workday", "Adobe Systems", "SAP SE",
]

variants = {
    "Accenture":           ["Accenture", "Accenture Ltd", "Accenture Limited", "ACCENTURE"],
    "IBM":                 ["IBM", "I.B.M.", "IBM India", "IBM Ltd"],
    "Oracle Corp":         ["Oracle Corp", "Oracle Corporation", "Oracle", "ORACLE CORP"],
    "Wipro":               ["Wipro", "Wipro Ltd", "Wipro Limited", "WIPRO"],
    "Amazon Web Services": ["Amazon Web Services", "AWS", "Amazon AWS"],
    "Deloitte":            ["Deloitte", "Deloitte & Co", "Deloitte Consulting"],
}

categories   = ["IT Services", "Consulting", "Cloud", "Software Licenses",
                 "Hardware", "Facilities", "Marketing", "Legal"]
cost_centres = ["CC-101 Finance", "CC-102 Operations", "CC-103 IT",
                 "CC-104 HR", "CC-105 Marketing", "CC-106 Legal"]

contract_rates = {c: round(random.uniform(5000, 50000), 2) for c in categories}

rows = []
for i in range(1000):
    base = random.choice(vendors)
    name = random.choice(variants[base]) if base in variants else base
    cat  = random.choice(categories)
    cr   = contract_rates[cat]
    off  = random.random() < 0.12
    amt  = round(cr * random.uniform(1.06, 1.40), 2) if off \
           else round(cr * random.uniform(0.60, 1.00), 2)
    date = (pd.Timestamp("2024-01-01")
            + pd.Timedelta(days=random.randint(0, 364))).strftime("%Y-%m-%d")
    rows.append({
        "TransactionID": f"AP-{10000 + i}",
        "VendorName":    name,
        "Category":      cat,
        "CostCentre":    random.choice(cost_centres),
        "Amount":        amt,
        "ContractRate":  cr,
        "Date":          date,
        "Currency":      random.choice(["INR", "USD", "EUR"]),
    })

df = pd.DataFrame(rows)
df.to_csv("ap_transactions.csv", index=False)
print(f"Generated {len(df)} rows → ap_transactions.csv")
print(f"Off-contract rows: {(df['Amount'] > df['ContractRate'] * 1.05).sum()}")
