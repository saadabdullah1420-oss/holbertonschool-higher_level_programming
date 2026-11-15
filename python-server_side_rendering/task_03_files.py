#!/usr/bin/env python3
"""Display and filter products loaded from JSON or CSV."""

import csv
import json
from pathlib import Path

from flask import Flask, render_template, request

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent


def read_json():
    """Read products from the JSON file."""
    with open(BASE_DIR / 'products.json', encoding='utf-8') as file:
        return json.load(file)


def read_csv():
    """Read products from the CSV file."""
    with open(
        BASE_DIR / 'products.csv', newline='', encoding='utf-8'
    ) as file:
        return list(csv.DictReader(file))


@app.route('/products')
def products():
    """Display products from the requested source, optionally by ID."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    else:
        return render_template(
            'product_display.html', products=[], error='Wrong source'
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
