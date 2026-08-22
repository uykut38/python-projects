import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

import matplotlib.pyplot as plt


# ==========================================
# 1. EXPENSE CLASS
# ==========================================

class Expense:

    def __init__(self, title, amount, person, category, date):
        self.title = title
        self.amount = amount
        self.person = person
        self.category = category
        self.date = date

    def get_grade(self):
        if self.amount >= 1000:
            return "Very High"
        elif self.amount >= 500:
            return "High"
        elif self.amount >= 200:
            return "Medium"
        else:
            return "Low"


# ==========================================
# 2. MAIN APPLICATION CLASS
# ==========================================

class ExpenseApp:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "Personal Expense Management System"
        )

        self.root.geometry("1200x850")

        self.root.minsize(1050, 750)

        self.root.configure(
            bg="#F4F6F8"
        )

        # --------------------------------------
        # LIST
        # --------------------------------------

        self.expenses = []

        # --------------------------------------
        # FILE
        # --------------------------------------

        self.file_name = "expenses.json"

        # --------------------------------------
        # TUPLE
        # --------------------------------------

        self.people = (
            "Me",
            "Children",
            "House Expenses",
            "Other Expenses"
        )

        # --------------------------------------
        # TUPLE
        # --------------------------------------

        self.categories = (
            "Food",
            "Daily Necessities",
            "Education",
            "Health",
            "Clothes",
            "Rent",
            "Bills",
            "Other"
        )

        # --------------------------------------
        # SET
        # --------------------------------------

        self.cities = {
            "Istanbul",
            "Ankara",
            "Bursa"
        }

        # --------------------------------------
        # DICTIONARY
        # --------------------------------------

        self.user_info = {
            "name": "Personal User",
            "currency": "TL",
            "system": "Personal Expense Manager"
        }

        # --------------------------------------
        # EDIT MODE
        # --------------------------------------

        self.editing_index = None

        # --------------------------------------
        # LOAD DATA
        # --------------------------------------

        self.load_expenses()

        # --------------------------------------
        # GUI
        # --------------------------------------

        self.create_style()
        self.create_gui()

        self.show_expenses()

        # --------------------------------------
        # CLOSE EVENT
        # --------------------------------------

        self.root.protocol(
            "WM_DELETE_WINDOW",
            self.close_program
        )


    # ==========================================
    # 3. STYLE
    # ==========================================

    def create_style(self):

        style = ttk.Style()

        style.theme_use("clam")

        style.configure(
            "Treeview",
            background="white",
            foreground="#222222",
            rowheight=34,
            fieldbackground="white",
            font=("Arial", 10)
        )

        style.configure(
            "Treeview.Heading",
            font=("Arial", 10, "bold"),
            padding=8
        )

        style.map(
            "Treeview",
            background=[
                ("selected", "#D6EAF8")
            ],
            foreground=[
                ("selected", "#000000")
            ]
        )

        style.configure(
            "TCombobox",
            padding=6,
            font=("Arial", 10)
        )


    # ==========================================
    # 4. GUI
    # ==========================================

    def create_gui(self):

        # ======================================
        # HEADER
        # ======================================

        header = tk.Frame(
            self.root,
            bg="#2C3E50",
            height=100
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(False)


        title = tk.Label(
            header,
            text="Personal Expense Manager",
            bg="#2C3E50",
            fg="white",
            font=("Arial", 26, "bold")
        )

        title.pack(
            pady=(18, 2)
        )


        subtitle = tk.Label(
            header,
            text="Manage your personal and children's expenses",
            bg="#2C3E50",
            fg="#D5DBDB",
            font=("Arial", 11)
        )

        subtitle.pack()


        # ======================================
        # DASHBOARD
        # ======================================

        dashboard = tk.Frame(
            self.root,
            bg="#F4F6F8"
        )

        dashboard.pack(
            fill="x",
            padx=25,
            pady=12
        )


        # 6 DASHBOARD CARDS
        self.total_card = self.create_card(
            dashboard,
            "Total Expenses",
            "#2C3E50"
        )
        self.total_card.grid(
            row=0,
            column=0,
            padx=4,
            pady=4,
            sticky="nsew"
        )

        self.my_card = self.create_card(
            dashboard,
            "My Expenses",
            "#27AE60"
        )
        self.my_card.grid(
            row=0,
            column=1,
            padx=4,
            pady=4,
            sticky="nsew"
        )

        self.children_card = self.create_card(
            dashboard,
            "Children Expenses",
            "#8E44AD"
        )
        self.children_card.grid(
            row=0,
            column=2,
            padx=4,
            pady=4,
            sticky="nsew"
        )

        self.house_card = self.create_card(
            dashboard,
            "House Expenses",
            "#D35400"
        )
        self.house_card.grid(
            row=0,
            column=3,
            padx=4,
            pady=4,
            sticky="nsew"
        )

        self.other_card = self.create_card(
            dashboard,
            "Other Expenses",
            "#16A085"
        )
        self.other_card.grid(
            row=0,
            column=4,
            padx=4,
            pady=4,
            sticky="nsew"
        )

        self.record_card = self.create_card(
            dashboard,
            "Number of Records",
            "#2980B9"
        )
        self.record_card.grid(
            row=0,
            column=5,
            padx=4,
            pady=4,
            sticky="nsew"
        )

        for i in range(6):
            dashboard.columnconfigure(i, weight=1)


        # ======================================
        # INPUT FRAME
        # ======================================

        input_frame = tk.LabelFrame(
            self.root,
            text="  Add / Edit Expense  ",
            bg="white",
            fg="#2C3E50",
            font=("Arial", 12, "bold"),
            padx=15,
            pady=10
        )

        input_frame.pack(
            fill="x",
            padx=25,
            pady=8
        )


        # TITLE

        tk.Label(
            input_frame,
            text="Title",
            bg="white",
            font=("Arial", 10, "bold")
        ).grid(
            row=0,
            column=0,
            padx=7,
            pady=6
        )


        self.title_entry = tk.Entry(
            input_frame,
            width=20,
            font=("Arial", 10)
        )

        self.title_entry.grid(
            row=0,
            column=1,
            padx=7
        )


        # AMOUNT

        tk.Label(
            input_frame,
            text="Amount (TL)",
            bg="white",
            font=("Arial", 10, "bold")
        ).grid(
            row=0,
            column=2,
            padx=7
        )


        self.amount_entry = tk.Entry(
            input_frame,
            width=15,
            font=("Arial", 10)
        )

        self.amount_entry.grid(
            row=0,
            column=3,
            padx=7
        )


        # DATE

        tk.Label(
            input_frame,
            text="Date",
            bg="white",
            font=("Arial", 10, "bold")
        ).grid(
            row=0,
            column=4,
            padx=7
        )


        self.date_entry = tk.Entry(
            input_frame,
            width=15,
            font=("Arial", 10)
        )

        self.date_entry.grid(
            row=0,
            column=5,
            padx=7
        )


        # PERSON

        tk.Label(
            input_frame,
            text="For",
            bg="white",
            font=("Arial", 10, "bold")
        ).grid(
            row=1,
            column=0,
            padx=7,
            pady=6
        )


        self.person_entry = ttk.Combobox(
            input_frame,
            values=self.people,
            width=17,
            state="readonly"
        )

        self.person_entry.grid(
            row=1,
            column=1,
            padx=7
        )


        # CATEGORY

        tk.Label(
            input_frame,
            text="Category",
            bg="white",
            font=("Arial", 10, "bold")
        ).grid(
            row=1,
            column=2,
            padx=7
        )


        self.category_entry = ttk.Combobox(
            input_frame,
            values=self.categories,
            width=17,
            state="readonly"
        )

        self.category_entry.grid(
            row=1,
            column=3,
            padx=7
        )


        # ======================================
        # BUTTON FRAME
        # ======================================

        button_frame = tk.Frame(
            self.root,
            bg="#F4F6F8"
        )

        button_frame.pack(
            pady=5
        )


        button_style = {
            "font": ("Arial", 9, "bold"),
            "width": 15,
            "height": 2,
            "relief": "flat",
            "cursor": "hand2"
        }


        # ROW 1

        tk.Button(
            button_frame,
            text="Add Expense",
            bg="#27AE60",
            fg="white",
            command=self.add_expense,
            **button_style
        ).grid(
            row=0,
            column=0,
            padx=4,
            pady=3
        )


        tk.Button(
            button_frame,
            text="Edit Expense",
            bg="#F39C12",
            fg="white",
            command=self.edit_expense,
            **button_style
        ).grid(
            row=0,
            column=1,
            padx=4,
            pady=3
        )


        tk.Button(
            button_frame,
            text="Update Expense",
            bg="#E67E22",
            fg="white",
            command=self.update_expense,
            **button_style
        ).grid(
            row=0,
            column=2,
            padx=4,
            pady=3
        )


        tk.Button(
            button_frame,
            text="Delete",
            bg="#E74C3C",
            fg="white",
            command=self.delete_expense,
            **button_style
        ).grid(
            row=0,
            column=3,
            padx=4,
            pady=3
        )


        # ROW 2

        tk.Button(
            button_frame,
            text="Show All",
            bg="#3498DB",
            fg="white",
            command=self.show_expenses,
            **button_style
        ).grid(
            row=1,
            column=0,
            padx=4,
            pady=3
        )


        tk.Button(
            button_frame,
            text="Search",
            bg="#8E44AD",
            fg="white",
            command=self.search_expense,
            **button_style
        ).grid(
            row=1,
            column=1,
            padx=4,
            pady=3
        )


        tk.Button(
            button_frame,
            text="Total Expense",
            bg="#16A085",
            fg="white",
            command=self.total_expense,
            **button_style
        ).grid(
            row=1,
            column=2,
            padx=4,
            pady=3
        )


        tk.Button(
            button_frame,
            text="Highest Expense",
            bg="#D68910",
            fg="white",
            command=self.highest_expense,
            **button_style
        ).grid(
            row=1,
            column=3,
            padx=4,
            pady=3
        )


        # ROW 3

        tk.Button(
            button_frame,
            text="Category Summary",
            bg="#2980B9",
            fg="white",
            command=self.category_summary,
            **button_style
        ).grid(
            row=2,
            column=0,
            padx=4,
            pady=3
        )


        tk.Button(
            button_frame,
            text="Monthly Summary",
            bg="#9B59B6",
            fg="white",
            command=self.monthly_summary,
            **button_style
        ).grid(
            row=2,
            column=1,
            padx=4,
            pady=3
        )


        tk.Button(
            button_frame,
            text="Expense Info",
            bg="#7F8C8D",
            fg="white",
            command=self.expense_info,
            **button_style
        ).grid(
            row=2,
            column=2,
            padx=4,
            pady=3
        )


        tk.Button(
            button_frame,
            text="Clear",
            bg="#95A5A6",
            fg="white",
            command=self.clear_entries,
            **button_style
        ).grid(
            row=2,
            column=3,
            padx=4,
            pady=3
        )


        # ROW 4

        tk.Button(
            button_frame,
            text="Save Data",
            bg="#1ABC9C",
            fg="white",
            command=self.save_expenses,
            **button_style
        ).grid(
            row=3,
            column=0,
            padx=4,
            pady=3
        )


        tk.Button(
            button_frame,
            text="Category Graph",
            bg="#34495E",
            fg="white",
            command=self.category_graph,
            **button_style
        ).grid(
            row=3,
            column=1,
            padx=4,
            pady=3
        )


        tk.Button(
            button_frame,
            text="Monthly Graph",
            bg="#34495E",
            fg="white",
            command=self.monthly_graph,
            **button_style
        ).grid(
            row=3,
            column=2,
            padx=4,
            pady=3
        )


        tk.Button(
            button_frame,
            text="Exit",
            bg="#2C3E50",
            fg="white",
            command=self.close_program,
            **button_style
        ).grid(
            row=3,
            column=3,
            padx=4,
            pady=3
        )


        # ======================================
        # FILTER + SORT FRAME
        # ======================================

        filter_frame = tk.LabelFrame(
            self.root,
            text="  Filter & Sort  ",
            bg="white",
            fg="#2C3E50",
            font=("Arial", 11, "bold"),
            padx=10,
            pady=8
        )

        filter_frame.pack(
            fill="x",
            padx=25,
            pady=8
        )


        # FILTER PERSON

        tk.Label(
            filter_frame,
            text="For:",
            bg="white",
            font=("Arial", 10, "bold")
        ).grid(
            row=0,
            column=0,
            padx=5
        )


        self.filter_person = ttk.Combobox(
            filter_frame,
            values=("All",) + self.people,
            width=14,
            state="readonly"
        )

        self.filter_person.set("All")

        self.filter_person.grid(
            row=0,
            column=1,
            padx=5
        )


        # FILTER CATEGORY

        tk.Label(
            filter_frame,
            text="Category:",
            bg="white",
            font=("Arial", 10, "bold")
        ).grid(
            row=0,
            column=2,
            padx=5
        )


        self.filter_category = ttk.Combobox(
            filter_frame,
            values=("All",) + self.categories,
            width=18,
            state="readonly"
        )

        self.filter_category.set("All")

        self.filter_category.grid(
            row=0,
            column=3,
            padx=5
        )


        # SORT

        tk.Label(
            filter_frame,
            text="Sort:",
            bg="white",
            font=("Arial", 10, "bold")
        ).grid(
            row=0,
            column=4,
            padx=5
        )


        self.sort_option = ttk.Combobox(
            filter_frame,
            values=(
                "None",
                "Amount: Low to High",
                "Amount: High to Low",
                "Title: A to Z",
                "Title: Z to A",
                "Date: New to Old",
                "Date: Old to New"
            ),
            width=22,
            state="readonly"
        )

        self.sort_option.set("None")

        self.sort_option.grid(
            row=0,
            column=5,
            padx=5
        )


        tk.Button(
            filter_frame,
            text="Apply Filter / Sort",
            bg="#2980B9",
            fg="white",
            font=("Arial", 9, "bold"),
            width=18,
            height=1,
            relief="flat",
            command=self.apply_filter_sort
        ).grid(
            row=0,
            column=6,
            padx=8
        )


        tk.Button(
            filter_frame,
            text="Reset",
            bg="#95A5A6",
            fg="white",
            font=("Arial", 9, "bold"),
            width=10,
            height=1,
            relief="flat",
            command=self.reset_filter
        ).grid(
            row=0,
            column=7,
            padx=5
        )


        # ======================================
        # TABLE
        # ======================================

        table_frame = tk.LabelFrame(
            self.root,
            text="  Expense Records  ",
            bg="white",
            fg="#2C3E50",
            font=("Arial", 11, "bold"),
            padx=8,
            pady=8
        )

        table_frame.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=8
        )


        columns = (
            "Title",
            "Amount",
            "For",
            "Category",
            "Date"
        )


        self.table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )


        for column in columns:

            self.table.heading(
                column,
                text=column
            )


        self.table.column(
            "Title",
            width=220,
            anchor="center"
        )

        self.table.column(
            "Amount",
            width=130,
            anchor="center"
        )

        self.table.column(
            "For",
            width=130,
            anchor="center"
        )

        self.table.column(
            "Category",
            width=230,
            anchor="center"
        )

        self.table.column(
            "Date",
            width=150,
            anchor="center"
        )


        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.table.yview
        )


        self.table.configure(
            yscrollcommand=scrollbar.set
        )


        self.table.pack(
            side="left",
            fill="both",
            expand=True
        )


        scrollbar.pack(
            side="right",
            fill="y"
        )


    # ==========================================
    # 5. CARD CREATOR
    # ==========================================

    def create_card(
        self,
        parent,
        title,
        color
    ):

        card = tk.LabelFrame(
            parent,
            text=title,
            bg="white",
            fg=color,
            font=("Arial", 10, "bold"),
            width=175,
            height=80
        )

        card.pack_propagate(False)


        value = tk.Label(
            card,
            text="0.00 TL",
            bg="white",
            fg=color,
            font=("Arial", 19, "bold")
        )

        value.pack(
            pady=13
        )


        if title == "Total Expenses":
            self.total_value = value

        elif title == "My Expenses":
            self.my_value = value

        elif title == "Children Expenses":
            self.children_value = value

        elif title == "House Expenses":
            self.house_value = value

        elif title == "Other Expenses":
            self.other_value = value

        elif title == "Number of Records":
            self.record_value = value


        return card


    # ==========================================
    # 6. ADD EXPENSE
    # ==========================================

    def add_expense(self):

        title = self.title_entry.get().strip()
        amount = self.amount_entry.get().strip()
        person = self.person_entry.get()
        category = self.category_entry.get()
        date = self.date_entry.get().strip()


        if (
            title == ""
            or amount == ""
            or person == ""
            or category == ""
            or date == ""
        ):

            messagebox.showwarning(
                "Warning",
                "Please fill all fields."
            )

            return


        try:

            amount = float(amount)

        except ValueError:

            messagebox.showerror(
                "Error",
                "Amount must be a number."
            )

            return


        if amount <= 0:

            messagebox.showerror(
                "Error",
                "Amount must be greater than 0."
            )

            return


        expense = Expense(
            title,
            amount,
            person,
            category,
            date
        )


        self.expenses.append(
            expense
        )


        self.save_expenses(
            show_message=False
        )


        self.clear_entries()

        self.show_expenses()


        messagebox.showinfo(
            "Success",
            "Expense added successfully!"
        )


    # ==========================================
    # 7. SHOW EXPENSES
    # ==========================================

    def show_expenses(
        self,
        expense_list=None
    ):

        if expense_list is None:

            expense_list = self.expenses


        for item in self.table.get_children():

            self.table.delete(item)


        for expense in expense_list:

            self.table.insert(
                "",
                tk.END,
                values=(
                    expense.title,
                    f"{expense.amount:.2f}",
                    expense.person,
                    expense.category,
                    expense.date
                )
            )


        self.update_dashboard()


    # ==========================================
    # 8. EDIT EXPENSE
    # ==========================================

    def edit_expense(self):

        selected = self.table.selection()


        if not selected:

            messagebox.showwarning(
                "Warning",
                "Please select an expense first."
            )

            return


        item = selected[0]


        values = self.table.item(
            item,
            "values"
        )


        title = values[0]
        amount = values[1]
        person = values[2]
        category = values[3]
        date = values[4]


        self.editing_index = None


        for index, expense in enumerate(
            self.expenses
        ):

            if (
                expense.title == title
                and f"{expense.amount:.2f}" == amount
                and expense.person == person
                and expense.category == category
                and expense.date == date
            ):

                self.editing_index = index

                break


        if self.editing_index is None:

            messagebox.showerror(
                "Error",
                "Expense could not be found."
            )

            return


        self.title_entry.delete(
            0,
            tk.END
        )

        self.title_entry.insert(
            0,
            title
        )


        self.amount_entry.delete(
            0,
            tk.END
        )

        self.amount_entry.insert(
            0,
            amount
        )


        self.person_entry.set(
            person
        )


        self.category_entry.set(
            category
        )


        self.date_entry.delete(
            0,
            tk.END
        )

        self.date_entry.insert(
            0,
            date
        )


        messagebox.showinfo(
            "Edit Mode",
            "Change the information and click "
            "'Update Expense'."
        )


    # ==========================================
    # 9. UPDATE EXPENSE
    # ==========================================

    def update_expense(self):

        if self.editing_index is None:

            messagebox.showwarning(
                "Warning",
                "Click 'Edit Expense' first."
            )

            return


        title = self.title_entry.get().strip()
        amount = self.amount_entry.get().strip()
        person = self.person_entry.get()
        category = self.category_entry.get()
        date = self.date_entry.get().strip()


        if (
            title == ""
            or amount == ""
            or person == ""
            or category == ""
            or date == ""
        ):

            messagebox.showwarning(
                "Warning",
                "Please fill all fields."
            )

            return


        try:

            amount = float(amount)

        except ValueError:

            messagebox.showerror(
                "Error",
                "Amount must be a number."
            )

            return


        if amount <= 0:

            messagebox.showerror(
                "Error",
                "Amount must be greater than 0."
            )

            return


        expense = self.expenses[
            self.editing_index
        ]


        expense.title = title
        expense.amount = amount
        expense.person = person
        expense.category = category
        expense.date = date


        self.save_expenses(
            show_message=False
        )


        self.editing_index = None

        self.clear_entries()

        self.show_expenses()


        messagebox.showinfo(
            "Updated",
            "Expense updated successfully!"
        )


    # ==========================================
    # 10. DELETE
    # ==========================================

    def delete_expense(self):

        selected = self.table.selection()


        if not selected:

            messagebox.showwarning(
                "Warning",
                "Please select an expense first."
            )

            return


        item = selected[0]


        values = self.table.item(
            item,
            "values"
        )


        title = values[0]
        amount = float(values[1])
        person = values[2]
        category = values[3]
        date = values[4]


        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Do you want to delete '{title}'?"
        )


        if not confirm:

            return


        for expense in self.expenses:

            if (
                expense.title == title
                and expense.amount == amount
                and expense.person == person
                and expense.category == category
                and expense.date == date
            ):

                self.expenses.remove(
                    expense
                )

                break


        self.save_expenses(
            show_message=False
        )


        self.show_expenses()


        messagebox.showinfo(
            "Deleted",
            f"{title} has been deleted."
        )


    # ==========================================
    # 11. SEARCH
    # ==========================================

    def search_expense(self):

        search_title = (
            self.title_entry
            .get()
            .strip()
            .lower()
        )


        if search_title == "":

            messagebox.showwarning(
                "Warning",
                "Enter a title first."
            )

            return


        found = []


        for expense in self.expenses:

            if search_title in expense.title.lower():

                found.append(
                    expense
                )


        if len(found) == 0:

            messagebox.showerror(
                "Not Found",
                "Expense not found."
            )

            return


        result = ""


        for expense in found:

            result += (
                f"Title: {expense.title}\n"
                f"Amount: {expense.amount:.2f} TL\n"
                f"For: {expense.person}\n"
                f"Category: {expense.category}\n"
                f"Date: {expense.date}\n"
                f"----------------------\n"
            )


        messagebox.showinfo(
            "Search Result",
            result
        )


    # ==========================================
    # 12. FILTER + SORT
    # ==========================================

    def apply_filter_sort(self):

        filtered = []


        selected_person = (
            self.filter_person.get()
        )


        selected_category = (
            self.filter_category.get()
        )


        # --------------------------------------
        # FILTER
        # --------------------------------------

        for expense in self.expenses:

            person_match = (
                selected_person == "All"
                or expense.person == selected_person
            )


            category_match = (
                selected_category == "All"
                or expense.category == selected_category
            )


            if (
                person_match
                and category_match
            ):

                filtered.append(
                    expense
                )


        # --------------------------------------
        # SORT
        # --------------------------------------

        sort_option = self.sort_option.get()


        if sort_option == "Amount: Low to High":

            filtered.sort(
                key=lambda x: x.amount
            )


        elif sort_option == "Amount: High to Low":

            filtered.sort(
                key=lambda x: x.amount,
                reverse=True
            )


        elif sort_option == "Title: A to Z":

            filtered.sort(
                key=lambda x: x.title.lower()
            )


        elif sort_option == "Title: Z to A":

            filtered.sort(
                key=lambda x: x.title.lower(),
                reverse=True
            )


        elif sort_option == "Date: New to Old":

            filtered.sort(
                key=lambda x: x.date,
                reverse=True
            )


        elif sort_option == "Date: Old to New":

            filtered.sort(
                key=lambda x: x.date
            )


        self.show_expenses(
            filtered
        )


        if len(filtered) == 0:

            messagebox.showinfo(
                "Filter Result",
                "No expenses found."
            )


    # ==========================================
    # 13. RESET FILTER
    # ==========================================

    def reset_filter(self):

        self.filter_person.set(
            "All"
        )

        self.filter_category.set(
            "All"
        )

        self.sort_option.set(
            "None"
        )

        self.show_expenses()


    # ==========================================
    # 14. TOTAL
    # ==========================================

    def total_expense(self):

        if len(self.expenses) == 0:

            messagebox.showwarning(
                "Warning",
                "No expenses available."
            )

            return


        total = 0


        for expense in self.expenses:

            total += expense.amount


        messagebox.showinfo(
            "Total Expense",
            f"Total Expenses:\n\n"
            f"{total:.2f} TL"
        )


    # ==========================================
    # 15. HIGHEST EXPENSE
    # ==========================================

    def highest_expense(self):

        if len(self.expenses) == 0:

            messagebox.showwarning(
                "Warning",
                "No expenses available."
            )

            return


        highest = self.expenses[0]


        for expense in self.expenses:

            if expense.amount > highest.amount:

                highest = expense


        messagebox.showinfo(
            "Highest Expense",
            f"Title: {highest.title}\n"
            f"Amount: {highest.amount:.2f} TL\n"
            f"For: {highest.person}\n"
            f"Category: {highest.category}\n"
            f"Date: {highest.date}"
        )


    # ==========================================
    # 16. CATEGORY SUMMARY
    # ==========================================

    def category_summary(self):

        if len(self.expenses) == 0:

            messagebox.showwarning(
                "Warning",
                "No expenses available."
            )

            return


        summary = {}


        for expense in self.expenses:

            if expense.category in summary:

                summary[
                    expense.category
                ] += expense.amount

            else:

                summary[
                    expense.category
                ] = expense.amount


        result = (
            "Category Summary\n"
            "====================\n\n"
        )


        for category, amount in summary.items():

            result += (
                f"{category}: "
                f"{amount:.2f} TL\n"
            )


        messagebox.showinfo(
            "Category Summary",
            result
        )


    # ==========================================
    # 17. MONTHLY SUMMARY
    # ==========================================

    def monthly_summary(self):

        if len(self.expenses) == 0:

            messagebox.showwarning(
                "Warning",
                "No expenses available."
            )

            return


        monthly = {}


        for expense in self.expenses:

            month = expense.date[3:10]


            if month in monthly:

                monthly[month] += expense.amount

            else:

                monthly[month] = expense.amount


        result = (
            "Monthly Summary\n"
            "====================\n\n"
        )


        for month, amount in monthly.items():

            result += (
                f"{month}: "
                f"{amount:.2f} TL\n"
            )


        messagebox.showinfo(
            "Monthly Summary",
            result
        )


    # ==========================================
    # 18. CATEGORY GRAPH
    # ==========================================

    def category_graph(self):

        if len(self.expenses) == 0:

            messagebox.showwarning(
                "Warning",
                "No expenses available."
            )

            return


        summary = {}


        for expense in self.expenses:

            if expense.category in summary:

                summary[
                    expense.category
                ] += expense.amount

            else:

                summary[
                    expense.category
                ] = expense.amount


        categories = list(
            summary.keys()
        )

        amounts = list(
            summary.values()
        )


        plt.figure(
            figsize=(10, 6)
        )


        plt.bar(
            categories,
            amounts
        )


        plt.title(
            "Expenses by Category"
        )

        plt.xlabel(
            "Category"
        )

        plt.ylabel(
            "Amount (TL)"
        )


        plt.xticks(
            rotation=30,
            ha="right"
        )


        plt.tight_layout()

        plt.show()


    # ==========================================
    # 19. MONTHLY GRAPH
    # ==========================================

    def monthly_graph(self):

        if len(self.expenses) == 0:

            messagebox.showwarning(
                "Warning",
                "No expenses available."
            )

            return


        monthly = {}


        for expense in self.expenses:

            month = expense.date[3:10]


            if month in monthly:

                monthly[month] += expense.amount

            else:

                monthly[month] = expense.amount


        months = list(
            monthly.keys()
        )

        amounts = list(
            monthly.values()
        )


        plt.figure(
            figsize=(10, 6)
        )


        plt.plot(
            months,
            amounts,
            marker="o"
        )


        plt.title(
            "Monthly Expenses"
        )

        plt.xlabel(
            "Month"
        )

        plt.ylabel(
            "Amount (TL)"
        )


        plt.xticks(
            rotation=30
        )


        plt.grid(
            True,
            alpha=0.3
        )


        plt.tight_layout()

        plt.show()


    # ==========================================
    # 20. EXPENSE INFO
    # ==========================================

    def expense_info(self):

        categories = ""


        for category in self.categories:

            categories += (
                "- "
                + category
                + "\n"
            )


        messagebox.showinfo(
            "Expense System Information",

            f"System: "
            f"{self.user_info['system']}\n\n"

            f"Currency: "
            f"{self.user_info['currency']}\n\n"

            f"People / Expense Types:\n"
            f"- Me\n"
            f"- Children\n"
            f"- House Expenses\n"
            f"- Other Expenses\n\n"

            f"Categories:\n"
            f"{categories}\n"

            f"Cities:\n"
            f"{', '.join(self.cities)}"
        )


    # ==========================================
    # 21. CLEAR
    # ==========================================

    def clear_entries(self):

        self.title_entry.delete(
            0,
            tk.END
        )


        self.amount_entry.delete(
            0,
            tk.END
        )


        self.person_entry.set(
            ""
        )


        self.category_entry.set(
            ""
        )


        self.date_entry.delete(
            0,
            tk.END
        )


        self.editing_index = None


    # ==========================================
    # 22. UPDATE DASHBOARD
    # ==========================================

    def update_dashboard(self):

        total = 0
        my_total = 0
        children_total = 0
        house_total = 0
        other_total = 0

        for expense in self.expenses:

            total += expense.amount

            if expense.person == "Me":
                my_total += expense.amount

            elif expense.person == "Children":
                children_total += expense.amount

            elif expense.person == "House Expenses":
                house_total += expense.amount

            elif expense.person == "Other Expenses":
                other_total += expense.amount

        self.total_value.config(
            text=f"{total:.2f} TL"
        )

        self.my_value.config(
            text=f"{my_total:.2f} TL"
        )

        self.children_value.config(
            text=f"{children_total:.2f} TL"
        )

        self.house_value.config(
            text=f"{house_total:.2f} TL"
        )

        self.other_value.config(
            text=f"{other_total:.2f} TL"
        )

        self.record_value.config(
            text=str(len(self.expenses))
        )


    # ==========================================
    # 23. SAVE
    # ==========================================

    def save_expenses(
        self,
        show_message=True
    ):

        data = []


        for expense in self.expenses:

            data.append(
                {
                    "title": expense.title,
                    "amount": expense.amount,
                    "person": expense.person,
                    "category": expense.category,
                    "date": expense.date
                }
            )


        try:

            with open(
                self.file_name,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    data,
                    file,
                    indent=4,
                    ensure_ascii=False
                )


            if show_message:

                messagebox.showinfo(
                    "Saved",
                    "All expenses have been saved."
                )


        except Exception as error:

            messagebox.showerror(
                "Save Error",
                str(error)
            )


    # ==========================================
    # 24. LOAD
    # ==========================================

    def load_expenses(self):

        if not os.path.exists(
            self.file_name
        ):

            return


        try:

            with open(
                self.file_name,
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)


            for item in data:

                expense = Expense(
                    item["title"],
                    float(item["amount"]),
                    item["person"],
                    item["category"],
                    item["date"]
                )


                self.expenses.append(
                    expense
                )


        except Exception as error:

            messagebox.showerror(
                "Load Error",
                str(error)
            )


    # ==========================================
    # 25. CLOSE
    # ==========================================

    def close_program(self):

        self.save_expenses(
            show_message=False
        )

        self.root.destroy()


# ==========================================
# 26. START PROGRAM
# ==========================================

root = tk.Tk()

app = ExpenseApp(root)

root.mainloop()