from flask import Flask, render_template, abort

app = Flask(__name__)

# --------------------------------------------------
# BUSINESS INFORMATION
# --------------------------------------------------

BUSINESS_NAME = "Shree Rajlaxmi Handloom & Furnishing"
PHONE = "9638635600"
WHATSAPP = "919638635600"
EMAIL = "niravrajlaxmi@gmail.com"

ADDRESS = (
    "First Floor, Vaidehi Plaza, Opp. Hanuman Ji Temple, "
    "Ravapar Ghunda Road, Morbi, Gujarat - 363641"
)

# --------------------------------------------------
# PRODUCTS
# --------------------------------------------------

PRODUCTS = [

    # SOFAS
    {
        "id": 1,
        "category": "sofas",
        "name": "Contemporary Sofa",
        "image": "product-23.jpeg",
        "price": "From ₹3,000",
        "description": "Modern comfort with a clean and elegant silhouette."
    },
    {
        "id": 2,
        "category": "sofas",
        "name": "Premium Comfort Sofa",
        "image": "product-16.jpeg",
        "price": "Enquire for price",
        "description": "Soft textures and thoughtful proportions for everyday comfort."
    },
    {
        "id": 3,
        "category": "sofas",
        "name": "Designer Sofa",
        "image": "product-17.jpeg",
        "price": "Enquire for price",
        "description": "A stylish statement sofa designed for modern interiors."
    },
    {
        "id": 4,
        "category": "sofas",
        "name": "Classic Sofa",
        "image": "product-18.jpeg",
        "price": "Enquire for price",
        "description": "A timeless design combining comfort and elegance."
    },

    # CURTAINS
    {
        "id": 5,
        "category": "curtains",
        "name": "Elegant Curtains",
        "image": "product-19.jpeg",
        "price": "₹250 – ₹1,200 / metre",
        "description": "Beautiful curtain fabrics for stylish and comfortable spaces."
    },
    {
        "id": 6,
        "category": "curtains",
        "name": "Premium Curtains",
        "image": "product-20.jpeg",
        "price": "₹250 – ₹1,200 / metre",
        "description": "Premium fabrics available in a variety of colours and patterns."
    },
    {
        "id": 7,
        "category": "curtains",
        "name": "Designer Curtains",
        "image": "product-21.jpeg",
        "price": "₹250 – ₹1,200 / metre",
        "description": "Designer curtain options to complement your interiors."
    },

    # MATTRESSES
    {
        "id": 8,
        "category": "mattresses",
        "name": "Comfort Mattress",
        "image": "product-22.jpeg",
        "price": "Enquire for price",
        "description": "Comfortable mattress options designed for restful sleep."
    },
    {
        "id": 9,
        "category": "mattresses",
        "name": "Premium Mattress",
        "image": "product-24.jpeg",
        "price": "Enquire for price",
        "description": "Premium comfort and support for your bedroom."
    },

    # FURNISHING
    {
        "id": 10,
        "category": "furnishing",
        "name": "Custom Furnishing",
        "image": "product-25.jpeg",
        "price": "Enquire for price",
        "description": "Custom furnishing solutions created according to your requirements."
    }
]


# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

@app.route("/")
def home():
    return render_template(
        "index.html",
        business_name=BUSINESS_NAME,
        phone=PHONE,
        whatsapp=WHATSAPP,
        email=EMAIL,
        address=ADDRESS,
        products=PRODUCTS
    )


# --------------------------------------------------
# COLLECTIONS PAGE
# --------------------------------------------------

@app.route("/collections")
def collections():
    return render_template(
        "collections.html",
        business_name=BUSINESS_NAME,
        phone=PHONE,
        whatsapp=WHATSAPP,
        email=EMAIL,
        address=ADDRESS,
        products=PRODUCTS
    )


# --------------------------------------------------
# CATEGORY PAGES
# --------------------------------------------------

@app.route("/collections/<category>")
def collection_category(category):

    valid_categories = [
        "sofas",
        "curtains",
        "mattresses",
        "furnishing"
    ]

    if category not in valid_categories:
        abort(404)

    category_products = [
        product for product in PRODUCTS
        if product["category"] == category
    ]

    category_names = {
        "sofas": "Sofas",
        "curtains": "Curtains",
        "mattresses": "Mattresses",
        "furnishing": "Custom Furnishing"
    }

    return render_template(
        "category.html",
        business_name=BUSINESS_NAME,
        phone=PHONE,
        whatsapp=WHATSAPP,
        email=EMAIL,
        address=ADDRESS,
        products=category_products,
        category=category_names[category]
    )


# --------------------------------------------------
# PRODUCT PAGE
# --------------------------------------------------

@app.route("/product/<int:product_id>")
def product(product_id):

    selected_product = next(
        (product for product in PRODUCTS if product["id"] == product_id),
        None
    )

    if selected_product is None:
        abort(404)

    return render_template(
        "product.html",
        business_name=BUSINESS_NAME,
        phone=PHONE,
        whatsapp=WHATSAPP,
        email=EMAIL,
        address=ADDRESS,
        product=selected_product
    )


# --------------------------------------------------
# ABOUT / OUR STORY
# --------------------------------------------------

@app.route("/our-story")
def our_story():
    return render_template(
        "our-story.html",
        business_name=BUSINESS_NAME,
        phone=PHONE,
        whatsapp=WHATSAPP,
        email=EMAIL,
        address=ADDRESS
    )


# --------------------------------------------------
# CUSTOMIZE
# --------------------------------------------------

@app.route("/customize")
def customize():
    return render_template(
        "customize.html",
        business_name=BUSINESS_NAME,
        phone=PHONE,
        whatsapp=WHATSAPP,
        email=EMAIL,
        address=ADDRESS
    )


# --------------------------------------------------
# CONTACT
# --------------------------------------------------

@app.route("/contact")
def contact():
    return render_template(
        "contact.html",
        business_name=BUSINESS_NAME,
        phone=PHONE,
        whatsapp=WHATSAPP,
        email=EMAIL,
        address=ADDRESS
    )


# --------------------------------------------------
# RUN APP
# --------------------------------------------------

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
