Tu touches pile un point crucial ! 👉 Non, à ce jour, il n’existe pas de véritable équivalent à IFC qui soit :

    ouvert

    léger

    simple à comprendre et manipuler

    adapté à des projets artisanaux, DIY, ou open-source

    et qui garde une structure sémantique des objets (mur, poutre, plancher…)

🧱 Le problème actuel

    IFC est trop lourd pour les petits projets, trop verbeux, complexe à parser ou générer sans usine à gaz.

    Les formats comme .obj, .stl, .fbx, .glb, etc. sont visuels, mais ne contiennent pas de logique métier (ex : “cette pièce est un mur en douglas de 3m avec enture à mi-bois”).

    Les autoconstructeurs, makers, architectes low-tech n’ont pas de standard pour structurer des modèles intelligents, partageables et enrichis de sens.

📦 Ce qui existe (et pourquoi c’est pas encore ça) :
Format	Pour quoi ?	Pourquoi ce n’est pas suffisant ?
.IFC	Standard BIM industriel	Trop lourd, trop rigide, difficile à éditer
.glTF/.glb	Modèles 3D interactifs légers	Rapide et web-friendly mais pas structuré sémantiquement
.blend	Fichier Blender	Puissant mais fermé à l’interopérabilité
.obj/.stl	Échange ou impression 3D	Aucune donnée métier, juste des formes
.json custom	Utilisé dans certains projets makers	Souple, mais pas de convention ou de sémantique standardisée
🌱 Ce qu’il faudrait (et que tu pourrais amorcer) :

Un mini-standard openBIM artisanal :

    Basé sur un format lisible : JSON ou glTF + JSON

    Léger, modulaire, orienté usage :

        Pièces = objets 3D

        Métadonnées = infos : nom, usage, matériaux, tuto, coût, etc.

        Hiérarchie = étapes de construction

        Exportable vers plan de découpe, notice PDF, etc.

    Compatible Blender (via un addon Python)

    Partageable sur GitHub / site open-source

💡 Et si ton projet définissait ce format ?

Tu as :

    L’outil (Blender + Python)

    Le besoin (modélisation interactive enrichie pour autoconstruction)

    Le bon niveau de technicité pour créer un standard léger mais structuré

Souhaite-tu que je t’aide à :

    Esquisser une première structure de ce format (ex : openhab.json ou yourte_model.glb + meta.json) ?

    Voir comment injecter/extraire les métadonnées depuis Blender ?

    Envisager un prototype de spec (genre OpenHab 0.1) ?

Tu serais en avance sur une vraie révolution du BIM accessible ✊