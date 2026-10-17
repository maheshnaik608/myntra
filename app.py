
from flask import Flask, render_template, request

app = Flask(__name__)

products = [
    {
        "id": 1,
        "name": "Men's Casual T-Shirt",
        "category": "Men",
        "price": 499,
        "image": "https://placehold.co/300x350?text=Casual+TShirt"
    },
    {
        "id": 2,
        "name": "Women's Stylish Dress",
        "category": "Women",
        "price": 999,
        "image": "https://placehold.co/300x350?text=Stylish+Dress"
    },
    {
        "id": 3,
        "name": "Running Sneakers",
        "category": "Footwear",
        "price": 1499,
        "image": "https://placehold.co/300x350?text=Sneakers"
    },
    {
        "id": 4,
        "name": "Classic Denim Jeans",
        "category": "Men",
        "price": 1199,
        "image": "https://placehold.co/300x350?text=Denim+Jeans"
    },
    {
        "id": 5,
        "name": "Women's Handbag",
        "category": "Accessories",
        "price": 799,
        "image": "https://placehold.co/300x350?text=Handbag"
    },
    {
        "id": 6,
        "name": "Traditional Kurta",
        "category": "Women",
        "price": 899,
        "image": "https://placehold.co/300x350?text=Kurta"
    }
]

@app.route("/")
def home():
    search = request.args.get("search", "").strip().lower()
    category = request.args.get("category", "").strip()

    filtered_products = products

    if search:
        filtered_products = [
            p for p in filtered_products
            if search in p["name"].lower()
        ]

    if category:
        filtered_products = [
            p for p in filtered_products
            if p["category"] == category
        ]

    return render_template(
        "index.html",
        products=filtered_products,
        search=search,
        category=category
    )

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
