#!/usr/bin/env python3
"""Display products from JSON, CSV, or SQLite."""

import csv
import json
import sqlite3
from contextlib import closing
from pathlib import Path

from flask import Flask, render_template, request

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent


def read_json():
    """Read products from JSON."""
    with open(BASE_DIR / 'products.json', encoding='utf-8') as file:
        return json.load(file)


def read_csv():
    """Read products from CSV."""
    with open(
        BASE_DIR / 'products.csv', newline='', encoding='utf-8'
    ) as file:
        return list(csv.DictReader(file))


def read_sql():
    """Read products from SQLite and close the connection."""
    database_uri = (BASE_DIR / 'products.db').as_uri() + '?mode=ro'
    with closing(sqlite3.connect(database_uri, uri=True)) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.execute(
            'SELECT id, name, category, price FROM Products'
        )
        return [dict(row) for row in cursor.fetchall()]


@app.route('/products')
def products():
    """Render products from the chosen source with optional filtering."""
    source = request.args.get('source')
    product_id = request.args.get('id')
    readers = {'json': read_json, 'csv': read_csv, 'sql': read_sql}

    if source not in readers:
        return render_template(
            'product_display.html', products=[], error='Wrong source'
        )

    try:
        data = readers[source]()
    except sqlite3.Error:
        app.logger.exception('Unable to read the products database.')
        return render_template(
            'product_display.html', products=[], error='Database error'
        )
    except (OSError, ValueError, csv.Error):
        app.logger.exception('Unable to read the products file.')
        return render_template(
            'product_display.html', products=[], error='File error'
        )

    if product_id is not None:
        data = [
            product for product in data
            if str(product['id']) == product_id
        ]
        if not data:
            return render_template(
                'product_display.html',
                products=[],
                error='Product not found'
            )

    return render_template(
        'product_display.html', products=data, error=None
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
