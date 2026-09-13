import json
import os

def main():
    # Directory the script is located in
    folder = os.path.dirname(os.path.abspath(__file__))

    script_name = os.path.basename(__file__)
    manifest_name = "manifest.json"
    manifest_path = os.path.join(folder, manifest_name)

    # If manifest.json already exists, delete it first
    if os.path.exists(manifest_path):
        os.remove(manifest_path)

    # Collect only .gpx files in the folder, ignoring the script itself and manifest.json
    files = [
        f for f in os.listdir(folder)
        if os.path.isfile(os.path.join(folder, f))
        and f not in (script_name, manifest_name)
        and f.lower().endswith(".gpx")
    ]

    # Sort alphabetically
    files.sort()

    manifest = {"files": files}

    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"Created {manifest_path} with {len(files)} file(s).")

if __name__ == "__main__":
    main()
