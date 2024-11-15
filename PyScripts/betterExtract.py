import os
import json
import pandas as pd

# Load the dataset with percentages
file_path_percent = '/Users/alyeldinshahin/Documents/GitHub/JamalElection/SupplementalData/PerPrecintPercent.csv'
data = pd.read_csv(file_path_percent)

# Rename columns for easier reference
data.columns = [
    'Precinct Name', 'Voting Type', 'Jamal_Aljahmi_Votes', 'Jamal_Aljahmi_Percent',
    'Amer_Zahr_Votes', 'Amer_Zahr_Percent', 'Robin_Makled_Votes', 
    'Robin_Makled_Percent', 'Total Votes'
]

# Filter out header rows and ensure all data is properly formatted
data = data[~data['Voting Type'].str.contains("Total|Voting Type", na=False)]

# Directory to save JSON files
output_dir = '/Users/alyeldinshahin/Documents/GitHub/JamalElection/VotingJson/temp'
os.makedirs(output_dir, exist_ok=True)

# Group by voting type and save each as a JSON file
for voting_type, group in data.groupby('Voting Type'):
    voting_data = {}
    for _, row in group.iterrows():
        precinct = row['Precinct Name']
        voting_data[precinct] = {
            "Jamal_Aljahmi_Votes": int(row['Jamal_Aljahmi_Votes']),
            "Jamal_Aljahmi_Percent": row['Jamal_Aljahmi_Percent'],
            "Amer_Zahr_Votes": int(row['Amer_Zahr_Votes']),
            "Amer_Zahr_Percent": row['Amer_Zahr_Percent'],
            "Robin_Makled_Votes": int(row['Robin_Makled_Votes']),
            "Robin_Makled_Percent": row['Robin_Makled_Percent'],
            "Total_Votes": int(row['Total Votes'])
        }
    
    # Save to JSON file
    file_name = f"{voting_type.replace(' ', '_').lower()}_data.json"
    file_path = os.path.join(output_dir, file_name)
    with open(file_path, 'w') as json_file:
        json.dump(voting_data, json_file, indent=4)

print(f"Data with percentages saved in {output_dir}")
