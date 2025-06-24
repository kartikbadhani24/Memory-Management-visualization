import tkinter as tk
from tkinter import messagebox, simpledialog
from math import ceil

class Block:
    def __init__(self, id, size):
        self.id = id
        self.size = size
        self.allocatedTo = -1

class Process:
    def __init__(self, id, size):
        self.id = id
        self.size = size

class MemorySimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("💥 Memory Allocation Simulator 💥")
        self.root.geometry("900x700")
        self.root.configure(bg="#1e1e2f")

        self.blocks = []
        self.processes = []

        self.setup_inputs()

    def setup_inputs(self):
        self.clear_frame()

        tk.Label(self.root, text="Number of Memory Blocks:", font=("Arial", 14), fg="white", bg="#1e1e2f").pack(pady=10)
        self.block_entry = tk.Entry(self.root, font=("Arial", 14), width=10)
        self.block_entry.pack()

        tk.Label(self.root, text="Number of Processes:", font=("Arial", 14), fg="white", bg="#1e1e2f").pack(pady=10)
        self.process_entry = tk.Entry(self.root, font=("Arial", 14), width=10)
        self.process_entry.pack()

        tk.Button(self.root, text="🎯 Submit", font=("Arial", 14, "bold"), bg="#61afef", fg="black",
                  command=self.init_blocks_processes).pack(pady=20)

    def init_blocks_processes(self):
        try:
            num_blocks = int(self.block_entry.get())
            num_processes = int(self.process_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid integers.")
            return

        self.blocks.clear()
        self.processes.clear()

        for i in range(num_blocks):
            size = simpledialog.askinteger("Block Size", f"Enter size of Block {i+1} (KB):", parent=self.root)
            self.blocks.append(Block(i+1, size))

        for i in range(num_processes):
            size = simpledialog.askinteger("Process Size", f"Enter size of Process {i+1} (KB):", parent=self.root)
            self.processes.append(Process(i+1, size))

        self.show_menu()

    def show_menu(self):
        self.clear_frame()

        btn_frame = tk.Frame(self.root, bg="#1e1e2f")
        btn_frame.pack(pady=10)

        options = [
            ("First Fit", self.first_fit),
            ("Best Fit", self.best_fit),
            ("Worst Fit", self.worst_fit),
            ("Buddy System", self.buddy_system),
            ("Paging Simulation", self.paging),
            ("Reset Allocations", self.reset_allocations),
            ("Deallocate Process", self.deallocate),
            ("Search Process", self.search_process),
            ("Exit", self.root.quit)
        ]

        for text, command in options:
            tk.Button(btn_frame, text=text, font=("Arial", 12, "bold"), width=22, height=1,
                      bg="#98c379", fg="black", activebackground="#c678dd",
                      command=command).pack(pady=5)

        self.output = tk.Text(self.root, height=20, width=90, font=("Consolas", 12), bg="#282c34", fg="#abb2bf")
        self.output.pack(pady=20)

    def reset_allocations(self):
        for b in self.blocks:
            b.allocatedTo = -1
        self.display_output("🚨 All allocations reset. Memory is now free.")

    def display_output(self, msg):
        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, "🧠 " + msg + "\n\n")
        self.display_memory()
        self.show_statistics()

    def display_memory(self):
        for b in self.blocks:
            bar_length = max(20, b.size // 5)  # Bigger bar for better visuals
            fill_char = "#" if b.allocatedTo != -1 else "-"
            bar = fill_char * bar_length
            label = f"{b.size}KB"
            middle = len(bar) // 2
            if len(label) <= len(bar):
                bar = bar[:middle - len(label)//2] + label + bar[middle + len(label)//2:]
            status = f"Block {b.id:>2} ▏{bar}▕ → " + (f"Process {b.allocatedTo}" if b.allocatedTo != -1 else "Free")
            self.output.insert(tk.END, status + "\n")



    def show_statistics(self):
        total = sum(b.size for b in self.blocks)
        used = sum(b.size for b in self.blocks if b.allocatedTo != -1)
        fragmentation = sum(b.size for b in self.blocks if b.allocatedTo == -1)
        efficiency = (used / total) * 100 if total > 0 else 0
        self.output.insert(tk.END, f"\n📊 Total: {total} KB | Used: {used} KB | Fragmentation: {fragmentation} KB\n")
        self.output.insert(tk.END, f"⚙️ Efficiency: {efficiency:.2f}%\n")

    def first_fit(self):
        self.reset_allocations()
        for p in self.processes:
            for b in self.blocks:
                if b.allocatedTo == -1 and b.size >= p.size:
                    b.allocatedTo = p.id
                    break
        self.display_output("🚀 First Fit Applied")

    def best_fit(self):
        self.reset_allocations()
        for p in self.processes:
            best = None
            for b in self.blocks:
                if b.allocatedTo == -1 and b.size >= p.size:
                    if best is None or b.size < best.size:
                        best = b
            if best:
                best.allocatedTo = p.id
        self.display_output("💎 Best Fit Applied")

    def worst_fit(self):
        self.reset_allocations()
        for p in self.processes:
            worst = None
            for b in self.blocks:
                if b.allocatedTo == -1 and b.size >= p.size:
                    if worst is None or b.size > worst.size:
                        worst = b
            if worst:
                worst.allocatedTo = p.id
        self.display_output("🔥 Worst Fit Applied")

    def buddy_system(self):
        self.reset_allocations()
        for p in self.processes:
            for b in self.blocks:
                if b.allocatedTo == -1 and b.size >= p.size:
                    while (b.size // 2) >= p.size:
                        b.size //= 2
                    b.allocatedTo = p.id
                    break
        self.display_output("👯 Buddy System Applied")

    def paging(self):
        pageSize = 100
        msg = "📘 Paging Simulation:\n"
        for p in self.processes:
            pages = ceil(p.size / pageSize)
            msg += f"Process {p.id} → {pages} pages ({p.size} KB)\n"
        self.display_output(msg)

    def deallocate(self):
        pid = simpledialog.askinteger("Deallocate", "Enter Process ID to deallocate:", parent=self.root)
        if pid is None:
            return
        found = False
        for b in self.blocks:
            if b.allocatedTo == pid:
                b.allocatedTo = -1
                found = True
        self.display_output(f"🧹 Process {pid} {'deallocated' if found else 'not found'}.")


    def search_process(self):
        pid = simpledialog.askinteger("Search", "Enter Process ID to search:", parent=self.root)
        if pid is None:
            return
        found = False
        for b in self.blocks:
            if b.allocatedTo == pid:
                self.display_output(f"🔎 Process {pid} is in Block {b.id} (Size: {b.size} KB)")
                found = True
                break
        if not found:
            self.display_output(f"❌ Process {pid} not found in memory.")


    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = MemorySimulator(root)
    root.mainloop()
