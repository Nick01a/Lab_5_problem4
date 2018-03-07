def get_valid_input(input_string, valid_options):
    """
    (str, list)->str
    Checks if input is correct
    """
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response

class Property:
    """
    Class which show property.
    """
    def __init__(self, square_feet='', beds='',baths='',**kwargs):
        """
        Initialise class Property
        """
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        """
        Show information about class Property
        """
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def prompt_init():
        """
        ()->dict
        Convert information about the class Property to dictionary
        """
        return dict(square_feet=input("Enter the square feet: "),beds = input("Enter number of bedrooms: "),
                    baths = input("Enter number of baths: "))
    prompt_init = staticmethod(prompt_init)

class Apartment(Property):
    """
    Show info about class Apartment we inherit class Property
    """
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")
    def __init__(self, balcony='', laundry='', **kwargs):
        """
        Initialisation class Property
        """
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        """
        Shows information about class Apartment items
        """
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)

    def prompt_init():
        """
        () -> dict
        From keyword to dictionary
        """
        parent_init = Property.prompt_init()
        laundry = get_valid_input(
            "What laundry facilities does the property have?", Apartment.valid_laundries)
        balcony = get_valid_input(
            "Does the property have a balcony", Apartment.valid_balconies)
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init
    prompt_init = staticmethod(prompt_init)

class House(Property):
    """
    Present class House we inherit class Property
    """
    valid_garage = ('attached', 'detached', 'none')
    valid_fenced = ('yes', 'no')

    def __init__(self, num_stories='',
                 garage='', fenced='', **kwargs):
        """
        (str, str, str) -> None
        Initialisation class House
        """
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        """
        Shows info about class House items
        """
        super().display()
        print('HOUSE DETAILS')
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        """
        () -> dict
        From keyboard to dictionary
        """
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ",
                                 House.valid_fenced)
        garage = get_valid_input("Is there a garage? ",
                                 House.valid_garage)
        num_stories = input("How many stories? ")

        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)

class Purchase:
    """
    Present class Purchase
    """

    def __init__(self, price='', taxes='', **kwargs):
        """
        Initialisation class Purchase
        """
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        """
        Shows information about class Purchase items
        """
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        """
        () -> dict
        Convert from keyboard to dictionary
        """
        return dict(
            price=input("What is the selling price? "),
            taxes=input("What are estimated taxes? "))

    prompt_init = staticmethod(prompt_init)

class Rental:
    """
    Present class Rental
    """

    def __init__(self, furnished='', utilities='',
                 rent='', **kwargs):
        """
        Initialisation class Rental
        """
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        """
        Shows information about class Rental items
        """
        super().display()
        print("RENTAL DETAILS")
        print('rent: {}'.format(self.rent))
        print("estimated utilities: {}".format(
            self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        """
        () -> dict
        Convert information from keyboard to dictionary
        """
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input(
                "What are the estimated utilities? "),
            furnished=get_valid_input(
                "Is the property furnished? ",
                                      ("yes", "no")))

    prompt_init = staticmethod(prompt_init)

class HouseRental(Rental, House):
    """
    Presents class HouseRental we inherit classes Rental and House
    """
    def prompt_init():
        """
        () -> dict
        Convert information from keyboard to dict
        """
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)

class ApartmentRental(Rental, Apartment):
    """
    Presents class ApartmentRental we inherit classes Rental and House
    """
    def prompt_init():
        """
        () -> dict
        Convert information from keyword to dictionary
        """
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)

class ApartmentPurchase(Purchase, Apartment):
    """
    Presents class ApartmentPurchase we inherit classes Purchase and Apartment
    """
    def prompt_init():
        """
        () -> dict
        Convert information from keyboard to dictionary
        """
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)

class HousePurchase(Purchase, House):
    """
    Presents class HousePurchase we inherit classes Purchase and House
    """
    def prompt_init():
        """
        () -> dict
        Convert information from keyboard to dictionary
        """
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)

class Agent:
    """
    Class represents Agent
    """

    def __init__(self):
        """
        Initialisation class Agent
        """
        self.property_list = []

    def display_properties(self):
        """
        Shows info about class Agent items
        """
        for property in self.property_list:
            property.display()

    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
    }

    def display_house_more(self, cost):
        """
        (int) -> None
        Shows houses with prices more than me put
        """
        for i in self.property_list:
            if type(i) in [HousePurchase]:
                if eval(i.price) > cost:
                    i.display()
    def display_house_less(self, cost):
        """
        (int) -> None
        Shows houses with prices less than me put
        """
        for i in self.property_list:
            if type(i) in [HousePurchase]:
                if eval(i.price) < cost:
                    i.display()

    def display_house_equal(self, cost):
        """
        (int) -> None
        Shows houses with equal prices
        """
        for i in self.property_list:
            if type(i) in [HousePurchase]:
                if eval(i.price) == cost:
                    i.display()

    def display_apartments_more(self, cost):
        """
        Shows apartments with prices more than we put
        """
        for i in self.property_list:
            if type(i) in [ApartmentRental]:
                if eval(i.rent) > cost:
                    i.display()
    def display_apartments_less(self, cost):
        """
        Shows apartments with prices less than we put
        """
        for i in self.property_list:
            if type(i) in [ApartmentRental]:
                if eval(i.rent) < cost:
                    i.display()
    def display_apartments_equal(self, cost):
        """
        Shows apartments with equal prices
        """
        for i in self.property_list:
            if type(i) in [ApartmentRental]:
                if eval(i.rent) == cost:
                    i.display()
    def more_beds(self, numb):
        """
        Shows hoses with beds which count is more than we put
        """
        for i in self.property_list:
            if type(i) in [HousePurchase]:
                if i.bedrooms >= numb:
                    i.display()
            else:
                return None

    def less_beds(self, numb):
        """
        Shows hoses with beds which count is less than we put
        """
        for i in self.property_list:
            if type(i) in [HousePurchase]:
                if i.bedrooms < numb:
                    i.display()
            else:
                return None

    def add_property(self):
        """
        Adds property which we choose (type)
        """
        property_type = get_valid_input(
            "What type of property? ",
            ("house", "apartment")).lower()
        payment_type = get_valid_input(
            "What payment type? ",
            ("purchase", "rental")).lower()

        PropertyClass = self.type_map[
            (property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        print(init_args)
        self.property_list.append(PropertyClass(**init_args))
