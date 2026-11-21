# Task 3 - Automated File Organizer & Cleanup Utility
# Datheon Python Programming Internship

import os
import shutil

# Extension -> Folder mapping
FILE_TYPES = {
    '.pdf': 'Documents',
    '.docx': 'Documents',
    '.txt': 'Documents',
    '.xlsx': 'Documents',
    '.pptx': 'Documents',
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.png': 'Images',
    '.gif': 'Images',
    '.mp4': 'Videos',
    '.mkv': 'Videos',
    '.mov': 'Videos',
    '.mp3': 'Music',
    '.wav': 'Music',
    '.zip': 'Archives',
    '.rar': 'Archives',
    '.py': 'Code',
    '.js': 'Code',
    '.html': 'Code',
    '.exe': 'Apps',
}

def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print("❌ Ye folder nahi mila!")
        return

    print(f"\nOrganizing: {folder_path}\n")
    files = os.listdir(folder_path)
    moved_count = 0

    for file in files:
        file_path = os.path.join(folder_path, file)

        # Folder ko skip karo, sirf files organize karo
        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(file)
        ext = ext.lower()

        category = FILE_TYPES.get(ext, 'Others')
        category_folder = os.path.join(folder_path, category)

        # Agar folder nahi hai to banao
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)
            print(f"📁 Folder banaya: {category}")

        # Agar same naam ki file pehle se hai to rename karo
        dest_path = os.path.join(category_folder, file)
        if os.path.exists(dest_path):
            name, extension = os.path.splitext(file)
            dest_path = os.path.join(category_folder, f"{name}_copy{extension}")

        try:
            shutil.move(file_path, dest_path)
            print(f"✅ {file} -> {category}/")
            moved_count += 1
        except PermissionError:
            print(f"⚠️ Permission denied: {file}")
        except Exception as e:
            print(f"⚠️ Error in {file}: {e}")

    print(f"\n🎉 Done! Total {moved_count} files organize ho gayi.")

def main():
    print("="*50)
    print("  AUTOMATED FILE ORGANIZER - Task 3")
    print("  Datheon Python Internship")
    print("="*50)
    print("\nExample: C:/Users/Keshav/Downloads")
    
    folder = input("\nKonsa folder organize karna hai? Path likho: ").strip()
    # Agar khali chhoda to current folder lega
    if folder == "":
        folder = os.getcwd()
        print(f"Current folder use kar rahe hai: {folder}")

    organize_folder(folder)

if __name__ == "__main__":
    main()
