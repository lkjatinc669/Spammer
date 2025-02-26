import argparse
import sys
import pyautogui as p
from time import sleep
import random


def countdown(seconds):
    """Displays a countdown before execution."""
    for i in range(seconds, 0, -1):
        print(f"Starting in {i}...", end="\r")
        sleep(1)
    print("Spamming now! 🚀")


def spam(message: str, times: int, ttw: int):
    """Function to spam messages after waiting for specified time."""
    countdown(ttw)
    print(f"Sending '{message}' {times} times with a {ttw}-second delay before start.")
    
    for _ in range(times):
        p.write(message)
        p.press('enter')

        delay = random.uniform(0.0, 1)  # Random delay between 0.5s - 2s
        sleep(delay)
    
    print("Spamming completed! ✅")


# Check if any arguments are passed
if len(sys.argv) == 1:
    print("Error: No arguments provided. Use --help for usage details.")
    sys.exit(1)

# Argument parser setup
parser = argparse.ArgumentParser(description="An Instagram message spammer.")
parser.add_argument("--message", type=str, required=True, help="The message to be sent.")
parser.add_argument("--times", type=int, default=10, help="Number of times the message is sent (default: 10).")
parser.add_argument("--ttw", type=int, default=5, help="Time (seconds) to wait before sending messages (default: 5).")

args = parser.parse_args()

# Validate numeric arguments
if args.times <= 0:
    print("Error: --times must be a positive integer.")
    sys.exit(1)

if args.ttw < 0:
    print("Error: --ttw must be zero or a positive integer.")
    sys.exit(1)

# Execute spamming function
spam(args.message, args.times, args.ttw)