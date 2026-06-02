import httpx

from app.core.config import settings


async def generate_ai_response(message: str) -> str:
    url = f"{settings.AI_BASE_URL}/chat/completions"

    payload = {
        "model": settings.DEFAULT_MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message},
        ],
    }

    headers = {
        "Authorization": f"Bearer {settings.AI_API_KEY}",
        "Content-Type": "application/json",
    }

    async with httpx.AsyncClient(timeout=120) as client:
        response = await client.post(url, json=payload, headers=headers)

    data = response.json()
    print(data)

    response.raise_for_status()

    return data["choices"][0]["message"]["content"]