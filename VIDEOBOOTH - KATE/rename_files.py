import os
from datetime import datetime
import shutil

# Folder where your videos are stored
VIDEO_DIR = 'videos'
BACKUP_DIR = 'backup_originals'

# Create backup folder if it doesn't exist
os.makedirs(BACKUP_DIR, exist_ok=True)

for filename in os.listdir(VIDEO_DIR):
    if filename.endswith('.mp4'):
        old_path = os.path.join(VIDEO_DIR, filename)
        stem = filename.split('.')[0]

        try:
            # interpret numeric name as milliseconds since epoch
            ts = int(stem)
            dt = datetime.fromtimestamp(ts / 1000)

            # Windows-safe filename (no ":" characters)
            new_name = dt.strftime('%m-%d-%y_%H-%M') + '.mp4'
            new_path = os.path.join(VIDEO_DIR, new_name)

            # Skip if name already exists
            if os.path.exists(new_path):
                print(f"⚠️ Skipping {filename}, {new_name} already exists.")
                continue

            # Backup original before renaming
            shutil.copy2(old_path, os.path.join(BACKUP_DIR, filename))

            # Rename file
            os.rename(old_path, new_path)
            print(f"✅ {filename} → {new_name}")

        except ValueError:
            print(f"Skipping {filename} (not a numeric name)")
