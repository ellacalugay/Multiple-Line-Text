# Ella Lureen C. Calugay | BSCPE 1-5 | Assignment #4 | PROBLEM 3
# Writing a method in python that writes multiple line of text contents into another text file.

# Pseudocode
# Import necessary modules
import pyfiglet
from colorama import Back, Fore
from termcolor import colored
from tqdm import tqdm
import time
import tkinter as tk

# Defining flower design function for the border design of Activity title.
def flower_design():
    print("🌷" * 62 )

# Define the text to display
text = "Life in multiple line contents"

# Set font and color for the header 
font = "standard"
color = "yellow"

# Pyfiglet for the header
result = pyfiglet.figlet_format(text, font=font, width=150)
colored_result = colored(result, color)

# Calling the define function
flower_design()

# Center align the output
for line in colored_result.split("\n"):
    print(line.center(80))

# Calling the define function again
flower_design()
print("\n".center(80))

# Set the number of iterations
total_iterations = 100

# Open a file "mylife.txt" in write mode.
with open ("mylife.txt", "w") as multiple_line_text:
# Create a while loop with a True condition.
    while True:
# Inside the loop, ask the user to input a line of text.
        user_input = str(input("\033[38;5;139;1m\033[48;5;225mEnter a line of text: \033[0m \033[38;5;226m"))
    # Write the entered line into the file using the write() function.
        multiple_line_text.write(user_input + "\n")
        while True:
        # Ask the user if they want to enter another line of input.
            user_response = input(Back.CYAN + "\n" + "\033[1mDo you want to enter another line? (y/n): \033[0m" + "\033[38;5;141m ")
            # Check if the user wants to continue.
            if user_response.lower() == "y":
                break # exit the loop and continue executing the code
            # Check if the user wants to stop.
            elif user_response.lower() == "n":
                print("\n")
                # Create a progress bar object
                progress_bar = tqdm(total=total_iterations)
                
                # Loop through the iterations
                for i in range(total_iterations):
                    time.sleep(0.1)
            
                    # update the progress bar
                    progress_bar.update(1)

                # Close the progress bar
                progress_bar.close()

                # Print a newline character to add spacing
                print("\n")

                # Use string formatting to center and add color to the flower emoji border
                print("{:^30}".format("\x1b[95m 🌸" * 10 + "\x1b[0m"))
                # Use string formatting to center and add color to the message text
                print("{:^62}".format("\033[38;5;139;1m\033[48;5;225mThanks for using the program!\033[0m"))
                # Use string formatting to center and add color to the flower emoji border again
                print("{:^30}".format("\x1b[95m 🌸" * 10 + "\x1b[0m"))
                break  # exit the loop and stop the execution of the code
            else:
                # If the user enters an invalid input, prompt them to enter a valid one
                print(Fore.RED + "\033[3mInvalid input. Please enter 'y' or 'n'. \033[0m")
        # Check if the user wants to stop again (in case they entered 'y' in the previous loop)
        if user_response.lower() == "n":
            break  # exit the outer loop and stop the execution of the code

# Create a tkinter window
window = tk.Tk()
window.title("PROGRAM 3")

# Create a scrollbar
scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a text widget with modified font, color, and background
text_widget = tk.Text(window, yscrollcommand=scrollbar.set, font=("Arial", 14), fg="pink", bg="black")
text_widget.pack(fill=tk.BOTH, expand=1)

# Open the "mylife.txt" file in read mode
with open("mylife.txt", "r") as file:
    # Delete the current contents of the text widget
    text_widget.delete("1.0", tk.END)
    # Insert the new text with tags
    text_widget.insert(tk.END, "My Life\n\n", "title")
    text_widget.insert(tk.END, file.read(), "body")

# Set the tags for the text widget
text_widget.tag_config("title", font=("Helvetica", 25), justify="center")
text_widget.tag_config("body", font=("Arial", 15), justify="left")

# Run the tkinter event loop
window.mainloop()

# End of the code.