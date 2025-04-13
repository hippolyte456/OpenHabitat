import json
import os
from datetime import datetime

def generate_metadata(model_path, output_dir, extra_data=None):
    metadata = {
        "name": os.path.basename(model_path),
        "exported_at": datetime.now().isoformat(),
        "author": "unknown",
        "description": "Modèle exporté depuis Blender vers .openhab",
        "components": [],
        "links": [],
    }

    if extra_data:
        metadata.update(extra_data)

    meta_path = os.path.join(output_dir, "meta.json")
    with open(meta_path, "w") as f:
        json.dump(metadata, f, indent=4)

    print(f"✅ Métadonnées générées : {meta_path}")
    return meta_path
