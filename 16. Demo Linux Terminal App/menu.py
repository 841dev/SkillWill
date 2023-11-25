import sys

import utils
from diarybook import Diary, DiaryBook


class Menu:
    def __init__(self):
        self.diarybook = DiaryBook()

        self.choices = {
            "1" : self.show_all_diaries,
            "2" : self.add_diary,
            "3" : self.search_diaries,
            "4" : self.quit
        }
    def show_all_diaries(self):
        if len(self.diarybook.diaries) == 0:
            print("There are no diaries in the database")
        for diary in self.diarybook.diaries:
            print(f"{diary.id} - {diary.memo}")

    def add_diary(self):
        memo = input("Enter a memo:  ")
        tags = input("Enter tags:  ")
        self.diarybook.new_diary(memo, tags)
        print("your note has been added successfully")


    def search_diaries(self):
        keyword = input("Enter a Keyword: ")
        filtered_diaries = self.diarybook.search_diary(keyword)
        for diary in filtered_diaries:
            print(f"{diary.id} - {diary.memo}")


    def populate_database(self):
        diaries = utils.raed_from_json_into_app("data.json")
        for diary in diaries:
            self.diarybook.diaries.append(diary)
    def quit(self):
        sys.exit(0)
        #exit()


    def display_menu(self):
        print("""
            Diarybook Menu:
            
            1. Show diaries
            2. Add diary
            3. Filter using keyword
            4. Quit program
        """)
    def run(self):
        self.populate_database()
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

if __name__ == "__main__":
    Menu().run()