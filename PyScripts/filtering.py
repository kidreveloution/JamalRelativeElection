import json

# Path to your GeoJSON file
file_path = '2024_Voting_Precincts.geojson'

# Load the GeoJSON data
with open(file_path, 'r') as f:
    precincts_data = json.load(f)

# Filter for entries where 'Precinct_Long_Name' contains 'Dearborn'
filtered_data = [
    feature for feature in precincts_data['features']
    if isinstance(feature['properties'].get('Precinct_Long_Name'), str) and 'City of Dearborn,' in feature['properties']['Precinct_Long_Name']
]

# Update the GeoJSON structure with filtered data
precincts_data['features'] = filtered_data

# Save the filtered data to a new GeoJSON file
output_path = 'Filtered_Dearborn_Precincts.geojson'
with open(output_path, 'w') as f:
    json.dump(precincts_data, f, indent=2)

print(f"Filtered data saved to {output_path}")
