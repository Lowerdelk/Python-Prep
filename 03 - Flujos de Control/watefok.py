if (input('Escribar "123" si quiere encontar un numero primo') == '123'):
    for number in range(1, 501):
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number)
            print('Quiere encontrar el proximo numero primo?')
            if (input() != '1'):
                break
