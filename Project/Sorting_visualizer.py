import tkinter as tk
from tkinter import ttk
import random
import time

#GLOBAL VARIABLES
data = []
running = False
complexities = {
    "Bubble Sort": ("O(n)", "O(n^2)", "O(n^2)", "O(1)"),
    "Selection Sort": ("O(n^2)", "O(n^2)", "O(n^2)", "O(1)"),
    "Insertion Sort": ("O(n)", "O(n^2)", "O(n^2)", "O(1)"),
    "Merge Sort": ("O(n log n)", "O(n log n)", "O(n log n)", "O(n)"),
    "Quick Sort": ("O(n log n)", "O(n log n)", "O(n^2)", "O(log n)")
}

#MAIN WINDOW
root = tk.Tk()
root.title("Sorting Visualizer")
root.maxsize(900, 600)
root.config(bg="black")

#GENERATE DATA
def generate_data():
    global data, running
    running = False
    data = [random.randint(10, 300) for _ in range(30)]
    draw_data(data, ['red'] * len(data))

#DRAW DATA
def draw_data(data, color_array):
    canvas.delete("all")
    c_height = 400
    c_width = 850
    bar_width = c_width / (len(data) + 1)

    normalized = [i / max(data) for i in data]

    for i, height in enumerate(normalized):
        x0 = i * bar_width + 10
        y0 = c_height - height * 300
        x1 = (i + 1) * bar_width
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
        canvas.create_text(x0 + 2, y0, anchor=tk.SW, text=str(data[i]))

    root.update_idletasks()

#STOP FUNCTION
def stop_sorting():
    global running
    running = False

#SORTING ALGORITHMS
    #bubble sort
def bubble_sort():
    global running
    for i in range(len(data)):
        if not running:
            return
        for j in range(len(data) - i - 1):
            if not running:
                return

            draw_data(data, ['yellow' if x == j or x == j+1 else 'red' for x in range(len(data))])
            time.sleep(speed_scale.get())

            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

    draw_data(data, ['green'] * len(data))

    #selection sort
def selection_sort():
    global running
    for i in range(len(data)):
        if not running:
            return

        min_idx = i
        for j in range(i+1, len(data)):
            if not running:
                return

            draw_data(data, ['yellow' if x == j or x == min_idx else 'red' for x in range(len(data))])
            time.sleep(speed_scale.get())

            if data[j] < data[min_idx]:
                min_idx = j

        data[i], data[min_idx] = data[min_idx], data[i]

    draw_data(data, ['green'] * len(data))

    #insertion sort
def insertion_sort():
    global running
    for i in range(1, len(data)):
        if not running:
            return

        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            if not running:
                return

            data[j+1] = data[j]
            j -= 1

            draw_data(data, ['yellow' if x == j or x == j+1 else 'red' for x in range(len(data))])
            time.sleep(speed_scale.get())

        data[j+1] = key

    draw_data(data, ['green'] * len(data))

#MERGE SORT
def merge_sort(left, right):
    global running
    if not running:
        return

    if left < right:
        mid = (left + right) // 2
        merge_sort(left, mid)
        merge_sort(mid+1, right)
        merge(left, mid, right)

def merge(left, mid, right):
    global running
    left_part = data[left:mid+1]
    right_part = data[mid+1:right+1]

    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        if not running:
            return

        draw_data(data, ['yellow' if x >= left and x <= right else 'red' for x in range(len(data))])
        time.sleep(speed_scale.get())

        if left_part[i] <= right_part[j]:
            data[k] = left_part[i]
            i += 1
        else:
            data[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        data[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        data[k] = right_part[j]
        j += 1
        k += 1

#QUICK SORT
def quick_sort(low, high):
    global running
    if not running:
        return

    if low < high:
        pi = partition(low, high)
        quick_sort(low, pi-1)
        quick_sort(pi+1, high)

def partition(low, high):
    global running
    pivot = data[high]
    i = low - 1

    for j in range(low, high):
        if not running:
            return

        draw_data(data, ['yellow' if x == j or x == high else 'red' for x in range(len(data))])
        time.sleep(speed_scale.get())

        if data[j] < pivot:
            i += 1
            data[i], data[j] = data[j], data[i]

    data[i+1], data[high] = data[high], data[i+1]
    return i+1

#Complexities
def show_complexity(algo):
    best, avg, worst, space = complexities[algo]

    algo_label.config(text=f"Algorithm: {algo}")
    time_label.config(text=f"Time: Best={best}, Avg={avg}, Worst={worst}")
    space_label.config(text=f"Space: {space}")
    
#START SORT
def start_sorting():
    global running
    running = True

    algo = algo_menu.get()

    show_complexity(algo)  # 🔥 ADD THIS

    if algo == "Bubble Sort":
        bubble_sort()
    elif algo == "Selection Sort":
        selection_sort()
    elif algo == "Insertion Sort":
        insertion_sort()
    elif algo == "Merge Sort":
        merge_sort(0, len(data)-1)
        draw_data(data, ['green'] * len(data))
    elif algo == "Quick Sort":
        quick_sort(0, len(data)-1)
        draw_data(data, ['green'] * len(data))

    running = False

#UI
frame = tk.Frame(root, bg="gray")
frame.pack(fill=tk.X)

algo_menu = ttk.Combobox(frame, values=[
    "Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort"
])
algo_menu.current(0)
algo_menu.pack(side=tk.LEFT, padx=5, pady=5)

algo_label = tk.Label(root, text="Algorithm: ", bg="black", fg="white", font=("Arial", 12))
algo_label.pack()

time_label = tk.Label(root, text="Time Complexity: ", bg="black", fg="white", font=("Arial", 12))
time_label.pack()

space_label = tk.Label(root, text="Space Complexity: ", bg="black", fg="white", font=("Arial", 12))
space_label.pack()


tk.Button(frame, text="Generate Data", command=generate_data).pack(side=tk.LEFT, padx=5)
tk.Button(frame, text="Start", command=start_sorting, bg="green", fg="white").pack(side=tk.LEFT, padx=5)
tk.Button(frame, text="Stop", command=stop_sorting, bg="red", fg="white").pack(side=tk.LEFT, padx=5)

speed_scale = tk.Scale(frame, from_=0.01, to=1.0, length=200,
                       digits=2, resolution=0.01,
                       orient=tk.HORIZONTAL, label="Speed")
speed_scale.set(0.1)
speed_scale.pack(side=tk.LEFT, padx=5)

canvas = tk.Canvas(root, width=850, height=400, bg="white")
canvas.pack(pady=20)

generate_data()
root.mainloop()
