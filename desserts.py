"""Dessert classes."""


class Cupcake:
    """A cupcake."""
    cache = {}

    def __repr__(self, name, flavor, price, qty):
        """Human-readable printout for debugging."""
        self.name = name
        self.flavor = flavor
        self.price = price
        self.qty = qty

        return f'<Cupcake name="{self.name}" qty={self.qty}>'

    def __init__(self):
        
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
