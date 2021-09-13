print("help!my tv doesnt work")
done=False
while not done:
    print("is the decoder powering on?")
    choice=input("(y/n)")
    if choice=='y':
        print("1.scanning\n2.not scanning?")
        choice=int( input("1 or 2"))
        if choice=='1':
            print("wait")
        else:
                print("reboot")
    else:
        print("please contact a technician")
        done=True


