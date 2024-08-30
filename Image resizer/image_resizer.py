import cv2  # Import the OpenCV library

# Load the image
image = cv2.imread('ali.jpg')  # Read the image from file

# Check if the image was successfully loaded
if image is None:  # If the image didn't load
    print("Error: Could not load image 'ali.jpg'")  # Print an error message
else:
    scale_percent = 50  # Set the scale to 50%

    # Define the desired dimensions for the resized image
    new_width = int(image.shape[1] * scale_percent / 100)  # Calculate new width
    new_height = int(image.shape[0] * scale_percent / 100)  # Calculate new height

    # Resize the image
    resized_image = cv2.resize(image, (new_width, new_height))  # Resize the image

    # Save the resized image
    cv2.imwrite('resized_image.png', resized_image)  # Save the resized image
    # cv2.waitKey(0)  # Wait for a key press (commented out)
    # cv2.destroyAllWindows()  # Close all windows (commented out)
