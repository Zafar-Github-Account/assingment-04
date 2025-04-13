import time

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)  # Convert seconds into minutes and seconds
        timer = f"{mins:02d}:{secs:02d}"  # Format time as MM:SS
        print(timer, end='\r')  # Print and overwrite the line
        time.sleep(1)  # Wait for one second
        seconds -= 1  # Decrease the time by one second

    print("00:00\nTime's up!")

# Get user input
def start_timer():
    while True:
        try:
            time_input = int(input("Enter the countdown time in seconds: "))
            if time_input <= 0:
                print("❌ Please enter a positive number of seconds.")
            else:
                print(f"Starting countdown for {time_input} seconds...")
                countdown_timer(time_input)
                break
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")

# Run the timer
start_timer()
