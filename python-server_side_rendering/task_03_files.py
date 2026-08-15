from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json():
    with open('products.json', 'r') as file:
        return json.load(file)


def read_csv():
    products = []

    with open('products.csv', 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)

    return products


@app.route('/products')
def products():
    source = request.args.get('source')

    if source == 'json':
        products_data = read_json()
    elif source == 'csv':
        products_data = read_csv()
    else:
        return render_template(
            'product_display.html',
            products=[],
            error='Wrong source'
        )

    product_id = request.args.get('id')

    if product_id:
        product_id = int(product_id)

        products_data = [
            product for product in products_data
            if product['id'] == product_id
        ]

        if not products_data:
            return render_template(
                'product_display.html',
                products=[],
                error='Product not found'
            )

    return render_template(
        'product_display.html',
        products=products_data,
        error=None
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
