
# Webhead Check

Webhead Check is a Python script for analyzing HTTP security headers. It processes a single URL or a list of URLs and generates a report highlighting the presence or absence of critical security headers. Designed for security professionals, it helps assess the security posture of web applications.

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
- **Single URL Mode**: Displays results directly in the terminal.
- **List Mode**: Processes multiple URLs from a file and generates a color-coded Excel report:
  - **Green** for headers implemented.
  - **Red** for headers missing.
- Real-time progress updates with a user-friendly progress bar.

## Prerequisites

- Python 3.6 or later.

## Installation

1. Clone this repository or copy the script to your local machine.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script with one of the following options:

### Single URL

Use the `-u` or `--url` option to analyze a single URL and display the results in the terminal.

```bash
python webhead_check.py -u <url>
```

Example:

```bash
python webhead_check.py -u https://example.com
```

### List of URLs

Use the `-l` or `--list` option to analyze a list of URLs from a file and generate an Excel report.

```bash
python webhead_check.py -l <list_file> [-o <output_file>]
```

Example:

```bash
python webhead_check.py -l urls.txt -o headers_report
```

This command will process the URLs in `urls.txt` and create an Excel report named `headers_report.xlsx`.

### Arguments

- `-u`, `--url`: Analyze a single URL.
- `-l`, `--list`: Path to the file containing the list of URLs (one URL per line).
- `-o`, `--output`: Name of the output Excel file. Defaults to `security_headers_report.xlsx`. If only a name is provided, the `.xlsx` extension will be added automatically.

## Output

For single URL analysis:

- Results are displayed in the terminal.

For multiple URL analysis:

- The script generates an Excel file with the following structure:
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
