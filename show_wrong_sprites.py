import xml.etree.ElementTree as ET
import os

def find_incorrect_sprites(file_path):
    # Expand ~ in the file path
    file_path = os.path.expanduser(file_path)

    # Parse the XML file
    try:
        tree = ET.parse(file_path)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return
    root = tree.getroot()

    # Find the <Sprites> tag
    game = root.find('Game')
    if game is None:
        print("No <Game> tag found.")
        return
    sprites = game.find('Sprites')
    if sprites is None:
        print("No <Sprites> tag found.")
        return

    # Initialize a list to hold incorrect sprites
    incorrect_sprites = []

    # Find all <FileName> tags under <Sprites>
    for file_name_tag in sprites.findall('.//FileName'):
        if file_name_tag.text and not file_name_tag.text.startswith("Y:\\Google Drive"):
            incorrect_sprites.append(file_name_tag.text)

    # Output the list of incorrect sprites, one per line
    if incorrect_sprites:
        print("Incorrect sprites found:")
        for sprite in incorrect_sprites:
            print(sprite)
    else:
        print("All sprites are correctly formatted.")

# Usage example
file_path = os.path.join(os.getcwd(), 'Game.agf')  # Use the Game.agf in the current directory
find_incorrect_sprites(file_path)
