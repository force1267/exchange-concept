from flask import Blueprint, request, g

from app.controller.exceptions import CryptoNotSupported, DBError, LowBalance
from app.controller.buy import buy as buy_controller


api = Blueprint('api', __name__, url_prefix='/api')

@api.before_request
def user_auth():
    # no auth for simplicity
    g.user = { 'id': request.json.get('user') }

@api.post('/buy')
def buy():
    crypto = request.json.get('crypto')

    try:
        amount = int(request.json.get('amount'))
    except:
        return {'msg': 'amount is not an integer'}, 400

    try:
        result = buy_controller(g.user.get('id'), crypto, amount)
    except CryptoNotSupported:
        return {'msg': 'crypto not supported'}, 400
    except LowBalance as e:
        return {'msg': 'balance is low'}, 402
    except DBError as e:
        print(e)
        return {'msg': 'internal error'}, 500
    except Exception as e:
        print(e)
        return {'msg': 'unknown error'}, 500

    return {'msg': "order placed", 'result': result}
