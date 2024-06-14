import sys
import os

# Add the parent directory to the module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request
from svg_progress_bar import create_progress_bar

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_progress_bar', methods=['POST'])
def update_progress_bar():
    percentage = int(request.form['percentage'])
    spacing = int(request.form['spacing'])
    stroke_width = int(request.form['stroke_width'])
    minus_radius = int(request.form['minus_radius'])
    bar_width_total = int(request.form['bar_width_total'])
    bar_height = int(request.form['bar_height'])
    fixed_sections = bool(request.form.get('fixed_sections'))

    # Check if the section_length key is present in the form data
    if 'section_length' in request.form:
        section_length = int(request.form['section_length'])
    else:
        # Set a default value for section_length
        section_length = 10

    svg_code = create_progress_bar(percentage, spacing, stroke_width, section_length, minus_radius, bar_width_total, bar_height, fixed_sections)

    # Convert the Drawing object to a string
    svg_code = svg_code.tostring()

    return svg_code

if __name__ == '__main__':
    app.run(debug=True)
