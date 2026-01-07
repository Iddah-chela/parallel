import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import time
import json
from multiprocessing import cpu_count

from serial_word_count import serial_word_count
from parallel_word_count import parallel_word_count
from distributed_word_count import distributed_word_count


class WordCountUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Parallel & Distributed Word Count")
        self.root.geometry("700x420")

        self.file_path = None

        self.create_widgets()

    def create_widgets(self):
        # Top frame
        top_frame = tk.Frame(self.root)
        top_frame.pack(pady=10)

        select_btn = tk.Button(
            top_frame, text="Select File (.txt / .json)", command=self.select_file
        )
        select_btn.pack(side=tk.LEFT, padx=5)

        run_btn = tk.Button(
            top_frame, text="Run Analysis", command=self.run_analysis
        )
        run_btn.pack(side=tk.LEFT, padx=5)

        # Table
        columns = ("Method", "Workers", "Time (s)", "Total Words")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")

        self.tree.pack(expand=True, fill="both", pady=10)

        # Fastest label
        self.fastest_label = tk.Label(
            self.root, text="", font=("Arial", 10, "bold")
        )
        self.fastest_label.pack(pady=5)

    def select_file(self):
        self.file_path = filedialog.askopenfilename(
            filetypes=[
                ("Text Files", "*.txt"),
                ("JSON Files", "*.json")
            ]
        )
        if self.file_path:
            messagebox.showinfo("File Selected", self.file_path)

    def load_words(self, path):
        # Handle TXT
        if path.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                return f.read().lower().split()

        # Handle JSON
        elif path.endswith(".json"):
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Convert all values to string
            text = json.dumps(data)
            return text.lower().split()

        else:
            raise ValueError("Unsupported file format")

    def measure(self, func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        return end - start, sum(result.values())

    def run_analysis(self):
        if not self.file_path:
            messagebox.showwarning("No File", "Please select a file first.")
            return

        # Clear table
        for row in self.tree.get_children():
            self.tree.delete(row)

        results = []

        # Serial
        t_serial, words_serial = self.measure(
            serial_word_count, self.file_path
        )
        results.append(("Serial", 1, t_serial, words_serial))

        # Parallel
        threads = 4
        t_parallel, words_parallel = self.measure(
            parallel_word_count, self.file_path, threads
        )
        results.append(("Parallel (Threads)", threads, t_parallel, words_parallel))

        # Distributed
        workers = cpu_count()
        t_distributed, words_distributed = self.measure(
            distributed_word_count, self.file_path, workers
        )
        results.append(("Distributed (Processes)", workers, t_distributed, words_distributed))

        # Insert into table
        for r in results:
            self.tree.insert(
                "", "end",
                values=(r[0], r[1], f"{r[2]:.3f}", r[3])
            )

        fastest = min(results, key=lambda x: x[2])
        self.fastest_label.config(
            text=f"Fastest Method: {fastest[0]}"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = WordCountUI(root)
    root.mainloop()
