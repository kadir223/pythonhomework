
class Date:
    def __init__(self, day, month, year):
        self.day= day
        self.month=month
        self.year=year
        self.months=[]
    def form1(self):
        return f"{self.month}/{self.day}/{self.year}"
    def form2(self):



date1=Date(11,8,2007)
print (date1.form1())