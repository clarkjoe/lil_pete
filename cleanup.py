import xml.etree.ElementTree as ET
import os
import argparse
import copy
import sys

default_paths = {
    "joey": {
        "source": "~/Google Drive/Shared drives/Lil Pete/LilPete_Game_Gold/Game.agf",
        "target": os.path.join(os.getcwd(), 'Game.agf'),
        "user_path": "Y:/Google Drive/Shared drives/Lil Pete/Pixel Studio/LilPete/",
        "user_path_other": "Y:/Google Drive/Shared drives/Lil Pete/Game_Assets_Gold/LilPete/"
    },
    "greg": {
        "source": "~/Google Drive/My Drive/Pixel Studio/LilPete/LilPete_game/Game_greg.agf",
        "target": os.path.join(os.getcwd(), 'Game_greg.agf'),
        "user_path": "G:/Users/Greg/"
    }
}

source_path_to_replace = "G:\\My Drive\\Pixel Studio\\LilPete\\"
source_path_to_replace_other = "G:\\My Drive\\Game_Assets_Gold\\LilPete\\"

def process_pre(source_file, target_file, user_path, user_path_other):
    source_file, target_file = get_expanded_file_paths(source_file, target_file)
    source_root, target_root = get_roots(source_file, target_file)

    replace_sprites_with_user_path(source_root, target_root, user_path, user_path_other)
    replace_views(source_root, target_root)
    write_xml_with_header(source_file, target_file, target_root, use_crlf=True)

def process_post(source_file, target_file, user_path):
    source_file, target_file = get_expanded_file_paths(source_file, target_file)
    placeholder = "PLACEHOLDER/"

    try:
        with open(source_file, 'r', encoding='utf-8', newline="\r\n") as file:
            content = file.read()

        updated_content = content.replace(user_path, placeholder)

        with open(target_file, 'w', encoding='utf-8', newline='') as file:
            file.write(updated_content)

        print(f"Replaced '{user_path}' with '{placeholder}' and saved to {target_file}.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

def process_convert(source_file, target_file, user_path):
    source_file, target_file = get_expanded_file_paths(source_file, target_file)
    placeholder = "PLACEHOLDER/"

    try:
        with open(source_file, 'r', encoding='utf-8', newline="\r\n") as file:
            content = file.read()

        updated_content = content.replace(placeholder, user_path)

        with open(target_file, 'w', encoding='utf-8', newline='') as file:
            file.write(updated_content)

        print(f"Replaced '{user_path}' with '{placeholder}' and saved to {target_file}.")
    
    except Exception as e:
        print(f"An error occurred: {e}")


def get_expanded_file_paths(source_file, target_file):
    source_file = os.path.expanduser(source_file)
    target_file = os.path.expanduser(target_file)
    return source_file, target_file

def get_roots(source_file, target_file):
    source_tree = ET.parse(source_file)
    target_tree = ET.parse(target_file)
    source_root = source_tree.getroot()
    target_root = target_tree.getroot()
    return source_root, target_root

def replace_sprites_with_user_path(source_root, target_root, user_path, user_path_other):
    source_game = source_root.find('Game')
    target_game = target_root.find('Game')

    if source_game is None or target_game is None:
        print("No <Game> tag found in the source or target file.")
        return

    source_sprites = source_game.find('Sprites')
    if source_sprites is None:
        print("No <Sprites> tag found in the source file.")
        return

    modified_sprites = copy.deepcopy(source_sprites)
    
    for sprite in modified_sprites.findall('.//FileName'):
        if sprite.text:
            sprite.text = sprite.text.replace(source_path_to_replace, user_path)
            sprite.text = sprite.text.replace(source_path_to_replace_other, user_path_other)
            sprite.text = sprite.text.replace("\\", "/")

    target_sprites = target_game.find('Sprites')
    if target_sprites is not None:
        target_game.remove(target_sprites)
    target_game.append(modified_sprites)

def replace_sprites_with_placeholder(source_root, target_root, user_path):
    source_game = source_root.find('Game')
    target_game = target_root.find('Game')

    if source_game is None or target_game is None:
        print("No <Game> tag found in the source or target file.")
        return

    source_sprites = source_game.find('Sprites')
    if source_sprites is None:
        print("No <Sprites> tag found in the source file.")
        return

    modified_sprites = copy.deepcopy(source_sprites)

    placeholder = "PLACEHOLDER/"
    for sprite in modified_sprites.findall('.//FileName'):
        if sprite.text:
            sprite.text = sprite.text.replace(user_path, placeholder)

    target_sprites = target_game.find('Sprites')
    if target_sprites is not None:
        target_game.remove(target_sprites)
    target_game.append(modified_sprites)

def replace_views(source_root, target_root):
    source_game = source_root.find('Game')
    target_game = target_root.find('Game')

    if source_game is None or target_game is None:
        print("No <Game> tag found in the source or target file.")
        return

    source_views = source_game.find('Views')
    if source_views is None:
        print("No <Views> tag found in the source file.")
        return

    target_views = target_game.find('Views')
    if target_views is not None:
        target_game.remove(target_views)
    target_game.append(source_views)

def write_xml_with_header(source_file, target_file, target_root, use_crlf=False):
    newline = '\r\n' if use_crlf else '\n'

    with open(source_file, 'r', encoding='utf-8', newline=newline) as src:
        initial_lines = []
        for line in src:
            initial_lines.append(line)
            if line.strip().startswith("<!--"):
                break

    xml_string = ET.tostring(target_root, encoding='unicode', method='xml')
    xml_string = xml_string.replace('\n', '\r\n')

    with open(target_file, 'w', encoding='utf-8', newline='') as tgt:
        tgt.writelines(initial_lines)
        tgt.write(xml_string)

def validate_args(args):
    if not (args.joey or args.greg):
        print("Error: You must provide exactly one of --joey or --greg.")
        sys.exit(1)

def get_user_path(args):
    if args.joey:
        return default_paths['joey']['user_path']
    elif args.greg:
        return default_paths['greg']['user_path']

def get_user_path_other(args):
    if args.joey:
        return default_paths['joey']['user_path_other']
    elif args.greg:
        return default_paths['greg']['user_path_other']

def get_file_paths(args):
    if args.joey:
        source = default_paths['joey']['source']
        target = default_paths['joey']['target']
    elif args.greg:
        source = default_paths['greg']['source']
        target = default_paths['greg']['target']
    return source, target

def main():
    parser = argparse.ArgumentParser(description="Process XML files and update file paths.")
    
    subparsers = parser.add_subparsers(dest="operation", help="Operation to perform: 'pre' or 'post'.")
    
    pre_parser = subparsers.add_parser('pre', help="Replace 'G:/My Drive/Pixel Studio' with a user-specific path.")
    pre_parser.add_argument("--joey", action="store_true", help="Use Joey's path.")
    pre_parser.add_argument("--greg", action="store_true", help="Use Greg's path.")

    post_parser = subparsers.add_parser('post', help="Restore user-specific path to PLACEHOLDER.")
    post_parser.add_argument("--joey", action="store_true", help="Use Joey's path for restoring.")
    post_parser.add_argument("--greg", action="store_true", help="Use Greg's path for restoring.")

    post_parser = subparsers.add_parser('convert', help="Replace PLACEHOLDER with user-specific path")
    post_parser.add_argument("--joey", action="store_true", help="Use Joey's path for restoring.")
    post_parser.add_argument("--greg", action="store_true", help="Use Greg's path for restoring.")
    
    args = parser.parse_args()

    validate_args(args)

    user_path = get_user_path(args)
    user_path_other = get_user_path_other(args)


    source_file, target_file = get_file_paths(args)

    print(f"Source file: {source_file}")
    print(f"Target file: {target_file}")

    if args.operation == 'pre':
        process_pre(source_file, target_file, user_path, user_path_other)
    elif args.operation == 'post':
        process_post(target_file, target_file, user_path)
    elif args.operation == 'convert':
        process_convert(target_file, target_file, user_path)
    else:
        print("Error: You must specify either 'pre' or 'post' as the operation.")
        sys.exit(1)

if __name__ == "__main__":
    main()
