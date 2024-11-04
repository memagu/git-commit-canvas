from pathlib import Path
import uuid

from canvas import Canvas
import charachter_maps
import git
import util

WEEKS = 53
DAYS = 7

REPO_PATH = Path("./tmp")


def draw_canvas_on_year(canvas: Canvas, year: int) -> None:
    REPO_PATH.mkdir(parents=True, exist_ok=True)
    git.init(REPO_PATH)

    for (week, day, weight) in canvas.get_pixels():
        date = util.week_and_weekday_to_date(week, day, year, year > 2013)
        for _ in range(weight):
            (REPO_PATH / str(uuid.uuid4())).touch(exist_ok=True)
            git.add_all(REPO_PATH)
            git.commit(f"({week}, {day}, {weight})", date, REPO_PATH)


def main() -> None:
    canvas = Canvas(WEEKS, DAYS)
    canvas.set_string(2, 0, "HELLOWORLD", charachter_maps.UPPER)
    draw_canvas_on_year(canvas, 2020)

    # canvas2 = Canvas(WEEKS, DAYS)
    # canvas2.set_string(13, 0, "START", charachter_maps.UPPER)
    # draw_canvas_on_year(canvas2, 1970)

    for year in range(1970, 2020):
        c = Canvas(WEEKS, DAYS)
        c.set_string(16, 0, str(year), charachter_maps.DIGITS)
        draw_canvas_on_year(c, year)
    
if __name__ == "__main__":
    main()
