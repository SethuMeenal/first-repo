def process_scores():
    stu_score = {'Sethu':[90,80,70,54], 'Dinesh':[12,99,34,80,4,28]}
    print(f"raw score dict taken is as follows: {stu_score}")
    average_score = dict()
    for stu_scores in stu_score:
        total = 0
        total = sum(stu_score[stu_scores])
        if (total > 0):
            average = total / len(stu_score[stu_scores])
        else:
            average = 0
        average_score[stu_scores] = round(average,2)
    return average_score
def classify_grades(average_score):
    graded = dict()
    for score in average_score:
        if average_score[score] >= 90:
            grade = 'A'
        elif (average_score[score] >= 75 and average_score[score] < 89):
            grade = 'B'
        elif (average_score[score] >= 60 and average_score[score] <= 74):
            grade = 'C'
        elif (average_score[score] < 60):
            grade = 'F'
        graded[score] = (round(average_score[score],2),grade)
    return graded
def generate_report(classified,passing_avg = 70):
    print(f"==== Student grade report ====")
    pass_cnt = 0
    for score in classified:
        if classified[score][0] >= passing_avg:
            status = 'PASS'
            pass_cnt+=1;
        else:
            status = 'FAIL'
        print(f"{score} | Avg: {classified[score][0]} | Grade: {classified[score][1]} | Status: {status}")
    print(f"=========================")
    print(f"Total students : {len(classified)}")
    print(f"Passed: {pass_cnt}")
    print(f"Failed: {(len(classified)-pass_cnt)}")
average_score = process_scores()
print(f"average score dict is as follows: {average_score}")
graded = classify_grades(average_score)
print(f"graded score dict is as follows: {graded}")
generate_report(graded)
