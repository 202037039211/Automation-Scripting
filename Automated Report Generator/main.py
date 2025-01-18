import os
import psutil
from datetime import datetime

# Path where the report will be saved (use your custom path)
REPORTS_DIR = os.path.expanduser("path/to/reports/")  # Replace with a valid directory path
os.makedirs(REPORTS_DIR, exist_ok=True)

# Generate a report file name with timestamp
REPORT_FILE = os.path.join(REPORTS_DIR, f"system_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")

# Function to gather system metrics like CPU, memory, disk, and network usage
def gather_system_metrics():
    metrics = {
        "cpu_usage": psutil.cpu_percent(interval=1),  # CPU usage in percentage
        "memory_usage": psutil.virtual_memory().percent,  # Memory usage in percentage
        "disk_usage": psutil.disk_usage('/').percent,  # Disk usage in percentage
        "network_sent": psutil.net_io_counters().bytes_sent,  # Data sent over the network (bytes)
        "network_received": psutil.net_io_counters().bytes_recv,  # Data received over the network (bytes)
    }
    return metrics

# Function to format the gathered metrics and write them to a text file
def write_report(metrics):
    with open(REPORT_FILE, 'w') as report:
        # Write header with timestamp
        report.write(f"System Health Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        report.write("="*50 + "\n")
        
        # Write the system metrics
        report.write(f"CPU Usage: {metrics['cpu_usage']}%\n")
        report.write(f"Memory Usage: {metrics['memory_usage']}%\n")
        report.write(f"Disk Usage: {metrics['disk_usage']}%\n")
        report.write(f"Network Sent: {metrics['network_sent']} bytes\n")
        report.write(f"Network Received: {metrics['network_received']} bytes\n")
        
        # Add footer
        report.write("="*50 + "\n")
    
    print(f"Report generated: {REPORT_FILE}")

# Main function to initiate the report generation
if __name__ == "__main__":
    system_metrics = gather_system_metrics()  # Gather system data
    write_report(system_metrics)  # Write data to the report file
