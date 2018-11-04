import sys

def calculateChange(price, payment):
    change = []
    change_to_give = payment - price
    d = [(100,'ONE HUNDRED'),(50,'FIFTY'),(20,'TWENTY'),(10,'TEN'),(5,'FIVE'),(2,'TWO'),(1,'ONE'),(0.5,'HALF DOLLAR'),(0.25,'QUARTER'),(0.1,'DIME'),(0.05,'NICKEL'),(0.01,'PENNY')]
    entry = 0
    while entry<len(d):
        if(d[entry][0]<=change_to_give):
            change_to_give=change_to_give-d[entry][0]
            change.append(d[entry][1])
        else:
            entry = entry + 1
    return change

for line in sys.stdin:
    change = []
    line_split = line.split(';')
    price_input = float(line_split[0])
    payment_input = float(line_split[1])
    
    if payment_input < price_input:
        change.append("ERROR")
    elif payment_input == price_input:
        change.append("ZERO")
    else:
        change = calculateChange(price_input, payment_input)
    
    change_output = ",".join(change)
    print change_output