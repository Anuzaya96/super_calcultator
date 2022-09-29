num_1 = int(input("Įveskite pirma skaičių: "))
num_2 = int(input("Įveskite antrą skaičių: "))
veiksmas = input("ka daryti?")
if veiksmas == "+":
    print(f"Suma: {num_1+num_2} ")
elif veiksmas == "-":
    print(f"Skirtumas: {num_1-num_2} ")
elif veiksmas == "*":
    print(f"Daugyba: {num_1*num_2} ")
elif veiksmas == "/":
    if num_2 == 0:
        print("dalyba is 0 negalima")
    else:
        print(f"Dalyba: {num_1/num_2} ")
else: 
    print("operacija neatpazinta")