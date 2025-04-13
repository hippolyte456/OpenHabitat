import bpy
import os

def export_to_glb(blend_path, output_dir, output_name="model.glb"):
    # Ouvrir le fichier .blend
    bpy.ops.wm.open_mainfile(filepath=blend_path)

    # Créer le chemin de sortie
    glb_path = os.path.join(output_dir, output_name)

    # Exporter en .glb
    bpy.ops.export_scene.gltf(filepath=glb_path, export_format='GLB')

    print(f"✅ Modèle exporté en .glb : {glb_path}")
    return glb_path
