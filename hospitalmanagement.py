class Patient:
    def __init__(self,name,age,disease):
        self.name=name
        self.age=age
        self.disease=disease
    def display(self):
        print(self.name,self.age,self.disease)

p=Patient("Likitha",21,"Fever")
p.display()