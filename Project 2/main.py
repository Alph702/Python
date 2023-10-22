class Question:
    def __init__(self, Questions: list[str]) -> None:
        self.questions = Questions

    def DisplayAvailableQuestions(self):
        print("The questions in this quiz is:")
        i = 0
        for Questions in self.questions:
            print(f"{i}. {Questions}")
            i += 1

    def AnsQ(self, ans, index, Q_Num):
        self.a = input("Ans of a question in [Y/n]: ")

        if Q_Num == index:
            if ans == self.a.upper():
                print("win.. win .. win..")
            else:
                print("wrong ans")

        else:
            print("Invalid input")


def main():
    Questions = [
        "Am I your friend?",
        "Is this a good restaurant?",
        "Are these islands Greek?",
        "Was his idea interesting?",
    ]

    
    Question(Questions=Questions).DisplayAvailableQuestions()

    q_Num = int(input("Enter a number of a question(Number of 1 question is 0): "))
    if q_Num == 0:
        Question(Questions=Questions).AnsQ("Y", 0, q_Num)
    elif q_Num == 1:
        Question(Questions=Questions).AnsQ("N", 0, q_Num)
    elif q_Num == 2:
        Question(Questions=Questions).AnsQ("Y", 0, q_Num)
    elif q_Num == 3:
        Question(Questions=Questions).AnsQ("N", 0, q_Num)

    else:
        print("Invalid input")

if __name__ == '__main__':
    main()
