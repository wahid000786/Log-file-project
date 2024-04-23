# Log File Monitor

This script continuously monitors log files in a specified directory for new entries and performs basic log analysis, such as counting occurrences of HTTP status codes and error messages.

## Features

- Monitors log files in real-time for new entries.
- Counts occurrences of warning, info, trace, debug and error messages.
- Generates summary reports for warning, info, trace, debug and error messages.

## Requirements

- Python 3.x

## Installation

1. Clone or download the repository to your local machine:

    ```
    git clone https://github.com/yourusername/log-file-monitor.git
    ```

2. Navigate to the directory containing the script:

    ```
    cd log-file-monitor
    ```

3. Install python if not installed:

    ```
   py -m pip --version
    ```
    
4. Run the script:
    ```
   python log_monitor.py
    ```
    
4. Specify the log file path when prompted.


## Usage

1. Ensure that your log files are located in the same directory as the script.
2. Run the script:

    ```
    python log_monitor.py
    ```

3. The script will continuously monitor the log files and display new entries in real-time.
4. Press `Ctrl+C` to stop the monitoring process.


