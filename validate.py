
def validate_plate(plate):
    check = False
    rplate = str(plate).replace(" ","")
    if len(rplate) <= 10 and len(rplate) >= 8:
        first_plate = rplate[0:2]
        second_plate = rplate[2:3]
        thirdth_plate = rplate[4:]
        #format theo biển số HCM
        if first_plate.isdigit() and thirdth_plate.isdigit() and int(first_plate) >= 50 and int(first_plate) <= 59 and second_plate.isalpha():
                check = True
    return check
