import argparse
import os
import requests
import time
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path
from zoneinfo import ZoneInfo

# Load environment variables
load_dotenv()

class AOCSession:
    def __init__(self, year):
        self.session = {'session': os.getenv('AOC_SESSION')}
        self.base_url = f'https://adventofcode.com/{year}'

    def get_input(self, day):
        url = f'{self.base_url}/day/{day}/input'
        response = requests.get(url, cookies=self.session)
        if response.status_code == 200:
            return response.text.strip()
        else:
            raise Exception(f"Failed to get input: {response.status_code}")

def get_solution_template(year, day):
    return f'''
import time
from typing import Any

def parse_input(data: str) -> Any:
    """Parse the puzzle input."""
    print("🔄 Parsing input...")
    lines = data.split('\\n')
    # TODO: Modify parsing logic
    return lines

def solve_part1(parsed_data: Any) -> Any:
    """Solve part 1 of the puzzle."""
    print("🎯 Solving part 1...")
    # TODO: Implement solution
    return 0

def solve_part2(parsed_data: Any) -> Any:
    """Solve part 2 of the puzzle."""
    print("🎯 Solving part 2...")
    # TODO: Implement solution
    return 0

# Uncomment and modify test data as needed
# test_input = """
# [Add test input here]
# """

if __name__ == "__main__":
    # Load input
    with open(f"inputs/day_{day}.txt", "r") as f:
        input_data = f.read().strip()

    # Parse input
    parsed_data = parse_input(input_data)

    # Optional: Run tests
    if 'test_input' in globals():
        print("🧪 Running tests...")
        test_parsed = parse_input(test_input)
        print(f"Test Part 1: {{solve_part1(test_parsed)}}")
        print(f"Test Part 2: {{solve_part2(test_parsed)}}")
        print()

    # Solve part 1
    start_time = time.time()
    answer1 = solve_part1(parsed_data)
    time1 = time.time() - start_time
    print(f"✨ Part 1 answer: {{answer1}} (took {{time1:.2f}}s)\\n")

    # Solve part 2
    start_time = time.time()
    answer2 = solve_part2(parsed_data)
    time2 = time.time() - start_time
    print(f"✨ Part 2 answer: {{answer2}} (took {{time2:.2f}}s)")
'''

def setup_day(year, day):
    # Create directories if they don't exist
    Path('inputs').mkdir(exist_ok=True)
    Path('solutions').mkdir(exist_ok=True)

    # Download input if needed
    input_file = Path(f'inputs/day_{day}.txt')
    if not input_file.exists():
        print(f"⬇️ Downloading input for day {day}...")
        aoc = AOCSession(year)
        input_data = aoc.get_input(day)
        input_file.write_text(input_data)
        print("✅ Input downloaded")

    # Create solution file if needed
    solution_file = Path(f'solutions/day_{day}.py')
    if not solution_file.exists():
        print("📝 Creating solution file...")
        solution_content = get_solution_template(year, day)
        solution_file.write_text(solution_content)
        print("✅ Solution template created")

    print(f"""
✨ Setup complete!
- Input file: {input_file}
- Solution file: {solution_file}

Next steps:
1. Edit the solution file
2. Run: python solutions/day_{day}.py
3. Submit answers on adventofcode.com

Good luck! 🎄
""")

if __name__ == "__main__":
    # Get current day in PT, but remember AOC puzzles unlock at 9PM PT the day before
    pt_time = datetime.now(ZoneInfo("America/Los_Angeles"))
    # If it's before 9PM PT, use the previous day
    if pt_time.hour < 21:  # 21:00 = 9PM
        default_day = max(1, pt_time.day - 1)
    else:
        default_day = pt_time.day

    parser = argparse.ArgumentParser(description='Setup Advent of Code solution file and input')
    parser.add_argument('day', type=int, nargs='?', default=default_day,
                       help='Day number (1-25), defaults to current PT day (or previous day before 9PM PT)')
    parser.add_argument('--year', type=int, default=2024,
                       help='Year (defaults to 2024)')

    args = parser.parse_args()

    # Validate day
    if not 1 <= args.day <= 25:
        parser.error("Day must be between 1 and 25")

    setup_day(args.year, args.day)
