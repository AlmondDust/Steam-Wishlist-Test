from flask import Flask

from steam import Steam
from decouple import config

app = Flask(__name__)

@app.route('/')
def hello_geek():
    config.encoding = 'cp1251'
    KEY = config("STEAM_API_KEY")

    print(f'Key = {KEY}')

    steam = Steam(KEY)
    user = steam.users.search_user("the12thchairman")

    raise Exception('test exception')

    return repr(user)


if __name__ == "__main__":
    app.run(debug=True)