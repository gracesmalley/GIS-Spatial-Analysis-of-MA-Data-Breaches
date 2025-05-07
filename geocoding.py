import pandas as pd
from opencage.geocoder import OpenCageGeocode
import time

# File paths
input_file = r"C:\Users\grace\PycharmProjects\dataBreachGIS\dataBreachesUSA_MAres_geocoded_updated.xlsx"
output_file = r"C:\Users\grace\PycharmProjects\dataBreachGIS\dataBreachesUSA_MAres_filtered.xlsx"

# API key
api_key = "YOUR_API_KEY_HERE"  # Replace with your actual key
geocoder = OpenCageGeocode(api_key)

# Load the data
df = pd.read_excel(input_file)

# Create the Address column if it doesn't exist
if "Address" not in df.columns:
    df["Address"] = None

# Only geocode if address is missing and organization name is present
missing_mask = df["Address"].isna() & df["Reporting Organization Name"].notna()
print(f"Geocoding {missing_mask.sum()} missing addresses...")

for idx in df[missing_mask].index:
    org_name = df.at[idx, "Reporting Organization Name"]
    try:
        query = org_name.strip() + ", United States"
        results = geocoder.geocode(query)
        if results:
            formatted_address = results[0].get("formatted")
            df.at[idx, "Address"] = formatted_address
            print(f"{org_name} → {formatted_address}")
        else:
            print(f"No result for {org_name}")
    except Exception as e:
        print(f"Error geocoding {org_name}: {e}")

    time.sleep(1.1)  # Respect OpenCage rate limits

# Save cleaned output
df.to_excel(output_file, index=False)
print(f" Geocoded data saved to:\n{output_file}")

