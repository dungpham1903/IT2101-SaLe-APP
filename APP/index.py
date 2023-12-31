from flask import render_template, request
import dao
from APP import app


@app.route("/")
def index():
    kw = request.args.get('kw')
    cates = dao.get_categories()
    prods = dao.get_products(kw)
    return render_template('index.html', categories = cates, products = prods)

if __name__ == '__main__':
    from APP import admin
    app.run(debug=True)