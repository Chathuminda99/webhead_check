import requests
import pandas as pd
from openpyxl import Workbook
import argparse
from tqdm import tqdm

# ASCII Art Title
print("""
                         /$$       /$$                                 /$$                 /$$                           /$$      
                        | $$      | $$                                | $$                | $$                          | $$      
 /$$  /$$  /$$  /$$$$$$ | $$$$$$$ | $$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$$        /$$$$$$$| $$$$$$$   /$$$$$$   /$$$$$$$| $$   /$$
| $$ | $$ | $$ /$$__  $$| $$__  $$| $$__  $$ /$$__  $$ |____  $$ /$$__  $$       /$$_____/| $$__  $$ /$$__  $$ /$$_____/| $$  /$$/
| $$ | $$ | $$| $$$$$$$$| $$  \ $$| $$  \ $$| $$$$$$$$  /$$$$$$$| $$  | $$      | $$      | $$  \ $$| $$$$$$$$| $$      | $$$$$$/ 
| $$ | $$ | $$| $$_____/| $$  | $$| $$  | $$| $$_____/ /$$__  $$| $$  | $$      | $$      | $$  | $$| $$_____/| $$      | $$_  $$ 
|  $$$$$/$$$$/|  $$$$$$$| $$$$$$$/| $$  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$      |  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$$| $$ \  $$
 \_____/\___/  \_______/|_______/ |__/  |__/ \_______/ \_______/ \_______//$$$$$$\_______/|__/  |__/ \_______/ \_______/|__/  \__/
                                                                         |______/                                                                                                                                                                                                                                                                                                                                                 
""")

# List of security headers to check
SECURITY_HEADERS = [
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "Referrer-Policy",
    "Permissions-Policy",
    "Cross-Origin-Embedder-Policy",
    "Cross-Origin-Resource-Policy",
    "Cross-Origin-Opener-Policy"
]

# Function to fetch headers for a URL
def fetch_headers(url):
    try:
        response = requests.head(url, timeout=10)
        return response.headers
    except requests.RequestException as e:
        print(f"Error fetching headers for {url}: {e}")
        return {}

# Read URLs from text file
def read_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file.readlines()]
    return urls

# Generate Excel sheet with header information
def generate_excel(urls, output_file):
    data = []

    # Fetch headers for each URL with progress view
    for url in tqdm(urls, desc="Processing URLs", unit="url"):
        headers = fetch_headers(url)
        row = [url]
        for header in SECURITY_HEADERS:
            status = "Header Implemented" if header in headers else "Header Not Implemented"
            row.append(status)
        data.append(row)

    # Create a DataFrame and save to Excel
    column_names = ["URL"] + SECURITY_HEADERS
    df = pd.DataFrame(data, columns=column_names)
    df.to_excel(output_file, index=False)

# Main script
def main():
    parser = argparse.ArgumentParser(description="Check security headers for a list of URLs and generate a report.")
    parser.add_argument("-u", "--urls", required=True, help="Path to the file containing the list of URLs.")
    parser.add_argument("-o", "--output", required=False, default="security_headers_report.xlsx", help="Name of the output Excel file.")
    args = parser.parse_args()

    input_file = args.urls  # File containing the list of URLs
    output_file = args.output

    # Ensure output file has .xlsx extension
    if not output_file.endswith(".xlsx"):
        output_file += ".xlsx"

    # Read URLs from file
    urls = read_urls_from_file(input_file)

    # Generate Excel report
    generate_excel(urls, output_file)

    print(f"Security headers report generated successfully: {output_file}")

if __name__ == "__main__":
    main()
