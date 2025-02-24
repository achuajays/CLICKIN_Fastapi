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
   git clone https://github.com/achuajays/CLICKIN_Fastapi.git
   cd CLICKIN_Fastapi
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Before running the application, ensure that the Groq client is properly configured with any required credentials or API keys. Adjust the client initialization in the code if necessary.

## API Endpoints

### 1. `/caption`

- **Method**: `POST`
- **Description**: Generates a caption that describes the contents of the uploaded image.
- **Parameters**:
  - `image` (UploadFile): The image file to be processed.
- **Example Request**:

   ```bash
   curl -X POST "http://localhost:8000/caption" \
        -F "image=@path/to/your/image.jpg"
   ```

### 2. `/instagram`

- **Method**: `POST`
- **Description**: Generates a creative Instagram post caption for the uploaded image.
- **Parameters**:
  - `image` (UploadFile): The image file to be processed.
- **Example Request**:

   ```bash
   curl -X POST "http://localhost:8000/instagram" \
        -F "image=@path/to/your/image.jpg"
   ```

## Running the Server

To run the application locally, use the following command:

```bash
uvicorn filename:app --host 0.0.0.0 --port 8000 --reload
```

Replace `filename` with the name of the Python file containing your FastAPI application.

## Usage

Once the server is running, you can use tools like `curl`, Postman, or your frontend application to send image files to the API endpoints.

For example, to test the image captioning endpoint:

```bash
curl -X POST "http://localhost:8000/caption" \
     -F "image=@path/to/your/image.jpg"
```

Similarly, test the Instagram captioning endpoint with:

```bash
curl -X POST "http://localhost:8000/instagram" \
     -F "image=@path/to/your/image.jpg"
```

## Error Handling

If an error occurs during image processing or while communicating with the Groq API, the endpoints return a 500 HTTP status code along with a detailed error message.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [Groq API](#) *(Replace with actual documentation URL if available)*



