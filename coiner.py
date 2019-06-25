"""
Coiner: Cloud
By smallpants
https://github.com/Coinerinc/coinerapi
"""
from flask import Flask

coiner = Flask(__name__)


"""Data Retrieval Endpoints"""


@coiner.route('/retrieve/user')
def retrieve_user():
    pass


@coiner.route('/retrieve/transactions')
def retrieve_transactions():
    # Will allow filtering by parameter
    pass


@coiner.route('/retrieve/rewards')
def retrieve_rewards():
    pass


@coiner.route('/retrieve/stores')
def retrieve_stores():
    # Retrieves all stores in a radius, contrary to retrieve_location().
    pass


@coiner.route('/retrieve/location')
def retrieve_location():
    # Location is an alias for a specific store.
    pass


"""Insert Endpoints"""


@coiner.route('/insert/user')
def insert_user():
    pass


@coiner.route('/insert/transaction')
def insert_transaction():
    pass


@coiner.route('/insert/reward')
def insert_reward():
    # Do we insert a reward from the app or award it from the API?
    pass


@coiner.route('/insert/store')
def insert_store():
    # Internal use only from a future admin dashboard
    # Registers a new location for a merchant
    pass


@coiner.route('/insert/kiosk')
def insert_kiosk():
    # Internal use only from a future admin dashboard
    # Registers a new kiosk
    pass


@coiner.route('/insert/merchant')
def insert_merchant():
    # Internal use only from a future admin dashboard
    # Registers a new merchant
    pass


"""Update Endpoints"""


@coiner.route('/update/user')
def update_user():
    # Make changes to a user profile
    pass


@ coiner.route('/update/store')
def update_store():
    # Internal use only from a future admin dashboard
    # Make changes to a store's registration
    pass


@coiner.route('/update/kiosk')
def update_kiosk_registration():
    # Internal use only from a future admin dashboard
    # Make changes to a kiosk's registration
    # This is not meant to send anything to a kiosk (i.e. code updates)
    pass


@coiner.route('/update/merchant')
def update_merchant():
    # Internal use only from a future admin dashboard
    # Make changes to a merchant's registration
    pass


if __name__ == '__main__':
    coiner.run()
