pos = (0,0)

points = [(34, -61), (33,-85), (32,-80), (31,-72), (30,-84), (29,-53), (28,-71), (27,-88), (26,-80), (25,-82), (24,-79), (23,-81), (22,-82), (21,-51), (20,-54), (19,-70), (18,-74), (17,-66), (16,-71), (15,-55), (14,-50), (13,-90), (12,-77), (11,-88), (10,-90), (9,-53), (8,-76), (7,-81), (6,-66), (5,-53), (4,-87), (3,-88), (2,-74), (1,-74), (0,-75)]

from math import sqrt

def move(new_pos):
    global pos
    #dist = int(sqrt((abs(new_pos[0] - pos[0])**2) + ((abs(new_pos[1] - pos[1])**2))))
    dist = new_pos[1] - pos[1]
    #if new_pos[1] < pos[1]:
    #    dist *= -1
    pos = new_pos
    return(dist)



last = '\x00'
out = ''
for i in points[::-1]:
    diff = move(i)
    out += last
    last = chr((ord(last)- diff) % 256)

print(out)

# RS{t0_svg_0R_n0t_svg}
