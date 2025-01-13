import tkinter as tk
from time import time, sleep

class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        
        # Stopwatch variables
        self.start_time = None
        self.running = False
        self.elapsed_time = 0
        
        # Display label
        self.time_label = tk.Label(root, text="00:00:00", font=("Arial", 40))
        self.time_label.pack(pady=20)
        
        # Buttons
        self.start_button = tk.Button(root, text="Start", command=self.start, font=("Arial", 14))
        self.start_button.pack(side=tk.LEFT, padx=10, pady=20)
        
        self.stop_button = tk.Button(root, text="Stop", command=self.stop, font=("Arial", 14))
        self.stop_button.pack(side=tk.LEFT, padx=10, pady=20)
        
        self.reset_button = tk.Button(root, text="Reset", command=self.reset, font=("Arial", 14))
        self.reset_button.pack(side=tk.LEFT, padx=10, pady=20)
    
    def update_time(self):
        if self.running:
            current_time = time()
            self.elapsed_time = current_time - self.start_time
            formatted_time = self.format_time(self.elapsed_time)
            self.time_label.config(text=formatted_time)
            self.root.after(50, self.update_time)  # Updates every 50ms

    def format_time(self, elapsed):
        hours, rem = divmod(elapsed, 3600)
        minutes, seconds = divmod(rem, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time() - self.elapsed_time  # Adjust for elapsed time
            self.update_time()
    
    def stop(self):
        if self.running:
            self.running = False
    
    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.time_label.config(text="00:00:00")

if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()
