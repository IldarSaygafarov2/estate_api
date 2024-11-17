from pathlib import Path

MEDIA_FOLDER = Path('media')


def create_estate_directory(estate_id: int):
    estate_dir = MEDIA_FOLDER / str(estate_id)
    estate_dir.mkdir(exist_ok=True, parents=True)
    return estate_dir



