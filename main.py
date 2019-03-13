from display import *
from draw import *
from par import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
points = []
transform = new_matrix()

parse_file( 'script', points, transform, screen, color )