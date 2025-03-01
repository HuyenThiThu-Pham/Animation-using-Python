from turtle import Screen, Turtle
from PIL import Image
import math
from random import randint

def resize_images():
    image_files = ["think-clever.gif", "always-deliver.gif", "better-together.gif", "embrace-unknown.gif"]
    new_size = (40, 40)
    
    for img_file in image_files:
        try:
            img = Image.open(img_file)
            img = img.resize(new_size)
            img_resized_name = img_file.replace(".gif", "_resized.gif")
            img.save(img_resized_name)
            print(f"Resized and saved: {img_resized_name}")
        except Exception as e:
            print(f"Error processing {img_file}: {str(e)}")

def draw_pulsing_logo():
    base_coords = [
        (2, 24),    # Start
        (19, -9),   # Point 1
        (10, -9),   # Point 2
        (2, 7),     # Point 3
        (-5, -9),   # Point 4
        (2, -9),    # Point 5
        (-1, -16),  # Point 6
        (-18, -16), # Point 7
        (2, 24)     # Back to start
    ]
    
    # Create a turtle for drawing the logo
    logo_turtle = Turtle()
    logo_turtle.hideturtle()
    logo_turtle.speed(1)
    logo_turtle.color('#6E44FF')
    
    # Create a turtle for drawing the name
    name_turtle = Turtle()
    name_turtle.hideturtle()
    name_turtle.penup()
    name_turtle.color('#6E44FF')
    
    def draw_scaled_logo(scale):
        logo_turtle.clear()
        logo_turtle.penup()
        # Scale the coordinates
        scaled_coords = [(x * scale, y * scale) for x, y in base_coords]
        # Move to the starting point
        logo_turtle.goto(scaled_coords[0])
        logo_turtle.pendown()
        logo_turtle.begin_fill()
        
        # Draw the logo using the scaled coordinates
        for x, y in scaled_coords[1:]:
            logo_turtle.goto(x, y)
        
        logo_turtle.end_fill()
        
        name_turtle.clear()
        name_turtle.goto(0, -45 * scale)
        name_turtle.write("aurizn", align="center", font=("Eina03", int(16 * scale), "bold"))
    
    def pulse():
        scales = ([1 + i * 0.01 for i in range(10)] + [1.1 - i * 0.01 for i in range(10)])
        for scale in scales:
            draw_scaled_logo(scale)
            screen.update()
        screen.ontimer(pulse, 50)
    
    return pulse

class FlowerOrbit:
    def __init__(self, image, radius, speed, color, values, angle_offset=0):
        self.turtle = Turtle()
        self.turtle.speed(1)
        self.image_map = {
            'Think Clever': "think-clever_resized.gif",
            'Always Deliver': "always-deliver_resized.gif",
            'Better Together': "better-together_resized.gif",
            'Embrace Unknown': "embrace-unknown_resized.gif"
        }
        try:
            self.turtle.shape(image)
        except:
            self.turtle.shape("circle")
            print(f"Failed to load shape: {image}")
        self.turtle.penup()
        
        self.text_turtle = Turtle()
        self.text_turtle.hideturtle()
        self.text_turtle.penup()
        
        self.trail_turtle = Turtle()
        self.trail_turtle.hideturtle()
        self.trail_turtle.penup()
        self.trail_turtle.color(color)
        
        self.radius = radius
        self.speed = speed
        self.color = color
        self.values = values
        self.current_value = 0
        self.angle = angle_offset
        self.trail_points = []
        
    def update(self):
        # Update angle
        self.angle = (self.angle + self.speed) % 360
        
        # Calculate position using parametric equations for figure-eight curve
        t = math.radians(self.angle)
        scale = self.radius
        x = scale * math.sin(2 * t) * math.cos(t)
        y = scale * math.sin(2 * t) * math.sin(t)
        
        # Rotate the figure-eight pattern based on initial offset
        rot_angle = math.radians(45)  # 45 degrees between each orbit
        final_x = x * math.cos(rot_angle) - y * math.sin(rot_angle)
        final_y = x * math.sin(rot_angle) + y * math.cos(rot_angle)
        
        # Move the turtle to the new position
        self.turtle.goto(final_x, final_y)
        
        # Update trail
        self.trail_points.append((final_x, final_y))
        if len(self.trail_points) > 20:
            self.trail_points.pop(0)
        
        # Update the text
        self.trail_turtle.clear()
        self.trail_turtle.penup()
        for i, point in enumerate(self.trail_points):
            self.trail_turtle.goto(point)
            alpha = (i / len(self.trail_points)) * 0.5
            self.trail_turtle.pendown()
            self.trail_turtle.dot(3)
            self.trail_turtle.penup()
        
        # Update text
        self.text_turtle.clear()
        self.text_turtle.goto(final_x, final_y + 25)
        self.text_turtle.color(self.color)
        current_text = self.values[self.current_value]
        self.text_turtle.write(current_text, align="center", font=("Eina03", 10, "bold"))
        
        # Update the turtle's shape based on the current value
        try:
            self.turtle.shape(self.image_map[current_text])
        except:
            self.turtle.shape("circle")
            print(f"Failed to load shape: {self.image_map[current_text]}")
            
        if self.angle >= 359:
            self.current_value = (self.current_value + 1) % len(self.values)

def register_shapes(screen):
    try:
        resize_images()
        
        image_files = [
            "think-clever_resized.gif",
            "always-deliver_resized.gif",
            "better-together_resized.gif",
            "embrace-unknown_resized.gif"
        ]
        
        for image in image_files:
            try:
                screen.register_shape(image)
                print(f"Successfully registered shape: {image}")
            except Exception as e:
                print(f"Error registering shape {image}: {str(e)}")
                
    except Exception as e:
        print(f"Error in register_shapes: {str(e)}")

def main():
    global screen
    screen = Screen()
    screen.setup(800, 800)
    screen.bgcolor('#8FE388')
    screen.tracer(0)
    
    register_shapes(screen)
    
    # Initialize pulsing logo animation
    pulse = draw_pulsing_logo()
    pulse()
    
    # Create flower pattern orbits with different angles
    orbits = [
    FlowerOrbit("think-clever_resized.gif", 250, 1, '#6E44FF', 
               ['Think Clever', 'Always Deliver', 'Embrace Unknown', 'Better Together'], 0),
    FlowerOrbit("always-deliver_resized.gif", 250, 1, '#6E44FF',
               ['Always Deliver', 'Better Together', 'Think Clever', 'Embrace Unknown'], 90),
    FlowerOrbit("better-together_resized.gif", 250, 1, '#6E44FF',
               ['Better Together', 'Embrace Unknown', 'Always Deliver', 'Think Clever'], 180),
    FlowerOrbit("embrace-unknown_resized.gif", 250, 1, '#6E44FF',
               ['Embrace Unknown', 'Think Clever', 'Better Together', 'Always Deliver'], 270)
    ]
    
    def update_animation():
        for orbit in orbits:
            orbit.update()
        screen.update()
        screen.ontimer(update_animation, 20)
    
    update_animation()
    screen.exitonclick()

if __name__ == "__main__":
    main()