
from app import db
from app.models import User
# 
from app.api.errors import bad_request, error_response
from flask import jsonify, url_for, request, g, abort
from app.api.auth import token_auth, basic_auth, verify_password
from app.api.tokens import get_token
from app.api import bp

from flask_httpauth import HTTPTokenAuth
from flask_login import login_user, logout_user, current_user
# from app.controllers import login_success

@bp.route('/users/login', methods=['POST'])
def API_login():
    data = request.get_json() or {}
    if 'username' not in data or 'password' not in data:
        return bad_request('must include username and password fields') 
    user = User.query.filter_by(username=data['username']).first()
    if user is None or not verify_password(data['username'], data['password']): 
       return bad_request('Invalid username or password')
    # login_success(user)
    response={
        "access_token": g.current_user.get_token(),
        "message": "login successful"
    }
    return  jsonify(response)
        
    

@bp.route('/users/<int:userId>', methods=['GET'])
@token_auth.login_required
# @auth.login_required
def get_user(userId):
    user=getUserById(userId)
    return jsonify(user)


@bp.route('/users', methods=['GET'])
@token_auth.login_required
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

@bp.route('/users/<int:userId>', methods=['PUT'])
@token_auth.login_required
def update_user(userId):
    user = User.query.get_or_404(userId)
    data = request.get_json() or {}
    if 'username' in data and data['username'] != user.username and \
            User.query.filter_by(username=data['username']).first():
        return bad_request('please use a different username')
    if 'email' in data and data['email'] != user.email and \
            User.query.filter_by(email=data['email']).first():
        return bad_request('please use a different email address')
    user.from_dict(data, new_user=False)
    db.session.commit()
    return jsonify(user.to_dict())