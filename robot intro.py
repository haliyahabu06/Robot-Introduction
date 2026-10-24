class Robot:
    company = "HalCybernetics"
    owner = "Haliyah"

    def __init__(self, name, age, model):
        self.name = name
        self.age = age
        self.model = model

    def introduce(self):
        return "Hi I am {}".format(self.name)

    def details(self):
        return "My name is {}, built by {} at {}. I am model {} and I am {} years old.".format(
            self.name, self.owner, self.company, self.model, self.age
        )

    def clean(self, area):
        return "{} is cleaning the {}".format(self.name, area)

 

tom = Robot("Tom", 5, "X-100")
jerry = Robot("Jerry", 3, "Z-200")

# Tom's outputs
print(tom.introduce())
print(tom.details())
print(tom.clean("kitchen"))

print("-" * 15)

print(jerry.introduce())
print(jerry.details())
print(jerry.clean("living room"))
