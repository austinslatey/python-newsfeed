from app import create_app
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = create_app()

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
