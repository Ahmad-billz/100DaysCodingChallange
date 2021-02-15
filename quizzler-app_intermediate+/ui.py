from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain : QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler ")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=400, height=300, highlightthickness=0)
        self.question_text = self.canvas.create_text(
            200,
            150,
            width=370,
            text="Hello from UI",
            fill=THEME_COLOR,
            font=("Courier", 16, 'italic')
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score_lb = Label(font=("Courier", 11), text='Score: ', bg=THEME_COLOR, fg='white')
        self.score_lb.grid(column=1, row=0)

        right_img = PhotoImage(file="images/true.png")
        self.right_btn = Button(image=right_img, highlightthickness=0, borderwidth=0, command=self.true_pressed)
        self.right_btn.grid(column=0, row=2)
        wrong_img = PhotoImage(file="images/false.png")
        self.wrong_btn = Button(image=wrong_img, highlightthickness=0, bd=0, command= self.false_pressed)
        self.wrong_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.right_btn.config(state="normal")
        self.wrong_btn.config(state="normal")
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.right_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.right_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")
            self.canvas.config(bg='green')
            self.score_lb.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg='red')
            self.right_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")
        self.window.after(1000, self.get_next_question)
