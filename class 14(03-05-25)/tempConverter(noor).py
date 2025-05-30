import sys

def convert_temperature(from_scale, to_scale, value):
    """Convert temperature between Celsius, Fahrenheit and Kelvin"""
    from_scale = from_scale.lower()
    to_scale = to_scale.lower()
    
 
    if from_scale == 'f':
        celsius = (value - 32) * 5/9
    elif from_scale == 'k':
        celsius = value - 273.15
    else:
        celsius = value
    

    if to_scale == 'f':
        return celsius * 9/5 + 32
    elif to_scale == 'k':
        return celsius + 273.15
    else:  
        return celsius


def main():
    from_scale = None
    to_scale = None
    value = None
    
    print(len(sys.argv))
    try:
        i = 1
        while i < len(sys.argv):
            # python .\game.py --from   c   --to   f   --value   20
            #            0        1     2     3    4     5        6
            arg = sys.argv[i]
            if arg == "--from":
                from_scale = sys.argv[i+1].lower()
                if from_scale not in ['c', 'f', 'k']:
                    raise ValueError("Invalid source scale. Must be c, f, or k")
                i += 2
            elif arg == "--to":
                # python .\game.py --from   c   --to   f   --value   20
                #            0        1     2     3    4     5        6
                to_scale = sys.argv[i+1].lower()
                if to_scale not in ['c', 'f', 'k']:
                    raise ValueError("Invalid target scale. Must be c, f, or k")
                i += 2
            elif arg == "--value":
                # python .\game.py --from   c   --to   f   --value   20
                #            0        1     2     3    4     5        6
                try:
                    value = float(sys.argv[i+1])
                except ValueError:
                    raise ValueError("Temperature value must be a number")
                i += 2
            else:
                raise ValueError(f"Unknown argument: {arg}")
        
        if from_scale is None or to_scale is None or value is None:
            raise ValueError("Missing required arguments")
        
        result = convert_temperature(from_scale, to_scale, value)
        
        scale_names = {'c': 'Celsius', 'f': 'Fahrenheit', 'k': 'Kelvin'}
        print(f"\n{value:.2f}°{from_scale.upper()} "
              f"({scale_names[from_scale]}) = "
              f"{result:.2f}°{to_scale.upper()} "
              f"({scale_names[to_scale]})")
              
    except IndexError:
        print("Error: Missing argument value")
        print("Usage: python file_name.py --from f --to c --value 32")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        print("Usage: python file_name.py --from f --to c --value 32")
        sys.exit(1)


main()