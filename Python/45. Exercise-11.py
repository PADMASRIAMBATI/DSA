# Shipping Labels

def shipping_labels(*args,**kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    #for key, value in kwargs.items():
    #   print(f"{key:6}: {value}")
    #print()
#    or
    if "apt" in kwargs:
        print(f"{kwargs.get('street')}, {kwargs.get('Dno')}, {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}, {kwargs.get('Dno')}")
    print(f"{kwargs.get('city')}, {kwargs.get('zip')}")

shipping_labels("MS.", "Padmasri", "Ambati", "(Sweety)",
                street="Ramalayam Veedhi",
                Dno="22-2-9",
                city="Peddapuram",
                zip="533437")