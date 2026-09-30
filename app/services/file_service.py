class FileService:

    def __init__(self, storage):
        self.storage = storage

    def list_files(self, path: str):
        return self.storage.list_files(path)

    def upload(self, path: str, content: bytes):
        return self.storage.upload(path, content)

    def download(self, path: str):
        return self.storage.download(path)

    def delete(self, path: str):
        return self.storage.delete(path)