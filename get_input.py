import os
import requests
import argparse

from datetime import datetime

# Replace with your AoC session cookie
SESSION_COOKIE = os.getenv("session")
BASE_URL = "https://adventofcode.com"

def get_input_data(year, day):
    """
    Fetch input data for the given year and day.
    """
    url = f"{BASE_URL}/{year}/day/{day}/input"
    cookies = {"session": SESSION_COOKIE}
    
    response = requests.get(url, cookies=cookies)
    if response.status_code == 200:
        return response.text
    else:
        response.raise_for_status()

def save_input_data(year, day, data):
    """
    Save input data to a file in the current directory.
    """
    directory = f"{year}/{day}"
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, "data.in")
    
    with open(filepath, "w") as f:
        f.write(data)
    print(f"Input data for {year} Day {day} saved to {filepath}")

def read_data(fn):
    """
    Read data as parsed list of integers
    """
    return [[int(i) for i in line.split()] for line in open(fn).read().splitlines()]

def main():
    # Parse command-line arguments
    today = datetime.now()

    parser = argparse.ArgumentParser(description="Fetch Advent of Code input data.")
    parser.add_argument("--year", type=int, default = today.year, help="The year of the puzzle (default: current year).")
    parser.add_argument("--day", type=int, default = today.day, help="The day of the puzzle (default: today's day).")
    args = parser.parse_args()
    
    try:
        print(f"Fetching input data for {args.year} Day {args.day}...")
        data = get_input_data(args.year, args.day)
        save_input_data(args.year, args.day, data)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()