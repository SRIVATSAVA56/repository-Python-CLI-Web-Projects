import os
import shutil

# 1. O(1) Space: Global dictionary for instant O(1) lookups.
EXT_MAP = {
    # Images
    '.jpg': 'Images', '.jpeg': 'Images', '.png': 'Images', '.gif': 'Images', '.svg': 'Images',
    # Docs
    '.pdf': 'Docs', '.docx': 'Docs', '.doc': 'Docs', '.txt': 'Docs', '.xlsx': 'Docs', '.pptx': 'Docs', '.csv': 'Docs',
    # Videos
    '.mp4': 'Videos', '.mkv': 'Videos', '.avi': 'Videos', '.mov': 'Videos'
}

def organize_files(target_dir="."):
    # 2. O(1) Auxiliary Space: Cache created folders to eliminate redundant os.makedirs calls.
    created_dirs = set()
    
    # 3. O(N) Time, O(1) Memory: os.scandir yields an iterator. 
    # It fetches file attributes from the OS cache, making it significantly faster than os.listdir().
    with os.scandir(target_dir) as entries:
        for entry in entries:
            # Skip directories to prevent moving folders into folders
            if not entry.is_file():
                continue
                
            # Extract the extension and convert to lowercase
            _, ext = os.path.splitext(entry.name)
            ext = ext.lower()
            
            # 4. O(1) Time: Dictionary lookup to find the target folder
            folder_name = EXT_MAP.get(ext)
            
            if folder_name:
                folder_path = os.path.join(target_dir, folder_name)
                dest_path = os.path.join(folder_path, entry.name)
                
                # 5. O(1) Time: Check local set instead of querying the OS file system
                if folder_name not in created_dirs:
                    os.makedirs(folder_path, exist_ok=True)
                    created_dirs.add(folder_name)
                    
                # 6. O(1) Time: Move the file
                shutil.move(entry.path, dest_path)

if __name__ == "__main__":
    print("--- Optimized File Organizer ---")
    path = input("Enter directory path to organize (leave blank for current dir): ").strip()
    
    # Default to current directory if nothing is entered
    if not path:
        path = "."
    
    if os.path.exists(path):
        organize_files(path)
        print("Done! Files organized successfully.")
    else:
        print("Error: Directory does not exist.")