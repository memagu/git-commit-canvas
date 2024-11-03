from datetime import datetime
import subprocess
from typing import Iterable, Optional

from pathlib import Path

def init(execute_at: Path = Path()) -> None:
    subprocess.run(
        ["git", "-C", str(execute_at.absolute()), "init"],
        check=True
    )

def add(files: Iterable[Path], execute_at: Path = Path()) -> None:
    subprocess.run(
        ["git", "-C", str(execute_at.absolute()), "add"] + [str(path.absolute()) for path in files],
        check=True
    )

def add_all(execute_at: Path = Path()) -> None:
    subprocess.run(
        ["git", "-C", str(execute_at.absolute()), "add", "."],
        check=True
    )

def commit(message: str, date: Optional[datetime] = None, execute_at: Path = Path()) -> None:
    date = date or datetime.now()

    subprocess.run(
        ["git", "-C", str(execute_at.absolute()), "commit", "-m", message, "--date", date.strftime("%Y-%m-%d %H:%M:%S")],
        check=True
    )