# scripts/update_hf_datasets.py

import json
import requests
import os

print("📡 Fetching Hugging Face datasets...")

try:
    url = "https://huggingface.co/api/datasets?full=true"
    response = requests.get(url)
    response.raise_for_status()
    raw_data = response.json()

    datasets = []
    for item in raw_data:
        if item.get("private") or item.get("disabled"):
            continue

        datasets.append({
            "id": item.get("id"),
            "author": item.get("author"),
            "description": item.get("description", "").strip().split("\n")[0],
            "likes": item.get("likes", 0),
            "downloads": item.get("downloads", 0),
            "url": f"https://huggingface.co/datasets/{item.get('id')}"
        })

    os.makedirs("data", exist_ok=True)
    with open("data/huggingface_datasets.json", "w") as f:
        json.dump(datasets, f, indent=2)

    print(f"✅ Saved {len(datasets)} datasets to data/huggingface_datasets.json")

except Exception as e:
    print(f"❌ Error fetching data: {e}")

