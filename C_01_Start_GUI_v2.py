from tkinter import *
from functools import partial # To prevent unwanted windows

class StartQuiz:

    """
    This is the initial quiz Gui the start gui
    """
    def __init__(self):
        """
        Gets number of question the users wants to answer
        """

        background = "#DAE8FC"
        self.start_frame = Frame(padx=70, pady=60)
        self.start_frame.grid()

        # MAKE THIS INTRO STRING IN ONE PARAGRAPH==-=-=
        introduction_string = ("History is not just a collection of dates"
        "it is a tapestry woven by the ambition, genius, and courage of individuals." 
        "From empire-builders to revolution-starters, the past is shaped by those who dared to act." 
        "Welcome to the Icons of History quiz. Can you identify the faces that changed the world?")

        #choose_string = "Oops - Please choose a whole number more than zero."
        choose_string = "how many questions do you want to answer?"
        second_introduction_string = "In this game you are given a question/clue about a certain figure, and you are to answer, which depends on the difficulty you chose."
        # List of labels to be made (text| font |fg)
        start_labels_list = [
            ["This is a Quiz about Historical Figures", ("Arial", 15, "bold"), None],
            [introduction_string, ("Arial", 12), None],
            [second_introduction_string, ("Arial", 12), None],
            [choose_string, ("Arial", 12, "bold"), "#000000"]
        ]

        # Create labels and add them to the reference list...

        start_label_ref = []
        for count, item in enumerate(start_labels_list):
            make_label = Label(self.start_frame, text=item[0], font=item[1],
                               fg=item[2],
                               wraplength=500, justify="left", pady=10, padx=20, border=10)
            make_label.grid(row=count)

            start_label_ref.append(make_label)

        # extract choice label so that it can be changed to an
        # error message if necessary.

        self.introduction = start_label_ref[0]
        self.introduction_2 = start_label_ref[1]
        self.choose_label = start_label_ref[2]
        self.chose_string_label = start_label_ref[3]


        self.num_rounds_entry = Entry(self.start_frame, font=("Arial", 20, "bold"),
                                      width=10)
        self.num_rounds_entry.grid(row=4, column=0, padx=10, pady=10)

        # Create play button ...
        self.play_button = Button(self.start_frame, font=("Arial", 16, "bold"),
                                  fg="#FFFFFF", bg="#fcbe03", text="Play", width=10,
                                  command=self.check_rounds)
        self.play_button.grid(row=5, column=0)
        # self.play_button.place(x=100, y=50)
        # self.play_button.pack (padx=10, pady=10)

        recolour_list = [self.introduction, self.introduction_2, self.choose_label, self.start_frame, self.chose_string_label]

        for item in recolour_list:
            item.config(bg=background)




    def check_rounds(self):
        """
        Checks users have entered 1 0r more rounds
        """

        # Retrieve temperature to be converted
        questions_wanted = self.num_rounds_entry.get()

        # Reset label and entry box (for when users come back to home screen)
        self.choose_label.config(fg="#DAE8FC", font=("Arial", "12", "bold"))
        self.num_rounds_entry.config(bg="#DAE8FC")

        error = "Pick a number.. That est not Null ZERO"
        has_errors = "no"

        # Checks that amount to be converted is a number above absolute zero
        try:
            questions_wanted = int(questions_wanted)
            if questions_wanted > 0:
                print("you want more than zero questions")
                # temporary success message, replace with call to PlayGame class
                self.choose_label.config(text=f"You have chosen to answer {questions_wanted} questions")
            else:
                has_errors = "yes"

        except ValueError:
            has_errors = "yes"

        # display the error if necessary
        if has_errors == "yes":
            self.choose_label.config(text=error, fg="#990000",
                                     font=("Arial", 10, "bold"))
            self.num_rounds_entry.config(bg="#F4CCCC")
            self.num_rounds_entry.delete(0, END)



# main routine
if __name__ == "__main__":
    root = Tk ()
    root.title("Historical Figures")
    StartQuiz()
    root.mainloop()

