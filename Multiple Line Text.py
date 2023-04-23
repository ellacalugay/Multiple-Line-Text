# Ella Lureen C. Calugay | BSCPE 1-5 | Assignment #4 | PROBLEM 3
# Writing a method in python that writes multiple line of text contents into another text file.

# Pseudocode
# Open a file "mylife.txt" in write mode.
with open ("mylife.txt", "w") as multiple_line_text:
# Create a while loop with a True condition.
    while True:
# Inside the loop, ask the user to input a line of text.
        user_input = str(input("Enter a line of text: "))
    # Write the entered line into the file using the write() function.
        multiple_line_text.write(user_input + "\n")
        while True:
        # Ask the user if they want to enter another line of input.
            user_response = input("Do you want to enter another line? (y/n): ")
            # Check if the user wants to continue.
            if user_response.lower() == "y":
                break # exit the loop and continue executing the code
            # Check if the user wants to stop.
            elif user_response.lower() == "n":
                print("Thanks for using the program!")
                break # exit the loop and stop the execution of the code
            else:
                # If the user enters an invalid input, prompt them to enter a valid one.
                print("Invalid input. Please enter 'y' or 'n'.")
        # Check if the user wants to stop again (in case they entered 'y' in the previous loop).
        if user_response.lower() == "n":
            # exit the outer loop and stop the execution of the code
# End of the code.