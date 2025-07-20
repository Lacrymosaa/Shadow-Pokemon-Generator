# Shadow Pokémon Generator

This script batch-generates Shadow Pokémon sprites by applying a semi-transparent overlay to images. It processes all `.png` images in specified source folders and saves the new Shadow variants with modified file names in corresponding output folders.

## Features

- Applies a colored overlay to every image with alpha transparency.
- Outputs images in the same structure, adding `_shadow` to file names.
- Customizable:
  - Overlay color (RGB)
  - Overlay opacity (0.0 to 1.0)
  - Source and destination folder pairs

## Usage

1. **Set your folder mappings** in the `SRC_FOLDERS` dictionary:

```python
SRC_FOLDERS = {
    "Back":  "Shadow_Back",
    "Front": "Shadow_Front",
    "Icons": "Shadow_Icons",
}
