nice=85
good=70
jige=60
score=[88, 92, 79, 95, 60, 73, 100, 45, 81, 67]
population=len(score)
print("人数:%d"%population)
max_score=max(score)
print("最高分:%d"%max_score)
min_score=min(score)
print("最低分:%d"%min_score)
avg_score=round(sum(score)/len(score),2)
print("平均分:%.2f"%avg_score)
extream_score=max_score - min_score
print("极差:%d"%extream_score)
if avg_score>=nice:
    print("优秀")
elif avg_score>=good:
    print("良好")
elif avg_score>=jige:
    print("及格")
else:
    print("需要补课")
per_extscore=((max_score-min_score)/min_score)*100
print("百分比%.2f%%"%per_extscore)
s=0
for i in score:
    if i>=jige:
        s+=1
print(f"及格人数:{s}人")
print(f"及格率:{((s/population)*100):.2f}%")
n=0
for i in score:
    if i>=90:
        n+=1
print(f"90分以上人数为{n}")
max_score1=score[0]
for i in score:
    if i>max_score1:
        max_score1=i
print(max_score1)


