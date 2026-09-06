def high_score():
     highest = 0
     for s in student:
          if int(s["score"]) > highest:
             highest = s["score"]
     return highest
student = [{"name" : "xiaoming", "score" : 99},{"name" : "xiaoya" ,"score" :93},{"name" :"xiaomao" ,"score" :200}]
sum = 0
for s in student:
    sum = sum + s["score"]
avg = sum / len(student)
print(sum)
print(avg)
print(high_score())    
