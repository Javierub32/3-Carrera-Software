import os
import json
import requests

URL = "https://api.tcgdex.net/v2/ja/cards"

def main():
    r = requests.get(URL, timeout=30)
    r.raise_for_status()
    cards = r.json()

    # 1. saco los nombres
    names = [c.get("name") for c in cards if c.get("name")]

    # 2. quito repetidos manteniendo orden
    names_unique = list(dict.fromkeys(names))

    out_path = os.path.join(os.getcwd(), "card_names_japanese.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(names_unique, f, ensure_ascii=False, indent=2)

    print(f"Total con repetidos: {len(names)}")
    print(f"Total únicos: {len(names_unique)}")
    print(f"Guardado en: {out_path}")

if __name__ == "__main__":
    main()
