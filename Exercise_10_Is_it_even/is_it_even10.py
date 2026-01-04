def even_or_odd(n):
    if n % 2 == 0:
        return "it is a even number"
    else:
        return "it is a odd number"
def the_main():
    number = int(input("please enter a number: "))
    result = even_or_odd(number)
    print(result)
the_main()