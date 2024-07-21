# # import tkinter as tk
# # from tkinter import ttk
# # import sqlite3

# # class CSIDashboard(tk.Tk):
# #     def __init__(self):
# #         super().__init__()

# #         self.title("CSI Dashboard")
# #         self.geometry("800x600")

# #         self.create_widgets()
# #         self.load_data()

# #     def create_widgets(self):
# #         # Create query execution frame
# #         query_frame = ttk.LabelFrame(self, text="Execute Query")
# #         query_frame.pack(padx=10, pady=10, fill=tk.X)

# #         self.query_entry = ttk.Entry(query_frame, width=100, height=50)
# #         self.query_entry.pack(side=tk.LEFT, padx=5, pady=5)

# #         execute_button = ttk.Button(query_frame, text="Execute", command=self.execute_query)
# #         execute_button.pack(side=tk.LEFT, padx=5, pady=5)

# #         # Create dashboard view frame
# #         dashboard_frame = ttk.LabelFrame(self, text="Dashboard View")
# #         dashboard_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# #         # Create a treeview to display the data
# #         self.tree = ttk.Treeview(dashboard_frame, columns=("Name", "Current Version", "Latest Version", "CVE Count", "ONTAP Version"), show="headings")
# #         self.tree.heading("Name", text="Package Name")
# #         self.tree.heading("Current Version", text="Current Version")
# #         self.tree.heading("Latest Version", text="Latest Version")
# #         self.tree.heading("CVE Count", text="CVE Count")
# #         self.tree.heading("ONTAP Version", text="ONTAP Version")
# #         self.tree.pack(fill=tk.BOTH, expand=True)

# #         # Add a scrollbar
# #         scrollbar = ttk.Scrollbar(dashboard_frame, orient=tk.VERTICAL, command=self.tree.yview)
# #         self.tree.configure(yscroll=scrollbar.set)
# #         scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# #     def load_data(self):
# #         # Clear existing data
# #         for i in self.tree.get_children():
# #             self.tree.delete(i)

# #         # Fetch data from SQLite
# #         conn = sqlite3.connect('csi_dashboard.db')
# #         cursor = conn.cursor()
# #         cursor.execute("SELECT name, current_version, latest_version, cve_count, ontap_version FROM packages")
# #         rows = cursor.fetchall()

# #         # Insert data into treeview
# #         for row in rows:
# #             self.tree.insert("", tk.END, values=row)

# #         conn.close()

# #     def execute_query(self):
# #         query = self.query_entry.get()
# #         if not query:
# #             return

# #         # Clear existing data
# #         for i in self.tree.get_children():
# #             self.tree.delete(i)

# #         try:
# #             conn = sqlite3.connect('csi_dashboard.db')
# #             cursor = conn.cursor()
# #             cursor.execute(query)
# #             rows = cursor.fetchall()

# #             # Update treeview with query results
# #             if rows:
# #                 # Update column headings
# #                 self.tree["columns"] = tuple(range(len(rows[0])))
# #                 for i, col in enumerate(cursor.description):
# #                     self.tree.heading(i, text=col[0])

# #                 # Insert data
# #                 for row in rows:
# #                     self.tree.insert("", tk.END, values=row)
# #             else:
# #                 self.tree.insert("", tk.END, values=("No results",))

# #             conn.close()
# #         except sqlite3.Error as e:
# #             self.tree.insert("", tk.END, values=(f"Error: {str(e)}",))

# # if __name__ == "__main__":
# #     app = CSIDashboard()
# #     app.mainloop()

# import tkinter as tk
# from tkinter import ttk, messagebox, filedialog
# import sqlite3
# import csv

# class CSIDashboard(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         self.title("CSI Dashboard")
#         self.geometry("1000x700")

#         self.create_widgets()
#         self.load_data()

#     def create_widgets(self):
#         # Create main frame
#         main_frame = ttk.Frame(self)
#         main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

#         # Create query execution frame
#         query_frame = ttk.LabelFrame(main_frame, text="Execute Query")
#         query_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

#         # Create text widget for query input
#         self.query_text = tk.Text(query_frame, wrap=tk.WORD, width=80, height=10)
#         self.query_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

#         # Add a scrollbar to the text widget
#         query_scrollbar = ttk.Scrollbar(query_frame, orient=tk.VERTICAL, command=self.query_text.yview)
#         self.query_text.configure(yscrollcommand=query_scrollbar.set)
#         query_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

#         # Create button frame
#         button_frame = ttk.Frame(main_frame)
#         button_frame.pack(fill=tk.X, padx=10, pady=5)

#         execute_button = ttk.Button(button_frame, text="Execute Query", command=self.execute_query)
#         execute_button.pack(side=tk.LEFT, padx=5)

#         clear_button = ttk.Button(button_frame, text="Clear Query", command=self.clear_query)
#         clear_button.pack(side=tk.LEFT, padx=5)

#         export_button = ttk.Button(button_frame, text="Export Results", command=self.export_results)
#         export_button.pack(side=tk.LEFT, padx=5)

#         # Create dashboard view frame
#         dashboard_frame = ttk.LabelFrame(main_frame, text="Dashboard View")
#         dashboard_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

#         # Create a treeview to display the data
#         self.tree = ttk.Treeview(dashboard_frame, columns=("Name", "Current Version", "Latest Version", "CVE Count", "ONTAP Version"), show="headings")
#         self.tree.heading("Name", text="Package Name")
#         self.tree.heading("Current Version", text="Current Version")
#         self.tree.heading("Latest Version", text="Latest Version")
#         self.tree.heading("CVE Count", text="CVE Count")
#         self.tree.heading("ONTAP Version", text="ONTAP Version")
#         self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#         # Add a scrollbar to the treeview
#         tree_scrollbar = ttk.Scrollbar(dashboard_frame, orient=tk.VERTICAL, command=self.tree.yview)
#         self.tree.configure(yscroll=tree_scrollbar.set)
#         tree_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

#     def load_data(self):
#         self.execute_query(default_query="SELECT name, current_version, latest_version, cve_count, ontap_version FROM packages")

#     def execute_query(self, default_query=None):
#         # Clear existing data
#         for i in self.tree.get_children():
#             self.tree.delete(i)

#         query = default_query or self.query_text.get("1.0", tk.END).strip()
#         if not query:
#             messagebox.showwarning("Empty Query", "Please enter a SQL query.")
#             return

#         try:
#             conn = sqlite3.connect('csi_dashboard.db')
#             cursor = conn.cursor()
#             cursor.execute(query)
#             rows = cursor.fetchall()

#             # Update treeview with query results
#             if rows:
#                 # Update column headings
#                 self.tree["columns"] = tuple(range(len(rows[0])))
#                 for i, col in enumerate(cursor.description):
#                     self.tree.heading(i, text=col[0])
#                     self.tree.column(i, width=100)  # Set a default width

#                 # Insert data
#                 for row in rows:
#                     self.tree.insert("", tk.END, values=row)
#             else:
#                 messagebox.showinfo("Query Result", "The query returned no results.")

#             conn.close()
#         except sqlite3.Error as e:
#             messagebox.showerror("Database Error", f"An error occurred: {str(e)}")

#     def clear_query(self):
#         self.query_text.delete("1.0", tk.END)

#     def export_results(self):
#         if not self.tree.get_children():
#             messagebox.showwarning("No Data", "There's no data to export.")
#             return

#         file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
#         if not file_path:
#             return

#         try:
#             with open(file_path, 'w', newline='') as csvfile:
#                 csv_writer = csv.writer(csvfile)
                
#                 # Write headers
#                 headers = [self.tree.heading(col)["text"] for col in self.tree["columns"]]
#                 csv_writer.writerow(headers)
                
#                 # Write data
#                 for item in self.tree.get_children():
#                     row = self.tree.item(item)['values']
#                     csv_writer.writerow(row)
            
#             messagebox.showinfo("Export Successful", f"Data exported successfully to {file_path}")
#         except Exception as e:
#             messagebox.showerror("Export Error", f"An error occurred while exporting: {str(e)}")

# if __name__ == "__main__":
#     app = CSIDashboard()
#     app.mainloop()


import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3
import csv

class CSIDashboard(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("CSI Dashboard")
        self.geometry("1000x700")
        self.configure(bg="#f0f0f0")  # Light gray background for the main window

        # Configure styles
        self.configure_styles()

        self.create_widgets()
        self.load_data()

    def configure_styles(self):
        style = ttk.Style(self)
        style.theme_use('clam')
        
        # Configure colors
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TLabelframe", background="#f0f0f0")
        style.configure("TLabelframe.Label", foreground="#2c3e50", background="#f0f0f0", font=('Arial', 12, 'bold'))
        style.configure("TButton", foreground="#ffffff", background="#3498db", font=('Arial', 10))
        style.map("TButton", background=[('active', '#2980b9')])
        style.configure("Treeview", background="#ffffff", fieldbackground="#ffffff", foreground="#2c3e50")
        style.configure("Treeview.Heading", background="#3498db", foreground="#ffffff", font=('Arial', 10, 'bold'))
        style.map("Treeview", background=[('selected', '#2980b9')], foreground=[('selected', '#ffffff')])

    def create_widgets(self):
        # Create main frame
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create query execution frame
        query_frame = ttk.LabelFrame(main_frame, text="Execute Query")
        query_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Create text widget for query input
        self.query_text = tk.Text(query_frame, wrap=tk.WORD, width=80, height=10, bg="#ffffff", fg="#2c3e50", font=('Arial', 11))
        self.query_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Add a scrollbar to the text widget
        query_scrollbar = ttk.Scrollbar(query_frame, orient=tk.VERTICAL, command=self.query_text.yview)
        self.query_text.configure(yscrollcommand=query_scrollbar.set)
        query_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create button frame
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, padx=10, pady=5)

        execute_button = ttk.Button(button_frame, text="Execute Query", command=self.execute_query)
        execute_button.pack(side=tk.LEFT, padx=5)

        clear_button = ttk.Button(button_frame, text="Clear Query", command=self.clear_query)
        clear_button.pack(side=tk.LEFT, padx=5)

        export_button = ttk.Button(button_frame, text="Export Results", command=self.export_results)
        export_button.pack(side=tk.LEFT, padx=5)

        # Create dashboard view frame
        dashboard_frame = ttk.LabelFrame(main_frame, text="Dashboard View")
        dashboard_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Create a treeview to display the data
        self.tree = ttk.Treeview(dashboard_frame, columns=("Name", "Current Version", "Latest Version", "CVE Count", "ONTAP Version"), show="headings")
        self.tree.heading("Name", text="Package Name")
        self.tree.heading("Current Version", text="Current Version")
        self.tree.heading("Latest Version", text="Latest Version")
        self.tree.heading("CVE Count", text="CVE Count")
        self.tree.heading("ONTAP Version", text="ONTAP Version")
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add a scrollbar to the treeview
        tree_scrollbar = ttk.Scrollbar(dashboard_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=tree_scrollbar.set)
        tree_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def load_data(self):
        self.execute_query(default_query="SELECT name, current_version, latest_version, cve_count, ontap_version FROM packages")

    def execute_query(self, default_query=None):
        # Clear existing data
        for i in self.tree.get_children():
            self.tree.delete(i)

        query = default_query or self.query_text.get("1.0", tk.END).strip()
        if not query:
            messagebox.showwarning("Empty Query", "Please enter a SQL query.")
            return

        try:
            conn = sqlite3.connect('csi_dashboard.db')
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()

            # Update treeview with query results
            if rows:
                # Update column headings
                self.tree["columns"] = tuple(range(len(rows[0])))
                for i, col in enumerate(cursor.description):
                    self.tree.heading(i, text=col[0])
                    self.tree.column(i, width=100)  # Set a default width

                # Insert data
                for row in rows:
                    self.tree.insert("", tk.END, values=row)
            else:
                messagebox.showinfo("Query Result", "The query returned no results.")

            conn.close()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {str(e)}")

    def clear_query(self):
        self.query_text.delete("1.0", tk.END)

    def export_results(self):
        if not self.tree.get_children():
            messagebox.showwarning("No Data", "There's no data to export.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return

        try:
            with open(file_path, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                
                # Write headers
                headers = [self.tree.heading(col)["text"] for col in self.tree["columns"]]
                csv_writer.writerow(headers)
                
                # Write data
                for item in self.tree.get_children():
                    row = self.tree.item(item)['values']
                    csv_writer.writerow(row)
            
            messagebox.showinfo("Export Successful", f"Data exported successfully to {file_path}")
        except Exception as e:
            messagebox.showerror("Export Error", f"An error occurred while exporting: {str(e)}")

if __name__ == "__main__":
    app = CSIDashboard()
    app.mainloop()