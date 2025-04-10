# ScratchSVGKorrektur
The Python program ScratchSVGKorrektur corrects SVG files by replacing specific strings in the files with predefined substitutions. It filters the input filenames to process only SVGs, reads their content, performs the replacements, and saves the modified files under a new name with the suffix "_corrected".

Here are the specific replacements:

XML Namespace:
Replaces 'style xmlns="http://www.w3.org/1999/xhtml"' with 'style' to ensure Inkscape can read style information correctly.

Style Changes:
Replaces a specific CSS rule for .blocklyDropdownText with a new rule that includes additional color definitions.

Font Changes:
Changes the font-family definition from 'font-family: "Helvetica Neue", Helvetica, sans-serif;' to include Arial.

Replacing URIs with SVG Paths:
For certain icons (like green flags, arrows, musical notes, etc.), replaces URI references with corresponding SVG paths to ensure proper display.

Dropdown Text Color:
Adds a CSS style for the dropdown text to set its color to white.

Visibility:
Changes 'visibility: hidden' to 'visibility: hidden; display: none' to ensure the element is not displayed.

These replacements are necessary to ensure that the SVG files render correctly in applications like Inkscape or web browsers.
