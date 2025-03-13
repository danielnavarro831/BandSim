from Utility.DocReader import DocReader
from Game.Member import Member
from tkinter import *
from Game.Band import Band
from Game.Location import Location
from Game.Album import Album


class Game:

    _active_member = ""
    _active_location = ""
    _members_for_hire = {}
    _methods_for_hiring = {1: "Post Flyers", 2: "Online Ad Campaign", 3: "Hire Talent Agent"}
    _costs_for_hiring_method = {1: 0, 2: 10000, 3: 100000}

    @classmethod
    def get_hiring_string(cls, level: int):
        hiring_string = Game._methods_for_hiring[level] + "\n" + str(Game._costs_for_hiring_method[level])
        return hiring_string

    @classmethod
    def set_active_member(cls, active_member_name: str):
        Game._active_member = active_member_name

    @classmethod
    def clear_active_member(cls):
        Game._active_member = ""

    @classmethod
    def set_active_location(cls, location_name: str):
        Game._active_location = location_name
        print("Active location set to: " + location_name)

    @classmethod
    def clear_active_location(cls):
        Game._active_location = ""
        print("Active location removed")

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

    def __init__(self):
        ################################################################################################################
        #                                               App Info
        ################################################################################################################
        self.version = "0.01"
        self.app = Tk()
        # self.app.iconbitmap("./nine_lives_32.ico") -- icon
        self.app.resizable(False, False)
        self.app.title("Band Simulator")
        self.band = Game.generate_new_band()
        band_name = DocReader.get_random_variable("Band")
        self.band.band_name = band_name
        Location.create_available_locations()
        ################################################################################################################
        #                                               Main Menu
        ################################################################################################################
        self.version_label = Label(self.app, text="Ver: " + self.version + " ", bd=1, relief=SUNKEN, anchor=E)
        self.menu = Menu(self.app)
        self.app.config(menu=self.menu)
        self.file_menu = Menu(self.menu)
        self.file_menu.add_command(label="Exit", command=self.app.quit)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.name_bar = Entry(self.app, width=35, justify="center")
        self.band_money_label = Label(self.app, text="Band Money: $")
        self.hype_label = Label(self.app, text="Album Hype: ")
        self.members_button = Button(self.app, text="Members", padx=35, pady=10, command=self.open_manage_members_menu)
        self.albums_button = Button(self.app, text="Albums", padx=34, pady=10, command=self.open_album_menu)
        self.perform_button = Button(self.app, text="Perform", padx=35, pady=10, command=self.open_performance_menu)
        ################################################################################################################
        #                                       Member Management Menu
        ################################################################################################################
        self.back_button = Button(self.app, text="<-Back", padx=35, pady=10, command=self.open_main_menu)
        self.member1_button = Button(self.app, text="Member1", padx=35, pady=10, command=lambda: self.open_member_profile_menu(self.member1_button["text"]))
        self.member2_button = Button(self.app, text="Member2", padx=35, pady=10, command=lambda: self.open_member_profile_menu(self.member2_button["text"]))
        self.member3_button = Button(self.app, text="Member3", padx=35, pady=10, command=lambda: self.open_member_profile_menu(self.member3_button["text"]))
        self.member4_button = Button(self.app, text="Member4", padx=35, pady=10, command=lambda: self.open_member_profile_menu(self.member4_button["text"]))
        self.member5_button = Button(self.app, text="Member5", padx=35, pady=10, command=lambda: self.open_member_profile_menu(self.member5_button["text"]))
        self.hire_button = Button(self.app, text="Hire", padx=35, pady=10, command=self.open_hire_members_menu)
        ################################################################################################################
        #                                          Hire Members Menu
        ################################################################################################################
        self.flyers_button = Button(self.app, text=Game.get_hiring_string(1), padx=35, pady=10, command=lambda: self.look_for_new_members(1))
        self.online_ad_button = Button(self.app, text=Game.get_hiring_string(2), padx=35, pady=10, command=lambda: self.look_for_new_members(2))
        self.hire_agent_button = Button(self.app, text=Game.get_hiring_string(3), padx=35, pady=10, command=lambda: self.look_for_new_members(3))
        ################################################################################################################
        #                                      Applicants For Hire Menu
        ################################################################################################################
        self.applicant1_button = Button(self.app, text="", padx=35, pady=10, command=lambda: self.open_applicant_profile(self.applicant1_button["text"]))
        self.applicant2_button = Button(self.app, text="", padx=35, pady=10, command=lambda: self.open_applicant_profile(self.applicant2_button["text"]))
        self.applicant3_button = Button(self.app, text="", padx=35, pady=10, command=lambda: self.open_applicant_profile(self.applicant3_button["text"]))
        ################################################################################################################
        #                                        Member Profile Menu
        ################################################################################################################
        self.fire_button = Button(self.app, text="fire", padx=35, pady=10)
        self.member_name_label = Label(self.app, text="")
        self.genre_specialty_label = Label(self.app, text="")
        self.salary_label = Label(self.app, text="")
        self.active_instrument_label = Label(self.app, text="")
        self.performance_label = Label(self.app, text="")
        self.theory_label = Label(self.app, text="")
        self.stamina_label = Label(self.app, text="")
        self.theory_class_button = Button(self.app, text="Music Theory Class", padx=35, pady=10, command=lambda: self.take_class(Game._active_member, "Music Theory"))
        self.performance_class_button = Button(self.app, text="Performance Class", padx=35, pady=10, command=lambda: self.take_class(Game._active_member, "Performance"))
        self.instrument_class_button = Button(self.app, text="Instrument Class", padx=35, pady=10, command=lambda: self.take_class(Game._active_member, self.get_active_member_instrument()))
        self.change_instrument_button = Button(self.app, text="Change Instrument", padx=35, pady=10, command=self.open_change_instrument_menu)
        ################################################################################################################
        #                                       Change Instrument Menu
        ################################################################################################################
        self.guitar_button = Button(self.app, text="Guitar", padx=35, pady=10, command=lambda: self.change_instrument_tapped("Guitar"))
        self.bass_button = Button(self.app, text="Bass", padx=35, pady=10, command=lambda: self.change_instrument_tapped("Bass"))
        self.drums_button = Button(self.app, text="Drums", padx=35, pady=10, command=lambda: self.change_instrument_tapped("Drums"))
        self.vocals_button = Button(self.app, text="Vocals", padx=35, pady=10, command=lambda: self.change_instrument_tapped("Vocals"))
        self.keyboard_button = Button(self.app, text="Keyboard", padx=35, pady=10, command=lambda: self.change_instrument_tapped("Keyboard"))
        ################################################################################################################
        #                                             Album Menu
        ################################################################################################################
        self.selected_genre = StringVar()
        self.genres = DocReader.get_all_genres()
        self.selected_genre.set(self.genres[0])
        self.genre_dropdown = OptionMenu(self.app, self.selected_genre, *self.genres)

        self.album_label = Label(self.app, text="Album Title: ")
        band_name = DocReader.get_random_variable("Band")
        self.name_bar.insert(0, band_name)

        self.selected_album_type = StringVar()
        self.album_types = Album.get_album_types()
        self.selected_album_type.set(self.album_types[0])
        self.album_types_dropdown = OptionMenu(self.app, self.selected_album_type, *self.album_types)
        self.discography_button = Button(self.app, text="Discography", padx=35, pady=10, command=self.open_discography_menu)

        self.make_album_button = Button(self.app, text="Make Album", padx=35, pady=10, command=self.make_album)
        ################################################################################################################
        #                                          Discography Menu
        ################################################################################################################
        self.discography = ["--"]
        self.selected_album = StringVar(master=self.app)
        self.selected_album.set(self.discography[0])
        self.view_button = Button(self.app, text="View", padx=35, pady=10, command=self.update_discography_labels)
        self.discography_dropdown = OptionMenu(self.app, self.selected_album, *self.discography)
        self.discography_album_title_label = Label(self.app, text="")
        self.discography_genre_label = Label(self.app, text="")
        self.discography_release_label = Label(self.app, text="")
        self.discography_credits_label = Label(self.app, text="")
        self.discography_ratings_label = Label(self.app, text="")
        self.discography_num_sold_label = Label(self.app, text="")
        self.discography_year_label = Label(self.app, text="")
        ################################################################################################################
        #                                           Performance Menu
        ################################################################################################################
        self.venue1_button = Button(self.app, text="", padx=35, pady=10, command=lambda: self.open_location_menu(self.venue1_button["text"]))
        self.venue2_button = Button(self.app, text="", padx=35, pady=10, command=lambda: self.open_location_menu(self.venue2_button["text"]))
        self.venue3_button = Button(self.app, text="", padx=35, pady=10, command=lambda: self.open_location_menu(self.venue3_button["text"]))
        ################################################################################################################
        #                                            Location Menu
        ################################################################################################################
        self.book_button = Button(self.app, text="Book Venue", padx=35, pady=10, command=self.perform_concert)
        self.ticket_cost = Label(self.app, text="Ticket Price: $")
        self.venue_cost = Label(self.app, text="Venue Cost: $")
        self.hype_generated = Label(self.app, text="Hype: ")
        ################################################################################################################
        #                                             Launch App
        ################################################################################################################
        self.version_label.grid(row=10, column=0, columnspan=2, sticky=W+E)
        self.open_main_menu()
        self.app.mainloop()  # Must be last line

    def get_active_member_instrument(self):
        member_name = Game._active_member
        member = self.band.members[member_name]
        return member.get_active_instrument()

    def close_all_menus(self):
        self.close_main_menu()
        self.close_manage_members_menu()
        self.close_member_profile_menu()
        self.close_change_instrument_menu()
        self.close_album_menu()
        self.close_performance_menu()
        self.close_location_menu()
        self.close_discography_menu()
        self.close_hire_members_menu()
        self.close_members_for_hire_menu()
        self.close_applicant_profile()

    def open_main_menu(self):
        self.close_all_menus()
        Game.clear_active_member()
        self.name_bar.delete(0, END)
        band_name = self.band.band_name
        self.name_bar.insert(0, band_name)
        self.name_bar.grid(row=0, column=0, columnspan=2)
        self.update_money_and_hype_labels()
        self.band_money_label.grid(row=1, column=0)
        self.hype_label.grid(row=1, column=1)
        self.members_button.grid(row=2, column=0, columnspan=2)
        self.albums_button.grid(row=3, column=0)
        self.perform_button.grid(row=3, column=1)

    def update_money_and_hype_labels(self):
        self.band_money_label["text"] = "Band Money: $" + str(self.band.money)
        self.hype_label["text"] = "Album Hype: " + str(Location.get_album_hype_generated())

    def close_main_menu(self):
        self.name_bar.grid_remove()
        self.band_money_label.grid_remove()
        self.hype_label.grid_remove()
        self.members_button.grid_remove()
        self.albums_button.grid_remove()
        self.perform_button.grid_remove()

    def open_manage_members_menu(self):
        self.close_all_menus()
        self.back_button["command"] = lambda: self.open_main_menu()
        self.update_money_and_hype_labels()
        self.band_money_label.grid(row=1, column=0)
        self.hype_label.grid(row=1, column=1)
        self.back_button.grid(row=2, column=0)
        self.hire_button.grid(row=2, column=1)
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

    def open_member_profile_menu(self, member: str):
        Game.set_active_member(member)
        active_member = self.band.members[member]
        active_instrument = active_member.get_active_instrument()
        self.close_all_menus()
        self.back_button["command"] = lambda: self.open_manage_members_menu()
        if active_instrument == "Drums" or active_instrument == "Vocals":
            active_instrument = active_instrument[:-1]
        self.instrument_class_button["text"] = active_instrument + " class"
        self.set_member_profile_labels(active_member)
        self.update_money_and_hype_labels()
        self.band_money_label.grid(row=1, column=0)
        self.hype_label.grid(row=1, column=1)
        self.back_button.grid(row=2, column=0)
        self.fire_button.grid(row=2, column=1)
        self.member_name_label.grid(row=3, column=0, columnspan=2)
        self.genre_specialty_label.grid(row=4, column=0)
        self.salary_label.grid(row=4, column=1)
        self.change_instrument_button.grid(row=5, column=0, columnspan=2)
        self.active_instrument_label.grid(row=6, column=0)
        self.instrument_class_button.grid(row=6, column=1)
        self.performance_label.grid(row=7, column=0)
        self.performance_class_button.grid(row=7, column=1)
        self.theory_label.grid(row=8, column=0)
        self.theory_class_button.grid(row=8, column=1)
        self.stamina_label.grid(row=9)

    def set_member_profile_labels(self, member: Member):
        self.member_name_label["text"] = member.name
        self.genre_specialty_label["text"] = "Genre Specialty: " + member.genre_specialty
        self.salary_label["text"] = "Salary: $" + str(member.stats["Salary"])
        active_instrument = member.get_active_instrument()
        instrument_level = member.instrument_stats[active_instrument]
        self.active_instrument_label["text"] = "Instrument: " + active_instrument + " (" + str(instrument_level) + ")"
        self.performance_label["text"] = "Performance: " + str(member.stats["Performance"])
        self.theory_label["text"] = "Song Writing: " + str(member.stats["Music Theory"])
        self.stamina_label["text"] = "Stamina: " + str(member.stats["Stamina"]) + "/" + str(member.stats["MaxStamina"])
        self.set_member_profile_button_texts(member)

    def set_member_profile_button_texts(self, member: Member):
        performance_cost = self.band.get_cost_of_stat_increase(member.stats["Performance"])
        self.performance_class_button["text"] = "Performance Class \n $" + str(performance_cost)
        theory_cost = self.band.get_cost_of_stat_increase(member.stats["Music Theory"])
        self.theory_class_button["text"] = "Music Theory Class \n $" + str(theory_cost)
        instrument_cost = self.band.get_cost_of_stat_increase(member.instrument_stats[member.get_active_instrument()])
        self.instrument_class_button["text"] = member.get_active_instrument() + "Class \n $" + str(instrument_cost)

    def close_member_profile_menu(self):
        self.back_button.grid_remove()
        self.fire_button.grid_remove()
        self.band_money_label.grid_remove()
        self.hype_label.grid_remove()
        self.member_name_label.grid_remove()
        self.genre_specialty_label.grid_remove()
        self.salary_label.grid_remove()
        self.active_instrument_label.grid_remove()
        self.performance_label.grid_remove()
        self.theory_label.grid_remove()
        self.stamina_label.grid_remove()
        self.theory_class_button.grid_remove()
        self.performance_class_button.grid_remove()
        self.instrument_class_button.grid_remove()
        self.change_instrument_button.grid_remove()

    def open_hire_members_menu(self):
        self.close_all_menus()
        self.back_button.grid(row=2, column=0)
        self.back_button["command"] = self.open_manage_members_menu
        self.flyers_button.grid(row=3, column=0, columnspan=2)
        self.online_ad_button.grid(row=4, column=0, columnspan=2)
        self.hire_agent_button.grid(row=5, column=0, columnspan=2)
        buttons = [self.applicant1_button, self.applicant2_button, self.applicant3_button]
        for i in range(len(buttons)):
            button = buttons[i]
            button["state"] = "normal"

    def close_hire_members_menu(self):
        self.back_button.grid_remove()
        self.flyers_button.grid_remove()
        self.online_ad_button.grid_remove()
        self.hire_agent_button.grid_remove()

    def open_members_for_hire_menu(self, level=1, back=False):
        self.close_all_menus()
        if not back:
            members_for_hire = Band.get_new_members(level)
            Game._members_for_hire = members_for_hire
        else:
            members_for_hire = Game._members_for_hire
        buttons = {1: self.applicant1_button, 2: self.applicant2_button, 3: self.applicant3_button}
        i = 1
        for member in members_for_hire.keys():
            applicant = members_for_hire[member]
            buttons[i]["text"] = applicant.name
            i += 1
        self.back_button.grid(row=2, column=0)
        self.back_button["command"] = self.open_hire_members_menu
        self.applicant1_button.grid(row=3, column=0)
        self.applicant2_button.grid(row=4, column=0)
        self.applicant3_button.grid(row=5, column=0)

    def close_members_for_hire_menu(self):
        self.back_button.grid_remove()
        self.applicant1_button.grid_remove()
        self.applicant2_button.grid_remove()
        self.applicant3_button.grid_remove()

    def look_for_new_members(self, method_int: int):
        hiring_cost = Game._costs_for_hiring_method[method_int]
        if self.check_band_funds(hiring_cost):
            self.band.decrease_money(hiring_cost)
            print("$" + str(hiring_cost) + " deducted for " + Game._methods_for_hiring[method_int])
            self.open_members_for_hire_menu(method_int)
        else:
            print("Not enough money!")

    def open_applicant_profile(self, applicant_name: str):
        applicant = Game._members_for_hire[applicant_name]
        self.close_all_menus()
        self.back_button.grid(row=2, column=0)
        self.back_button["command"] = lambda: self.open_members_for_hire_menu(1, True)
        self.hire_button.grid(row=2, column=1)
        self.hire_button["command"] = lambda: self.hire_applicant(applicant)
        self.set_member_profile_labels(applicant)
        self.update_money_and_hype_labels()
        self.band_money_label.grid(row=1, column=0)
        self.hype_label.grid(row=1, column=1)
        self.back_button.grid(row=2, column=0)
        self.member_name_label.grid(row=3, column=0, columnspan=2)
        self.genre_specialty_label.grid(row=4, column=0)
        self.salary_label.grid(row=4, column=1)
        self.active_instrument_label.grid(row=6, column=0)
        self.performance_label.grid(row=7, column=0)
        self.theory_label.grid(row=8, column=0)

    def hire_applicant(self, member: Member):
        self.band.add_member(member)
        buttons = [self.applicant1_button, self.applicant2_button, self.applicant3_button]
        for i in range(len(buttons)):
            button = buttons[i]
            if button["text"] == member.name:
                button["state"] = "disabled"

    def close_applicant_profile(self):
        self.back_button.grid_remove()
        self.hire_button.grid_remove()
        self.band_money_label.grid_remove()
        self.hype_label.grid_remove()
        self.member_name_label.grid_remove()
        self.genre_specialty_label.grid_remove()
        self.salary_label.grid_remove()
        self.active_instrument_label.grid_remove()
        self.performance_label.grid_remove()
        self.theory_label.grid_remove()

    def take_class(self, member_name: str, stat: str):
        band_member = self.band.members[member_name]
        stat_value = band_member.check_current_stat_value(stat)
        class_cost = Band.get_cost_of_stat_increase(stat_value)
        print("Class cost: " + str(class_cost))
        if not self.check_band_funds(class_cost):
            print("Not enough funds")
            return
        self.band.take_class(member_name, stat)
        member = self.band.members[member_name]
        self.set_member_profile_labels(member)
        self.band.decrease_money(class_cost)
        self.update_money_and_hype_labels()
        self.set_member_profile_button_texts(member)

    def close_manage_members_menu(self):
        self.back_button.grid_remove()
        self.hire_button.grid_remove()
        self.hype_label.grid_remove()
        self.band_money_label.grid_remove()
        self.member1_button.grid_remove()
        self.member2_button.grid_remove()
        self.member3_button.grid_remove()
        self.member4_button.grid_remove()
        self.member5_button.grid_remove()

    def open_change_instrument_menu(self):
        self.close_all_menus()
        self.back_button["command"] = lambda: self.open_member_profile_menu(Game._active_member)
        self.back_button.grid(row=2, column=0)
        active_member = self.band.members[Game._active_member]
        active_instrument = active_member.get_active_instrument()
        buttons = {"Guitar": self.guitar_button, "Bass": self.bass_button, "Drums": self.drums_button,
                   "Vocals": self.vocals_button, "Keyboard": self.keyboard_button}
        row = 3
        for button in buttons.keys():
            instrument_level = active_member.instrument_stats[button]
            buttons[button]["text"] += " (" + str(instrument_level) + ")"
            if button == active_instrument:
                buttons[button]["state"] = "disabled"
            else:
                buttons[button]["state"] = "normal"
            buttons[button].grid(row=row, column=0)
            row += 1

    def close_change_instrument_menu(self):
        buttons = {"Guitar": self.guitar_button, "Bass": self.bass_button, "Drums": self.drums_button,
                   "Vocals": self.vocals_button, "Keyboard": self.keyboard_button}
        for button in buttons.keys():
            buttons[button]["text"] = button
        self.back_button.grid_remove()
        self.guitar_button.grid_remove()
        self.bass_button.grid_remove()
        self.drums_button.grid_remove()
        self.vocals_button.grid_remove()
        self.keyboard_button.grid_remove()

    def change_instrument_tapped(self, instrument: str):
        self.band.members[Game._active_member].set_active_instrument(instrument)
        self.close_all_menus()
        self.open_member_profile_menu(Game._active_member)
        print(Game._active_member + " changed instruments to " + instrument)

    def open_album_menu(self):
        self.close_all_menus()
        self.back_button["command"] = self.open_main_menu
        self.album_label.grid(row=1, column=0)
        self.name_bar.grid(row=1, column=1)
        self.name_bar.delete(0, END)
        self.name_bar.insert(0, DocReader.get_random_variable("Band"))
        self.update_money_and_hype_labels()
        self.band_money_label.grid(row=2, column=0)
        self.hype_label.grid(row=2, column=1)
        self.back_button.grid(row=3, column=0)
        self.discography_button.grid(row=3, column=1)
        self.genre_dropdown.grid(row=4, column=0)
        self.album_types_dropdown.grid(row=4, column=1)
        self.make_album_button.grid(row=5, column=0, columnspan=2)

    def close_album_menu(self):
        self.back_button.grid_remove()
        self.discography_button.grid_remove()
        self.album_label.grid_remove()
        self.name_bar.grid_remove()
        self.band_money_label.grid_remove()
        self.hype_label.grid_remove()
        self.genre_dropdown.grid_remove()
        self.album_types_dropdown.grid_remove()
        self.make_album_button.grid_remove()

    def make_album(self):
        album_type = str(self.selected_album_type.get())
        album_cost = Album.get_album_cost(album_type)
        if not self.check_band_funds(album_cost):
            print("Not enough band funds!")
            return
        album_name = self.name_bar.get()
        if self.band.check_if_album_name_exists(album_name):
            print("Album title already used")
        else:
            print("Album Name: " + album_name)
            genre = str(self.selected_genre.get())
            print("Genre: " + genre)
            print("Album Type: " + album_type)
            hype = Location.get_album_hype_generated()
            print("Hype Generated: " + str(hype))
            self.band.make_album(album_name, genre, hype, album_type)
            self.open_discography_menu()
            self.selected_album.set(self.discography[-1])
            self.update_discography_labels()
            self.band.decrease_money(album_cost)
            self.update_money_and_hype_labels()

    def check_band_funds(self, cost: int):
        if self.band.money >= cost:
            return True
        return False

    def open_discography_menu(self):
        self.close_all_menus()
        self.back_button["command"] = self.open_album_menu
        self.back_button.grid(row=1, column=0)
        self.discography = self.band.get_discography()
        self.discography_dropdown["menu"].delete(0, "end")
        for item in self.discography:
            print("doing the thing")
            self.discography_dropdown["menu"].add_command(
                label=item, command=lambda value=item: self.selected_album.set(value)
            )
            print("Problem not here")
        self.discography_album_title_label["text"] = "Album Title: "
        self.discography_year_label["text"] = "Year: "
        self.discography_genre_label["text"] = "Genre: "
        self.discography_ratings_label["text"] = "Rating: "
        self.discography_num_sold_label["text"] = "Sold: "
        self.discography_credits_label["text"] = "Credits: "
        self.discography_dropdown.grid(row=2, column=0)
        self.view_button.grid(row=2, column=1)
        self.discography_album_title_label.grid(row=3, column=0, columnspan=2)
        self.discography_genre_label.grid(row=4, column=0)
        self.discography_year_label.grid(row=4, column=1)
        self.discography_ratings_label.grid(row=5, column=0)
        self.discography_num_sold_label.grid(row=5, column=1)
        self.discography_credits_label.grid(row=6, column=0, columnspan=2)

    def update_discography_labels(self):
        print("attempting to get")
        album_name = self.selected_album.get()
        self.discography_album_title_label["text"] = "Album Title: "
        self.discography_year_label["text"] = "Year: "
        self.discography_genre_label["text"] = "Genre: "
        self.discography_ratings_label["text"] = "Rating: "
        self.discography_num_sold_label["text"] = "Sold: "
        self.discography_credits_label["text"] = "Credits: \n"
        if album_name == "--":
            print("Returning")
            return
        else:
            album = self.band.get_album(album_name)
            self.discography_album_title_label["text"] += album_name
            self.discography_genre_label["text"] += album.genre
            self.discography_year_label["text"] += str(album.year_released)
            self.discography_ratings_label["text"] += str(album.rating["Overall"]) + "/100"
            self.discography_num_sold_label["text"] += str(album.num_sold)
            self.discography_credits_label["text"] += album.stringify_credits()

    def close_discography_menu(self):
        self.back_button.grid_remove()
        self.discography_dropdown.grid_remove()
        self.view_button.grid_remove()
        self.discography_album_title_label.grid_remove()
        self.discography_year_label.grid_remove()
        self.discography_genre_label.grid_remove()
        self.discography_ratings_label.grid_remove()
        self.discography_credits_label.grid_remove()
        self.discography_num_sold_label.grid_remove()

    def open_performance_menu(self):
        self.close_all_menus()
        locations = Location.get_available_locations()
        button_map = {1: self.venue1_button, 2: self.venue2_button, 3: self.venue3_button}
        i = 1
        for location in locations.keys():
            button_map[i]["text"] = location
            i += 1
        self.update_money_and_hype_labels()
        self.band_money_label.grid(row=1, column=0)
        self.hype_label.grid(row=1, column=1)
        self.back_button["command"] = self.open_main_menu
        self.back_button.grid(row=2, column=0)
        self.venue1_button.grid(row=3, column=0, columnspan=2)
        self.venue2_button.grid(row=4, column=0, columnspan=2)
        self.venue3_button.grid(row=5, column=0, columnspan=2)

    def close_performance_menu(self):
        self.back_button.grid_remove()
        self.hype_label.grid_remove()
        self.band_money_label.grid_remove()
        self.venue1_button.grid_remove()
        self.venue2_button.grid_remove()
        self.venue3_button.grid_remove()

    def open_location_menu(self, location_name: str):
        self.close_all_menus()
        Game.set_active_location(location_name)
        location = Location.get_specific_location(Game._active_location)
        self.venue_cost["text"] += str(location.venue_cost)
        self.ticket_cost["text"] += str(location.ticket_cost)
        self.hype_generated["text"] += str(location.hype_generated)
        self.back_button["command"] = self.open_performance_menu
        self.update_money_and_hype_labels()
        self.band_money_label.grid(row=1, column=0)
        self.hype_label.grid(row=1, column=1)
        self.back_button.grid(row=2, column=0)
        self.ticket_cost.grid(row=3, column=0, columnspan=2)
        self.hype_generated.grid(row=4, column=0, columnspan=2)
        self.venue_cost.grid(row=5, column=0, columnspan=2)
        self.book_button.grid(row=6, column=0, columnspan=2)

    def close_location_menu(self):
        self.clear_active_location()
        self.ticket_cost["text"] = "Ticket Price: $"
        self.venue_cost["text"] = "Venue Cost: $"
        self.hype_generated["text"] = "Hype: "
        self.band_money_label.grid_remove()
        self.hype_label.grid_remove()
        self.back_button.grid_remove()
        self.ticket_cost.grid_remove()
        self.hype_generated.grid_remove()
        self.venue_cost.grid_remove()
        self.book_button.grid_remove()

    def perform_concert(self):
        fame = Band.calculate_fame_level(self.band)
        print("Fame level: " + str(fame))
        venue = Location.get_specific_location(Game._active_location)
        print("Venue: " + str(venue.location_name))
        print("Obj test: " + str(venue))
        income = venue.sell_tickets(fame)
        print("Income generated: " + str(income))
        self.band.increase_money(income)
        venue.generate_hype(self.band.get_group_stat("Performance"))
        print("Hype Generated: " + str(venue.hype_generated))
        Location.log_performance_hype(venue)
        tour_length = len(Location.get_hype_tracker())
        print("Tour Length: " + str(tour_length))
        self.band.decrease_band_stamina(tour_length)
        print("Band Stamina decreased")
        self.open_main_menu()


game = Game()
