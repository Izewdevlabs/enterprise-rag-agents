from pathlib import Path

ALLOWED_EXT = {".pdf", ".txt", ".csv", ".xlsx", ".xls"}

def validate_upload(filename: str, size_bytes: int, max_mb: int):
    ext = Path(filename).suffix.lower()
    if ext not in ALLOWED_EXT:
        raise ValueError(f"Unsupported file type: {ext}")
    if size_bytes > max_mb * 1024 * 1024:
        raise ValueError(f"File too large. Max {max_mb} MB.")