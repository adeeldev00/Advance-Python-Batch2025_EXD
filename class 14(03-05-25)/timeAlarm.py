import time
import datetime
import os
import platform

# Play sound or say a message when time is up
def notify_user(message="Time's up!"):
    system = platform.system()

    if system == "Windows":
        try:
            import winsound
            winsound.Beep(1000, 2000)  # Frequency, Duration in milliseconds
        except ImportError:
            print("winsound module not available.")
        print(message)

    elif system == "Darwin":  # macOS
        os.system(f'say "{message}"')

    elif system == "Linux":
        os.system(f'echo "{message}"')  # You can replace with 'aplay' if sound file is available
        print(message)
    else:
        print(message)

# Timer Function
def set_timer(seconds):
    print(f"\n⏳ Timer started for {seconds} seconds.\n")
    time.sleep(seconds)
    print("⏰ Timer Done!")
    notify_user("Timer finished!")

# Alarm Function
def set_alarm(alarm_time):
    print(f"\n🔔 Alarm set for {alarm_time}.\n")
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == alarm_time:
            print("⏰ Wake up! Alarm ringing!")
            notify_user("Alarm ringing!")
            break
        time.sleep(10)  # Check every 10 seconds

# Main function
def main():
    print(f'╭──────────────────────────.★..─╮\n  Welcome to Timer and Alarm Clock ⏰\n╰─..★.──────────────────────────╯')
    print("-----------------------------")

    choice = input("Do you want to set a timer or an alarm? (timer/alarm): ").strip().lower()

    if choice == "timer":
        try:
            seconds = int(input("Enter time in seconds: "))
            set_timer(seconds)
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "alarm":
        alarm_time = input("Enter alarm time (HH:MM in 24-hour format): ")
        try:
            datetime.datetime.strptime(alarm_time, "%H:%M")  # Validate format
            set_alarm(alarm_time)
        except ValueError:
            print("Invalid time format. Please use HH:MM (24-hour).")

    else:
        print("Invalid choice. Please type 'timer' or 'alarm'.")

# Run the program
if __name__ == "__main__":
    main()
