def add(a , b):
    return a + b
def hi(name):
    return "hi  " + name
def total(student):
    total = 0
    for s in student:
        total = total+ s["score"]
    return total
def avg(student):
    avg = total(student) /len(student)
    return avg
def high_score(student):
     highest = 0
     for s in student:
          if s["score"] > highest:
             highest = s["score"]
     return highest