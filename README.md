
# Webhead Check

Webhead Check is a Python script that fetches HTTP headers for a list of URLs and generates a report in an Excel file. It helps identify the presence or absence of critical security headers for each URL.

## Features

- Checks for the following security headers:
  - `X-Frame-Options`
  - `X-Content-Type-Options`
  - `Strict-Transport-Security`
  - `Content-Security-Policy`
  - `Referrer-Policy`
  - `Permissions-Policy`
  - `Cross-Origin-Embedder-Policy`
  - `Cross-Origin-Resource-Policy`
  - `Cross-Origin-Opener-Policy`
- Generates a color-coded Excel report:
  - **Green** for headers that are implemented.
  - **Red** for headers that are missing.
- Displays a progress bar while processing URLs.

## Prerequisites

- Python 3.6 or later.

## Installation

1. Clone this repository or copy the script to your local machine.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script with the following arguments:

```bash
python webhead_check.py -u <urls_file> [-o <output_file>]
```

### Arguments:

- `-u`, `--urls` (required): Path to the file containing the list of URLs (one URL per line).
- `-o`, `--output` (optional): Name of the output Excel file. Defaults to `security_headers_report.xlsx`. If only a name is provided, the `.xlsx` extension will be added automatically.

### Example:

```bash
python webhead_check.py -u urls.txt -o headers_report
```

This command will process the URLs in `urls.txt` and create an Excel report named `headers_report.xlsx`.

## Output

The script generates an Excel file with the following structure:

- Column 1: URL
- Columns 2+: Security headers
- Each cell indicates whether the header is implemented (`Header Implemented`) or missing (`Header Not Implemented`).

## Dependencies

- `requests`
- `pandas`
- `openpyxl`
- `tqdm`

## License

This script is open-source and available under the MIT License. Feel free to modify and use it as per your requirements.
