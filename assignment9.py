#2 / 3 + 4/5 = (2*5) + (4*3)/ (3*5)

def sum(x, y):
    result = {}
    result["s"] = (x["s"]* y["m"]) + (y["s"] * x["m"])
    result["m"] = x["m"] * y["m"]
    return result


def multiplay(x , y):
    result = {}
    result["s"] = x["s"] * y["s"]
    result["m"] = x["m"] * y["m"]
    return result

def subtraction(x, y):
    result = {}
    result["s"] = (x["s"]* y["m"]) - (y["s"] * x["m"])
    result["m"] = x["m"] * y["m"]
    return result


def division(x , y): 
    result = {}
    result["s"] = x["s"] * y["m"]
    result["m"] = x["m"] * y["s"]
    return result


def show(r):
    print(f"{r['s']} / {r['m']}")

f1 = {"s": 2, "m": 3}
f2 = {"s": 5, "m": 4}

result_s = sum(f1, f2)
show(result_s)

result_m = multiplay(f1 , f2)
show(result_m)

result_su = subtraction(f1 , f2)
show(result_su)

result_d = division(f1, f2)
show(result_d)
