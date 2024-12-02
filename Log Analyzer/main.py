#!/usr/bin/env python3

import os
import re
from collections import Counter, defaultdict
from datetime import datetime

# Configuration
LOG_FILE = os.path.expanduser("path/to/server.log")  # Path to the server log file
REPORT_FILE = os.path.expanduser("path/to/log_report.txt")  # Path for the summary report output

# Regular expressions for parsing logs (adjust patterns to match log format)
timestamp_pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
error_pattern = r'(ERROR|WARN|CRITICAL)'
traffic_pattern = r'GET|POST|PUT|DELETE'

# Data holders
error_counts = Counter()
traffic_counts = defaultdict(int)
hourly_traffic = Counter()

def parse_logs(log_file):
    """
    Parse the log file to extract relevant information like error types,
    traffic request types, and hourly traffic data.
    """
    with open(log_file, 'r') as file:
        for line in file:
            # Extract timestamp
            timestamp_match = re.search(timestamp_pattern, line)
            if timestamp_match:
                timestamp_str = timestamp_match.group()
                timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
                hour = timestamp.strftime('%Y-%m-%d %H:00')
                hourly_traffic[hour] += 1

            # Check for error messages
            error_match = re.search(error_pattern, line)
            if error_match:
                error_type = error_match.group()
                error_counts[error_type] += 1

            # Track traffic request types
            traffic_match = re.search(traffic_pattern, line)
            if traffic_match:
                traffic_counts[traffic_match.group()] += 1

def generate_report(report_file):
    """
    Generate a summary report with error counts, traffic counts, and peak traffic times.
    """
    with open(report_file, 'w') as report:
        report.write("Log Analysis Summary\n")
        report.write("="*20 + "\n\n")

        # Error Summary
        report.write("Error Summary:\n")
        for error_type, count in error_counts.items():
            report.write(f"{error_type}: {count}\n")
        report.write("\n")

        # Traffic Summary
        report.write("Traffic Summary by Request Type:\n")
        for request_type, count in traffic_counts.items():
            report.write(f"{request_type}: {count}\n")
        report.write("\n")

        # Peak Traffic Times
        report.write("Hourly Traffic Summary:\n")
        peak_hour, peak_count = max(hourly_traffic.items(), key=lambda x: x[1])
        for hour, count in hourly_traffic.items():
            report.write(f"{hour}: {count} requests\n")
        report.write(f"\nPeak Traffic: {peak_hour} with {peak_count} requests\n")

def main():
    """
    Main function to handle log parsing and report generation.
    """
    try:
        print(f"Starting log analysis on {LOG_FILE}...")
        parse_logs(LOG_FILE)
        generate_report(REPORT_FILE)
        print(f"Log analysis complete. Summary report generated at {REPORT_FILE}")
    except FileNotFoundError:
        print(f"Error: The log file {LOG_FILE} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
