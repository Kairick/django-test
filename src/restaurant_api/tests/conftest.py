import shutil
from io import BytesIO

import pytest
from PIL import Image


@pytest.fixture
def fake_image():
    image = Image.new('RGBA', size=(500, 500), color=(255, 0, 0))
    image_file = BytesIO()
    image.save(image_file, 'PNG')
    image_file.name = 'test.png'
    image_file.seek(0)

    return image_file


@pytest.fixture(autouse=True)
def clean_media():
    """Очищает папку с медиа после теста"""
    yield

    try:
        shutil.rmtree('test_data')
    except OSError:
        pass
