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
    # TODO 1: Follow Step 4. Replace pass with your calculation and return.
    pass


def shipping_fee(subtotal):
    """Return the Delivery fee, using the ORIGINAL item subtotal."""
    # TODO 2: Follow Step 4. Replace pass with your decision and return.
    pass


st.title("Bright Bakery Interactive Order Calculator")
st.caption("A class practice app that calculates a quote.")
st.info("Starter file loaded. Complete the TODO sections before submitting.")

# TODO 3 - Step 5: Put the required controls in a sidebar.
st.sidebar.header("Order Options")
customer_name = st.sidebar.text_input("Customer name", value="")
product = st.sidebar.selectbox("Product", list(menu.keys()))
quantity = st.sidebar.number_input("Quantity", min_value=1, max_value=30, value=1, step=1)
fulfillment = st.sidebar.selectbox("Fulfillment", ["Pickup", "Delivery"])
show_chart = st.sidebar.checkbox("Show sample sales chart", value=True)

# TODO 4 - Step 6: Calculate unit_price, subtotal and discounted_subtotal.
unit_price = menu[product]
subtotal = unit_price * quantity
discounted_subtotal = apply_discount(subtotal)
discount_amount = round(subtotal - discounted_subtotal, 2)
# Pickup costs $0.00; Delivery uses shipping_fee(subtotal) based on the original subtotal
delivery_fee = 0.00 if fulfillment == "Pickup" else shipping_fee(subtotal)
total = round(discounted_subtotal + delivery_fee, 2)

# TODO 5 - Step 7: Show the quote in two columns with dollars to 2 decimals.
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

# TODO 6 - Step 8: Build and display the menu table from the menu dictionary.
st.subheader("Bakery Menu")
menu_data = {
    "Product": list(menu.keys()),
    "Price ($)": [f"${price:.2f}" for price in menu.values()]
}
st.dataframe(menu_data, hide_index=True)

st.subheader("Sample Sales")
st.caption("Fictional sample sales data for display practice.")
# Add a clearly labeled fictional sample-sales chart controlled by show_chart.
if show_chart:
    st.bar_chart(data=sample_sales, x="Product", y="Units sold", sort=False)

# TODO 7 - Step 9: Add a Check quote button.
if st.button("Check quote"):
    cleaned_name = customer_name.strip()
    if not cleaned_name:
        st.warning("Please enter a customer name or nickname.")
    else:
        st.success(f"Quote checked successfully for {cleaned_name}! Note: This practice app does not save an order or take a payment.")

# TODO 8: Test, add your own comments and remove the starter info message.
