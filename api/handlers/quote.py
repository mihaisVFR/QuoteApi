from api import app, db, request
from api.models.author import AuthorModel
from api.models.quote import QuoteModel
from api.schemas.quote import quotes_schema, quote_schema

@app.route('/quotes/<int:quote_id>', methods=["GET"])
def get_quotes(quote_id):
    quote = QuoteModel.query.get(quote_id)
    if quote is not None:
        return quote_schema.dump(quote), 200
    return {"Error": "Quote not found"}, 404


@app.route('/quotes', methods=["GET"])
def all_quotes():
    quotes = QuoteModel.query.all()
    if quotes:
        return quotes_schema.dump(quotes)
    return {"Error": "Quotes not found"}, 404


@app.route('/authors/<int:author_id>/quotes', methods=["GET"])
def quote_by_author(author_id):
    author = AuthorModel.query.get(author_id)
    if author is None:
        return {"Error": f"Author id={author_id} not found"}, 404
    quotes = author.quotes.all()
    return quotes_schema.dump(quotes), 200



@app.route('/authors/<int:author_id>/quotes', methods=["POST"])
def create_quote(author_id):
    quote_data = request.json
    author = AuthorModel.query.get(author_id)
    if author is None:
        return {"Error": f"Author id={author_id} not found"}, 404

    quote = QuoteModel(author, quote_data["text"])
    db.session.add(quote)
    db.session.commit()
    return quote_schema.dump(quote), 201


@app.route('/quotes/<int:quote_id>', methods=["PUT"])
def edit_quote(quote_id):
    quote_data = request.json
    quote = QuoteModel.query.get(quote_id)
    if quote is None:
        return {"Error": f"Quote id={quote_id} not found"}, 404
    for key, value in quote_data.items():
        setattr(quote, key, value)
    db.session.commit()
    return quote_schema.dump(quote), 200


@app.route('/quotes/<int:quote_id>', methods=["DELETE"])
def delete_quote(quote_id):
    quote = QuoteModel.query.get(quote_id)
    if quote is not None:
        db.session.delete(quote)
        db.session.commit()
        return {"Success": f"quote {quote_id} deleted"}, 200
    return {"Error": f"Quote id={quote_id} not found"}, 404
