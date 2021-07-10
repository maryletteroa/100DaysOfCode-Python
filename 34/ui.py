from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
PADDING = 20
FONT = ("Arial", 15, "italic")
HEIGHT = 250
WIDTH = 300

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=PADDING, pady=PADDING, bg=THEME_COLOR)

        # score
        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)


        # questions
        self.canvas = Canvas(width=WIDTH, height=HEIGHT, bg="white")
        self.question_text = self.canvas.create_text(
            WIDTH/2, 
            HEIGHT/2, 
            width=WIDTH-20, #wrap the text
            text="Some Question Text", 
            fill=THEME_COLOR, 
            font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=PADDING)

        # buttons
        true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(
            image=true_img, 
            highlightthickness=0,
            command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(
            image=false_img, 
            highlightthickness=0,
            command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)