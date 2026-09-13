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
