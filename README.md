# FastAPI Image Captioning & Instagram Caption API

This repository contains a FastAPI backend application that provides two endpoints powered by the Groq API. One endpoint generates a caption describing the contents of an image, while the other creates a creative Instagram post caption.

## Features

- **Image Captioning**: Upload an image and receive a descriptive caption.
- **Instagram Captioning**: Upload an image and receive a creative Instagram post caption.
- **Base64 Image Encoding**: Efficiently encodes image bytes into a base64 string for API transmission.
- **Error Handling**: Returns clear HTTP error messages if processing fails.

## Prerequisites

- **Python 3.7+**
- **FastAPI**
- **Uvicorn**
- **groq** package (ensure you have the necessary credentials/config for accessing the Groq API)

## Installation

1. **Clone the Repository**

   ```bash
   git clone <repository_url>
   cd <repository_directory>
