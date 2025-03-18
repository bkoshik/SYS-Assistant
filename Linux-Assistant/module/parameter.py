from pathlib import Path

current_file = Path(__file__).resolve()
file2_path = current_file.parents[1]

params = {
    "path": file2_path,
    "my_id": 0
}
