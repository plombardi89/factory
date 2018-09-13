from factory.workspace import Workspace


class Context:

    def __init__(self, workspace: Workspace) -> None:
        self.workspace = workspace
