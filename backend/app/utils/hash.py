import hashlib
from pathlib import Path


def calculate_sha256(path: Path) -> str:

    sha = hashlib.sha256()

    with open(path, "rb") as f:

        while chunk := f.read(8192):

            sha.update(chunk)

    return sha.hexdigest()