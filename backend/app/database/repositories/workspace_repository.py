from app.database.models.workspace import Workspace
from app.database.repositories.base_repository import BaseRepository


class WorkspaceRepository(BaseRepository):
    """
    Handles database operations for workspaces.
    """

    def get_by_name(
        self,
        name: str,
    ) -> Workspace | None:

        return (
            self.db.query(Workspace)
            .filter(
                Workspace.name == name
            )
            .first()
        )

    def create(
        self,
        name: str,
        description: str = "",
    ) -> Workspace:

        workspace = Workspace(
            name=name,
            description=description,
        )

        self.db.add(workspace)

        self.db.commit()

        self.db.refresh(workspace)

        return workspace