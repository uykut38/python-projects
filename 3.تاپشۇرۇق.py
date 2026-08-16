
name = input("ئىسمىڭىز نىمە؟")
balance = 1000
print(f",ياخشىمۇسىز؟{name}")
print(f"سىزنىڭ ھېساباتىڭىزدىكى خامچوتىڭىز بولسا${balance}")
amount = float(input("سىزنەچچەپۇل ئامماقچى ؟"))
if amount <= 0:
    print("invalid amount!")
elif amount > balance:
    print("insufficient balance")
else:
    balance =balance - amount
    print(f"سىزنىڭ قېپ قالغان خامچوتىڭىز بولسا${balance}")
if balance >500:
    print("your balance is healthy")
elif balance >=100:
    print("be careful with your spending")
else:
    print("your balance low!")
