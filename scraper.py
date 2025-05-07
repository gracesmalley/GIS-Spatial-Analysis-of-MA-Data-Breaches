import pdfplumber
import pandas as pd

# File paths
file_paths = [
    r"C:\Users\grace\Downloads\DataBreaches2024.pdf",
    r"C:\Users\grace\Downloads\DataBreaches2025.pdf"
]

# Target organization types
target_types = {"Local Government", "Educational", "Health Care"}

# Desired output columns
desired_columns = [
    "Breach Number",
    "Date Reported to OCA",
    "Reporting Organization Name",
    "Reporting Organization Type",
    "MA Residents Affected",
    "SSN Breached",
    "Medical Records Breached",
    "Financial Account Breached",
    "Driver's License Breached",
    "Town"
]

# Clean a valid row into a dictionary
def clean_row(row):
    return {
        "Breach Number": row[0],
        "Date Reported to OCA": row[1],
        "Reporting Organization Name": row[2],
        "Reporting Organization Type": row[3],
        "MA Residents Affected": row[4],
        "SSN Breached": row[5],
        "Medical Records Breached": row[6],
        "Financial Account Breached": row[7],
        "Driver's License Breached": row[8],
        "Town": None
    }

# Extract data from one PDF
def extract_target_orgs(file_path):
    results = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            for table in page.extract_tables():
                for row in table:
                    if row and len(row) >= 9 and any(t in row for t in target_types):
                        results.append(clean_row(row))
    return results

# Extract and combine from both PDFs
all_data = []
for path in file_paths:
    all_data.extend(extract_target_orgs(path))

# Create DataFrame and reorder columns
df = pd.DataFrame(all_data)[desired_columns]

# Save to Excel
df.to_excel("dataBreachesUSA_MAres.xlsx", index=False)
print("Saved as dataBreachesUSA_MAres.xlsx")

# Optional: print a preview to console
print(df.to_string(index=False))

