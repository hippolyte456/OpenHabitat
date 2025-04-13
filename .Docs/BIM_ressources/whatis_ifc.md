🧱 IFC = Industry Foundation Classes

C’est un format de fichier standardisé utilisé dans le BIM (Building Information Modeling) pour permettre l’échange de modèles 3D riches en données entre différents logiciels d’architecture, d’ingénierie et de construction.
🔍 En clair :

    C’est un format ouvert (open standard) développé par buildingSMART

    Il permet de décrire un bâtiment : formes, matériaux, propriétés, relations, phases, etc.

    Contrairement à un simple fichier 3D (comme .obj ou .fbx), il contient aussi :

        Des informations structurelles (mur, dalle, fenêtre…)

        Des liens fonctionnels (mur porteur, cloison, étage…)

        Des métadonnées : matériaux, dates, constructeurs, etc.

        Des phases de construction

        Et même des liens vers des docs techniques ou vidéos si tu veux

📁 Exemple :

Un fichier .ifc peut contenir une maison complète avec :

    Une dalle → avec son type de béton et sa surface

    Des murs → avec l’épaisseur, l’isolation, la fonction

    Des fenêtres → avec la marque, les dimensions, l’ouverture

    Une chronologie → étape 1 : dalle, étape 2 : murs, etc.

    Et tout ça est lisible par plein de logiciels (Revit, FreeCAD, BlenderBIM, etc.)

⚠️ À retenir :

    IFC, c’est un pont entre les logiciels 3D et les métiers du bâtiment.
    C’est parfait si tu veux que ton modèle 3D soit constructible, compréhensible et utilisable pour un projet d’habitat partagé, open-source, etc.