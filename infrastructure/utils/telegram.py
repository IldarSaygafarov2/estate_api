import httpx
from PIL import Image
from io import BytesIO
from config.loader import Config

# name
# description
# price
# realtor_phone
# manager_phone

# condition
# district
# room
# floor
# storey
# type


def create_telegram_message(**kwargs):
    return f"""
{kwargs['name']}

{kwargs['description']}

Балкон: {kwargs['balcony']}
Состояние: {kwargs['condition']}
Район: {kwargs['district']}
Комнат: {kwargs['room']}
Этаж: {kwargs['floor']}
Этажность: {kwargs['storey']}
Тип: {kwargs['type']}
Цена: {kwargs['price']}
Номер менеджера: {kwargs['manager_phone']}
Номер риелтора: {kwargs['realtor_phone']}
"""


async def send_message_to_channel(config: Config, message: str, **kwargs):
    url = config.telegram.send_message_endpoint
    params = {
        "chat_id": f"@{config.telegram.channel_username}",
        "text": message,
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, params=params)
        return response.json()


# async def send_images_with_description(files: List[UploadFile], description: str):
#     # Проверка, что все файлы - изображения
#     media_group = []

#     for file in files:
#         file_content = await file.read()
#         media_group.append(
#             {
#                 "type": "photo",
#                 "media": file_content,
#                 "caption": description,
#             }
#         )

#     url = f"https://api.telegram.org/bot{API_TOKEN}/sendMediaGroup"
#     params = {"chat_id": CHANNEL_ID}
#     response = await httpx.post(url, params=params, files=media_group)

#     if response.status_code == 200:
#         logging.info("Images sent successfully.")
#         return {"status": "success", "message": "Images sent successfully."}
#     else:
#         logging.error(f"Error sending images: {response.json()}")
#         return {"status": "error", "message": response.json()}


def compress_image(image_path: str, max_size: int = 20 * 1024 * 1024) -> BytesIO:
    """
    Сжимает изображение до максимального размера (по умолчанию 20 MB).
    :param image_path: Путь к изображению.
    :param max_size: Максимальный размер файла в байтах (по умолчанию 20 MB).
    :return: Объект BytesIO с сжатыми данными изображения.
    """
    with Image.open(image_path) as img:
        # Определяем формат изображения
        img_format = img.format
        img = img.convert("RGB")  # Конвертируем в RGB для совместимости с форматом JPEG

        # Сжимаем изображение
        output = BytesIO()
        quality = 95  # Начальное качество
        img.save(output, format="JPEG", quality=quality)
        output.seek(0)  # Сбросить указатель на начало файла
        compressed_data = output.read()

        # Если изображение все еще слишком большое, уменьшаем качество
        while len(compressed_data) > max_size and quality > 10:
            output.seek(0)  # Сбросить указатель на начало
            quality -= 5  # Уменьшаем качество
            img.save(output, format="JPEG", quality=quality)
            output.seek(0)
            compressed_data = output.read()

        output.seek(0)  # Сбросить указатель на начало
        return output
