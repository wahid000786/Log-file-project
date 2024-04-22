# Log File Monitor

This script continuously monitors log files in a specified directory for new entries and performs basic log analysis, such as counting occurrences of HTTP status codes and error messages.

## Features

- Monitors log files in real-time for new entries.
- Counts occurrences of HTTP status codes and error messages.
- Generates summary reports for HTTP status codes and error messages.

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

3. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. Ensure that your log files are located in the same directory as the script.
2. Run the script:

    ```
    python log_monitor.py
    ```

3. The script will continuously monitor the log files and display new entries in real-time.
4. Press `Ctrl+C` to stop the monitoring process.

## Configuration

- Modify the `log_file` variable in the script to specify the path to your log file(s).
- You can also customize the list of keywords or patterns to search for in the log files.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
