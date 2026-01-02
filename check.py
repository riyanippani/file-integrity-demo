from pathlib import Path

config_file = Path("config.txt")
baseline_file = Path("baseline.txt")

#read current file contents
current_contents = config_file.read_text(encoding="utf-8")

#read baseline contents
baseline_contents = baseline_file.read_text(encoding="utf-8")

#compare contents
if current_contents == baseline_contents:
    print("OK: file integrity verified (no changes detected)")
else:
    print("WARNING: file integrity violation detected")
