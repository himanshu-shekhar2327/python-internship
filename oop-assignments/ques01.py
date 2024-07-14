class Person:
    def __init__(self,name,age,gender) :
        self.name=name
        self.age=age
        self.gender=gender

    def introduce(self) :
        print(f"name is : {self.name}.\n age is : {self.age} \n gender is :  {self.gender}.")

# here we take input from the user
inp_name = input("Enter the name :")
inp_age = int(input("Enter the age : "))
inp_gender=input("Enter the gender :")
person1 = Person(inp_name,inp_age, inp_gender)

person1.introduce()
