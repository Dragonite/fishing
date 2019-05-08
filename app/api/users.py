# from app.api import bp
from app import db
from app.models import User
# from app.api.errors import bad_request, error_response
from flask import jsonify, url_for, request, g, abort
# from app.api.auth import token_auth
from app.api import bp
from app.controllers import getUserById


@bp.route('/users/<int:userId>', methods=['GET'])
def get_user(userId):
    # if g.current_user != userId:
    #      abort(403)
    # user=User.query.get_or_404(userId).to_dict()
    user=getUserById(userId)
    return jsonify(user)



@bp.route('/users', methods=['GET'])
def get_users():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = User.to_collection_dict(User.query, page, per_page, 'api.get_users')
    return jsonify(data)

@bp.route('/users', methods=['POST'])
def create_user():
#     pass

# @app.route('/users/<int:id>', methods=['PUT'])
# def update_user(id):
#     pass