
def total(student):
    zong = 0
    for s in student:
        zong = zong+ s["score"]
    return zong
def avg(student):
    pj = total(student) /len(student)
    return pj
def high_score(student):
     highest = 0
     for s in student:
          if s["score"] > highest:
             highest = s["score"]
     return highest