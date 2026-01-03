from backend.filesystem.os_file_system import OSFileSystem
from backend.cache.lru_cache import LRUCache
from datetime import datetime

class FileManager:
    def __init__(self):
        self.fs = OSFileSystem()
        self.cache = LRUCache(capacity=3)
        self.logs = []

    def _log(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.logs.insert(0, f"[{timestamp}] {message}")

    def create_directory(self, path, name):
        msg = self.fs.create_directory(path, name)
        self._log(msg)

    def create_file(self, path, name, size):
        msg = self.fs.create_file(path, name, size)
        self._log(msg)

    def access_file(self, name):
        cached = self.cache.get(name)
        if cached:
            self._log(f"File accessed (Cache Hit): {name}.txt")
            return "Cache Hit"

        content = self.fs.read_file(name)
        if content:
            self.cache.put(name, content)
            self._log(f"File accessed (Cache Miss): {name}.txt")
            return "Cache Miss"
        return "File not found"

    def delete_file(self, name):
        msg = self.fs.delete_file(name)
        self._log(msg)

    def rename_file(self, old, new):
        msg = self.fs.rename_file(old, new)
        self._log(msg)

    def get_tree(self):
        return self.fs.build_tree()

    def get_cache(self):
        return self.cache.list_cache()

    def get_logs(self):
        return self.logs[:10]

