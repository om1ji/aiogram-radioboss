# telegram-radioboss
Telegram Bot to control RadioBOSS streaming software

Requirements:
[aiogram (3.x)](https://github.com/aiogram/aiogram/archive/refs/heads/dev-3.x.zip)
[requests](https://pypi.org/project/requests/)

Firstly configure your bot via changing variables values located in [consts.py](https://github.com/om1ji/telegram-radioboss/blob/main/consts.py)

Available commands:

```/info``` - shows current track plaiyng in RadioBOSS and current amount of listeners of your audiostream

```/next``` - switches track to next in playlist

Run with ```python main.py```
