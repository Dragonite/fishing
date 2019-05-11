# from app.api import bp
from app import db
from app.models import User
from app.api.errors import bad_request, error_response
from flask import jsonify, url_for, request, g, abort
# from app.api.auth import token_auth
from app.api import bp
from app.controllers import getUserById


@bp.route('/users/<int:userId>', methods=['GET'])
def get_user(userId):
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
    data = request.get_json() or {}
    if 'username' not in data or 'email' not in data or 'password' not in data or 'firstName' not in data:
        return bad_request('must include username, firstName, email and password fields')
    if User.query.filter_by(username=data['username']).first():
        return bad_request('please use a different username')
    if User.query.filter_by(email=data['email']).first():
        return bad_request('please use a different email address')
    user = User()
    user.from_dict(data, new_user=True)
    db.session.add(user)
    db.session.commit()
    response = jsonify(user.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('api.get_user', userId=user.userId)
    return response

# @app.route('/users/<int:id>', methods=['PUT'])
# def update_user(id):
#     pass