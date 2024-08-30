import pandas as pd
import re
import json

def load_json_data(json_filename):
    with open(json_filename, 'r') as file:
        return json.load(file)

def extract_name(email, email_to_name_mapping):
    for name, emails in email_to_name_mapping.items():
        if email in emails:
            return name
    return "Unknown"

def parse_email_to_name_mapping(mapping_file):
    email_to_name_mapping = {}
    with open(mapping_file, 'r') as file:
        for line in file:
            match = re.findall(r"<([^>]+)>", line)
            name = re.sub(r"<[^>]+>", "", line).strip()
            email_to_name_mapping[name] = match
    return email_to_name_mapping

def create_authorship_table(json_data, email_to_name_mapping):
    # Extracting users data
    users_data = json_data["users"]
    
    # Mapping emails to names
    table_data = []
    for user in users_data:
        name = extract_name(user["email"], email_to_name_mapping)
        table_data.append({
            "Name": name,
            "Email": user["email"],
            "Authorship": user["authorship"],
            "Normalized Authorship": user["normalizedAuthorship"]
        })
    
    # Convert the data to a DataFrame
    df = pd.DataFrame(table_data)
    
    return df

def save_table_to_csv(df, output_file):
    df.to_csv(output_file, index=False)

# Example usage:
if __name__ == "__main__":
    # Assume `json_data` is already loaded from the JSON file
    json_data = load_json_data('astropy_astropy_bus_factor.json')
    
    # Path to the email-to-name mapping file
    mapping_file = "astropy.mailmap"
    
    # Path to the output CSV file
    output_csv = "astropy_authorship_table.csv"
    
    # Parse the email to name mapping
    email_to_name_mapping = parse_email_to_name_mapping(mapping_file)
    
    # Create the authorship table
    authorship_df = create_authorship_table(json_data, email_to_name_mapping)
    
    # Save the table to a CSV file
    save_table_to_csv(authorship_df, output_csv)
