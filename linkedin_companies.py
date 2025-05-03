
# This is a simulated example. LinkedIn blocks scraping - use APIs or tools like PhantomBuster in real life.

companies = [
    {"name": "Google", "industry": "Tech", "employees": "100k+"},
    {"name": "Tesla", "industry": "Automotive", "employees": "70k+"},
]

import csv
with open("linkedin_companies.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "industry", "employees"])
    writer.writeheader()
    writer.writerows(companies)
