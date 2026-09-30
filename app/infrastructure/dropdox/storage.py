import dropbox

from app.domain.interfaces.storage import StorageProvider
from app.domain.models.file import FileItem


class DropboxStorage(StorageProvider):

    def __init__(self, access_token: str):
        self.client = dropbox.Dropbox(access_token)

    def list_files(self, path: str) -> list[FileItem]:
        result = self.client.files_list_folder(path)

        return [
            FileItem(
                name=entry.name,
                path=entry.path_display,
                size=getattr(entry, "size", None),
                modified_at=getattr(entry, "server_modified", None),
                is_folder=not hasattr(entry, "size"),
            )
            for entry in result.entries
        ]