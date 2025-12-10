def cel_to_far(value,temp):
    match value:
        case 'C':
            Far = ((9*temp)/5)+32
            return ("Fareheit value for", temp ,"degree celcius in farenheit is", Far)
        case 'F':
            Cel = ((temp-32)/9)*5
            return ("Celcius value for", temp ,"degree farenheit in celcius is", Cel)

degree = int(input("Enter the temperature:"))
value_in = input("Enter 'C' if your entered value is celcius and enter 'F' if its farenheit")
result = cel_to_far(value_in, degree)

print(result)
