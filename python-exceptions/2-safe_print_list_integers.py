def safe_print_list_integers(my_list=[], x=0):
    inex = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            inex += 1
        except ValueError:
            continue
        except TypeError:
            continue
    print()
    return inex
