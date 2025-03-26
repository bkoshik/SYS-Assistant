from pathlib import Path
import os

current_file = Path(__file__).resolve()
dir = current_file.parents[1]

# os.environ["API_WEATHER"] = "Введите ваш API ключ от OpenWeatherMap"
# os.environ["API_CUR"] = "Введите ваш API ключ от ExchangeRate-API"

params = {
    "path": dir,
    "my_id": 0,
    "api_weather": os.environ.get("API_WEATHER"),
    "api_cur": os.environ.get("API_CUR")
}
