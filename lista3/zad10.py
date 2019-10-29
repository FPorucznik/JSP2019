liczby=[]
for i in range(100,401):
    testowana=str(i)
    if((int(testowana[0])%2==0) and (int(testowana[1])%2==0)and (int(testowana[2])%2==0)):
        liczby.append(testowana)
print(",".join(liczby))