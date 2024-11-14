import json

# Load the geojson file directly as JSON
with open('Filtered_Dearborn_Precincts.geojson', 'r') as f:
    geojson_data = json.load(f)

# Replace NAME with Precinct_Long_Name in the properties of each feature
for feature in geojson_data.get('features', []):
    properties = feature.get('properties', {})
    long_precinct_name = properties.get('Precinct_Long_Name', '')
    properties['NAME'] = long_precinct_name  # Replace NAME with Precinct_Long_Name

# Save the modified GeoJSON data back to a file
output_geojson_path = 'Modified_Dearborn_Precincts.geojson'
with open(output_geojson_path, 'w') as f:
    json.dump(geojson_data, f, indent=2)

output_geojson_path
