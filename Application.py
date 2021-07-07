import core.userInput as userInput

location = input("please provide location of badminton video here: ")

no_lines = int(input("please enter no of user input lines: "))

skip = int(input("please provide values for skipping initinals of video: "))

userInput.setBoundaries(location, no_lines, skip)