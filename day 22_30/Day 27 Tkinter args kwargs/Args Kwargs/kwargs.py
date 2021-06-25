def calculate(n,**kwargs):
    # kwargs is of type dictionary
    # 
    n += kwargs['add']
    n *= kwargs['multiply']
    return n

print(calculate(2, add=3, multiply=5))


class Car:
    def __init__(self,**kwargs):
        # get command will pass none if kwarg ddosn't exist
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')
        self.colour = kwargs.get('colour')

my_car = Car(make='Ford', model='Escort')
print(my_car.make, my_car.model, my_car.colour) # => returns Ford Escort None

