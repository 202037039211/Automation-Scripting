# File Synchronizer

This Python tool helps synchronize files from a source directory to a destination directory. It only copies files that are newer or missing in the destination directory, ensuring that the destination is an up-to-date copy of the source.

## Features

- **Sync Files**: Copies missing or newer files from the source directory to the destination directory.
- **Log Sync Actions**: Logs each synchronization action with timestamps.

## Requirements

- Python 3.x
- `os`, `shutil`, and `datetime` (all included in Python's standard library)

## Installation

1. Clone or download this repository.
2. Modify the source and destination directory paths in the script (`SOURCE_DIR` and `DESTINATION_DIR`).
3. Run the script in your terminal or Python IDE.

## Usage

1. Run the script.
2. The script will sync files from the source directory to the destination directory, copying only missing or newer files.
3. Sync actions will be logged in the `sync_log.txt` file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
