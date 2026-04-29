import os
import sys
from pathlib import Path


def create_structure_from_yaml(yaml_dir, target_path):
    """
    Creates folders and files from a YAML file.
    
    Args:
        yaml_dir: Directory where folder.yaml is located
        target_path: Target path where the structure should be created
    """
    
    yaml_file_path = Path(yaml_dir) / "folder.yaml"
    
    if not yaml_file_path.exists():
        print(f"❌ Error: {yaml_file_path} not found!")
        sys.exit(1)
    
    target_path = Path(target_path)
    target_path.mkdir(parents=True, exist_ok=True)
    
    print(f"📄 YAML source: {yaml_file_path}")
    print(f"📁 Target directory: {target_path}")
    print("-" * 60)
    
    with open(yaml_file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    path_stack = [target_path]
    
    for line in lines:
        if not line.strip():
            continue
        
        indent_level = 0
        space_count = 0

        for char in line:
            if char == '\t':
                indent_level += 1
            elif char == ' ':
                space_count += 1
                if space_count == 4:
                    indent_level += 1
                    space_count = 0
            else:
                break
        
        line_content = line.lstrip('\t')
        
        if '#' in line_content:
            line_content = line_content.split('#')[0]
        
        line_content = line_content.strip()
        
        if not line_content:
            continue
        
        is_file = line_content.endswith(':file')
        
        if ':' in line_content:
            name = line_content.split(':')[0].strip()
        else:
            name = line_content.strip()
        
        path_stack = path_stack[:indent_level + 1]
        
        current_path = path_stack[-1] / name
        
        if is_file:
            current_path.parent.mkdir(parents=True, exist_ok=True)
            current_path.touch()
            print(f"📄 File created: {current_path.relative_to(target_path)}")
        else:
            current_path.mkdir(parents=True, exist_ok=True)
            print(f"📁 Folder created: {current_path.relative_to(target_path)}")
            
            path_stack.append(current_path)
    
    print("-" * 60)
    print(f"✅ Done! Structure created in: {target_path}")


def main():
    if len(sys.argv) != 3:
        print("Usage: python create_structure.py <yaml_directory> <target_path>")
        print()
        print("Example:")
        print("  python create_structure.py C:\\Config C:\\Users\\Name\\Projects\\NewProject")
        print()
        print("Note: The folder.yaml file must be located in the specified yaml_directory.")
        sys.exit(1)
    
    yaml_dir = sys.argv[1]
    target_path = sys.argv[2]
    
    create_structure_from_yaml(yaml_dir, target_path)


if __name__ == "__main__":
    main()