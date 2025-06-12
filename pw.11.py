class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def hello(self):
        print("hello my name is" + self.name + "my age is" +str(self.age))
        
    def __str__(self):
        return f"{self.name}({self.age})"
p1 = person("sangay", 20)
print(p1)
        
    

       