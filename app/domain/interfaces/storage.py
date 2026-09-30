from abc import ABC, abstractmethod

from app.domain.models.file import FileItem


class StorageProvider(ABC):

    @abstractmethod
    def list_files(self, path: str) -> list[FileItem]:
        pass

    @abstractmethod
    def upload(self, path: str, content: bytes) -> FileItem:
        pass

    @abstractmethod
    def download(self, path: str) -> bytes:
        pass

    @abstractmethod
    def delete(self, path: str) -> None:
        pass

    @abstractmethod
    def create_folder(self, path: str) -> FileItem:
        pass