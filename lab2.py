import cairo

# Image surface dimensions
WIDTH, HEIGHT = 800, 600

# Colors
HOUSE_COLOR = (0.66, 0.66, 0.66)  # Grey
ROOF_COLOR = (0.1, 0.1, 0.4)      # Dark blue
ROOF_SHADOW_COLOR = (0.05, 0.05, 0.2)  # Darker blue for shadow
CHIMNEY_COLOR = (0.66, 0.66, 0.66)  # Grey
WINDOW_COLOR = (0.7, 0.9, 1.0)    # Light blue
WINDOW_FRAME_COLOR = (0.2, 0.2, 0.2)  # Dark gray
DOOR_COLOR_LIGHT = (0.7, 0.9, 1.0)  # Light blue
DOOR_COLOR_DARK = (0.1, 0.1, 0.4)  # Dark blue
PLATFORM_COLOR = (0.4, 0.8, 0.4)   # Lighter green
WINDOW_DIVIDER_COLOR = (0, 0, 0)   # Black

# Create a surface
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

# Background
ctx.set_source_rgb(0.9, 0.9, 0.9)  # Light gray
ctx.rectangle(0, 0, WIDTH, HEIGHT)
ctx.fill()

# Draw the green platform
ctx.set_source_rgb(*PLATFORM_COLOR)
platform_x, platform_y = 250, 400
platform_width, platform_height = 300, 40
ctx.rectangle(platform_x, platform_y, platform_width, platform_height)
ctx.fill()

# Function to draw a framed window
def draw_window(x, y, width, height):
    frame_thickness = 5
    # Draw the frame
    ctx.set_source_rgb(*WINDOW_FRAME_COLOR)
    ctx.rectangle(x, y, width, height)
    ctx.fill()
    # Draw the glass
    ctx.set_source_rgb(*WINDOW_COLOR)
    ctx.rectangle(
        x + frame_thickness, y + frame_thickness,
        width - 2 * frame_thickness, height - 2 * frame_thickness
    )
    ctx.fill()
    # Draw the divider
    ctx.set_source_rgb(*WINDOW_DIVIDER_COLOR)
    ctx.rectangle(x + width / 2 - 1, y + frame_thickness, 2, height - 2 * frame_thickness)
    ctx.fill()

# House Dimensions
house_width = 200
house_height = 300
side_depth = 100

# Front face (Face 1)
ctx.set_source_rgb(*HOUSE_COLOR)
ctx.move_to(300, 200)  # Top-left corner
ctx.line_to(300 + house_width, 200)  # Top-right corner
ctx.line_to(300 + house_width, 200 + house_height)  # Bottom-right corner
ctx.line_to(300, 200 + house_height)  # Bottom-left corner
ctx.close_path()
ctx.fill()

# Side face (Face 2)
ctx.set_source_rgb(*HOUSE_COLOR)
ctx.move_to(300 + house_width, 200)  # Top-right corner of Face 1
ctx.line_to(300 + house_width + side_depth, 200 - side_depth / 2)  # Top-right corner of Face 2
ctx.line_to(300 + house_width + side_depth, 200 + house_height - side_depth / 2)  # Bottom-right corner of Face 2
ctx.line_to(300 + house_width, 200 + house_height)  # Bottom-right corner of Face 1
ctx.close_path()
ctx.fill()

# Roof (3D perspective with shadow)
# Front roof
ctx.set_source_rgb(*ROOF_COLOR)
ctx.move_to(300, 200)  # Top-left corner of Face 1
ctx.line_to(300 + house_width / 2, 100)  # Peak
ctx.line_to(300 + house_width, 200)  # Top-right corner of Face 1
ctx.close_path()
ctx.fill()
# Side roof with shadow
ctx.set_source_rgb(*ROOF_SHADOW_COLOR)
ctx.move_to(300 + house_width, 200)  # Top-right corner of Face 1
ctx.line_to(300 + house_width / 2, 100)  # Peak
ctx.line_to(300 + house_width + side_depth, 200 - side_depth / 2)  # Top corner of Face 2
ctx.close_path()
ctx.fill()

# Chimney
ctx.set_source_rgb(*CHIMNEY_COLOR)
ctx.rectangle(330, 120, 20, 60)  # x, y, width, height
ctx.fill()

# Add features on Face 1 (stacked windows)
draw_window(320, 230, 60, 60)  # Top window
draw_window(320, 330, 60, 60)  # Bottom window

# Add features on Face 2 (door and window)
draw_window(420, 220, 60, 60)  # Side window
ctx.set_source_rgb(*DOOR_COLOR_LIGHT)
door_width, door_height = 80, 120
ctx.rectangle(420, 380, door_width, door_height)  # Fixed door part
ctx.fill()

ctx.set_source_rgb(*DOOR_COLOR_DARK)
ctx.rectangle(420 + door_width / 2, 380, door_width / 2, door_height)  # Open door part
ctx.fill()

# Save the result
surface.write_to_png("house.png")
