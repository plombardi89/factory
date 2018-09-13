from factory.workspace import *
from factory.context import *

from typing import Any, Dict, Optional, Tuple


class ProjectConfig:

    def __init__(self) -> None:
        self.name = None

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> 'ProjectConfig':
        return None


class Project:

    def __init__(self, workspace: Workspace):
        self.ws = workspace
        self.ctx = Context(self.ws)

        (self.initialized, self.project_config) = Project.check_initialized(self.ws)

    def initialize(self):
        pass

    @staticmethod
    def get(project_path: Path, create: bool = True) -> 'Project':
        ws = Workspace(project_path)
        p = Project(ws)

        if not p.initialized:
            p.initialize()

        return p

    @staticmethod
    def check_initialized(workspace: Workspace) -> Tuple[bool, Optional[ProjectConfig]]:
        initialized = False
        config = None

        filenames = [os.getenv("FACTORY_FILE", "factory.yaml"), "factory.yml"]

        for filename in filenames:
            try:
                with (workspace.location / filename).open("r") as f:
                    initialized = True
                    config = ProjectConfig.from_dict({})
                    break
            except IOError:
                pass

        return initialized, config
