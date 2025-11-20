import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Paint – Lab 9")
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'          # Current drawing color
    points = []            # List of points to draw lines between
    shape = "circle"       # Default shape
    erase_mode = False     # Erase mode flag
        
    # Function to draw between two points with selected shape and color
    def drawLineBetween(screen, index, start, end, width, color_mode, shape):
        # Create gradient effect based on index
        c1 = max(0, min(255, 2 * index - 256))
        c2 = max(0, min(255, 2 * index))
        
        # Determine color
        if color_mode == 'blue':
            color = (c1, c1, c2)
        elif color_mode == 'red':
            color = (c2, c1, c1)
        elif color_mode == 'green':
            color = (c1, c2, c1)
        elif color_mode == 'yellow':
            color = (c2, c2, c1)
        elif color_mode == 'cyan':
            color = (c1, c2, c2)
        elif color_mode == 'pink':
            color = (c2, c1, c2)
        
        # Calculate distance between points
        dx = start[0] - end[0]
        dy = start[1] - end[1]
        iterations = max(abs(dx), abs(dy))
        
        # Draw shapes along the line
        for i in range(iterations):
            progress = 1.0 * i / iterations
            aprogress = 1 - progress
            x = int(aprogress * start[0] + progress * end[0])
            y = int(aprogress * start[1] + progress * end[1])
            
            if shape == "circle":
                pygame.draw.circle(screen, color, (x, y), width)
            elif shape == "square":
                pygame.draw.rect(screen, color, (x, y, 2*width, 2*width))
            elif shape == "right_triangle":
                pygame.draw.polygon(screen, color, ((x, y), (x + 2*width, y), (x + 2*width, y - 2*width)))
            elif shape == "eq_triangle":
                h = int(4*width * (3**0.5)/4)
                pygame.draw.polygon(screen, color, ((x, y), (x + 4*width, y), (x + 2*width, y - h)))
            elif shape == "rhombus":
                d = int(2*width * 2**0.5 / 2)
                pygame.draw.polygon(screen, color, ((x, y), (x - d, y - width), (x, y - 2*width), (x + d, y - width)))
    
    # -------------------- MAIN LOOP --------------------
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            # Quit events
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held: return
                if event.key == pygame.K_F4 and alt_held: return
                if event.key == pygame.K_ESCAPE: return
                
                # Change color
                if event.key == pygame.K_r: mode = 'red'
                elif event.key == pygame.K_g: mode = 'green'
                elif event.key == pygame.K_b: mode = 'blue'
                elif event.key == pygame.K_y: mode = 'yellow'
                elif event.key == pygame.K_c: mode = 'cyan'
                elif event.key == pygame.K_p: mode = 'pink'

                # Activate erase mode
                if event.key == pygame.K_6:
                    erase_mode = True

                # Change shape
                if event.key == pygame.K_1: shape = "circle"
                elif event.key == pygame.K_2: shape = "square"
                elif event.key == pygame.K_3: shape = "right_triangle"
                elif event.key == pygame.K_4: shape = "eq_triangle"
                elif event.key == pygame.K_5: shape = "rhombus"

            # Adjust radius with mouse buttons
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left click increases radius
                    radius = min(200, radius + 1)
                elif event.button == 3:  # right click decreases radius
                    radius = max(1, radius - 1)

            # Track mouse movement for drawing
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                points.append(position)
                points = points[-256:]  # keep last 256 points for performance

        # -------------------- DRAW --------------------
        if erase_mode:
            screen.fill((0,0,0))  # clear screen
            points = []            # reset points
            erase_mode = False

        screen.fill((0,0,0))
        for i in range(len(points) - 1):
            drawLineBetween(screen, i, points[i], points[i+1], radius, mode, shape)

        pygame.display.update()
        clock.tick(60)

main()