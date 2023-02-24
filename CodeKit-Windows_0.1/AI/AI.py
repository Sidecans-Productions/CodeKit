def runAI(lins):
    for x in range(len(lins) + 1):
        y = x-1
        checkData(lins[y])

def checkData(lin):
    if "print" in lin:
        print(lin + " | Function Found | Print - 01")

    elif "var" in lin:
        print(lin + " | Function Found | Variable - 02")

    elif "if" in lin:
        print(lin + " | Function Found | If Statement - 03")

    elif "int" in lin:
        print(lin + " | Function Found | Integer Data Type - 05")

    elif "str" in lin:
        print(lin + " | Function Found | String Data Type - 06")

    elif "bool" in lin:
        print(lin + " | Function Found | Boolean Data Type - 07")

    elif "dict" in lin:
        print(lin + " | Function Found | Dictionary - 08")

    elif "del" in lin:
        print(lin + " | Function Found | Deletion - 10")

    elif "elif" in lin or "else if" in lin:
        print(lin + " | Function Found | Else If Function - 11")

    elif "func" in lin or "function" in lin or "def" in lin:
        print(lin + " | Function Found | Function Statement - 12")

    elif "while" in lin:
        print(lin +  " | Function Found | Function Statement - 13")

    elif "for" in lin:
        print(lin + " | Function Found | For Statement - 14")
 

