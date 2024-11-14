import json
import pandas as pd 
# Load the geojson file directly as JSON
with open('Filtered_Dearborn_Precincts.geojson', 'r') as f:
    geojson_data = json.load(f)

# Extract Name and Long_Precinct_Name if they exist in properties
data = []
for feature in geojson_data.get('features', []):
    properties = feature.get('properties', {})
    name = properties.get('NAME', '')
    long_precinct_name = properties.get('Precinct_Long_Name', '')
    data.append({'NAME': name, 'Precinct_Long_Name': long_precinct_name})

# Convert to DataFrame
df = pd.DataFrame(data)

# Save the extracted data to a CSV
output_csv_path = 'Name_Long_Precinct_Name.csv'
df.to_csv(output_csv_path, index=False)

output_csv_path
