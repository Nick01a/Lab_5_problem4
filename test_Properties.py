from Properties import *
get_valid_input("what laundry?", ("coin", "ensuite", "none"))
init = HouseRental.prompt_init()
"""
Enter the square feet: 1
Enter number of bedrooms: 2
Enter number of baths: 3
Is the yard fenced? no
Is there a garage? none
How many stories? 4
What is the monthly rent? 5
What are the estimated utilities? 6
Is the property furnished? no
"""
house = HouseRental(**init)
house.display()
agent = Agent()
agent.add_property()
"""
What type of property? house
What payment type? rental
Enter the square feet: 900
Enter number of bedrooms: 2
Enter number of baths: one and half
Is the yard fenced? yes
Is there a garage? detached
How many stories? 1
What is the monthly rent? 1200
What are the estimated utilities? included
Is the property furnished? no
>>>{'square_feet': '900', 'beds': '2', 'baths': 'one and half', 'fenced': 'yes', 'garage': 'detached', 'num_stories': '1', 'rent': '1200', 'utilities': 'included', 'furnished': 'no'}
"""
agent.add_property()
"""
What type of property?  apartment
What payment type?  purchase
Enter the square feet:  800
Enter number of bedrooms:  3
Enter number of baths:  2
What laundry facilities does the property have?  ensuite
Does the property have a balcony  yes
What is the selling price?  $200,000
What are estimated taxes?  1500
>>>{'square_feet': '800', 'beds': '3', 'baths': '2', 'laundry': 'ensuite', 'balcony': 'yes', 'price': '$200,000', 'taxes': '1500'}
"""
agent.display_properties()
agent.display_apartments_more("$100")
agent.more_beds(4)
agent.less_beds(4)
agent.display_apartments_less("$100")
agent.display_apartments_equal("$100")
agent.display_house_equal("$100")
agent.display_house_less("$100")
agent.display_house_more("$100")
