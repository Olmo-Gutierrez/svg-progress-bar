// Get the progress bar element
const progressBar = document.getElementById('progress-bar');

// Get all the slider elements
const percentageSlider = document.getElementById('percentage');
const spacingSlider = document.getElementById('spacing');
const strokeWidthSlider = document.getElementById('stroke-width');
const minusRadiusSlider = document.getElementById('minus-radius');
const barWidthTotalSlider = document.getElementById('bar-width-total');
const barHeightSlider = document.getElementById('bar-height');
const fixedSectionsCheckbox = document.getElementById('fixed-sections');
const sectionLengthSlider = document.getElementById('section-length');

// Function to update the progress bar
function updateProgressBar() {
    // Get the current values of the sliders and checkbox
    const percentage = percentageSlider.value;
    const spacing = spacingSlider.value;
    const strokeWidth = strokeWidthSlider.value;
    const minusRadius = minusRadiusSlider.value;
    const barWidthTotal = barWidthTotalSlider.value;
    const barHeight = barHeightSlider.value;
    const fixedSections = fixedSectionsCheckbox.checked;
    const sectionLength = sectionLengthSlider.value;

    // Generate the new progress bar SVG
    const svg = createProgressBar(percentage, spacing, strokeWidth, sectionLength, minusRadius, barWidthTotal, barHeight, fixedSections);

    // Create a data URL for the SVG
    const svgDataUrl = 'data:image/svg+xml;utf8,' + encodeURIComponent(svg.tostring());

    // Update the progress bar element with the new SVG data URL
    progressBar.data = svgDataUrl;

}

// Add event listeners to the sliders and checkbox
percentageSlider.addEventListener('input', updateProgressBar);
spacingSlider.addEventListener('input', updateProgressBar);
strokeWidthSlider.addEventListener('input', updateProgressBar);
minusRadiusSlider.addEventListener('input', updateProgressBar);
barWidthTotalSlider.addEventListener('input', updateProgressBar);
barHeightSlider.addEventListener('input', updateProgressBar);
fixedSectionsCheckbox.addEventListener('change', updateProgressBar);
sectionLengthSlider.addEventListener('input', updateProgressBar);

// Function to show/hide the section length slider based on the fixed sections checkbox
function toggleSectionLengthSlider() {
    if (fixedSectionsCheckbox.checked) {
        sectionLengthSlider.style.display = 'flex';
        sectionLengthInput.disabled = true;
    } else {
        sectionLengthSlider.style.display = 'flex';
        sectionLengthInput.disabled = false;
    }
}


// Add event listener to the fixed sections checkbox
fixedSectionsCheckbox.addEventListener('change', toggleSectionLengthSlider);

// Initial update of the progress bar
updateProgressBar();
