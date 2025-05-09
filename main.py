from fastapi import FastAPI, UploadFile, File, HTTPException
import base64
from groq import Groq
from cors_config import add_cors

app = FastAPI()
add_cors(app)
# Initialize the Groq client (ensure you have your credentials/config if required)
client = Groq()


def encode_image_bytes(image_bytes: bytes) -> str:
    """
    Encodes image bytes to a base64 string.
    """
    return base64.b64encode(image_bytes).decode('utf-8')


@app.post("/caption")
async def image_caption(image: UploadFile = File(...)):
    """
    Endpoint for generating a caption describing the contents of an image.
    """
    try:
        # Read the image file bytes
        image_bytes = await image.read()
        # Convert the bytes to a base64 string
        base64_image = encode_image_bytes(image_bytes)

        # Call the Groq API with a captioning prompt
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "What's in this image?"},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}",
                            },
                        },
                    ],
                }
            ],
            model="meta-llama/llama-4-scout-17b-16e-instruct",
        )
        caption = response.choices[0].message.content
        return {"caption": caption}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing image: {e}")


@app.post("/instagram")
async def instagram_post(image: UploadFile = File(...)):
    """
    Endpoint for generating an Instagram post caption for an image.
    """
    try:
        # Read the image file bytes
        image_bytes = await image.read()
        # Convert the bytes to a base64 string
        base64_image = encode_image_bytes(image_bytes)

        # Call the Groq API with a creative Instagram caption prompt
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Write a creative Instagram post caption for this image."},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}",
                            },
                        },
                    ],
                }
            ],
            model="meta-llama/llama-4-scout-17b-16e-instruct",
        )
        instagram_caption = response.choices[0].message.content
        return {"instagram_caption": instagram_caption}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing image: {e}")


# For local development, you can run the app with: uvicorn filename:app --reload
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0",port=8000)
