
import os
import shutil
from pathlib import Path

# File extension mapping
file_types = {
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".ppt": "Documents",
    ".pptx": "Documents",
    ".xls": "Documents",
    ".xlsx": "Documents",

    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".svg": "Images",

    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",

    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",

    ".py": "Code",
    ".java": "Code",
    ".cpp": "Code",
    ".c": "Code",
    ".html": "Code",
    ".css": "Code",
    ".js": "Code"
}


def get_unique_path(destination):
    """Generate a unique filename if one already exists."""

    if not destination.exists():
        return destination

    folder = destination.parent
    name = destination.stem
    extension = destination.suffix

    count = 1

    while True:
        new_name = f"{name}_{count}{extension}"
        new_path = folder / new_name

        if not new_path.exists():
            return new_path

        count += 1


def organize_files():

    print("\n===== AUTOMATIC FILE ORGANIZER =====")

    folder_path = input(
        "\nEnter folder path to organize: "
    ).strip().strip('"')

    source = Path(folder_path).expanduser()

    if not source.exists() or not source.is_dir():
        print("Error: Invalid folder path!")
        return

    if not os.access(source, os.R_OK | os.W_OK):
        print("Error: Folder permission denied!")
        return

    # Scan files and prepare a plan
    plan = []

    try:
        with os.scandir(source) as entries:

            for entry in entries:

                if not entry.is_file(follow_symlinks=False):
                    continue

                file_path = Path(entry.path)

                extension = file_path.suffix.lower()

                category = file_types.get(
                    extension, "Others"
                )

                destination_folder = source / category

                destination = (
                    destination_folder / file_path.name
                )

                destination = get_unique_path(destination)

                plan.append(
                    (file_path, destination)
                )

    except PermissionError:
        print("Error: Cannot access this folder!")
        return

    if not plan:
        print("\nNo files found to organize.")
        return

    # Preview the operations
    print("\nFiles to be organized:")
    print("--------------------------------")

    for old_path, new_path in plan:
        print(
            old_path.name,
            " --> ",
            new_path.parent.name
        )

    print("--------------------------------")
    print("Total files found:", len(plan))

    choice = input(
        "\nDo you want to organize these files? (yes/no): "
    ).lower()

    if choice != "yes":
        print("Organization cancelled.")
        return

    # Move files safely
    moved = 0
    failed = 0

    for old_path, new_path in plan:

        try:
            new_path.parent.mkdir(
                parents=True, exist_ok=True
            )

            # Check filename again before moving
            new_path = get_unique_path(new_path)

            shutil.move(
                str(old_path),
                str(new_path)
            )

            print("Moved:", old_path.name)
            moved += 1

        except (PermissionError, OSError) as error:
            print("Cannot move:", old_path.name)
            print("Reason:", error)
            failed += 1

    # Final summary
    print("\n===== ORGANIZATION SUMMARY =====")
    print("Total files found:", len(plan))
    print("Files moved:", moved)
    print("Files failed:", failed)
    print("Organization completed!")


# Run the organizer
if __name__ == "__main__":
    organize_files()
