#!/bin/bash

# Configuration: Set these paths according to your needs
BACKUP_SOURCE="path/to/importantFiles"               # Files or directories to back up
BACKUP_DESTINATION="path/to/importantFiles_archive"  # Location to store backup archives
LOG_FILE="$BACKUP_DESTINATION/backup_log.txt"      # Log file path

# Create Backup and Destination directories if they don't exist
mkdir -p "$BACKUP_SOURCE" "$BACKUP_DESTINATION"

# Create Backup Function
backup() {
    TIMESTAMP=$(date +"%Y%m%d_%H%M%S")  # Generate timestamp for backup file name
    BACKUP_FILE="$BACKUP_DESTINATION/backup_$TIMESTAMP.tar.gz"  # Backup file path
    
    # Create a backup archive
    tar -czf "$BACKUP_FILE" "$BACKUP_SOURCE" && echo "Backup created: $BACKUP_FILE" | tee -a "$LOG_FILE"
    
    if [ $? -eq 0 ]; then
        echo "$(date): Backup successful - $BACKUP_FILE" >> "$LOG_FILE"  # Log success
    else
        echo "$(date): Backup failed" >> "$LOG_FILE"  # Log failure
    fi
}

# Restore Backup Function
restore() {
    echo "Available backups:"
    
    # List available backup files
    ls "$BACKUP_DESTINATION"/backup_*.tar.gz
    
    # Prompt user to specify which backup to restore
    read -p "Enter the filename of the backup to restore (e.g., backup_20240101_123456.tar.gz): " RESTORE_FILE
    RESTORE_PATH="${BACKUP_SOURCE}_restored"  # Path where restored files will be placed
    
    # Check if the backup file exists
    if [ -f "$BACKUP_DESTINATION/$RESTORE_FILE" ]; then
        mkdir -p "$RESTORE_PATH"  # Create a new folder for restoring files
        # Extract the backup file to the restore path
        tar -xzf "$BACKUP_DESTINATION/$RESTORE_FILE" -C "$RESTORE_PATH" && echo "Backup restored to $RESTORE_PATH" | tee -a "$LOG_FILE"
        echo "$(date): Restored $RESTORE_FILE to $RESTORE_PATH" >> "$LOG_FILE"  # Log restoration
    else
        echo "Backup file not found: $RESTORE_FILE" | tee -a "$LOG_FILE"  # Log error if file is not found
    fi
}

# Main Menu
echo "Select an option:"
echo "1) Backup"
echo "2) Restore"
read -p "Enter choice [1-2]: " CHOICE

# Handle user choice
case $CHOICE in
    1) backup ;;  # Call backup function
    2) restore ;;  # Call restore function
    *) echo "Invalid option. Please select 1 or 2." ;;  # Handle invalid choice
esac
