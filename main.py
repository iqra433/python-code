from Navigation import Navigation
from productselection import Product
from checkout import Checkout
# Step 1: Open site
nav = Navigation()
driver = nav.open_site()

# Step 2: Pass driver to Product
select = Product(driver)
select.add_product()

checkout = Checkout(driver)
checkout.place_order()