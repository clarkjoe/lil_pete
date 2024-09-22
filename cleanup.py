import xml.etree.ElementTree as ET
import os
import argparse

def replace_tags(source_file, target_file, reverse=False):
    # Expand ~ in file paths to full paths
    source_file = os.path.expanduser(source_file)

    # Parse the source XML file
    try:
        source_tree = ET.parse(source_file)
    except FileNotFoundError:
        print(f"Source file not found: {source_file}")
        return
    source_root = source_tree.getroot()

    # Parse the target XML file
    try:
        target_tree = ET.parse(target_file)
    except FileNotFoundError:
        print(f"Target file not found: {target_file}")
        return
    target_root = target_tree.getroot()

    # Replace <Sprites> tag with text replacement (G:\ <-> Y:\Google Drive\ based on reverse flag)
    replace_sprites(source_root, target_root, reverse)

    # Replace <Views> tag (no text replacement, just a direct copy)
    replace_views(source_root, target_root)

    # Write the modified tree back to the target file with the original XML declaration and comments
    write_with_declaration(source_file, target_file, target_root)


def replace_sprites(source_root, target_root, reverse):
    # Find the <Sprites> tag under <AGSEditorDocument><Game> in the source file
    source_game = source_root.find('Game')
    if source_game is None:
        print("No <Game> tag found in the source file.")
        return
    source_sprites = source_game.find('Sprites')

    if source_sprites is None:
        print("No <Sprites> tag found in the source file.")
        return

    # Determine the replacement direction
    if reverse:
        from_path = "Y:\\Google Drive\\"
        to_path = "G:\\"
    else:
        from_path = "G:\\"
        to_path = "Y:\\Google Drive\\"

    # Replace all occurrences based on the direction
    for elem in source_sprites.iter():
        if elem.text:
            elem.text = elem.text.replace(from_path, to_path)
        if elem.tail:
            elem.tail = elem.tail.replace(from_path, to_path)

    # Find the <Sprites> tag under <AGSEditorDocument><Game> in the target file
    target_game = target_root.find('Game')
    if target_game is None:
        print("No <Game> tag found in the target file.")
        return
    target_sprites = target_game.find('Sprites')

    if target_sprites is not None:
        # Remove the existing <Sprites> tag in the target file
        target_game.remove(target_sprites)
    
    # Append the modified <Sprites> tag from the source to the target file's <Game> section
    target_game.append(source_sprites)


def replace_views(source_root, target_root):
    # Find the <Views> tag under <AGSEditorDocument><Game> in the source file
    source_game = source_root.find('Game')
    if source_game is None:
        print("No <Game> tag found in the source file.")
        return
    source_views = source_game.find('Views')

    if source_views is None:
        print("No <Views> tag found in the source file.")
        return

    # Find the <Views> tag under <AGSEditorDocument><Game> in the target file
    target_game = target_root.find('Game')
    if target_game is None:
        print("No <Game> tag found in the target file.")
        return
    target_views = target_game.find('Views')

    if target_views is not None:
        # Remove the existing <Views> tag in the target file
        target_game.remove(target_views)
    
    # Append the modified <Views> tag from the source to the target file's <Game> section
    target_game.append(source_views)


def write_with_declaration(source_file, target_file, target_root):
    """
    Writes the XML to the target file, ensuring the XML declaration, comments, and Windows-style
    newlines (\r\n) are preserved.
    """
    # Open the source file to copy the XML declaration and comments, but skip <AGSEditorDocument> tag
    with open(source_file, 'r', encoding='utf-8') as src:
        initial_lines = []
        for line in src:
            # Stop reading once we reach the start of the <AGSEditorDocument> tag
            if line.strip().startswith("<AGSEditorDocument"):
                break
            initial_lines.append(line)

    # Convert the modified target XML tree back to a string
    xml_string = ET.tostring(target_root, encoding='unicode', method='xml')

    # Write everything to the target file with Windows-style newlines
    with open(target_file, 'w', encoding='utf-8', newline='\r\n') as tgt:
        # Write the initial lines (XML declaration and comments)
        tgt.writelines(initial_lines)

        # Write the rest of the XML content (including the <AGSEditorDocument> tag)
        tgt.write(xml_string)


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Replace tags in XML files with optional reverse replacement.")
    parser.add_argument(
        "source_file", 
        nargs="?", 
        default="~/Google Drive/My Drive/Pixel Studio/LilPete/LilPete_game/Game.agf", 
        help="The path to the source XML file (default: '~/Google Drive/My Drive/Pixel Studio/LilPete/LilPete_game/Game.agf')."
    )
    parser.add_argument(
        "target_file", 
        nargs="?", 
        default=os.path.join(os.getcwd(), 'Game.agf'), 
        help="The path to the target XML file (default: './Game.agf')."
    )
    parser.add_argument(
        "--reverse", 
        action="store_true", 
        help="Reverse the replacement (replace Y:\\Google Drive\\ with G:\\)."
    )

    # Parse arguments
    args = parser.parse_args()

    # Call the replace_tags function with the reverse flag
    replace_tags(args.source_file, args.target_file, reverse=args.reverse)


if __name__ == "__main__":
    main()
