# SVG Progress Bar Generator
**You can try it here: https://svg-progress-bar.onrender.com/**

This Python script generates an SVG progress bar based on a given percentage. The progress bar can be customized with various parameters such as spacing, stroke width, minus radius, bar width, bar height, and section length.

## Features

- Generates a gradient-filled progress bar.
- Supports discontinuous progress bars with customizable section lengths.
- Allows for customization of spacing, stroke width, minus radius, bar width, and bar height.

## Usage

1. Install the required `svgwrite` library using pip:

```bash
pip install svgwrite
```

2. Run the script with your desired parameters:

```python
percentage = 80
spacing = 7
stroke_width = 6
minus_radius = 10
bar_width_total = 400
bar_height = 50
fixed_sections = False
section_length = 10

dwg = create_progress_bar(percentage, spacing, stroke_width, section_length, minus_radius, bar_width_total, bar_height, fixed_sections)
dwg.saveas('progress_bar.svg')
```

3. The generated SVG progress bar will be saved as `progress_bar.svg` in your current working directory.

## Parameters

- `percentage`: The completion percentage of the progress bar (0-100).
- `spacing`: The space between the progress bar and the outer border.
- `stroke_width`: The width of the outer border.
- `minus_radius`: The amount to subtract from the corner radius of the progress bar and outer border.
- `bar_width_total`: The total width of the progress bar.
- `bar_height`: The height of the progress bar.
- `fixed_sections`: Whether to use fixed-length sections for the discontinuous progress bar.
- `section_length`: The length of each section in the discontinuous progress bar.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
