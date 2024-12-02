# Data Backup and Restore Script

This script allows users to back up files or directories into compressed `.tar.gz` archives and restore them from backups. The script logs all actions to a log file for reference.

## Requirements

- Bash (for Linux/macOS)
- `tar` command (for creating and extracting archives)

## How to Use

1. **Make the script executable**:
```bash
chmod +x backup_restore.sh
```

2. **Run the script**:
```bash
./backup_restore.sh
```

3. **Choose an option**:
Select 1 to create a backup of the specified directory.
Select 2 to restore a backup from available archives.

4. **Backup Location**:
Backups will be stored in `path/to/importantFiles_archive/`.
Logs of all actions will be stored in a file named backup_log.txt inside the backup destination folder.

5. **Backup Files**:
The backup files are named in the format `backup_YYYYMMDD_HHMMSS.tar.gz`, with the timestamp reflecting when the backup was created.
