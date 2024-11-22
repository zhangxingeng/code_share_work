import re

# Mapping Oracle month abbreviations to numerical values
month_map = {
    'JAN': '01', 'FEB': '02', 'MAR': '03', 'APR': '04',
    'MAY': '05', 'JUN': '06', 'JUL': '07', 'AUG': '08',
    'SEP': '09', 'OCT': '10', 'NOV': '11', 'DEC': '12'
}

def convert_to_pgsql_date(line):
    """
    Converts an Oracle TO_DATE to a PostgreSQL DATE format within a SQL INSERT line.
    """
    # Define the regex pattern
    pattern = r"TO_DATE\('(\d{2})-([A-Z]{3})-(\d{2})', 'DD-MON-RR'\)"
    
    def replacement(match):
        day, month, year_rr = match.groups()
        # Map the month abbreviation to its numerical equivalent
        month_num = month_map[month]
        # Convert RR year to full year
        year_full = int(year_rr) + (2000 if int(year_rr) < 50 else 1900)
        return f"DATE '{year_full}-{month_num}-{day}'"
    
    # Substitute all matches in the line
    return re.sub(pattern, replacement, line)

def process_sql_file(input_file, output_file):
    """
    Reads a SQL file line by line, converts Oracle TO_DATE to PostgreSQL DATE, and writes to a new file.
    """
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            converted_line = convert_to_pgsql_date(line)
            outfile.write(converted_line)

# File paths
input_file = './query.sql'
output_file = './query_pg.sql'

# Process the file
process_sql_file(input_file, output_file)

print(f"Converted SQL queries have been written to {output_file}")
