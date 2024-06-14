document.addEventListener('DOMContentLoaded', function() {
    const progress = document.getElementById('progress');
    const slider = document.getElementById('percentage-slider');

    function updateProgressBar(percentage) {
        const barWidthTotal = 400;
        const spacing = 7;
        const stroke_width = 6;
        const section_length = 10;
        const minus_radius = 10;
        const barHeight = 50;

        const barWidth = barWidthTotal * percentage / 100;
        const numSections = Math.floor(barWidthTotal / section_length);
        const closestSectionLength = barWidthTotal / (numSections + 1);
        const numSectionsForBar = Math.floor(barWidth / (closestSectionLength * 2));
        const remainingWidth = barWidth % (closestSectionLength * 2);

        progress.style.width = `${barWidth}px`;

        // Remove any existing gap divs
        const existingGaps = document.querySelectorAll('.gap');
        existingGaps.forEach(gap => gap.remove());

        // Add gap divs
        for (let i = 0; i < numSectionsForBar; i++) {
            const gapDiv = document.createElement('div');
            gapDiv.classList.add('gap');
            gapDiv.style.width = `${closestSectionLength}px`;
            gapDiv.style.height = `${barHeight}px`;
            gapDiv.style.position = 'absolute';
            gapDiv.style.left = `${i * closestSectionLength * 2 + closestSectionLength}px`;
            gapDiv.style.top = '0';
            gapDiv.style.backgroundColor = 'white';
            progress.appendChild(gapDiv);
        }
    }

    slider.addEventListener('input', function() {
        const percentage = slider.value;
        updateProgressBar(percentage);
    });

    // Initialize progress bar with default percentage
    updateProgressBar(slider.value);
});
