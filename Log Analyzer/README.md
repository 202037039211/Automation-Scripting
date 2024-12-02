# Log Analyzer

This script parses a server log file, analyzes the traffic and error data, and generates a summary report. It is designed to work with logs containing timestamps, error types (ERROR, WARN, CRITICAL), and HTTP request methods (GET, POST, PUT, DELETE).

## Features
- **Log Parsing**: Extracts error types, traffic request methods, and hourly traffic data.
- **Summary Report**: Generates a report with error counts, request method counts, and peak traffic times.

## Requirements
- Python 3.x

## Installation
1. Clone or download this repository.
2. Adjust the `LOG_FILE` and `REPORT_FILE` paths in the script as needed.
3. Ensure your log file is structured with timestamps, error levels, and HTTP request methods (GET, POST, etc.).

## Usage
1. Place your server log file at the specified path (`LOG_FILE`).
2. Run the script to generate a log analysis summary.
3. The summary will be saved in the specified output file (`REPORT_FILE`).

## License
This project is licensed under the MIT License - see the LICENSE file for details.
