import os
from pathlib import Path

BASE_DIR = Path("storage/file-management-root")

class OSFileSystem:
    def __init__(self):
        BASE_DIR.mkdir(parents=True, exist_ok=True)

    def create_directory(self, path, name):
        full_path = BASE_DIR / path.strip("/") / name
        full_path.mkdir(parents=True, exist_ok=True)
        return f"Directory created: {full_path}"

    def create_file(self, path, name, size):
        full_path = BASE_DIR / path.strip("/") / f"{name}.txt"
        full_path.parent.mkdir(parents=True, exist_ok=True)
        with open(full_path, "w") as f:
            f.write(f"File: {name}\nSize: {size} KB\n")
        return f"File created: {full_path.name}"

    def delete_file(self, name):
        for root, _, files in os.walk(BASE_DIR):
            if f"{name}.txt" in files:
                file_path = Path(root) / f"{name}.txt"
                file_path.unlink()
                return f"File deleted: {file_path.name}"
        return "File not found"

    def rename_file(self, old_name, new_name):
        for root, _, files in os.walk(BASE_DIR):
            if f"{old_name}.txt" in files:
                old_path = Path(root) / f"{old_name}.txt"
                new_path = Path(root) / f"{new_name}.txt"
                old_path.rename(new_path)
                return f"File renamed: {old_name}.txt → {new_name}.txt"
        return "File not found"

    def read_file(self, name):
        for root, _, files in os.walk(BASE_DIR):
            if f"{name}.txt" in files:
                with open(Path(root) / f"{name}.txt", "r") as f:
                    return f.read()
        return None

    def build_tree(self):
        tree = "📁 root\n"
        for root, _, files in os.walk(BASE_DIR):
            level = root.replace(str(BASE_DIR), "").count(os.sep)
            indent = "  " * level
            tree += f"{indent}📁 {Path(root).name}\n"
            for file in files:
                tree += f"{indent}  📄 {file}\n"
        return tree
