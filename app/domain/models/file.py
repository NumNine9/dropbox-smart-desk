
from dataclasses import dataclass
from datetime import datetime

@dataclass
class FileItem:
    name: str
    path: str
    size: int | None
    modified_at: datetime | None
    is_folder: bool