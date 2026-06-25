
positive_count = 0
negative_count = 0
neutral_count = 0

risk_words_found = []
positive_words_found = []

while True:
    question = input("Give me an interview question: ")

    words = question.lower().split()

#Find more research backed words 
#EEOC - Questions that are considered illegal 
    positive_words = ["resourceful", "objective", "collaboration", "numbers", "leadership", "yourself", "experience", "goals", "skills"]
    negative_words = ["emotion", "sensitive", "provider", "balance", "children", "bossy", "retiring", "pregnant", "child", "divorced", "spouse", "accent"]
    nuetral_words = [""]


    for i in words:
        i = i.strip(".,?!,-,:/")

        if i in positive_words:
            positive_count += 1
            positive_words_found.append(i)
        elif i in negative_words:
            negative_count += 1
            risk_words_found.append(i)
            #print("Possible risk question")
        else:
            neutral_count += 1

    total_count = positive_count + negative_count + neutral_count

    if question.lower() == "exit":
        print("Analysis Done: ")
        break 


print("\n---- Interview Analysis Summary ----")

print(f"Positive Words: {positive_count}")
print("Positive Words found:", " ," .join(positive_words_found))

print(f"Negative Words: {negative_count}")
if negative_count > 0:
    print(f" ⚠️   Flagged Risk - Word Count {negative_count}")
    print("Risk Words Found: ", ", ".join(risk_words_found) )

print(f"Neutral Words: {neutral_count}")


#Update percentages 

if negative_count >= 4:
        print("Overall Result: High Risk")
elif negative_count >= 1:
        print("Overall Result: Moderate Risk")
else:
     print("Overall Risk: Strong Interview")





