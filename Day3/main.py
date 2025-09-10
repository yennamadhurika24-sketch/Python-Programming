import ecommerce_utils

cart = {
    "Laptop": 50000,
    "Mouse": 500,
    "Keyboard": 1500
}

ecommerce_utils.generate_invoice(cart, discount_percent=10, gst_percent=18)
