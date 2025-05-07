# GIS Massachusetts Data Breach Analysis

This project extracts, geocodes, and analyzes data breach incidents affecting Massachusetts residents, focusing on local government, education, and healthcare organizations. It combines automated data extraction and geospatial processing to support GIS-based cybersecurity research.

## Project Overview

The dataset was sourced from public data breach reports published by mass.gov in PDF format. The project includes four main Python scripts:

### 1. `scraper.py`
- Extracts tabular data from two official PDF reports (2024 and 2025).
- Filters rows where the **Reporting Organization Type** is one of the following:
  - `Health Care`
  - `Educational`
  - `Local Government`
- Outputs the structured and filtered data to an Excel file.

### 2. `geocoder.py`
- Uses the **OpenCage Geocode API** to geocode the `Reporting Organization Name` field.
- Populates a new `Address` column with the full formatted address.
- Saves the output to a new Excel file with geocoded addresses.

### 3. `statistics.py`
- Analyzes the dataset to find:
  - Incidents that impacted the **most Massachusetts residents**.
- Outputs a sorted list or summary for reporting or mapping purposes.

### 4. `practice.py`
- Aggregates the number of breaches involving different types of sensitive information:
  - Social Security Numbers (SSN)
  - Financial Account Information
  - Driver’s License Numbers
  - Medical Records
- Helps visualize breach trends by data type.

## Dependencies
- `pandas`
- `pdfplumber`
- `opencage` (OpenCage Geocode API)

## How to Run
1. Run `scraper.py` to create the initial structured Excel file.
2. Run `geocoder.py` to append address information.
3. Use `statistics.py` and `practice.py` to generate analytics and summaries for mapping and presentation.

## Use Case
The output of this pipeline is designed for spatial analysis in GIS platforms (I used ArcGIS Pro). It supports identifying:
- Regional hotspots of sensitive data breaches
- Organization types most frequently targeted
- Data types most commonly exposed

## Author
Grace Smalley – Bridgewater State University  
Cybersecurity & GIS Research | Spring 2025  
