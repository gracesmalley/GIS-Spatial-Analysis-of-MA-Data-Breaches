import pandas as pd

# Load the Excel file
file_path = r"C:\Users\grace\PycharmProjects\dataBreachGIS\dataBreachesUSA_MAres_geocoded_updated.xlsx"
df = pd.read_excel(file_path)

# Clean up the "MA Residents Affected" column and convert to numeric
df["MA Residents Affected"] = pd.to_numeric(df["MA Residents Affected"], errors="coerce").fillna(0)

# Extract states from the "Address" column using last token before "United States"
df["State"] = df["Address"].str.extract(r",\s*([A-Z]{2})\s*,?\s*United States", expand=False)

# Get top 5 most impactful breaches (with all columns)
top_5_breaches_full = df.nlargest(5, "MA Residents Affected")

# Count frequency of each state
state_counts = df["State"].value_counts().reset_index()
state_counts.columns = ["State", "Breach Count"]

# Get state with most breaches impacting MA residents
top_state = state_counts.iloc[0]

# Save to Excel
output_path = r"C:\Users\grace\PycharmProjects\dataBreachGIS\dataBreachStatistics.xlsx"
top_5_breaches_full.to_excel(output_path, index=False)

print("\nTop 5 Most Impactful Breaches saved to:", output_path)
print("\nState with the Most Breaches Impacting MA Residents:\n", top_state)
