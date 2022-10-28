weight = int(input('Weight: ')) ## Alawys the input method returns string
# so to do mathematical operations convert the strint to int
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f'You are {converted} kilos')
else:
    converted = weight / 0.45
    print(f'You are {converted} pounds')