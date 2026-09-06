def high_score():
     highest = 0
     for s in student:
          if s["score"] > highest:
             highest = s["score"]
     return highest
student = [{"name" : "xiaoming", "score" : 99},{"name" : "xiaoya" ,"score" :93},{"name" :"xiaomao" ,"score" :200}]
total = 0
for s in student:
    total = total+ s["score"]
avg = total / len(student)
print(total)
print(avg)
print(high_score())    
