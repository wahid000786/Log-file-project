import logging
import time
import signal
import re

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='log_monitor.log')

def monitor_log(log_file):
    try:
        keywords_count = {'error': 0, 'info': 0, 'warning': 0, 'trace': 0, 'debug': 0}  
        # Initialize keyword count dictionary
        keyword_patterns = {'error': re.compile(r'error', re.IGNORECASE),
                            'info': re.compile(r'info', re.IGNORECASE),
                            'warning': re.compile(r'warning', re.IGNORECASE),
                            'trace': re.compile(r'trace', re.IGNORECASE),
                            'debug': re.compile(r'debug', re.IGNORECASE)}

        with open(log_file, 'r') as f:
            # Move the pointer to the end of the file
            f.seek(0, 2)  
            while True:
                new_line = f.readline()
                if new_line:
                    logging.info(new_line.strip())
                    # Display new log entry
                    print(new_line.strip())  

                    # Perform basic analysis
                    for keyword, pattern in keyword_patterns.items():
                        if pattern.search(new_line):
                            keywords_count[keyword] += 1

                    # Print keyword counts
                    print("Keyword Counts:", keywords_count)

                time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
        logging.info("Monitoring stopped by user.")
    except FileNotFoundError:
        print(f"Error: Log file '{log_file}' not found.")
        logging.error(f"Log file '{log_file}' not found.")

def signal_handler(sig, frame):
    raise KeyboardInterrupt

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    log_file = "sample.log"  
    # Change this to your log file path
    print(f"Monitoring log file: {log_file}")
    logging.info(f"Monitoring log file: {log_file}")
    monitor_log(log_file)
