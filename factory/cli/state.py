from pathlib import Path

from factory.workspace import Workspace


class CliState:

    def __init__(self, workspace: Workspace) -> None:
        self.workspace = workspace

    @staticmethod
    def load(path: Path, create: bool = True) -> 'CliState':
        if not path.is_dir() and create:
            path.mkdir(parents=True)

        return CliState(Workspace(path))