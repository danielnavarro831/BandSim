from Utility.DocReader import DocReader
from Game.Member import Member
from tkinter import *
from Game.Band import Band
from Game.Location import Location
from Game.Album import Album


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
        self.members_button = Button(self.app, text="Members", padx=35, pady=10, command=lambda: self.open_manage_members_menu())
        self.albums_button = Button(self.app, text="Albums", padx=34, pady=10)
        self.perform_button = Button(self.app, text="Perform", padx=35, pady=10)
        self.back_button = Button(self.app, text="<-Back", padx=35, pady=10, command=lambda: self.open_main_menu())
        self.member1_button = Button(self.app, text="Member1", padx=35, pady=10)
        self.member2_button = Button(self.app, text="Member2", padx=35, pady=10)
        self.member3_button = Button(self.app, text="Member3", padx=35, pady=10)
        self.member4_button = Button(self.app, text="Member4", padx=35, pady=10)
        self.member5_button = Button(self.app, text="Member5", padx=35, pady=10)
        self.hire_button = Button(self.app, text="Hire", padx=35, pady=10)
        self.fire_button = Button(self.app, text="fire", padx=35, pady=10)
        self.name_bar = Entry(self.app, width=35, justify="center")
        band_name = DocReader.get_random_variable("Band")
        self.name_bar.insert(0, band_name)

        self.open_main_menu()
        self.version_label.grid(row=10, column=0, columnspan=2, sticky=W+E)
        self.band = Game.generate_new_band()
        self.band.band_name = band_name
        self.app.mainloop()  # Must be last line

    def close_all_menus(self):
        self.close_main_menu()
        self.close_manage_members_menu()

    def open_main_menu(self):
        self.close_all_menus()
        self.name_bar.grid(row=0, column=0, columnspan=2)
        self.members_button.grid(row=2, column=0, columnspan=2)
        self.albums_button.grid(row=3, column=0)
        self.perform_button.grid(row=3, column=1)

    def close_main_menu(self):
        self.name_bar.grid_remove()
        self.members_button.grid_remove()
        self.albums_button.grid_remove()
        self.perform_button.grid_remove()

    def open_manage_members_menu(self):
        self.close_all_menus()
        self.back_button.grid(row=2, column=0)
        self.hire_button.grid(row=3, column=0)
        self.fire_button.grid(row=3, column=1)
        buttons = {1: self.member1_button, 2: self.member2_button, 3: self.member3_button, 4: self.member4_button,
                   5: self.member5_button}
        i = 1
        curr_row = 4
        curr_column = 0
        for member in self.band.members.keys():
            buttons[i]["text"] = str(member)
            buttons[i].grid(row=curr_row, column=curr_column)
            if curr_column == 0:
                curr_column += 1
            else:
                curr_row += 1
                curr_column = 0
            i += 1

    def close_manage_members_menu(self):
        self.back_button.grid_remove()
        self.hire_button.grid_remove()
        self.fire_button.grid_remove()
        self.member1_button.grid_remove()
        self.member2_button.grid_remove()
        self.member3_button.grid_remove()
        self.member4_button.grid_remove()
        self.member5_button.grid_remove()

    @classmethod
    def generate_new_band(cls):
        band = Band()
        starting_members = ["Guitar", "Vocals", "Drums"]
        for i in range(len(starting_members)):
            instrument = starting_members[i]
            data = Member.get_starting_stats(1, instrument)
            member = Member(data)
            band.add_member(member)
        return band


# game = Game()

band = Game.generate_new_band()
band.make_album("New", "Nu", 15)