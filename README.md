# MP3 / MP4 to Text

Переводит речь из аудио- или видеофайла в текст с помощью [OpenAI Whisper](https://github.com/openai/whisper).

Поддерживаемые форматы: mp3, mp4, wav, m4a, flac, ogg, webm, mkv, avi, mov.

## Установка

```bash
pip install -r requirements.txt
```

Whisper нужен [ffmpeg](https://ffmpeg.org/download.html). Скачайте его и либо положите `ffmpeg.exe` рядом с `my_transcriber.py`, либо добавьте ffmpeg в `PATH`.

## Запуск

```bash
python my_transcriber.py "C:\путь\к\лекции.mp4"
```

Текст сохранится рядом с исходным файлом, в `.txt` с тем же именем. Модель (`MODEL_NAME`) и язык (`LANGUAGE`) задаются в начале скрипта. При первом запуске Whisper скачает модель сам.
