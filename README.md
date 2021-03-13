# Description

youtube_dl_fastapi

# How to run

Download or clone the project from [here](https://github.com/kashyapm94/youtube_dl_fastapi.git)

Please note that all the code is currently in the **develop** branch

For this project [pipenv](https://pipenv.pypa.io/en/latest/) is being used to create virtual env, but a **requirements.txt** file is made available for other venv.

The project folder must contain a `.env` file and must contain the name of the folder where you would like to download the `mp3` version of the youtube video. Example:

`UPLOAD_FOLDER=<enter_path_here>`

The important dependencies to install:
- Fastapi
- uvicorn
- youtube-dl
- python-dotenv

Once these dependencies are downloaded, the app can be run as follows:

`uvicorn app.main:app --reload`

Go to: http://127.0.0.1:8000/docs and enter the link of the youtube video in the **GET** route and click execute