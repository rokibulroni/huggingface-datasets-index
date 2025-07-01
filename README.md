## 🔄 Auto-updated Hugging Face Dataset Index

This repository automatically fetches and maintains an up-to-date index of public datasets available on [Hugging Face Datasets Hub](https://huggingface.co/datasets).

### ✅ Features

* Updates every **3 days** via GitHub Actions
* Uses the public API endpoint: `https://huggingface.co/api/datasets?full=true`
* Extracts top **1000 datasets** (latest and trending)
* Saves to: [`data/huggingface_datasets.json`](data/huggingface_datasets.json)
* Includes metadata like:

  * `id`, `author`, `likes`, `description`, `downloads`
  * `task_categories`, `license`, `size`, `tags`, `createdAt`, `lastModified`

### 📁 JSON Data Preview

You can access the live auto-updated JSON here:
🔗 [`https://raw.githubusercontent.com/rokibulroni/huggingface-datasets-index/main/data/huggingface_datasets.json`](https://raw.githubusercontent.com/rokibulroni/huggingface-datasets-index/main/data/huggingface_datasets.json)

Sample entry:

```json
{
  "id": "facebook/seamless-interaction",
  "author": "facebook",
  "description": "A large-scale multimodal dataset of human interactions.",
  "downloads": 1,
  "likes": 58,
  "task_categories": ["audio", "video"],
  "license": "cc-by-nc-4.0",
  "url": "https://huggingface.co/datasets/facebook/seamless-interaction"
}
```

---

### 🔧 GitHub Actions Workflow

This project uses a simple CI pipeline:

* **Workflow file**: `.github/workflows/update_hf.yml`
* **Python script**: `scripts/update_hf_datasets.py`
* Dependencies: `requests`

The workflow runs every 3 days and commits new changes if the dataset list is updated.

---

### 👨‍💻 Developer Info

Built with ❤️ by [Rokibul Islam Roni](https://rokibulroni.com)
Cybersecurity Researcher & Full-Stack Developer
🔗 [rokibulroni.com](https://rokibulroni.com)
