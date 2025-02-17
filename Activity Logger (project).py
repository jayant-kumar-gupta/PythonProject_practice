import datetime

class ActivityLogger:
    def __init__(self, filename="activity_log.txt"):
        self.filename = filename

    def log_activity(self, activity):
        """
        Logs the given activity to the log file with a timestamp.
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - {activity}\n"
        try:
            with open(self.filename, "a") as log_file:
                log_file.write(log_entry)
            print("Activity logged successfully.")
        except Exception as e:
            print(f"Error logging activity: {e}")

    def read_logs(self):
        """
        Reads and displays all log entries from the log file.
        """
        try:
            with open(self.filename, "r") as log_file:
                logs = log_file.readlines()
            if logs:
                print("\nActivity Logs:")
                print("".join(logs))
            else:
                print("No logs available.")
        except FileNotFoundError:
            print("Log file not found. No activities logged yet.")
        except Exception as e:
            print(f"Error reading log file: {e}")


# Main Program
def main():
    logger = ActivityLogger()

    while True:
        print("\nMenu:")
        print("1. Log an activity")
        print("2. View logs")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            activity = input("Enter the activity description: ").strip()
            logger.log_activity(activity)
        elif choice == "2":
            logger.read_logs()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
