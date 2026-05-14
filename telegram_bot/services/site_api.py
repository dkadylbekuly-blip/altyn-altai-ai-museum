import requests
from pathlib import Path

from bot_config import SITE_URL


def send_recognition_to_site(user_id: int, result: dict, image_path: str):
    api_url = f"{SITE_URL}/api/save-recognition/"

    image_file = Path(image_path)

    if not image_file.exists():
        return False

    data = {
        "user_id": user_id,
        "mineral_name": result.get("name", "unknown"),
        "confidence": result.get("confidence", 0),
    }

    try:
        with open(image_file, "rb") as f:
            files = {
                "image": (image_file.name, f, "image/jpeg")
            }

            response = requests.post(
                api_url,
                data=data,
                files=files,
                timeout=10
            )

        return response.status_code in [200, 201]

    except Exception as e:
        print("SITE API ERROR:", e)
        return False