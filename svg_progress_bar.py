import svgwrite
import math

# Test the function
percentage = 80
spacing = 7
stroke_width = 6
minus_radius = 10
bar_width_total = 400
bar_height = 50
fixed_sections = False
section_length = 10

def calculate_section_length(section_length, bar_width_total):
    # Calculate the number of sections
    num_sections = math.floor(bar_width_total / section_length)
    # Calculate the closest section length
    closest_section_length = bar_width_total / (num_sections + 1)
    return closest_section_length

def create_progress_bar(percentage, spacing, stroke_width, section_length, minus_radius, bar_width_total, bar_height, fixed_sections):
    # Calculate the width and height of the progress bar
    bar_width = bar_width_total * percentage / 100
    
    # Calculate the section length
    if fixed_sections:
        num_sections = 1

    print(f"Bar width: {bar_width}")

    # Calculate the position and size of the outer stroke rectangle
    outer_width = bar_width_total + 2 * spacing + stroke_width
    outer_height = bar_height + 2 * spacing + stroke_width
    # Calculate the dimensions of the canvas
    canvas_width = outer_width + stroke_width
    canvas_height = outer_height + stroke_width
    # Create a new SVG drawing
    dwg = svgwrite.Drawing(profile='tiny', size=(canvas_width, canvas_height))
    # Define the gradient fill for the progress bar and outer border
    gradient = dwg.defs.add(dwg.linearGradient(id='gradient', x1='0%', y1='0%', x2='100%', y2='0%'))
    gradient.add_stop_color(offset=0, color='#407adb')
    gradient.add_stop_color(offset=1, color='#b247de')
    # Calculate the position of the outer border
    outer_posx = stroke_width / 2
    outer_posy = stroke_width / 2
    # Calculate the corner radius for the outer border
    outer_radius = outer_height / 2 - minus_radius
    # Create a rounded rectangle for the outer border
    outer_border = dwg.rect(insert=(outer_posx, outer_posy), size=(outer_width, outer_height), rx=outer_radius, ry=outer_radius, fill='none', stroke=f'url(#gradient)', stroke_width=stroke_width)
    dwg.add(outer_border)
    # Calculate the position and width of the discontinuous progress bar
    inner_posx = spacing + stroke_width
    inner_posy = (outer_height + stroke_width) / 2 - (bar_height / 2)
    # Calculate the closest section length
    closest_section_length = calculate_section_length(section_length, bar_width_total)
    print(f"Closest section length: {closest_section_length}")
    # Calculate the number of sections
    if closest_section_length > 0:
        num_sections = int(bar_width / (closest_section_length * 2))
        remaining_width = bar_width % (closest_section_length * 2)
    else:
        num_sections = 0
        remaining_width = bar_width

    print(f"Number of sections: {num_sections}")
    print(f"Remaining width: {remaining_width}")
    # Calculate the corner radius for the progress bar
    inner_radius = bar_height / 2 - minus_radius
    # Create a rounded rectangle for the main gradient-filled progress bar
    progress_bar = dwg.rect(insert=(inner_posx, inner_posy), size=(bar_width, bar_height), rx=inner_radius, ry=inner_radius, fill=f'url(#gradient)')
    dwg.add(progress_bar)
    # Create white rectangles for the gaps
    if not fixed_sections:
        for i in range(num_sections):
            discontinuous_section_posx = inner_posx + i * closest_section_length * 2 + closest_section_length
            discontinuous_section_width = closest_section_length
            discontinuous_section = dwg.rect(insert=(discontinuous_section_posx, inner_posy), size=(discontinuous_section_width, bar_height), fill='white')
            dwg.add(discontinuous_section)
    # Return the SVG drawing
    return dwg

# Test the function

# dwg = create_progress_bar(percentage, spacing, stroke_width, section_length, minus_radius, bar_width_total, bar_height, fixed_sections)

# Save the SVG image
# dwg.saveas('progress_bar.svg')