from flask import Flask, jsonify
from .applianceparts365_scraper import scrape_applianceparts365

app = Flask(__name__)

@app.route("/applianceparts365/product-price", methods=["GET"])
def get_product_price():
    url = "https://applianceparts365.com/dishwasher-bottom-door-gasket-for-frigidaire-809006501-1058857"
    product_price = scrape_applianceparts365(url)
    return jsonify({"price": product_price})

if __name__ == "__main__":
    app.run(debug=True)