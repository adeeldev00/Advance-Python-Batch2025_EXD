import os
import sys

def print_tree(directory, prefix=''):
    """Recursively print directory structure with visual hierarchy"""
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory")
        return

    # Get all entries in the directory
    try:
        entries = os.listdir(directory)
    except PermissionError:
        print(f"{prefix}└── [Permission Denied]")
        return

    entries.sort()  
    for i, entry in enumerate(entries):
        path = os.path.join(directory, entry)
        is_last = i == len(entries) - 1

        connector = "└── " if is_last else "├── "
        
        print(f"{prefix}{connector}{entry}")

        if os.path.isdir(path):
            # For directories, add vertical lines for hierarchy
            extension = "    " if is_last else "│   "
            print_tree(path, prefix + extension)

def main():
    if len(sys.argv) != 2:
        print("Usage: python dirtree.py <directory_path>")
        sys.exit(1)

    root_dir = sys.argv[1]
    print(f"Directory tree for: {root_dir}")
    print_tree(root_dir)

if __name__ == "__main__":
    main()