# Game Structure Generator

A small Python utility that generates a folder and file structure from a simple YAML definition.
It is particularly useful for quickly bootstrapping new projects (e.g., game projects with consistent layouts).

---

## Overview

This script reads a `folder.yaml` file and recreates the defined structure inside a target directory.

* Supports nested folders via indentation
* Can create empty files using a `:file` suffix
* Works well for reusable project templates

---

## Requirements

* Python 3.7+
* No external dependencies

---

## Usage

```bash
python game_structure.py <yaml_directory> <target_path>
```

### Arguments

| Argument         | Description                                   |
| ---------------- | --------------------------------------------- |
| `yaml_directory` | Directory containing `folder.yaml`            |
| `target_path`    | Directory where the structure will be created |

---

## Example

```bash
python game_structure.py C:\Config C:\Projects\MyGame
```

This will:

* Read: `C:\Config\folder.yaml`
* Create the structure inside: `C:\Projects\MyGame`

---

## YAML Format

The structure is defined using indentation (tabs or consistent spaces).

### Folders

```yaml
main:
	scenes:
	scripts:
```

### Files

Add `:file` to create a file:

```yaml
game_manager.gd:file
```

### Example Structure

```yaml
main:
	scenes:
	scripts:
		game_manager.gd:file

autoload:
	globals.gd:file
	constants.gd:file
```

---

## Notes

* Indentation defines hierarchy — keep it consistent.
* Mixed tabs and spaces may lead to incorrect results.
* Files are created empty by default.

---

## Use Cases

* Game project scaffolding (e.g., Godot)
* Rapid prototyping
* Standardizing team project layouts

---

## Limitations

* Not a full YAML parser (structure is indentation-based)
* No validation of duplicate paths
* No file content generation (only empty files)

---

## License

MIT (or specify your preferred license)

