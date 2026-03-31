"""
Сохранение и загрузка настроек в JSON-файл.

Файл: <project_root>/settings.json
"""

import json
import pathlib

import pygame

from src.settings import DEFAULT_SETTINGS

_SAVE_FILE = pathlib.Path(__file__).resolve().parents[2] / "settings.json"


def _key_to_str(code: int) -> str:
    """Сохраняем scan-code как 'kscan:N'."""
    return f"kscan:{code}"


def _str_to_key(s: str, default: int) -> int:
    """Парсим 'kscan:N' обратно в int; при ошибке возвращаем default."""
    if isinstance(s, str) and s.startswith("kscan:"):
        try:
            return int(s[6:])
        except ValueError:
            pass
    return default


def _settings_to_json(settings: dict) -> dict:
    """Конвертирует pygame scan-коды в строки для JSON."""
    controls_str = {
        action: _key_to_str(code)
        for action, code in settings["controls"].items()
    }
    return {
        "music_volume": settings["music_volume"],
        "sfx_volume":   settings["sfx_volume"],
        "fullscreen":   settings["fullscreen"],
        "controls":     controls_str,
    }


def _json_to_settings(data: dict) -> dict:
    """Конвертирует строки обратно в scan-коды."""
    controls = {}
    for action, val in data.get("controls", {}).items():
        controls[action] = _str_to_key(val, DEFAULT_SETTINGS["controls"][action])

    return {
        "music_volume": float(data.get("music_volume", DEFAULT_SETTINGS["music_volume"])),
        "sfx_volume":   float(data.get("sfx_volume",   DEFAULT_SETTINGS["sfx_volume"])),
        "fullscreen":   bool(data.get("fullscreen",    False)),
        "controls":     controls if controls else dict(DEFAULT_SETTINGS["controls"]),
    }


def save_settings(settings: dict) -> None:
    """Сохраняет словарь настроек на диск."""
    try:
        data = _settings_to_json(settings)
        _SAVE_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False))
    except Exception:
        pass   # молча игнорируем — настройки не критичны


def load_settings() -> dict | None:
    """
    Загружает настройки с диска.
    Возвращает dict или None если файл отсутствует/повреждён.
    """
    if not _SAVE_FILE.exists():
        return None
    try:
        data = json.loads(_SAVE_FILE.read_text())
        return _json_to_settings(data)
    except Exception:
        return None
