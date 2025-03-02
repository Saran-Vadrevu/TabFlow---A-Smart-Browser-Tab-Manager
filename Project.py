import time

class Browser:
    class Queue:
        def __init__(self):
            self.sz = 0
            self.arr_site = []
            self.arr_time = []

    class Tab:
        class Stack:
            def __init__(self):
                self.size = 0
                self.arr = []

        def __init__(self, tabname, site):
            self.tabn = tabname
            self.current_site = site
            self.ForwardStack = self.Stack()
            self.BackwardStack = self.Stack()
            self.next = None
            self.prev = None

    def __init__(self):
        self.no_tabs = 0
        self.first_Tab = None
        self.q = self.Queue()
        self.bookmarks = set()
        self.closed_tabs = []

    def show_menu(self):
        """Display the operations menu after every action."""
        print("\n=== Select an Operation ===")
        print(" 1. Create Tab")
        print(" 2. Show Tabs")
        print(" 3. Delete Tab")
        print(" 4. Reopen Last Closed Tab")
        print(" 5. Switch Tab")
        print(" 6. View Current Tab")
        print(" 7. Open Link")
        print(" 8. Move Back")
        print(" 9. Move Front")
        print("10. Bookmark Current Site")
        print("11. View Bookmarks")
        print("12. Clear History")
        print("13. Duplicate Tab")
        print("14. Exit")
        print("===========================\n")

    def create_tab(self):
        """Create a new tab."""
        tabname = input("\n Enter the Tab name: ")
        site = input(f" Enter the Site to open in {tabname}: ")

        newt = self.Tab(tabname, site)
        if self.first_Tab:
            newt.next = self.first_Tab
            self.first_Tab.prev = newt
        self.first_Tab = newt
        self.no_tabs += 1
        print("\n\n >> Tab created!!")
        self.show_tabs()
        self.show_menu()

    def show_tabs(self):
        """Display all open tabs."""
        if self.no_tabs > 0:
            print("\n >> Open Tabs:")
            f = self.first_Tab
            while f:
                print(f" - {f.tabn}: {f.current_site}")
                f = f.next
        else:
            print("\n\n !! No Tabs exist !!")

    def delete_tab(self):
        """Delete a tab."""
        tabname = input("\n Enter the Tab name to delete: ")
        f = self.first_Tab
        while f:
            if f.tabn == tabname:
                self.closed_tabs.append((f.tabn, f.current_site))
                if f.prev:
                    f.prev.next = f.next
                if f.next:
                    f.next.prev = f.prev
                if f == self.first_Tab:
                    self.first_Tab = f.next
                self.no_tabs -= 1
                print("\n\n >> Tab deleted!!")
                self.show_tabs()
                self.show_menu()
                return
            f = f.next
        print("\n\n !! Tab not found !!")
        self.show_menu()

    def exit_program(self):
        """Exit the browser simulation."""
        print("\n\n !! Terminating... Thank you !!")
        exit()

# Main execution
firefox = Browser()
print("\n===== Browser Opened =====")
firefox.show_menu()

while True:
    try:
        opt = int(input("\nEnter operation: "))
    except ValueError:
        print("\nInvalid input! Please enter a number from 1 to 14.")
        continue

    actions = {
        1: firefox.create_tab,
        2: firefox.show_tabs,
        3: firefox.delete_tab,
        14: firefox.exit_program
    }

    if opt in actions:
        actions[opt]()
    else:
        print("\n Invalid choice, please enter a valid option.")
