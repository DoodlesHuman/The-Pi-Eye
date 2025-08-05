# OCR API Wrapper

import requests

API_KEY = '4ad763d7c288957'

def ocrspace(filename, overlay=False, api_key=API_KEY, language='eng'):
    """
    OCR.space API request with a local file.

    :param filename: File path and name
    :param overlay: Whether to include overlay in response
    :param api_key: OCR.space API key
    :param language: Language code for OCR (default: 'eng')
    :return: JSON response
    """
    payload = {
        'isOverlayRequired': overlay,
        'apikey': api_key,
        'language': language,
    }

    with open(filename, 'rb') as f:
        response = requests.post(
            'https://api.ocr.space/parse/image',
            files={filename: f},
            data=payload
        )

    return response.json()
