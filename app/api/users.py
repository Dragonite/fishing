from app.api import bp
from app.models import User
from flask import jsonify
from app.controllers import getUserById




@bp.route('/users/<int:userId>', methods=['GET'])

def get_user(userId):
    # return jsonify(getUserById(id).to_dict())
    return jsonify(User.query.get_or_404(userId).to_dict())


@bp.route('/users', methods=['GET'])
def get_users():
    pass

@bp.route('/users', methods=['POST'])
def create_user():
    pass

@bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    pass