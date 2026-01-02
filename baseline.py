#import Path for file handling
from pathlib import Path

config_file = Path("config.txt")
baseline_file = Path("baseline.txt")

#read current file contents
current_contents = config_file.read_text(encoding="utf-8")

#write current contents to baseline file
baseline_file.write_text(current_contents, encoding="utf-8")

print("Baseline created from monitored_file/config.txt")
