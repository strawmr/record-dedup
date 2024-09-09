import pandas as pd

# Step 1: Read the two CSV files
df1 = pd.read_csv('file1.csv')  # Replace 'file1.csv' with the path to your first file
df2 = pd.read_csv('file2.csv')  # Replace 'file2.csv' with the path to your second file

# Step 2: Identify unique new records in the second DataFrame
# Remove records in df2 that already exist in df1
df2_unique = df2[~df2['Email'].isin(df1['Email'])]


# Step 3: Remove any remaining duplicates (just in case)
df2_unique_cleaned = df2_unique.drop_duplicates(subset=['Email'])

# Step 4: Save the cleaned, merged DataFrame to a new CSV file
df2_unique_cleaned.to_csv('unique_emails.csv', index=False)

print("Unique records from the second file added, duplicates removed, and saved to 'unique_emails.csv'.")
