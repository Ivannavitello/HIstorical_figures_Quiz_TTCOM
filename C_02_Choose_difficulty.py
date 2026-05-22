from tkinter import *


class Difficulty:
    """THis will be the difficulty widget with buttons
     that will lead to different functions/difficulty"""


    def __init__(self):


        self.difficulty_frame = Frame(padx=30, pady=200)
        self.difficulty_frame.grid()
        self.difficulty_frame.config(wraplength=350, justify="left", pady=10, padx=20)


        # start_label_ref = []
        # for count, item in enumerate(start_labels_list):
        #     make_label = Label(self.difficulty_frame, text=item[0], font=item[1],
        #                        fg=item[2],
        #                        wraplength=350, justify="left", pady=10, padx=20)
        #     make_label.grid(row=count)

            # start_label_ref.append(make_label)

            # extract choice label so that it can be changed to an
            # error message if necessary.


            # Frame so that entry box and button can be in the  same row.


if __name__ == "__main__":
    root = Tk ()
    root.title("Difficulty")
    Difficulty()
    root.mainloop()

