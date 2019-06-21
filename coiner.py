"""
Coiner: Cloud
By smallpants
https://github.com/Coinerinc/coinerapi
"""
from flask import Flask

coiner = Flask(__name__)


@coiner.route('/')
def landing():
    return 'Nope!'


if __name__ == '__main__':
    coiner.run()
