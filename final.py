def start():
    print("")
    print("█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█   ▄▀█ █░░ █ █▄█ ▄▀█ █░█ ▀ █▀   █░█ █▀▀ █▄░█ █▀▄ █ █▄░█ █▀▀   █▀▄▀█ ▄▀█ █▀▀ █░█ █ █▄░█ █▀▀")
    print("▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█   █▀█ █▄▄ █ ░█░ █▀█ █▀█ ░ ▄█   ▀▄▀ ██▄ █░▀█ █▄▀ █ █░▀█ █▄█   █░▀░█ █▀█ █▄▄ █▀█ █ █░▀█ ██▄")
    print ("")
    cost1 =float(2.50)
    cost2 =float(4.50)
    cost3 =float(3.99)
    cost4 =float(4.50)
    cost5 =float(3.66)
    cost6 =float(5.57)
    cost7 =float(3.42)
    cost8 =float(4.23)
    cost9 =float(7.99)
    cost10 =float(8.50)
    cost11 =float(2.50)
    cost12 =float(6.50)
    cost13 =float(3.99)
    cost14 =float(5.99)
    cost15 =float(1.50)
    
    print ("")
    print("███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗")
    print("████╗░████║██╔════╝████╗░██║██║░░░██║")
    print("██╔████╔██║█████╗░░██╔██╗██║██║░░░██║")
    print("██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║")
    print("██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝")
    print("╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░")
    print ("")
    print("press 1 for Pepsi")
    print("press 2 for Pineapple juice")
    print("press 3 for Coconut juice")
    print("press 4 for Doritos")
    print("press 5 for Lays")
    print("press 6 for Cheetos")
    print("press 7 for Kitkat")
    print("press 8 for Snickers")
    print("press 9 for Reeses")
    print("press 10 for Brownie")
    print("press 11 for Oreo")
    print("press 12 for Pepero sticks")
    print("press 13 for Cookie")
    print("press 14 for Pretzels")
    print("press 15 for Salted nuts")
    print("")
    print             ("█▀▀ █▄░█ ▀█▀ █▀▀ █▀█   █▄█ █▀█ █░█ █▀█   █▀▄▀█ █▀█ █▄░█ █▀▀ █▄█")
    bank = float(input("██▄ █░▀█ ░█░ ██▄ █▀▄   ░█░ █▄█ █▄█ █▀▄   █░▀░█ █▄█ █░▀█ ██▄ ░█░ "))
    print("")
    while bank > 8.50:
        print                   ("█▀ █▀▀ █░░ █▀▀ █▀▀ ▀█▀   █▄█ █▀█ █░█ █▀█   █▀█ █▀█ █▀▄ █▀▀ █▀█")
        order_option = int(input("▄█ ██▄ █▄▄ ██▄ █▄▄ ░█░   ░█░ █▄█ █▄█ █▀▄   █▄█ █▀▄ █▄▀ ██▄ █▀▄ "))
        if bank < 8.50:
                print ("your money is not enough")
                break
        if order_option == 1:
                print("You picked Pepsi, your change is", bank - cost1)
                break
        if order_option == 2:
                print("You picked Pineapple juice, your change is", bank - cost2)
                break
        if order_option == 3:
                print("You picked Coconut juice, your change is", bank - cost3)
                break
        if order_option == 4:
                print("You picked Doritos, your change is", bank - cost4)
                break
        if order_option == 5:
                print("You picked Lays, your change is", bank - cost5)
                break
        if order_option == 6:
                print("You picked Cheetos, your change is", bank - cost6)
                break
        if order_option == 7:
                print("You picked Kitkat, your change is", bank - cost7)
                break
        if order_option == 8:
                print("You picked Snickers, your change is", bank - cost8)
                break
        if order_option == 9:
                print("You picked Reeses, your change is", bank - cost9)
                break
        if order_option == 10:
                print("You picked Brownie, your change is", bank - cost10)
                break
        if order_option == 11:
                print("You picked Oreo, your change is", bank - cost11)
                break
        if order_option == 12:
                print("You picked Pepero sticks, your change is", bank - cost12)
                break
        if order_option == 13:
                print("You picked Cookie, your change is", bank - cost13)
                break
        if order_option == 14:
                print("You picked Pretzels, your change is", bank - cost14)
                break
        if order_option == 15:
                print("You picked Salted nuts, your change is", bank - cost15)
                break
    repeat = input("Press 0 if you would you like to restart again ".lower())
    if repeat == "0":
            start()
    else:
            print("Goodbye")
    exit()
start()