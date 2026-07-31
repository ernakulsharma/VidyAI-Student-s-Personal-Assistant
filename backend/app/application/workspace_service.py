from app.database.repositories.workspace_repository import WorkspaceRepository
from app.database.session import SessionLocal


class WorkspaceService:
    """
    Handles workspace management.
    """

    def __init__(self):

        self.db = SessionLocal()

        self.repository = WorkspaceRepository(
            self.db
        )

    def get_or_create_default_workspace(self):

        workspace = self.repository.get_by_name(
            "Default Workspace"
        )

        if workspace:

            return workspace

        return self.repository.create(
            name="Default Workspace",
            description="Automatically created workspace",
        )