from pathlib import Path
import uuid

from canvas import Canvas
import charachter_maps
import git
import util

YEAR = 2020
WEEKS = 53
DAYS = 7

def main() -> None:
    canvas = Canvas(WEEKS, DAYS)
    canvas.set_string(2, 0, "HELLOWORLD", charachter_maps.UPPER)

    repo_path = Path("./repo")

    repo_path.mkdir(parents=True, exist_ok=True)
    git.init(repo_path)

    for (week, day, weight) in canvas.get_pixels():
        date = util.week_and_weekday_to_date(week, day, YEAR)
        for _ in range(weight):
            (repo_path / str(uuid.uuid4())).touch(exist_ok=True)
            git.add_all(repo_path)
            git.commit(f"({week}, {day}, {weight})", date, repo_path)

if __name__ == "__main__":
    main()