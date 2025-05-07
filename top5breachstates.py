import pandas as pd

# Load the updated Excel file
file_path = r"C:\Users\grace\PycharmProjects\dataBreachGIS\dataBreachesUSA_MAres_geocoded_updated.xlsx"
df = pd.read_excel(file_path)

# Extract the state from the Address column
df["State"] = df["Address"].str.extract(r",\s*([A-Z]{2})\s*,?\s*United States", expand=False)

# Count the frequency of each state, excluding any NaNs
state_counts = df["State"].value_counts().reset_index()
state_counts.columns = ["State", "Breach Count"]

# Save to a new Excel file
output_path = r"C:\Users\grace\PycharmProjects\dataBreachGIS\dataBreachesFrequency_AllStates.xlsx"
state_counts.to_excel(output_path, index=False)

state_counts.head(10)

