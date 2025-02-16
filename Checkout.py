class Checkout:
    class Discount:
        def __init__(self, nbrItems, price):
            self.nbrItems = nbrItems  # Number of items needed for discount
            self.price = price  # Discounted price

    def __init__(self):
        self.prices = {}  # Store item prices
        self.discounts = {}  # Store discount rules
        self.items = {}  # Track added items

    def additemprice(self, item, price):
        """Add price for a given item."""
        self.prices[item] = price

    def additem(self, item):
        """Add an item and track its quantity."""
        if item not in self.prices:
            if item not in self.prices:
                raise Exception("Bad Item")
            # Ensure item price exists
            raise KeyError(f"Price for item '{item}' not set")
        if item not in self.items:
            self.items[item] = 0
        self.items[item] += 1

    def calculateTotal(self):
        """Calculate the total price including discounts."""
        total = 0
        for item, quantity in self.items.items():
            if item in self.discounts:
                discount = self.discounts[item]
                # Apply discount: calculate how many sets of the discount apply
                sets_of_discount = quantity // discount.nbrItems
                remaining_items = quantity % discount.nbrItems
                total += sets_of_discount * discount.price
                total += remaining_items * self.prices[item]
            else:
                total += quantity * self.prices[item]
        return total

    def adddiscount(self, item, nbrofitems, price):
        """Add a discount rule for a specific item."""
        self.discounts[item] = self.Discount(nbrofitems, price)

    def calculateItemDiscountedTotal(self, item, cnt, discount):
        total = 0
        nbrOfDiscounts = cnt / discount.nbrItems
        total += nbrOfDiscounts * discount.price
        remaining = cnt % discount.nbrItems
        total += remaining * self.prices[item]
        return total

