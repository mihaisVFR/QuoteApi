from api import app, db, request
from api.models.user import UserModel
from api.schemas.user import user_schema, users_schema


@app.get("/users/<int:user_id>")
def get_user_by_id(user_id):
    user = UserModel.query.get(user_id)
    if user is None:
        return {"Error": f"User id={user} not found"}, 404
    return user_schema.dump(user), 200


@app.get("/users")
def get_users():
    users = UserModel.query.all()
    if users is None:
        return {"Error": f"Users not found"}, 404
    return users_schema.dump(users), 200


@app.post("/users")
def create_user():
    user_data = request.json
    user = UserModel(**user_data)
    db.session.add(user)
    db.session.commit()
    return user_schema.dump(user), 201


@app.route('/users/<int:user_id>', methods=["DELETE"])
def delete_user(user_id):
    user = UserModel.query.get(user_id)
    if user is not None:
        db.session.delete(user)
        db.session.commit()
        return {"Success": f"user with id={user_id} deleted"}, 200
    return {"Error": f"user id={user_id} not found"}, 404

