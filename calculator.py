# %%

# Calculator Project  with OOP
# add, multiply, division, subtraction

class Calculator(object):
    
    def __init__(self, value_1, value_2):
        
        self.value_1 = value_1
        self.value_2 = value_2
        
    def add(self):
        return self.value_1 + self.value_2
    
    def subtraction(self):
        return self.value_1 - self.value_2
    
    def multiply(self):
        return self.value_1 * self.value_2
    
    def division(self):
        return self.value_1 / self.value_2
    
   
first_value = int(input("Enter the first number: "))
second_value = int(input("Enter the second number: "))
values = Calculator(first_value, second_value)

print("Please choose the operation:")
proper_selections = ["0", "1", "2", "3", "4"]

while True:
    
    selection = input(
        "\tPress '0' for cancellation"                  
        "\n\tPress '1' for addition"
        "\n\tPress '2' for multiplication"
        "\n\tPress '3' for subtraction"
        "\n\tPress '4' for division"
        "\n\nYour selection is ")
    
    if selection in proper_selections:
        break
    
    else:
        print("\nPlease check your selection...")

if selection == "1":
    print("\nAddition result: ", format(values.add()))
elif selection == "2":
    print("\nMultiplication result: ", format(values.multiply()))
elif selection == "3":
    print("\nSubtration result: ", format(values.subtraction()))
elif selection == "4":
    print("\nDivision result: ", format(values.division()))
    
    
    
























