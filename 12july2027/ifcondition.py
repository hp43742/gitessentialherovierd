#conditional statements
x=100
if x > 10:
    print("x is greater than 10")
else:
    print("x is not greater than 10")

age = 10

if age >= 0 and age <= 17:
    print("Minor")
elif age >= 18 and age < 60:
    print("Adult")
elif age >= 60:
    print("Senior Citizen")
else:
    print("Invalid Age")


    #age >18 ,cibil >= 700,MAB>5000 ,eligible ofr loan

    age =17.9
    Cibil_score= 750
    MAB= 10000
    Ac_balance= 30000

    if age > 18:
        print("Eligible for loan")
    if Cibil_score >= 700:
        print("cibil criteria pass")
    else:
        print("cibil criteria fails")
    if MAB > 5000:
        print("Eligible for loan")
    elif Ac_balance > 10000:
        print("Eligible for loan")
    else:
        print("Not Eligible for loan")  