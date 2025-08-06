# 🖼️ JPG to GIF Converter with ImageIO

This Python script reads a list of `.jpg` images and combines them into a looping `.gif` using the `imageio.v3` library.

## 📋 What It Does

- Loads images from a predefined list (`filenames`)
- Appends them to a list
- Saves them as a GIF (`shukla.gif`)
- Sets a frame duration of 500ms per image
- The GIF loops infinitely

## 🧾 Requirements

- Python 3.x
- `imageio` library (v3)

Install `imageio` via pip:

```bash
pip install imageio
