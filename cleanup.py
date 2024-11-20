import xml.etree.ElementTree as ET
import os
import argparse
import copy
import sys

shared_drive_game_file = "~/Google Drive/Shared drives/Lil Pete/LilPete_Game_Gold/Game.agf"
local_game_file = os.path.join(os.getcwd(), 'Game.agf')

joey_pixel_studio_path = "Y:/Google Drive/Shared drives/Lil Pete/Pixel Studio/LilPete/"
joey_game_assets_path = "Y:/Google Drive/Shared drives/Lil Pete/Game_Assets_Gold/LilPete/"

daniel_pixel_studio_path = "G:\\My Drive\\Pixel Studio\\LilPete\\"
daniel_game_assets_path = "G:\\My Drive\\Game_Assets_Gold\\LilPete\\" 

greg_pixel_studio_path = "G:\\.shortcut-targets-by-id\\1QlgbrPTE3dUNfoYltEKQEvFMZU4Fk016\\Pixel Studio\\LilPete\\"
greg_game_assets_path = "G:\\.shortcut-targets-by-id\\1XYZWSeIYkulML3AjBdv5RVqh0AjYO6Vp\\\\Game_Assets_Gold\\LilPete\\"

def find_and_replace(source_file, target_file, first_replacement_path, second_replacement_path, first_match_path, second_match_path):
    source_file, target_file = get_expanded_file_paths(source_file, target_file)
    source_root, target_root = get_roots(source_file, target_file)

    replace_sprites_with_user_path(source_root, target_root, first_replacement_path, second_replacement_path, first_match_path, second_match_path)
    replace_views(source_root, target_root)
    write_xml_with_header(source_file, target_file, target_root, use_crlf=True)

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

def replace_sprites_with_user_path(source_root, target_root, first_replacement_path, second_replacement_path, first_match_path, second_match_path):
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
            sprite.text = sprite.text.replace(first_match_path, first_replacement_path)
            sprite.text = sprite.text.replace(second_match_path, second_replacement_path)
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

def main():
    parser = argparse.ArgumentParser(description="Process XML files and update file paths.")
    
    subparsers = parser.add_subparsers(dest="operation", help="Operation to perform: 'pre' or 'post'.")
    
    pre_parser = subparsers.add_parser('pre', help="Replace 'G:/My Drive/Pixel Studio' with a user-specific path.")
    post_parser = subparsers.add_parser('post', help="Restore user-specific path to PLACEHOLDER.")
    
    args = parser.parse_args()

    print(f"Source file: {shared_drive_game_file}")
    print(f"Target file: {local_game_file}")

    if args.operation == 'pre':
        print(f"First replacement path: {joey_pixel_studio_path}")
        print(f"Second replacement path: {joey_game_assets_path}")
        print(f"First match path: {greg_pixel_studio_path}")
        print(f"Second match path: {greg_game_assets_path}")
        find_and_replace(local_game_file, local_game_file, joey_pixel_studio_path, joey_game_assets_path, greg_pixel_studio_path, greg_game_assets_path)
        print(f"First replacement path: {joey_pixel_studio_path}")
        print(f"Second replacement path: {joey_game_assets_path}")
        print(f"First match path: {daniel_pixel_studio_path}")
        print(f"Second match path: {daniel_game_assets_path}")
        find_and_replace(shared_drive_game_file, local_game_file, joey_pixel_studio_path, joey_game_assets_path, daniel_pixel_studio_path, daniel_game_assets_path)
    elif args.operation == 'post':
        find_and_replace(local_game_file, local_game_file, greg_pixel_studio_path, greg_game_assets_path, joey_pixel_studio_path, joey_game_assets_path)
    else:
        print("Error: You must specify either 'pre' or 'post' as the operation.")
        sys.exit(1)

if __name__ == "__main__":
    main()
