import tools
student = [{"name" : "xiaoming", "score" : 99},{"name" : "xiaoya" ,"score" :93},{"name" :"xiaomao" ,"score" :200}]
print("总分：" , tools.total(student))
print("平均分：" , tools.avg(student))
print("最高分：" , tools.high_score(student))