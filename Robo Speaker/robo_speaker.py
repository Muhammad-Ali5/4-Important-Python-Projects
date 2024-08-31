import pyttsx3  # Import the pyttsx3 library for text-to-speech conversion

if __name__ == "__main__":  # Check if the script is being run directly
    print("WELCOME TO ROBO SPEAKER 2.0 CREATED BY M-ALI")  
    print("---------------------------------------------")  
    while True:  # Start an infinite loop
        x = input("Enter what you want to speak: ")
        if x == 'q' or x == 'Q':  # Check if the user wants to quit
            engine = pyttsx3.init()  # Initialize the text-to-speech engine
            engine.say("Bye Bye friend...")  # Make the engine say goodbye
            engine.runAndWait()  # Wait for the engine to finish speaking
            break  # Exit the loop
        engine = pyttsx3.init()  # Initialize the text-to-speech engine
        engine.say(x)  # Make the engine speak the entered text
        engine.runAndWait()  # Wait for the engine to finish speaking
