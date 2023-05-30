# TagSync Audio Renamer

## Description

TagSync Audio Renamer is a Python script that automates the process of renaming audio files based on their ID3 tags. The script utilizes the eyeD3 library to access metadata information such as the artist and title. This information is then used to generate a new name for the audio file.

The script also uses the rich library to create a neat, color-coded console table output that clearly displays the changes made to each file name.

## Functionalities

- Scans a specified directory for audio files
- Accesses ID3 tags (metadata) within each file
- Extracts Artist and Title information from the metadata
- Constructs a new file name in the format `Artist - Title.mp3`
- Special characters (`<`, `>`, `/`, `\`, `:`, `*`, `?`, `|`, `"`) in the title are replaced to avoid file naming issues
- Renames the file using the newly constructed name
- If the ID3 tags are missing or incomplete, the file is not renamed and an error message is displayed in the console
- Displays a table in the console to show the old and new names of each file

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. Make sure Python 3 and pip are installed in your system
4. Install the dependencies:
    ```
    pip install eyed3 rich
    ```

## Note

The audio files should be in `.mp3` format and must contain valid ID3 tags (Artist and Title). The script is not designed to handle other file formats or missing tags.

## Dependencies

- [eyed3](https://eyed3.readthedocs.io/en/latest/): A Python module for manipulating ID3 tags.
- [rich](https://rich.readthedocs.io/en/latest/): A Python library for rich text and beautiful formatting in the terminal.
