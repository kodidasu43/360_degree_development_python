import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Canvas Demo")

# Create a canvas widget
canvas = tk.Canvas(root, width=400, height=300, bg="lightgray")
canvas.pack()

# Draw shapes on the canvas
canvas.create_line(10, 10, 390, 50, fill="blue", width=3)  # Line
canvas.create_rectangle(50, 80, 250, 200, fill="green")  # Rectangle
canvas.create_oval(300, 150, 380, 230, fill="red")  # Oval
canvas.create_text(200, 150, text="Hello, Canvas!", font=("Arial", 18))  # Text
# Add an image
photo = tk.PhotoImage(file="tomato.png")  # Replace with your image path
canvas.create_image(100, 150, image=photo)
root.mainloop()
