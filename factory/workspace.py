import os
from pathlib import Path


class Workspace:

    def __init__(self, location: Path = Path.cwd()) -> None:
        self.location = location

