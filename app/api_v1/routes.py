from flask import jsonify, request

from app import db
from app.api_v1 import api_v1
from app.models import Astronomer, Keyword, Librarian


@api_v1.route('/librarians', methods=['GET'])
def get_librarians():
    librarians = [librarian.export_data() for librarian in Librarian.query.all()]
    return jsonify(librarians), 200


@api_v1.route('/librarians/<uuid>', methods=['GET'])
def get_librarian(uuid):
    return jsonify(Librarian.query.get_or_404(uuid).export_data())


@api_v1.route('/librarians', methods=['POST'])
def create_librarian():
    librarian = Librarian()
    librarian.import_data(request.get_json(force=True))
    db.session.add(librarian)
    db.session.commit()

    return jsonify(librarian.export_data()), 201, {'Location': librarian.get_url()}


@api_v1.route('/librarians/<uuid>', methods=['PUT'])
def update_librarian(uuid):
    librarian = Librarian.query.get_or_404(uuid)
    librarian.import_data(request.get_json(force=True))
    db.session.add(librarian)
    db.session.commit()

    return jsonify(librarian.export_data()), 200


@api_v1.route('/librarians/<uuid>', methods=['DELETE'])
def delete_librarian(uuid):
    librarian = Librarian.query.get_or_404(uuid)
    db.session.delete(librarian)
    db.session.commit()

    return jsonify({}), 204


@api_v1.route('/astronomers', methods=['GET'])
def get_astronomers():
    astronomers = [astronomer.export_data() for astronomer in Astronomer.query.all()]
    return jsonify(astronomers), 200


@api_v1.route('/astronomers/<uuid>', methods=['GET'])
def get_astronomer(uuid):
    return jsonify(Astronomer.query.get_or_404(uuid).export_data())


@api_v1.route('/astronomers', methods=['POST'])
def create_astronomer():
    astronomer = Astronomer()
    astronomer.import_data(request.get_json(force=True))
    db.session.add(astronomer)
    db.session.commit()

    return jsonify(astronomer.export_data()), 201, {'Location': astronomer.get_url()}


@api_v1.route('/astronomers/<uuid>', methods=['PUT'])
def update_astronomer(uuid):
    astronomer = Astronomer.query.get_or_404(uuid)
    astronomer.import_data(request.get_json(force=True))
    db.session.add(astronomer)
    db.session.commit()

    return jsonify(astronomer.export_data()), 200


@api_v1.route('/astronomers/<uuid>', methods=['DELETE'])
def delete_astronomer(uuid):
    astronomer = Astronomer.query.get_or_404(uuid)
    db.session.delete(astronomer)
    db.session.commit()

    return jsonify({}), 204


@api_v1.route('/keywords', methods=['GET'])
def get_keywords():
    keywords = [keyword.export_data() for keyword in Keyword.query.all()]
    return jsonify(keywords), 200


@api_v1.route('/keywords/<uuid>', methods=['GET'])
def get_keyword(uuid):
    return jsonify(Keyword.query.get_or_404(uuid).export_data()), 200


@api_v1.route('/keywords', methods=['POST'])
def create_keyword():
    keyword = Keyword()
    keyword.import_data(request.get_json(force=True))
    db.session.add(keyword)
    db.session.commit()

    return jsonify(keyword.export_data()), 201, {'Location': keyword.get_url()}


@api_v1.route('/keywords/<uuid>', methods=['PUT'])
def update_keyword(uuid):
    keyword = Keyword.query.get_or_404(uuid)
    keyword.import_data(request.get_json(force=True))
    db.session.add(keyword)
    db.session.commit()

    return jsonify(keyword.export_data()), 200


@api_v1.route('/keywords/<uuid>', methods=['DELETE'])
def delete_keyword(uuid):
    keyword = Keyword.query.get_or_404(uuid)
    db.session.delete(keyword)
    db.session.commit()

    return jsonify({}), 204
