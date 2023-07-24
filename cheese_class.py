class Cheese():
    """A complex attempt to model cheese."""
    def __init__(self, variation, aged, taste):
        """Make some attributes to fit your cheese."""
        self.variation = variation
        self.aged = aged
        self.taste = taste
        

    def get_descriptive_info(self):
        """Return info about da cheese"""
        info = self.variation + " " + str(self.aged) + " " + self.taste
        return info.title()
    
    def read_taste(self):
        """print a statement showing taste of the cheese"""
        print(f"This cheeses tastes rather {self.taste}.")

    
my_favorite_cheese = Cheese("parmesan", 9, "salty")
print(my_favorite_cheese.get_descriptive_info())
my_favorite_cheese.read_taste()