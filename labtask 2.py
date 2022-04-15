result  = ""
print("AND")
a = True
b= True
if ( a and b ):
    result = "T"
else:
    result = "F"
print("T T => ",result)

a = True
b = False
if ( a and b ):
    result = "T"
else:
    result = "F"
print("T F => ",result)

a = False
b = True
if ( a and b ):
    result = "T"
else:
    result = "F"
print("F T => ",result)

a = False
b = False
if ( a and b ):
    result = "T"
else:
    result = "F"
print("F F => ",result)
# ========================================================
print("OR")
a = True
b= True
if ( a or b ):
    result = "T"
else:
    result = "F"
print("T T => ",result)

a = True
b = False
if ( a or b ):
    result = "T"
else:
    result = "F"
print("T F => ",result)

a = False
b = True
if ( a or b ):
    result = "T"
else:
    result = "F"
print("F T => ",result)

a = False
b = False
if ( a or b ):
    result = "T"
else:
    result = "F"
print("F F => ",result)
# ========================================================
print("NAND")
a = True
b= True
if ( a and b ):
    result = "F"
else:
    result = "T"
print("T T => ",result)

a = True
b = False
if ( a and b ):
    result = "F"
else:
    result = "T"
print("T F => ",result)

a = False
b = True
if ( a and b ):
    result = "F"
else:
    result = "T"
print("F T => ",result)

a = False
b = False
if ( a and b ):
    result = "F"
else:
    result = "T"
print("F F => ",result)
# ========================================================
print("NOR")
a = True
b= True
if ( a or b ):
    result = "F"
else:
    result = "T"
print("T T => ",result)

a = True
b = False
if ( a or b ):
    result = "F"
else:
    result = "T"
print("T F => ",result)

a = False
b = True
if ( a or b ):
    result = "F"
else:
    result = "T"
print("F T => ",result)

a = False
b = False
if ( a or b ):
    result = "F"
else:
    result = "T"
print("F F => ",result)
# ========================================================