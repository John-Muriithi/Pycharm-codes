def netsalaryfunc():
    print("\nENTER THE EMPLOYEE'S PARTICULARS AS ASKED")
    name = str(input("\nProvide the employee's name"))
    id_no = int(input("provide the employee's ID NUMBER"))
    salary = eval(input("provide the employee's salary"))
    electricity = eval(input("provide the employee's electricity bill"))
    NHIF = 500
    NSSF = 500
    if salary > 0 and salary < 15000:
        tax = 0
    elif salary > 15000 and salary < 50000:
        tax = 0.1*salary
    elif salary > 50000 and salary < 100000:
        tax = 0.15*salary
    else:
        tax = 0.2*salary
    total_deductions = NHIF+NSSF+electricity
    net_salary = salary - (total_deductions+tax)
    print("\n*************************************")
    print("\nNAME:",name,"\nID NUMBER:",id_no,"\nSALARY: KSh.",salary,"\nDEDUCTIONS:\tNHIF: KSh.",NHIF,"\n\t\t\tNSSF: KSh.",NSSF,
          "\n\t\t\tELECTRICITY BILL: KSh.",electricity,"\n\t\t\t==============================","\n\t\t\tTOTAL DEDUCTIONS: KSh.",
          total_deductions,"\n\nTAX: KSh.",tax,"\n____________________________\n\nNET SALARY: KSh.",net_salary,"\n____________________________")
    return;