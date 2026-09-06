import student_utils
student = [{"name" : "xiaoming", "score" : 99},{"name" : "xiaoya" ,"score" :93},{"name" :"xiaomao" ,"score" :200}]
print("总分：" , student_utils.total(student))
print("平均分：" , student_utils.avg(student))
print("最高分：" , student_utils.high_score(student))