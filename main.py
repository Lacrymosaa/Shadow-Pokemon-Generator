from pathlib import Path
from typing import Tuple
import numpy as np
from PIL import Image

OVERLAY_COLOR: Tuple[int, int, int] = (0x47, 0x21, 0x55)
OPACITY: float = 0.7

SRC_FOLDERS = {
    "Back":  "Shadow_Back",
    "Front": "Shadow_Front",
    "Icons": "Shadow_Icons",
}

IMG_EXT = {".png"}

def apply_overlay(src_path: Path, dst_path: Path) -> None:
    img = Image.open(src_path).convert("RGBA")
    data = np.asarray(img, dtype=float)
    mask = data[..., 3] > 0
    for ch, value in enumerate(OVERLAY_COLOR):
        data[..., ch][mask] = (1 - OPACITY) * data[..., ch][mask] + OPACITY * value
    result = Image.fromarray(data.astype(np.uint8), "RGBA")
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    result.save(dst_path)

def process_folder(src_root: Path, dst_root: Path) -> None:
    for src_file in src_root.rglob("*"):
        if src_file.suffix.lower() in IMG_EXT:
            rel = src_file.relative_to(src_root)
            shadow_rel = rel.parent / f"{rel.stem}_shadow{rel.suffix}"
            dst_file = dst_root / shadow_rel
            apply_overlay(src_file, dst_file)

def main() -> None:
    for src_name, dst_name in SRC_FOLDERS.items():
        src_root = Path(src_name)
        dst_root = Path(dst_name)
        if not src_root.exists():
            print(f"Aviso: pasta '{src_root}' não encontrada, pulando.")
            continue
        process_folder(src_root, dst_root)
        print(f"{src_root} -> {dst_root}")

if __name__ == "__main__":
    main()