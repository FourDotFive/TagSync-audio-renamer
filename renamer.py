import os
import eyed3
from rich.table import Table
from rich.console import Console


def rename_files():
    path = input("Path: ")

    table = Table()

    table.add_column("Before", style="cyan", no_wrap=True)
    table.add_column("After", style="green")

    file_list = os.listdir(path)

    for file_name in file_list:
        file_path = os.path.join(path, file_name)
        audio_file = eyed3.load(file_path)

        if audio_file is not None:
            artist = audio_file.tag.artist
            title = audio_file.tag.title
            if artist is not None and title is not None:
                characters = ['<', '>', '/', '\\', ':', '*', '?', '|', '\"']
                for char in characters:
                    title = title.replace(char, '')
                try:
                    os.rename(file_path, path + "\\" + artist + " - " + title + ".mp3")
                    table.add_row(file_name, artist + " - " + title + ".mp3")
                except OSError as ex:
                    print("{} - {}".format(artist, title))
            else:
                table.add_row(file_name, 'Error. Check file\'s tags')
    console = Console()
    console.print(table)


if __name__ == "__main__":
    rename_files()
