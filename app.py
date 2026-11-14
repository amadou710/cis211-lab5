# CIS 211 Lab 5 - Bright Bakery Interactive Order Calculator
# Complete the TODO sections using the Lab 5 instructions.
# Add at least THREE explanatory comments of your own.

import streamlit as st

# Supplied data: keep these products, prices and sample counts unchanged.
menu = {
    "cupcake": 3.75,
    "cookie": 2.00,
    "muffin": 2.75,
    "scone": 3.25,
    "brownie": 3.00,
}

sample_sales = {
    "Product": ["cupcake", "cookie", "muffin", "scone", "brownie"],
    "Units sold": [18, 30, 12, 10, 15],
}


def apply_discount(subtotal):
    """Return the remaining item subtotal after any eligible discount."""
    # Apply a 10% discount when the original subtotal reaches or exceeds $50.00[cite: 2, 4]
    if subtotal >= 50.00:
        return round(subtotal * 0.90, 2)
    return subtotal


def shipping_fee(subtotal):
    """Return the Delivery fee, using the ORIGINAL item subtotal."""
    # Delivery is free if the original subtotal is $35.00 or more; otherwise $5.99[cite: 2, 4]
    if subtotal >= 35.00:
        return 0.00
    return 5.99


st.title("Bright Bakery Interactive Order Calculator")
st.caption("A class practice app that calculates a quote.")

# TODO 3 - Step 5: Put the required controls in a sidebar.[cite: 5]
st.sidebar.header("Order Options")
customer_name = st.sidebar.text_input("Customer name", value="")
product = st.sidebar.selectbox("Product", list(menu.keys()))
quantity = st.sidebar.number_input("Quantity", min_value=1, max_value=30, value=1, step=1)
fulfillment = st.sidebar.selectbox("Fulfillment", ["Pickup", "Delivery"])
show_chart = st.sidebar.checkbox("Show sample sales chart", value=True)

# TODO 4 - Step 6: Calculate unit_price, subtotal and discounted_subtotal.[cite: 6]
unit_price = menu[product]
subtotal = unit_price * quantity
discounted_subtotal = apply_discount(subtotal)
# Ensure discounted_subtotal defaults correctly if a function branch lacks a return statement
if discounted_subtotal is None:
    discounted_subtotal = subtotal
discount_amount = round(subtotal - discounted_subtotal, 2)
# Pickup costs $0.00; Delivery uses shipping_fee(subtotal) based on the original subtotal[cite: 2, 6]
delivery_fee = 0.00 if fulfillment == "Pickup" else shipping_fee(subtotal)
if delivery_fee is None:
    delivery_fee = 5.99
total = round(discounted_subtotal + delivery_fee, 2)

# TODO 5 - Step 7: Show the quote in two columns with dollars to 2 decimals.[cite: 6]
st.subheader("Current Quote")
col1, col2 = st.columns(2)

with col1:
    st.write(f"**Selected product:** {product}")
    st.write(f"**Quantity:** {quantity}")
    st.write(f"**Unit price:** ${unit_price:.2f}")
    st.write(f"**Fulfillment:** {fulfillment}")

with col2:
    st.write(f"**Original item subtotal:** ${subtotal:.2f}")
    st.write(f"**Discount amount:** -${discount_amount:.2f}")
    st.write(f"**Delivery fee:** ${delivery_fee:.2f}")
    st.metric("Final total", f"${total:.2f}")

# TODO 6 - Step 8: Build and display the menu table from the menu dictionary.[cite: 7]
st.subheader("Bakery Menu")
menu_data = {
    "Product": list(menu.keys()),
    "Price ($)": [f"${price:.2f}" for price in menu.values()]
}
st.dataframe(menu_data, hide_index=True)

st.subheader("Sample Sales")
st.caption("Fictional sample sales data for display practice.")
# Add a clearly labeled fictional sample-sales chart controlled by show_chart.[cite: 7]
if show_chart:
    st.bar_chart(data=sample_sales, x="Product", y="Units sold", sort=False)

# TODO 7 - Step 9: Add a Check quote button.[cite: 7]
if st.button("Check quote"):
    cleaned_name = customer_name.strip()
    if not cleaned_name:
        st.warning("Please enter a customer name or nickname.")
    else:
        st.success(f"Quote checked successfully for {cleaned_name}! Note: This practice app does not save an order or take a payment.")

# TODO 8: Test, add your own comments and remove the starter info message.[cite: 7]
