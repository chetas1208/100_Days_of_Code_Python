total=int(input("Total bill amount: "))
tip=int(input("Tip percentage: "))
people=int(input("Number of people: "))
tip_amount=(total*tip)/100
total_amount=total+tip_amount
amount_per_person=total_amount/people
print(f"Each person should pay: {amount_per_person}")