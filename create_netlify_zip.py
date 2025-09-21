import os
import zipfile
from datetime import datetime

def create_netlify_zip():
    # Files to include in the zip
    files_to_include = [
        'static_index.html',
        'netlify.toml',
        'README.md'
    ]
    
    # Create zip filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_filename = f"netlify_deployment_{timestamp}.zip"
    
    # Create the zip file
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for file in files_to_include:
            if os.path.exists(file):
                zipf.write(file)
                print(f"Added {file} to {zip_filename}")
            else:
                print(f"Warning: {file} not found, skipping")
    
    print(f"\nZip file created: {zip_filename}")
    print("You can now upload this zip file to Netlify using the drag-and-drop interface.")

if __name__ == "__main__":
    create_netlify_zip()