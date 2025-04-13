import argparse
from converter import export_to_glb
from meta_generator import generate_metadata
import os

def main():
    parser = argparse.ArgumentParser(description="Convertisseur Blender → .openhab")
    parser.add_argument("blend_file", help="Chemin vers le fichier .blend")
    parser.add_argument("output_dir", help="Dossier de sortie")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    glb_path = export_to_glb(args.blend_file, args.output_dir)
    generate_metadata(glb_path, args.output_dir)

if __name__ == "__main__":
    main()
