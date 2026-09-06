import student_utils
class Students:
    def __init__(self,name,score):
        self.name = name 
        self.score = score
    def behave(self):
        return f"我是： {self.name} 分数: {self.score}"
    def is_pass(self):
        if self.score >= 60:
            return "pass"
        else:
            return "not pass"
s1 = Students("yqh",99)
s2 = Students("ywh",55)
print(s1.behave() , s1.is_pass())
print(s2.behave() , s2.is_pass())
print(s1.name, s1.score, s1.is_pass())
print(s2.name, s2.score, s2.is_pass())
# student = [{"name" : "xiaoming", "score" : 99},{"name" : "xiaoya" ,"score" :93},{"name" :"xiaomao" ,"score" :200}]
# print("总分：" , student_utils.total(student))
# print("平均分：" , student_utils.avg(student))
# print("最高分：" , student_utils.high_score(student))