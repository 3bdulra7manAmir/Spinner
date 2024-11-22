import sys
import time

def spinning_loader(duration):
    spinner = ['|', '/', '-', '\\']  # Sequence of spinner characters
    end_time = time.time() + duration  # Stop after the specified duration
    while time.time() < end_time:
        for char in spinner:
            sys.stdout.write(f'\t\t\r{char}')  # Overwrite the current line
            sys.stdout.flush()  # Ensure output is shown immediately
            time.sleep(0.1)  # Adjust speed of the spinner


if __name__ == "__main__":
    # Example usage
    print("Loading... ", end="")
    spinning_loader(10)  # Spinner for 5 seconds
    print("\nDone!")