# 🐱 toolkitten

**Toolkitten** is a lightweight utility library for Python, offering tools for plotting, mathematics, and machine learning — with a touch of feline charm.

> _"Toolkitten: Smart utilities wrapped in a soft purr."_

---

## 🔍 Overview

Toolkitten is designed to simplify routine plotting tasks, layout computations, and experiment visualization. It's particularly useful for data scientists, researchers, and ML enthusiasts who want a quick and customizable way to visualize and organize their results.

---

## ✨ Features

- 📊 Plot multiple functions with automatic subplot arrangements
- 🧮 Utility functions for visualizing images and data side-by-side
- 🧠 Simple, flexible interface for reusable plotting logic
- 🐾 Clean architecture with type-safe protocols and custom exceptions

---

## 📦 Example Usage

```python
from toolkitten.plot import plot_subplots
from toolkitten.plot.function import plot_image

# Prepare some example image plots
plot1 = plot_image(img1, "First image")
plot2 = plot_image(img2, "Second image")

# Display them
plot_subplots([plot1, plot2], title="Image Comparison")
```
