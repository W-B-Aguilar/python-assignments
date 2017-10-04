variables = {"sI": 45, "mI": 100, "bI": 455, "eI": 0, "spI": -23, "sS": "Rubber baby buggy bumpers", "mS": "Experience is simply the name we give our mistakes", "bS": "Tell me and I forget. Teach me and I remember. Involve me and I learn.", "eS": "", "aL": [1,7,4,21], "mL": [3,5,7,34,3,2,113,65,8,89], "lL": [4,34,22,68,9,13,3,5,7,9,2,12,45,923], "eL": [], "spL": ['name','address','phone number','social security number']}

for i in variables:
    if type(variables[i]) == int:
        if variables[i] > 100:
            print "{} is a big number".format(i)
        elif variables[i] < 100:
            print "{} is a small number".format(i)
    elif type(variables[i]) == str:
        if len(variables[i]) > 50:
            print "{} is a long sentance".format(i)
        elif len(variables[i]) < 50:
            print "{} is a short sentance".format(i)
    elif type(variables[i]) == list :
        if len(variables[i]) > 10:
            print "{} is a big list".format(i)
        elif len(variables[i]) < 10:
            print "{} is a small list".format(i)