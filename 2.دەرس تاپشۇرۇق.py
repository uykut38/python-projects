#name = input(":ئىسمىڭىزنى كىرگۈزۈڭ")
#age = int(input("يېشىڭىزنى كىرگۈزۈڭ:"))
#height = float(input("بوي ئېگىزلىكىڭىزنى كىرگۈزۈڭ(cm):"))
#study_hours = float(input("بىر كۈندە قانچە سائەت ئوقۇيسىز؟"))

#print(name,"ئىسمىڭىز:")
#print("يېشىڭىز:",age)
#print("بوي ئېگىزلىكىڭىز",height,"cm")
#print("بىركۈندە ئوقۇش ۋاقتىڭىز",study_hours,"سائەت")

score = int(input("ئىمتىھان نۇمۇرنى كىرگۈزۈڭ:"))
if score < 0 or score > 100:
    print("invalid score")
elif score >= 90:
    print("excellent")
elif score >= 80:
    print("very good")
elif score >= 70:
    print("good")
elif score >= 60:
    print("pass")
else:
    print("fail")
