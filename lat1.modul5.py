scores_list = []

while True:
    grade_input = input("Masukkan nilai (tekan Enter untuk menghentikan): ")
    
    if grade_input == "":
        break
    
    try:
        score = float(grade_input)
        if score == 4.00:
            grade = 'A'
        elif score > 3.75 and score < 4.00:
            grade = 'A-'
        elif score > 3.50 and score <= 3.75:
            grade = 'B+'
        elif score == 3.00:
            grade = 'B'
        elif score > 2.75 and score < 3.00:
            grade = 'B-'
        elif score > 2.50 and score <= 2.75:
            grade = 'C+'
        elif score == 2.00:
            grade = 'C'
        elif score > 1.75 and score < 2.00:
            grade = 'C-'
        elif score > 1.50 and score <= 1.75:
            grade = 'D'
        else:
            grade = 'E'

        scores_list.append(score)
        print(f"Score: {score}, Grade: {grade}")
    except ValueError:
        print(f"Nilai {grade_input} tidak valid.")

if scores_list:
    average_score = sum(scores_list) / len(scores_list)
    if average_score == 4.00:
        average_grade = 'A'
    elif average_score > 3.75 and average_score < 4.00:
        average_grade = 'A-'
    elif average_score > 3.50 and average_score <= 3.75:
        average_grade = 'B+'
    elif average_score == 3.00:
        average_grade = 'B'
    elif average_score > 2.75 and average_score < 3.00:
        average_grade = 'B-'
    elif average_score > 2.50 and average_score <= 2.75:
        average_grade = 'C+'
    elif average_score == 2.00:
        average_grade = 'C'
    elif average_score > 1.75 and average_score < 2.00:
        average_grade = 'C-'
    elif average_score > 1.50 and average_score <= 1.75:
        average_grade = 'D'
    else:
        average_grade = 'E'

    print(f"Rata-rata skor: {average_score:.2f}, Grade: {average_grade}")
else:
    print("Tidak ada nilai yang dimasukkan.")
