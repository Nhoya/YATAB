# YATAB
Yet another telegram administration bot


#### Overview
YATAB is a modular multi-group telegram administration helper

## Installation

### Dependencies
YATAB needs [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) to works properly:

`pip3 install python-telegram-bot`

### Installation
First you need to clone the repository

`git clone https://github.com/Nhoya/telegram_lamebuster/`

Now you have to [create a bot](https://core.telegram.org/bots#creating-a-new-bot) and paste the APIKEY inside the `config.py` file inside the `TOKEN` variable

You have to create an `sqlite3` file called `buster.db` using this command

`sqlite3 busterdb < db.sql`

And finally you can run you personal istance of `YATAB`

`chmod +x yatab.py`

`./yatab`

### Modules
There are 2 different kinds of modules:

#### Commands modules
These modules contains only the single commands you can use with `/name-of-the-command`

### Onjoin modules
These are all the actions the bot will make every time a new user join


