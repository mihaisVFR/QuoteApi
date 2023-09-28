from api import app, db, request, basic_auth
from api.models.author import AuthorModel
from api.schemas.author import authors_schema, author_schema
from api.models.quote import QuoteModel


@app.route('/authors', methods=["GET"])
def get_authors():
    authors = AuthorModel.query.all()
    return authors_schema.dump(authors), 200


@app.route('/authors/<int:author_id>', methods=["GET"])
def get_author_by_id(author_id):
    author = AuthorModel.query.get(author_id)
    if not author:
        return {"Error": f"Author id={author_id} not found"}, 404

    return author_schema.dump(author), 200


@app.route('/authors', methods=["POST"])
@basic_auth.login_required
def create_author():
    # print("user=", auth.current_user())
    author_data = request.json
    author = AuthorModel(**author_data)
    db.session.add(author)
    db.session.commit()
    return author_schema.dump(author), 201


@app.route('/authors/<int:author_id>', methods=["PUT"])
@basic_auth.login_required
def edit_author(author_id):
    author_data = request.json
    author = AuthorModel.query.get(author_id)
    if author is None:
        return {"Error": f"Author id={author_id} not found"}, 404
    for key, value in author_data.items():
        setattr(author, key, value)
    db.session.commit()
    return author_schema.dump(author), 200


@app.route('/authors/<int:author_id>', methods=["DELETE"])
@basic_auth.login_required
def delete_author(author_id):
    author = AuthorModel.query.get(author_id)
    if author is not None:
        db.session.delete(author)
        db.session.commit()
        return {"Success": f"author {author_id} and all his quotes are deleted"}, 200
    return {"Error": f"Author id={author_id} not found"}, 404