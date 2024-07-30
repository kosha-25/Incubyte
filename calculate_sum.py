
from task import StringCalculator

def main():
    calculator = StringCalculator()
    # Example inputs
    # input_strings = [
    #     "",
    #     "1",
    #     "1,2",
    #     "1,2,3,4,5",
    #     "1\n2,3",
    #     "//;\n1;2",
    #     "1,-2,3,-4",
    #     "25,17,10"
        
    # ]


    
    while True:
        input_str = input("Enter numbers (or 'exit' to quit): ")
        
        if input_str.lower() == 'exit':
            break
        
        # # Remove enclosing double quotes if present
        # if input_str.startswith('"') and input_str.endswith('"'):
        #     input_str = input_str[1:-1]
        
        #  # Replace escaped newline characters with actual newline characters
        # input_str = input_str.encode().decode('unicode_escape')
        # input_str = input_str.strip('"')
        
        try:
            result = calculator.add(input_str)
            print(f"Input: '{input_str}' -> Sum: {result}")
        except ValueError as e:
            print(f"Input: '{input_str}' -> Exception: {e}")

if __name__ == "__main__":
    main()
