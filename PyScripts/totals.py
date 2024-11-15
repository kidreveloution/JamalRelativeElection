import pandas as pd
import json

# Load the dataset
file_path = '/Users/alyeldinshahin/Documents/GitHub/JamalElection/SupplementalData/PerPrecinctClean.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Rename columns for easier reference
data.columns = ['Precinct Name', 'Voting Type', 'Jamal_Aljahmi_Votes', 
                'Amer_Zahr_Votes', 'Robin_Makled_Votes', 'Total_Votes']

# Filter the dataset to include only rows with 'Total' in the 'Voting Type' column
total_rows = data[data['Voting Type'].str.contains("Total", na=False)]

# Dictionary to store the 'Total' rows grouped by precinct
total_data = {}
for _, row in total_rows.iterrows():
    precinct = row['Precinct Name']
    jamal_votes = int(row['Jamal_Aljahmi_Votes'])
    amer_votes = int(row['Amer_Zahr_Votes'])
    robin_votes = int(row['Robin_Makled_Votes'])
    total_votes = int(row['Total_Votes'])

    # Calculate percentages
    jamal_percent = round((jamal_votes / total_votes) * 100, 2) if total_votes > 0 else 0
    amer_percent = round((amer_votes / total_votes) * 100, 2) if total_votes > 0 else 0
    robin_percent = round((robin_votes / total_votes) * 100, 2) if total_votes > 0 else 0

    # Add data to dictionary
    total_data[precinct] = {
        "Jamal_Aljahmi_Votes": jamal_votes,
        "Jamal_Aljahmi_Percent": f"{jamal_percent}%",
        "Amer_Zahr_Votes": amer_votes,
        "Amer_Zahr_Percent": f"{amer_percent}%",
        "Robin_Makled_Votes": robin_votes,
        "Robin_Makled_Percent": f"{robin_percent}%",
        "Total_Votes": total_votes
    }

# Save the 'Total' data to a JSON file
output_file_path = 'total_votes.json'  # Replace with your desired output file path
with open(output_file_path, 'w') as json_file:
    json.dump(total_data, json_file, indent=4)

print(f"Total votes data with percentages has been saved to {output_file_path}")
