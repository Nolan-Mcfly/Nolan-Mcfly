import csv

input_file = 'input.csv'  # The name of your input CSV file
output_file = 'output.csv'  # The name of the file to output to

# Open the input CSV file for reading
with open(input_file, mode='r', newline='') as infile:
    # Open the output CSV file for writing
    with open(output_file, mode='w', newline='') as outfile:
        # Create a CSV reader and writer
        reader = csv.reader(infile, delimiter=';')
        writer = csv.writer(outfile, delimiter=';')
        
        # Iterate over each row in the input CSV
        for row in reader:
            # Replace the FQDN in the second column (index 1) with 'generic.domain.com'
            row[1] = 'generic.domain.com'
            # Write the modified row to the output CSV
            writer.writerow(row)

print(f'File processed. The modified data is saved in {output_file}')
