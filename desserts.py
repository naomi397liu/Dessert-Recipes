"""Dessert classes."""


class Cupcake:
    """A cupcake."""
    cache = {}

    def __repr__(self):
        """Human-readable printout for debugging."""
        

        return f'<Cupcake name="{self.name}" qty={self.qty}>'

    def __init__(self, name, flavor, price):
        self.name = name
        self.flavor = flavor
        self.price = price
        self.qty = 0
    
        self.cache[self.name] = self
    
    def add_stock(self, amount_added):
        self.qty = self.qty + amount_added
    
    def sell(self, amount_bought):
        if self.qty == 0:
            print('Sorry, these cupcakes are sold out')
        elif amount_bought > self.qty:
            self.qty = 0
        else:   
            self.qty = self.qty - amount_bought
    
    @staticmethod
    def scale_recipe(ingredients, amounts):
        recipe_list = []
        for ingredient in ingredients:
            modified_ingredient = (ingredient[0], ingredient[1] * amounts)
            recipe_list.append(modified_ingredient)
        return recipe_list
    
    @classmethod
    def get(cls, name):
        selected_cupcake = cls.cache.get(name)
        if selected_cupcake == None:
            print("Sorry, that cupcake doesn't exist")
        return selected_cupcake

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
