def main():
    print("Welcome to the converters program!")
    print()
    
    while True:
        print("List of conversions:")
        print("[inches] (to centimeters)")
        print("[centimeters] (to inches)")
        
    starting_unit = input("Enter the type of value you wish to convert: ")
    starting_value = float(input("How many " + starting_unit + "?"))
    
    if starting_unit == "inches":
        inches_to_centimeters()
    elif starting_unit == "centimeters":
        centimeters_to_inches()
    print(result)
    print()
    
def inches_to_centimeters(inches):
    """Converts from inches to centimeters

    Parameters:
        inches - the number of inches to convert
        
    Conversion factor: 1 cm = 2.54 in
    """
    centimeters = inches * 2.54
    return centimeters

def centimeters_to_inches(centimeters):
    inches = centimeters/2.54
    print(inches)
    
    return inches

