# correction function for SVG, to be called via GUI button click
def correct_svg(list_of_filenames):
    # two-dimensional list with all replacements that need to be made. The string in listOfCorrections[0][0] will later be replaced with listOfCorrections[0][1], listOfCorrections[1][0] with listOfCorrections[1][1], and so on.
    # SVG descriptions of the URIs to be replaced come from GitHub
    # for normal icons: https://github.com/LLK/scratch-blocks/blob/develop/media/rotate-left.svg?short_path=42f5919
    # for extension icons for Scratch: https://github.com/LLK/scratch-gui/tree/develop/src/lib/libraries/extensions
    listOfCorrections = [
        # replace header so Inkscape can read style information, don't know why this is necessary
        ['style xmlns="http://www.w3.org/1999/xhtml"', 'style'],
        # Add and correct style information
        ['.blocklyDropdownText {\n        fill: #fff !important;\n    }\n    </style>', '.blocklyDropdownText {fill: #fff !important;}.st0{fill:#45993D;}.st1{fill:#4CBF56;}.st2{fill:#CF8B17;}.st3{fill:#FFFFFF;}.st4{fill:red}.st5{fill:#e0e0e0}.st6{fill:none;stroke:#666;stroke-width:.5;stroke-miterlimit:10}.cls-1{fill:#3d79cc;}.cls-2{fill:#fff;}</style>'],
        # Adds Arial as font
        ['font-family: "Helvetica Neue", Helvetica, sans-serif;', 'font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;'],
        # replace URIs with SVG paths
        # green flag
        ['<image height="24px" width="24px" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="data:image/svg+xml;base64,...', '<path class="st0" d="M20.8,3.7c-0.4-0.2-0.9-0.1-1.2,0.2...'],
        # repeat arrow
        ['<image height="24px" width="24px" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="data:image/svg+xml;base64,...', '<path class="st2" d="M23.3,11c-0.3,0.6-0.9,1-1.5,1h-1.6c-0.1,1.3-0.5,2.5-1,3.6...'],
        # rotate right arrow
        ['<image height="24px" width="24px" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="data:image/svg+xml;base64,...', '<path class="cls-1" d="M22.68,12.2a1.6,1.6,0,0,1-1.27.63H13.72...'],
        # rotate left arrow
        ['<image height="24px" width="24px" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="data:image/svg+xml;base64,...', '<path class="cls-1" d="M20.34,18.21a10.24,10.24,0,0,1-8.1,4.22...'],
        # music
        ['<image height="40px" width="40px" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="data:image/svg+xml;base64,...', '<defs><path d="M32.18 25.874C32.636 28.157 30.512 30 27.433 30c-3.07 0-5.923-1.843-6.372-4.126...'],
        # drawing pen
        ['<image height="40px" width="40px" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="data:image/svg+xml;base64,...', '<g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><use fill="#FFF" xlink:href="#a"/><path stroke-opacity=".1" stroke="#000" d="M28.456 21.675c-.01-.312-.087-.825-.256-1.702...'],
        # video sensing
        ['<image height="40px" width="40px" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="data:image/svg+xml;base64,...', '<g id="video-motion" transform="translate(0.000000, 10.000000)" fill-rule="nonzero" stroke="#000000"><circle id="Oval-Copy" fill="#FFFFFF"...'],
        # text to speech
        ['<image height="40px" width="40px" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="data:image/svg+xml;base64,...', '<g id="text2speech" transform="translate(4.000000, 4.000000)" fill-rule="nonzero" stroke="#000000"><path d="M11.5,17.6693435 C11.5,16.6539269 10.0060145,16.0844274 9.11256024,16.8883...'],
        # translate
        # cannot be replaced because there is no vector graphic of the icon on GitHub
        # MakeyMakey
        ['<image height="40px" width="40px" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="data:image/svg+xml;base64,...', '<g id="makeymakey-block-icon" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g id="makeymakey" transform="translate(3.500000, 6.000000)">...'],
        # replaces URI of dropdown arrow with SVG path and places it correctly in group, necessary because dropdown arrow is not its own group, but only an element in the dropdown group
        # removes URI and creates a group to place the dropdown arrow correctly
        ['<image height="12px" width="12px" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="data:image/svg+xml;base64,...', '<g '],
        # replaces URI of dropdown arrow with SVG path and closes the opened group
        ['xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="data:image/svg+xml;base64,...', 'style="cursor: default;"><g opacity="0.1"><path d="M12.71,2.44A2.41,2.41,0,0,1,12,4.16L8.08,8.08a2.45,2.45,0,0,1-3.45,0L0.72,4.16A2.42,2.42,0,0,1,0,2.44,2.48,2.48,0,0,1,.71.71C1,0.47,1.43,0,6.36,0S11.75,0.46,12,.71A2.44,2.44,0,0,1,12.71,2.44Z" fill="#231f20"/></g><path d="M6.36,7.79a1.43,1.43,0,0,1-1-.42L1.42,3.45a1.44,1.44,0,0,1,0-2c0.56-.56,9.31-0.56,9.87,0a1.44,1.44,0,0,1,0,2L7.37,7.37A1.43,1.43,0,0,1,6.36,7.79Z" fill="#fff"/></g>'],
        # Corrects error where dropdown text is shown in color of blocklyEditableText, when it actually should be white; hardcoded, not elegant
        ['<text class="blocklyText blocklyDropdownText" ', '<text class="blocklyText blocklyDropdownText" style="fill: #ffffff;" '],
        ['visibility: hidden', 'visibility: hidden; display: none']
    ]

    # returns only the filenames of .svg files, all other file types are ignored 
    svg_filenames = [s for s in list_of_filenames if '.svg' in s]

    # raises an error if no SVG files are selected
    if svg_filenames == []:
        raise NameError('Please select one or more SVG files.')
    else:
        # Loop over all files in folder
        for svg_filename in svg_filenames:
            # read content of file
            with open(svg_filename, "r") as f:
                filedata = f.read()

            # Replace the target string
            for i in range(len(listOfCorrections)):
                filedata = filedata.replace(listOfCorrections[i][0], listOfCorrections[i][1])
            
            # Add suffix "_corrected" to filename and create full new filepath
            new_filename = svg_filename.replace(".svg", "_corrected.svg")

            # write corrected content to new file
            with open(new_filename, "w") as f:
                f.write(filedata)
    # returns number of SVG files among the selected, and number of selected files
    return len(svg_filenames), len(list_of_filenames)