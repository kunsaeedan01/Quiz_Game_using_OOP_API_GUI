from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain ):
        self.quiz = quiz_brain
        # Window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Label
        self.score = Label(text="Score:0", bg=THEME_COLOR, fg="white", font=("Arial", 15, "italic"))
        self.score.grid(column=1, row=0)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas_text = self.canvas.create_text(150, 125, width=280, text="Some text", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Buttons
        checkmark_img = PhotoImage(file="images/true.png")
        cross_img = PhotoImage(file="images/false.png")
        self.checkmark = Button(image=checkmark_img, highlightthickness=0, command=self.checkmark_pressed)
        self.checkmark.grid(column=0, row=2)
        self.cross = Button(image=cross_img, highlightthickness=0, command=self.cross_pressed)
        self.cross.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="You've reached the end of the quiz")
            self.checkmark.config(state="disabled")
            self.cross.config(state="disabled")
    def checkmark_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def cross_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)