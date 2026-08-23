from flask import Flask, abort, render_template

app = Flask(__name__)

PRODUCTS = [
    {"name": "Contemporary Sofa", "image": "product-23.jpeg", "price": "From ₹3,000", "description": "Modern comfort with a clean, elegant silhouette."},
    {"name": "Premium Comfort Sofa", "image": "product-16.jpeg", "price": "Enquire for price", "description": "Soft textures and thoughtful proportions for modern homes."},
    {"name": "Designer Curtains", "image": "product-20.jpeg", "price": "₹250 – ₹1,200 / metre", "description": "Elegant fabrics that transform the feel of a room."},
    {"name": "Elegant Drape", "image": "product-22.jpeg", "price": "From ₹250 / metre", "description": "Soft textures and timeless window styling."},
    {"name": "Comfort Mattress", "image": "product-4.jpeg", "price": "Enquire for price", "description": "Designed for comfortable, restful sleep."},
    {"name": "Premium Rest Mattress", "image": "product-6.jpeg", "price": "Enquire for price", "description": "Supportive comfort for everyday relaxation."},
]

CATEGORIES = {
    "sofas": {
        "label": "SOFA COLLECTION",
        "title": "Sofas made for living.",
        "description": "Explore custom sofas designed around your room, your comfort and the way you gather at home.",
        "images": ["product-1.png", "product-2.jpeg", "product-5.jpeg", "product-16.jpeg", "product-17.jpeg", "product-18.jpeg", "product-19.jpeg", "product-21.jpeg", "product-23.jpeg", "image-9.jpeg", "image-13.jpeg"],
        "features": ["Custom sizes and layouts", "Comfort-focused foam options", "Fabric and colour selection"],
    },
    "curtains": {
        "label": "CURTAIN COLLECTION",
        "title": "Curtains that frame your space.",
        "description": "Find the right fall, texture and light control for every window, with fabrics selected for your room.",
        "images": ["product-9.jpeg", "product-10.jpeg", "product-11.jpeg", "product-12.png", "product-20.jpeg", "product-22.jpeg"],
        "features": ["Blackout and light-filtering options", "Custom measurements", "Pleat and rod styles"],
    },
    "mattresses": {
        "label": "MATTRESS COLLECTION",
        "title": "Better comfort. Better rest.",
        "description": "Explore mattress styles and speak with us about density, thickness, fabric and the right fit for your bed.",
        "images": ["product-4.jpeg", "product-6.jpeg", "product-8.jpeg"],
        "features": ["Foam density from 32 to 50", "Thickness from 4 to 12 inches", "GC cotton, cotton, jacquard and polyster fabrics"],
    },
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/products")
def products():
    return render_template("products.html", products=PRODUCTS)

@app.route("/category/<category_name>")
def category(category_name):
    category_data = CATEGORIES.get(category_name)
    if category_data is None:
        abort(404)
    return render_template("category.html", category=category_data, category_name=category_name)


if __name__ == "__main__":
    app.run(debug=True)
