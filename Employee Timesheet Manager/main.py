import csv
from datetime import datetime

# Path to the timesheet CSV file
TIMESHEET_FILE = 'timesheet.csv'

def add_work_hours(employee_id, date, start_time, end_time):
    """
    Adds work hours for an employee into the timesheet CSV file.
    
    Args:
    - employee_id (str): Unique ID of the employee
    - date (str): Work date in YYYY-MM-DD format
    - start_time (str): Start time in HH:MM format
    - end_time (str): End time in HH:MM format
    """
    with open(TIMESHEET_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([employee_id, date, start_time, end_time])

def generate_report(start_date, end_date):
    """
    Generates a report of total hours worked by employees within a specific date range.
    
    Args:
    - start_date (datetime): Start date of the report period
    - end_date (datetime): End date of the report period
    
    Returns:
    - dict: A dictionary with employee ID as keys and total hours worked as values
    """
    report = {}
    
    # Read the timesheet CSV file and calculate hours worked
    with open(TIMESHEET_FILE, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            employee_id, date, start_time, end_time = row
            date = datetime.strptime(date, '%Y-%m-%d')
            if start_date <= date <= end_date:
                start = datetime.strptime(start_time, '%H:%M')
                end = datetime.strptime(end_time, '%H:%M')
                hours_worked = (end - start).total_seconds() / 3600
                # Add hours worked to the employee's total in the report
                report[employee_id] = report.get(employee_id, 0) + hours_worked
    return report

def main():
    """
    Main function for interacting with the user. Provides options to add work hours
    or generate a report.
    """
    while True:
        print("1. Add Work Hours")
        print("2. Generate Report")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            # Input work hours for an employee
            employee_id = input("Enter Employee ID: ")
            date = input("Enter Date (YYYY-MM-DD): ")
            start_time = input("Enter Start Time (HH:MM): ")
            end_time = input("Enter End Time (HH:MM): ")
            add_work_hours(employee_id, date, start_time, end_time)

        elif choice == '2':
            # Generate a report for a specified date range
            start_date = datetime.strptime(input("Enter Start Date (YYYY-MM-DD): "), '%Y-%m-%d')
            end_date = datetime.strptime(input("Enter End Date (YYYY-MM-DD): "), '%Y-%m-%d')
            report = generate_report(start_date, end_date)
            print("Employee Hours Report:")
            for emp_id, hours in report.items():
                print(f"Employee ID: {emp_id}, Total Hours: {hours:.2f}")

        elif choice == '3':
            # Exit the program
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
