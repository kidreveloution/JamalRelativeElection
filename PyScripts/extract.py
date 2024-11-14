import pandas as pd
import json

# Load the Excel file
file_path = '/Users/alyeldinshahin/Desktop/JamalDataReview/SupplementalData/Per Precinct Data.xlsx'  # Replace with the actual file path
precinct_data = pd.read_excel(file_path, sheet_name=0)

# Rename columns for easier reference
precinct_data.columns = [
    "Precinct_Name", "Vote_Type", "Jamal_Aljahmi_Votes", "Jamal_Aljahmi_Percent", 
    "Amer_Zahr_Votes", "Amer_Zahr_Percent", "Robin_Makled_Votes", 
    "Robin_Makled_Percent", "Total_Votes"
]

# Fill down merged cells in the 'Precinct_Name' column
precinct_data['Precinct_Name'] = precinct_data['Precinct_Name'].fillna(method='ffill')

# Remove rows that do not contain relevant vote data (e.g., totals or headers)
precinct_data = precinct_data.dropna(subset=["Vote_Type"]).reset_index(drop=True)

# Function to transform the DataFrame into the specified dictionary format
def transform_to_dict(dataframe):
    result = {}
    for _, row in dataframe.iterrows():
        # Apply the replacement in precinct names
        precinct_name = row["Precinct_Name"].replace(" Of ", " of ")
        result[precinct_name] = {
            "Jamal_Aljahmi_Votes": int(row["Jamal_Aljahmi_Votes"]),
            "Amer_Zahr_Votes": int(row["Amer_Zahr_Votes"]),
            "Robin_Makled_Votes": int(row["Robin_Makled_Votes"])
        }
    return result

# Separate data by Vote_Type
early_voting_data = precinct_data[precinct_data["Vote_Type"] == "Early Voting"]
election_day_data = precinct_data[precinct_data["Vote_Type"] == "Election Day"]
absentee_data = precinct_data[precinct_data["Vote_Type"] == "Absentee"]

# Transform each DataFrame into a dictionary
early_voting_dict = transform_to_dict(early_voting_data)
election_day_dict = transform_to_dict(election_day_data)
absentee_dict = transform_to_dict(absentee_data)

# Print the dictionaries for each vote type
print("Early Voting Data:", early_voting_dict)
print("Election Day Data:", election_day_dict)
print("Absentee Data:", absentee_dict)

# Optionally, save each dictionary to a JSON file
with open('early_voting_data.json', 'w') as f:
    json.dump(early_voting_dict, f, indent=4)
with open('election_day_data.json', 'w') as f:
    json.dump(election_day_dict, f, indent=4)
with open('absentee_data.json', 'w') as f:
    json.dump(absentee_dict, f, indent=4)
