import pandas as pd

# Load the CSV file
file_path = 'test_cloudflare_parse_product_0.csv' 
df = pd.read_csv(file_path)

# Remove rows where all columns are empty
df_cleaned = df.dropna(how='all')

# Save the cleaned DataFrame back to a CSV file
output_file = 'cleaned_file.csv'  # Replace with the desired output file path
df_cleaned.to_csv(output_file, index=False)

print("Cleaned file saved as:", output_file)
