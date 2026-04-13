#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate PWA icons for Slime Simulator with blob/slime visuals."""

from PIL import Image, ImageDraw, ImageFilter
import math
import os
import sys
import io

# Set stdout to handle UTF-8
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def create_blob_icon(size, is_maskable=False):
    """Generate a blob icon with slime-like appearance."""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img, 'RGBA')

    cx, cy = size // 2, size // 2
    base_radius = size // 2.5

    # Generate blob shape with random wobbles
    points = []
    num_points = 32
    for i in range(num_points):
        angle = (i / num_points) * 2 * math.pi
        # Add wobble to make it organic
        wobble = base_radius * (0.85 + 0.15 * math.sin(i * 0.5))
        x = cx + wobble * math.cos(angle)
        y = cy + wobble * math.sin(angle)
        points.append((x, y))

    # Draw blob with gradient-like fill
    # Base color: a nice slime pink/peach
    draw.polygon(points, fill=(255, 107, 157, 255), outline=(200, 60, 110, 255))

    # Add shine effect
    shine_radius = int(base_radius * 0.4)
    shine_x = int(cx - base_radius * 0.3)
    shine_y = int(cy - base_radius * 0.3)
    draw.ellipse(
        [shine_x - shine_radius, shine_y - shine_radius,
         shine_x + shine_radius, shine_y + shine_radius],
        fill=(255, 180, 200, 180)
    )

    # Apply blur for softer edges
    img = img.filter(ImageFilter.GaussianBlur(radius=2))

    # For maskable icons, ensure enough padding for safe zone
    if is_maskable:
        # Create a slightly larger image and place blob in center
        safe_size = int(size * 0.8)
        final_img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        offset = (size - safe_size) // 2
        img_resized = img.resize((safe_size, safe_size), Image.Resampling.LANCZOS)
        final_img.paste(img_resized, (offset, offset), img_resized)
        return final_img

    return img

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    print("Generating PWA icons...")

    # 192x192 regular icon
    icon_192 = create_blob_icon(192, is_maskable=False)
    icon_192.save('icon-192.png')
    print("[OK] icon-192.png")

    # 512x512 regular icon
    icon_512 = create_blob_icon(512, is_maskable=False)
    icon_512.save('icon-512.png')
    print("[OK] icon-512.png")

    # 192x192 maskable icon
    maskable_192 = create_blob_icon(192, is_maskable=True)
    maskable_192.save('icon-maskable-192.png')
    print("[OK] icon-maskable-192.png")

    # 512x512 maskable icon
    maskable_512 = create_blob_icon(512, is_maskable=True)
    maskable_512.save('icon-maskable-512.png')
    print("[OK] icon-maskable-512.png")

    print("\nAll icons generated successfully!")

if __name__ == '__main__':
    main()
