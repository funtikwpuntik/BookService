import dataclasses
import datetime
import json

from flask import Blueprint, current_app, request

from context import get_context
from domain.db_tables import Book

bp = Blueprint("book", __name__)


@bp.route("/")
def get_books():
    ctx = get_context(current_app)

    return ctx.book_service.get()


@bp.route("/", methods=["POST"])
def add_book():
    ctx = get_context(current_app)
    book = Book(
        title=request.json['title'],
        description=request.json['description'],
        publish_year=request.json['publish_year'],
        pages_count=request.json['pages_count'],
        created_at=datetime.datetime.now(),
    )
    book_data = ctx.book_service.add(book)
    return {"book_id": book_data["id"], "book": book_data["data"]}


@bp.route("/<id>", methods=["DELETE"])
def delete_book(id):
    ctx = get_context(current_app)

    book_data = ctx.book_service.delete(id)

    return {}

@bp.route("/<id>", methods=["PATCH"])
def update_book(id):
    ctx = get_context(current_app)

    ctx.book_service.update(id, request.json)

    return {}