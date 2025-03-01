from turtle import Screen, Turtle
from PIL import Image

# List of GIF image filenames to resize
image_files = ["think-clever.gif", "always-deliver.gif", "better-together.gif", "embrace-unknown.gif"]

# Desired size
new_size = (20, 20)  # Adjust as needed

# Loop through each image, resize, and save
for img_file in image_files:
    img = Image.open(img_file)
    img = img.resize(new_size)  # Resize the image
    img_resized_name = img_file.replace(".gif", "_resized.gif")  # Rename with "_resized"
    img.save(img_resized_name)  # Save as a resized GIF
    #print(f"Resized and saved: {img_resized_name}")  # Confirmation message




def draw_logo():
    logo_turtle = Turtle()
    logo_turtle.hideturtle()
    logo_turtle.speed(1)
    logo_turtle.penup()
    logo_turtle.goto(2,24)
    logo_turtle.pendown()
    logo_turtle.color('#6E44FF')
    logo_turtle.begin_fill()
    logo_turtle.goto(19,-9)
    logo_turtle.goto(10,-9)
    logo_turtle.goto(2,7)
    logo_turtle.goto(-5,-9)
    logo_turtle.goto(2,-9)
    logo_turtle.goto(-1,-16)
    logo_turtle.goto(-18,-16)
    logo_turtle.goto(2,24)
    logo_turtle.end_fill()

# Register the company logos as shapes
def register_shapes():
    screen.register_shape("think-clever_resized.gif")  # Value 1
    screen.register_shape("always-deliver_resized.gif")  # Value 2
    screen.register_shape("better-together_resized.gif")  # Value 3
    screen.register_shape("embrace-unknown_resized.gif")  # Value 4

values = {
    'Think_Clever': {
        'image': "think-clever_resized.gif",
        'orbit': 58, 
        'speed': 7.5, 
        'color': '#6E44FF',
        'values': [
            'Always deliver',
            'Embrace the unknown',
            'Think clever',
            'Be Better together'
        ],
        'current_value': 0
    },
    'Embrace_Unkown': {
        'image': "embrace-unknown_resized.gif",
        'orbit': 108, 
        'speed': 3, 
        'color': '#6E44FF',
        'values': [
            'Always deliver',
            'Embrace the unknown',
            'Think clever',
            'Be Better together'
        ],
        'current_value': 0
    },
    'Always_Deliver': {
        'image': "always-deliver_resized.gif",
        'orbit': 150, 
        'speed': 2, 
        'color': '#6E44FF',
        'values': [
            'Always deliver',
            'Embrace the unknown',
            'Think clever',
            'Be Better together'
        ],
        'current_value': 0
    },
    'Be_Better__Together': {
        'image': "better-together_resized.gif",
        'orbit': 228, 
        'speed': 1, 
        'color': '#6E44FF',
        'values': [
            'Always deliver',
            'Embrace the unknown',
            'Think clever',
            'Be Better together'
        ],
        'current_value': 0
    }
}

def setup_values(values):
    for value in values:
        dictionary = values[value]
        # Create main orbiting turtle with company logo
        turtle = Turtle()
        turtle.speed("fastest")
        turtle.shape(dictionary['image'])  # Use the company logo image
        turtle.penup()
        turtle.sety(-dictionary['orbit'])
        turtle.pendown()
        dictionary['turtle'] = turtle
        
        # Create text turtle for displaying values
        text_turtle = Turtle()
        text_turtle.hideturtle()
        text_turtle.penup()
        text_turtle.color(dictionary['color'])
        dictionary['text_turtle'] = text_turtle

    screen.ontimer(revolve, 50)

def update_value_text(dictionary, company_name):
    # Get current position of the orbiting turtle
    x = dictionary['turtle'].xcor()
    y = dictionary['turtle'].ycor()
    
    # Update text position
    text_turtle = dictionary['text_turtle']
    text_turtle.clear()
    text_turtle.goto(x, y + 20)  # Position text above the logo
    
    # Get current value to display
    current_value = dictionary['values'][dictionary['current_value']]
    text_turtle.write(f"{current_value}", align="center", font=("Eina03", 8, "bold"))
    
    # Rotate through values every full circle (approximately)
    if dictionary['turtle'].heading() >= 350:
        dictionary['current_value'] = (dictionary['current_value'] + 1) % len(dictionary['values'])

def revolve():
    for value in values:
        dictionary = values[value]
        dictionary['turtle'].pensize(0)
        dictionary['turtle'].circle(dictionary['orbit'], dictionary['speed'])
        update_value_text(dictionary, value)
    
    screen.ontimer(revolve, 50)

screen = Screen()
screen.bgcolor('#8FE388')
register_shapes()  # Register the company logo images
setup_values(values)
draw_logo()
screen.exitonclick()