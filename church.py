import cairo
import math

# Create surface and context
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 400, 300)
ctx = cairo.Context(surface)

# Background color
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

ctx.set_line_width(2)

# Change the structure below the cross to a square and set it to blue
ctx.rectangle(180, 50, 30, 30)
ctx.set_source_rgb(0, 0, 1)  # Blue color
ctx.fill()

# Cross on top of the square shape
ctx.move_to(195, 50)
ctx.line_to(195, 15)
ctx.move_to(185, 25)
ctx.line_to(205, 25)
ctx.set_source_rgb(0, 0, 0)
ctx.stroke()

# The bar below the cross
ctx.rectangle(160, 91, 70, 9)
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

# Side rectangles
ctx.rectangle(50, 220, 80, 40)
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

ctx.rectangle(260, 220, 80, 40)
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

# Small white rectangles on the sides
ctx.rectangle(60, 230, 20, 15)
ctx.set_source_rgb(1, 1, 1)
ctx.fill()
ctx.rectangle(90, 230, 20, 15)
ctx.set_source_rgb(1, 1, 1)
ctx.fill()

ctx.rectangle(280, 230, 20, 15)
ctx.set_source_rgb(1, 1, 1)
ctx.fill()
ctx.rectangle(310, 230, 20, 15)
ctx.set_source_rgb(1, 1, 1)
ctx.fill()

# Trapezoidal shapes on the sides
ctx.move_to(80, 190)
ctx.line_to(130, 190)
ctx.line_to(130, 220)
ctx.line_to(40, 220)
ctx.close_path()
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()
