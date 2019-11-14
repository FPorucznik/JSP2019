def zamiana(rzymska, klucz={'M': 1000, 'D': 500, 'C': 100, 'L': 50, 
                                'X': 10, 'V': 5, 'I': 1}):
    liczby = []
    for i in rzymska:
        liczby.append(klucz[i]) 
    total = 0
    for num1, num2 in zip(liczby, liczby[1:]):
        if num1 >= num2:
            total += num1
        else:
            total -= num1
    print(total+num2)
    print(list(zip(liczby, liczby[1:])))

zamiana('MCCXLIV')
