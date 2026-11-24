# Inference API

> A FastAPI service that serves the skin tone model to apps.

**Part of [Inclusive Skin AI](https://github.com/tbrunoh#inclusive-skin-ai)**, an end to end system for skin analysis built for melanin-rich skin first. Most skin analysis models learn from lighter skin and misread darker tones; this project starts from the other end.

## What it does

Accepts an image URL, runs the [skin tone classifier](https://github.com/tbrunoh/ml-ai-skintone) and returns the Monk Skin Tone class. It is the backend for the [skin tone analysis app](https://github.com/tbrunoh/ml-ai-skintone-ui).

## Endpoints

| Method | Path | Purpose |
|:--|:--|:--|
| POST | `/skintone/infer` | Classify skin tone from an image |
| POST | `/skintones/inference` | Alternate inference route |
| POST | `/communication/email/` | Send an email through Azure Communication Services |
| GET | `/health` | Health check |

## Quickstart

```bash
git clone https://github.com/tbrunoh/ml-ai-client-api.git
cd ml-ai-client-api
pip install -r Requirements.txt
python -m uvicorn app.main:app --reload
```

Open http://localhost:8000/docs for the interactive API reference. `run.sh` packages the weights for TorchServe, and the Dockerfile builds the production image.

## The Inclusive Skin AI repositories

| Layer | Repository | Role |
|:--|:--|:--|
| MODEL | [ml-ai-skintone](https://github.com/tbrunoh/ml-ai-skintone) | Skin tone classifier on the Monk Skin Tone scale |
| MODEL | [ml-ai-skin-conditions](https://github.com/tbrunoh/ml-ai-skin-conditions) | Skin condition model package, early stage |
| CORE | [ml-ai-core](https://github.com/tbrunoh/ml-ai-core) | Shared PyTorch base classes and utilities |
| SERVE | **ml-ai-client-api** | FastAPI inference service for the skin tone model |
| DATA | [ml-data-upload-api](https://github.com/tbrunoh/ml-data-upload-api) | FastAPI upload service feeding storage and labeling |
| DATA | [ml-data-labelling-ui](https://github.com/tbrunoh/ml-data-labelling-ui) | Label Studio deployment for image annotation |
| PRODUCT | [ml-ai-skintone-ui](https://github.com/tbrunoh/ml-ai-skintone-ui) | Next.js skin tone analysis app |
| PRODUCT | [ml-landing-page](https://github.com/tbrunoh/ml-landing-page) | Next.js landing page for the consumer app |
| INFRA | [ml-terraform](https://github.com/tbrunoh/ml-terraform) | Azure infrastructure as code |
| INFRA | [ml-terraform-modules](https://github.com/tbrunoh/ml-terraform-modules) | Reusable Terraform modules |
| RESEARCH | [ml-ai-samples](https://github.com/tbrunoh/ml-ai-samples) | Reference PyTorch experiments |

## Status

The cloud environment behind this project has been retired. The code is published as a reference implementation, and every endpoint, key and project identifier in configuration files is a placeholder you replace with your own.

---

<sub>Maintained by <a href="https://github.com/tbrunoh">Tom Bruno</a>. Original engineering by Nelson Kigen. Part of <a href="https://github.com/tbrunoh#inclusive-skin-ai">Inclusive Skin AI</a>.</sub>
