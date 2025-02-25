from Utility.DocReader import DocReader
from Game.Member import Member
from tkinter import *
from Game.Band import Band


class Game:
    def __init__(self):
        self.version = "0.01"
        self.app = Tk()
        # self.app.iconbitmap("./nine_lives_32.ico") -- icon
        self.app.resizable(False, False)
        self.app.title("Band Simulator")

        self.version_label = Label(self.app, text="Ver: " + self.version + " ", bd=1, relief=SUNKEN, anchor=E)
        self.menu = Menu(self.app)
        self.app.config(menu=self.menu)
        self.file_menu = Menu(self.menu)
        self.file_menu.add_command(label="Exit", command=self.app.quit)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        # self.pet_button = Button(self.app, text="Pet", padx=38, pady=10, command=lambda: self.pet_pet(self.pet))
        self.members_button = Button(self.app, text="Members", padx=35, pady=10)
        self.albums_button = Button(self.app, text="Albums", padx=34, pady=10)
        self.perform_button = Button(self.app, text="Perform", padx=35, pady=10)
        self.name_bar = Entry(self.app, width=12, justify="center")
        band_name = DocReader.get_random_variable("Band")
        self.name_bar.insert(0, band_name)

        self.name_bar.grid(row=0, column=0, columnspan=2)
        self.members_button.grid(row=2)
        self.albums_button.grid(row=3, column=0)
        self.perform_button.grid(row=3, column=1)
        self.version_label.grid(row=4, column=0, columnspan=2, sticky=W+E)
        Game.generate_new_band()
        self.app.mainloop()  # Must be last line

    def open_manage_members_screen(self):
        pass

    @classmethod
    def generate_new_band(cls):
        band = Band()
        starting_members = ["Guitar", "Vocals", "Drums"]
        for i in range(len(starting_members)):
            instrument = starting_members[i]
            data = Member.get_starting_stats(1, instrument)
            member = Member(data)
            band.add_member(member)
        print("Band: " + str(band.members))


game = Game()
