'''You are asked to build a simple E-commerce Billing System using Python modules.
Create a module file named ecommerce_utils.py that contains the following functions:
->apply_discount(price, discount_percent) → applies a discount and returns the discounted price.
->add_gst(price, gst_percent=18) → adds GST (default 18%) and returns the new price.
generate_invoice(cart, discount_percent=0, gst_percent=18) → accepts a dictionary cart (with product names as keys and prices as values) and prints a detailed invoice.
Create a main program file named main.py that:
Imports the ecommerce_utils module.
Creates a shopping cart (dictionary) with at least 3 products.
Calls the module functions to generate an invoice.'''
def apply_discount(price, discount_percent):
    discount = (discount_percent / 100) * price
    amount = price - discount
    print(f"Amount after {discount_percent}% is= {amount}")
    return amount

def add_gst(price, gst_percent):
    gst_amount = (gst_percent / 100) * price
    after_gst = price + gst_amount
    print(f"Afer {gst_percent}% gst= {after_gst}")
    return after_gst

def generate_invoice(cart, discount_percent, gst_percent):
    print("\n========= INVOICE =========")
      # ✅ initialize subtotal before adding
    
    for k, v in cart.items():
        print(f'{k}: Rs.{v}')
        price = sum(cart.values())
    
    print("----------------------------")
    print(f"Subtotal        : ₹{price}")
    
    # Apply discount
    price_after_discount = apply_discount(price, discount_percent)
    
    # Apply GST
    final_price = add_gst(price_after_discount, gst_percent)
    
    print("----------------------------")
    print(f"TOTAL PAYABLE   : ₹{final_price:.2f}")
    print("============================")
    return final_price
