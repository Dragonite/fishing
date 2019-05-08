# from app.api import bp
from app import db
from app.models import User
# from app.api.errors import bad_request, error_response
from flask import jsonify, url_for, request#, g, abort
# from app.api.auth import token_auth
from app.api import bp



@bp.route('/users/<int:userId>', methods=['GET'])
def get_user(userId):
    # if g.current_user != userId:
    #     abor(403)
    user=User.query.get_or_404(userId).to_dict()
    return jsonify(user)
    # return jsonify(User.query.get_or_404(userId).to_dict())


# @app.route('/users', methods=['GET'])
# def get_users():
#     pass

# @app.route('/users', methods=['POST'])
# def create_user():
#     pass

# @app.route('/users/<int:id>', methods=['PUT'])
# def update_user(id):
#     pass