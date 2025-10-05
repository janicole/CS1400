# CS 1400
# Assigment 5: Image Processing
# Written by David Johnson, Noelle Brown, and Jana Johnson

from random import *

# This brings in functions from the graphics.py file
from graphics import *


# Make a new image that moves the red intensity value of a pixel in the original image to the green part of a pixel, moves the green value to
# blue, and the blue value to red. An image that had a bright red part will end up with that part being bright green in the new image.
#
# Study the pattern of the loop inside a loop (called nested loops). Each time the first loop does a single repeat, the entire
# inner loop does all its repetitions.
#
# Look how to get the color at a pixel, change the color, and set the pixel to the new color. The assignment problems below will use these steps.
# This function returns a new image with changed colors. The code in main calls this function and draws the returned new image.
def switch_image_colors(image):
    # copy the image into an image the code will modify
    switched_image = image.clone()
    # The for x loop goes through all its iterations and then the for y loop goes down a row.
    for y in range(0, image.getHeight()):
        for x in range(0, image.getWidth()):
            # Each pixel has a location like an index in x and an index in y
            color = image.getPixel(x, y)
            # color is assigned a list with [red, green, blue] values each from 0-255.
            # color[0] is the red intensity, color[1] is green, color[2] is blue.
            new_color = [color[2], color[0], color[1]]
            # Set the pixel in the changed image to the new color
            switched_image.setPixel(x, y, new_color)
    # return the finished changed image
    return switched_image


# This function loads the image file called filename and centers it in the window.
# The image is returned so it can be drawn.
def load_image(filename):
    # Load the image
    image = Image(Point(0, 0), filename)
    # Center it
    image.move(int(image.getWidth() / 2), int(image.getHeight() / 2))
    return image


# Function color_image_to_grayscale takes an image and returns a new (cloned) image with the grayscale equivalent.
# The approach to use is red * 0.299 + green * 0.587 + blue * 0.114.
# The intensity will be floating point number but the graphics code requires an integer.
# Do a conversion to into
def color_image_to_gray_scale(image):
    gray_image = image.clone()
    for y in range(0, image.getHeight()):
        for x in range(0, image.getWidth()):
            # Get the color at this pixel
            color = image.getPixel(x, y)
            gray_value = [int(color[0] * 0.299 + color[1] * 0.587 + color[2] * 0.114)]
            gray_color = [gray_value[0], gray_value[0], gray_value[0]]
            gray_image.setPixel(x, y, gray_color)
    return gray_image


# Converts a color image to black and white. First, we must have our threshold value decide whether a pixel is white or black.
# Then, we set the pixel to white if the sum of the color values is above the threshold, else set it to black.
def color_image_to_black_and_white(image, threshold):
    bw_image = image.clone()
    for y in range(0, image.getHeight()):
        for x in range(0, image.getWidth()):
            # Get the color at this pixel
            color = image.getPixel(x, y)
            # If the sum of the color values is above the threshold, set it to white, else set it to black
            if sum(color) > threshold:
                bw_color = [255, 255, 255]
            else:
                bw_color = [0, 0, 0]
            bw_image.setPixel(x, y, bw_color)
    return bw_image


# A Function that replaces every pixel with the sepia Equivalent. We separate our RGB values into single values and then convert them to sepia
# By converting them first to int values so I can manipulate and then putting them together again into one RGB Value to 
# satisfy the graphics.py requirements.
def sepia_image(image):
    sepia_image = image.clone()
    for y in range(0, image.getHeight()):
        for x in range(0, image.getWidth()):
            # Get the color at this pixel
            color = image.getPixel(x, y)
            # Separate the color into single RGB values so we can manipulate them individually 
            red = color[0]
            green = color[1]
            blue = color[2]
            # Convert our RGB values to sepia by converting to int first
            new_red = int((red * 0.393) + (green * 0.769) + (blue * 0.189))
            new_green = int((red * 0.349) + (green * 0.686) + (blue * 0.168))
            new_blue = int((red * 0.272) + (green * 0.534) + (blue * 0.131))
            # Cant let colors go above 255
            if new_red > 255:
                new_red = 255
            if new_green > 255:
                new_green = 255
            if new_blue > 255:
                new_blue = 255
            # Set our new colors by returning three new integers
            sepia_color = [new_red, new_green, new_blue]
            sepia_image.setPixel(x, y, sepia_color)
    return sepia_image


# This function creates a rainbow gradient image. It uses the same technique as the sepia filter.
# It uses the same formula for converting RGB values to sepia, but it uses the y coordinate of the pixel
# to determine how much to convert. The formula is y / image_height.
def rainbow_gradient(image):
    rainbow_gradient = image.clone()
    image_width = image.getWidth()
    image_height = image.getHeight()
    for y in range(0, image_height):
        for x in range(0, image_width):
            # Get the color at this pixel
            color = image.getPixel(x, y)
            # Separate the color into single RGB values so we can manipulate them individually 
            red = color[0]
            green = color[1]
            blue = color[2]
            # Convert our RGB values to sepia by converting to int first
            y_coord_of_pixel = y

            gradient_ratio = y_coord_of_pixel / image_height

            gradient_ratio = y_coord_of_pixel / image_height
            new_red = int(red * (1 - gradient_ratio))
            new_green = int(green * (1 - abs(2 * gradient_ratio - 1)))
            new_blue = int(blue * gradient_ratio)

            new_color = [new_red, new_green, new_blue]
            rainbow_gradient.setPixel(x, y, new_color)
    return rainbow_gradient


# For this custom filter, I decided to put a vignette on my image.
# I used the formula for the vignette (That I found online) as a function of the distance from the center of the image.
# Then I was able to use some of the same practices of manipulating the RGB values as I did for the sepia filter.
def custom_filter(image):
    custom_filter = image.clone()
    image_width = image.getWidth()
    image_height = image.getHeight()
    for y in range(0, image_height):
        for x in range(0, image_width):
            # Get the color at this pixel
            color = image.getPixel(x, y)
            # Separate the color into single RGB values so we can manipulate them individually
            red = color[0]
            green = color[1]
            blue = color[2]
            # Calculate the distance from the center of the image
            distance_from_center = ((x - image_width / 2) ** 2 + (y - image_height / 2) ** 2) ** 0.5
            # Calculate the vignette value
            vignette_value = 1 - distance_from_center / (image_width / 2)
            # Multiply the red, green, and blue values by the vignette value
            new_red = int(red * vignette_value)
            new_green = int(green * vignette_value)
            new_blue = int(blue * vignette_value)
            # Set the pixel to the new color
            new_color = [new_red, new_green, new_blue]
            custom_filter.setPixel(x, y, new_color)
    return custom_filter

# This function takes two images and merges them together. The green screen image is used to replace the green pixels in the background image.
# We check if the pixel is green and set it to the background color (new image) and keep the rest as our old image.
def green_screen_image(g_screen_img, background_img):
    green_screen_image = g_screen_img.clone()
    for y in range(0, g_screen_img.getHeight()):
        for x in range(0, g_screen_img.getWidth()):
            # Get the color at this pixel
            color = g_screen_img.getPixel(x, y)
            # Separate the color into single RGB values so we can manipulate them individually
            red = color[0]
            green = color[1]
            blue = color[2]
            # Check if the pixel is green and set it to the background color
            if green == 255 and red == 0 and blue == 0:
                # Get the color of the pixel in the background image
                background_color = background_img.getPixel(x, y)
                # Set the pixel to the background color
                green_screen_image.setPixel(x, y, background_color)
                # Set the pixel to the background color
            else:
                green_screen_image.setPixel(x, y, color)
    return green_screen_image


# This function creates a pointillist of random pixels in the image. The number of points is randomly generated and
# the function loops through that number of times. Each time, it gets a random pixel location and draws a circle at that
# location filled with the pixel color onto the image in the window.
def color_image_to_pointillist(image, win, num_points):
    image_width = image.getWidth()
    image_height = image.getHeight()
    # Randomly pick a pixel location, and get it's color values, and draw a circle at that
    # location filled with the pixel color onto the image in the window.
    for i in range(num_points):
        # Get a pixel with a random (width) and (height) place
        x = randint(0, image_width - 1)
        y = randint(0, image_height - 1)
        # Get the color at this pixel
        color = image.getPixel(x, y)

        # Teacher Code
        circle = Circle(Point(x, y), 5)
        circle.setFill(color[0], color[1], color[2])
        circle.setWidth(0)
        circle.draw(win)
    return color_image_to_pointillist


def main():
    # Load the image first, so we know how big to make the window.
    arches_image = load_image("Arches.png")
    cat_image = load_image("green-screen-cat.png")

    # Set up the window using the image size
    win = GraphWin('Image Art',
                   arches_image.getWidth(),
                   arches_image.getHeight(),
                   autoflush=False)

    # Draw the original image and wait for a mouse click to move to the next step
    arches_image.draw(win)
    win.getMouse()

    # Make a new image with green intensity put in red, blue put in green, and red in blue.
    switched_image = switch_image_colors(arches_image)
    switched_image.draw(win)
    win.getMouse()

    # Test the grayscale
    gray_image = color_image_to_gray_scale(arches_image)
    gray_image.draw(win)
    gray_image.save("gray.png")
    win.getMouse()

    # Test the black and white
    bw_image = color_image_to_black_and_white(arches_image, 200)
    bw_image.draw(win)
    bw_image.save("bw.png")
    win.getMouse()

    # Test the sepia
    sepia = sepia_image(arches_image)
    sepia.draw(win)
    sepia.save("sepia.png")
    win.getMouse()

    # Test the rainbow gradient
    rainbow_image = rainbow_gradient(arches_image)
    rainbow_image.draw(win)
    rainbow_image.save("rainbow.png")
    win.getMouse()

    # Test the custom filter
    custom_image = custom_filter(arches_image)
    custom_image.draw(win)
    custom_image.save("custom.png")
    win.getMouse()

    # Make a merged image between a green screen image and a background
    merged_image = green_screen_image(cat_image, arches_image)
    merged_image.draw(win)
    merged_image.save("merged.png")
    win.getMouse()

    # Test the pointillist function. It is just drawn on the window. You will need to
    # screen capture the image to save it for submitting.
    color_image_to_pointillist(arches_image, win, 25000)
    win.getMouse()

    win.close()


# Execute main when this file is run.
if __name__ == "__main__":
    main()
