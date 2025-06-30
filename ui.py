from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class UserInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Test your knowledge.")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white", font=("Arial", 10, "bold"))
        self.score_label.grid(column=1, row=0, padx=20, pady=20)

        self.question_canvas = Canvas(width=300, height=250)
        self.question_text = self.question_canvas.create_text(150, 125, width=280, text="question from data", font=FONT)
        self.question_canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        self.true_button = Button()
        self.true_photo = PhotoImage(file="images/true.png", width=100, height=97)
        self.true_button.config(image=self.true_photo, highlightthickness=0, command=self.pressed_true)
        self.true_button.grid(row=2, column=0, padx=20, pady=20)

        self.false_button = Button()
        self.false_photo = PhotoImage(file="images/false.png", width=100, height=97)
        self.false_button.config(image=self.false_photo, highlightthickness=0, command=self.pressed_false)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.question_canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.question_canvas.itemconfig(self.question_text, text="That was the last question")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.question_canvas.config(bg="white")

    def pressed_true(self):
        is_correct = self.quiz.check_answer("True")
        self.feedback(is_correct)

    def pressed_false(self):
        is_correct = self.quiz.check_answer("False")
        self.feedback(is_correct)

    def feedback(self, is_correct):
        if is_correct:
            self.question_canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.question_canvas.config(bg="red")

        self.window.after(1000, func=self.get_next_question)




