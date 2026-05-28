from tkinter import *


class StartQUiz:
    """
    Initial Game interface (asks users how many rounds they
    would like to play)
    """

    def __init__(self):
        """
        Gets number of rounds from user
        """

        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Create play button...
        self.play_button = Button(self.start_frame, font=("Arial", 16, "bold"),
                                  fg="#FFFFFF", bg="#0057D8", text="Play", width=10,
                                  command=self.check_rounds)
        self.play_button.grid(row=0, column=1)

    def check_rounds(self):
        """
        Checks users have entered 1 or more rounds
        """

        Difficulty(5)
        # Hide root window (ie: hide rounds choice window).
        root.withdraw()

class Difficulty:
    """
    Choose difficulty window, this is where the user will choose
    a difficultly after they have entered in
    how many questions they want to answer.
    """

    def __init__(self, how_many):
        self.how_many = how_many
        #This is the frame and whole configure for the whole GUI
        self.difficulty_box = Toplevel()
        #TITLe
        self.difficulty_box.title("Choose Difficulty")
        self.difficulty_box.geometry("328x326")
        self.difficulty_box.resizable(False, False)
        self.difficulty_box.configure(bg="#b8c7cf")

        # Added color to frame, and made the pack fill in.

        self.difficulty_frame = Frame(
            self.difficulty_box,bg="#b8c7cf")
        self.difficulty_frame.pack(fill=BOTH, expand=True)

        # the heading label for the Difficult GUI
        self.heading_label = Label(
            self.difficulty_frame, text="Choose your difficulty", font=("Arial", 18, "bold"),
            bg="#b8c7cf", fg="black")
        self.heading_label.pack(pady=(0, 22))
        # simple config for button fonts
        button_font = ("Arial", 11, "bold")

        # The first button made which has an active button and when click the button slightly will change its colors
        self.easy_button = Button(self.difficulty_frame, text="Easy", font=button_font, bg="#4caf0b",fg="white",
            activebackground="#3f9409",activeforeground="white",width=10,height=2,bd=1,
            relief="solid")
        self.easy_button.pack(pady=(0, 29))

        # Normal button with basically the same features but different colors
        self.normal_button = Button(self.difficulty_frame,text="Normal",font=button_font,bg="#e6cf00",fg="white",
            activebackground="#c9b600",activeforeground="white",width=10,height=2,bd=1,relief="solid",)
        self.normal_button.pack(pady=(0, 29))

        # Hard Mode added the same way
        self.hard_button = Button(self.difficulty_frame,text="Hard",font=button_font,bg="#f51f14",fg="white",
            activebackground="#d71910",activeforeground="white",width=10,
            height=2,bd=1, relief="solid",)
        self.hard_button.pack(pady=(0, 15))

        # Disclaimer button added too
        self.disclaimer_button = Button(self.difficulty_frame,text="Disclaimer Difficulty",font=button_font,bg="#0059e8",
            fg="white", activebackground="#0049bd",activeforeground="white",width=20,
            height=2,bd=1,relief="solid",)
        self.disclaimer_button.pack()


# THE main routine starts here
if __name__ == "__main__":
    root = Tk ()
    root.title("Difficulty")
    StartQUiz()
    root.mainloop()


