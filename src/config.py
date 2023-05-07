from dataclasses import dataclass
from os import environ


@dataclass
class Config:
    TELEGRAM_TOKEN: str = environ['TELEGRAM_TOKEN']
    SITE_URL: str = 'https://winline.by/sport/100248/102580'
