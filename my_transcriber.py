import os
import sys
from pathlib import Path

import whisper

# ffmpeg.exe лежит рядом со скриптом — Whisper найдёт его через PATH
os.environ['PATH'] += os.pathsep + str(Path(__file__).resolve().parent)

MODEL_NAME = 'base'  # tiny / base / small / medium / large: точнее, но медленнее
LANGUAGE = 'ru'
SUPPORTED_EXTENSIONS = {'.mp3', '.mp4', '.wav', '.m4a', '.flac', '.ogg', '.webm', '.mkv', '.avi', '.mov'}


def transcribe(media_path):
    """Расшифровывает аудио/видео и сохраняет текст рядом с исходным файлом."""
    print('Загрузка модели...')
    model = whisper.load_model(MODEL_NAME)

    # Whisper сам извлечёт аудиодорожку из видео через ffmpeg
    print(f'Расшифровка файла {media_path.name}...')
    text = model.transcribe(str(media_path), language=LANGUAGE)['text']

    text_path = media_path.with_suffix('.txt')
    text_path.write_text(text, encoding='utf-8')
    return text_path, text


def main():
    raw_path = sys.argv[1] if len(sys.argv) > 1 else input('Путь к аудио/видео файлу: ')
    media_path = Path(raw_path.strip('"')).expanduser()

    if not media_path.is_file():
        sys.exit(f'Файл не найден: {media_path}')
    if media_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
        sys.exit(f'Формат {media_path.suffix} не поддерживается. '
                 f'Поддерживаемые форматы: {", ".join(sorted(SUPPORTED_EXTENSIONS))}')

    text_path, text = transcribe(media_path)
    print(f'Готово! Текст сохранён в: {text_path}')
    print(f'\nПервые 200 символов:\n{text[:200]}...')


if __name__ == '__main__':
    main()
