'''
The mayor of a city has to plan a new neighborhood.  You are part of
the architectural firm that has to design the neighborhood. You
are provided with a file that contains, divided into rows, the
information that describes the East-West (E-W) strip of buildings in
the plan. Each building is described with width, height, color.

The buildings must be arranged in a rectangular plan so that:
  - all around the neighborhood there is a street of minimum width
    indicated.
  - in the E-W (horizontal) direction, there are the main streets,
    straight and of the same minimum width, separating one strip of
    E-W buildings from the next.  Each E-W strip may
    contain a variable number of buildings.  If a strip contains one
    building will be placed in the center of the strip.
  - in the N-S direction, between each pair of consecutive buildings,
    there must be at least room for a side street of the same
    minimum width as the others.  


You are asked to calculate the minimum size of the plot of land that
will contain the buildings.  And also to construct the map that shows
the buildings in the plan.

Your firm of architects has decided to arrange the buildings so that
they are **equally spaced** in the E-W direction, and to make sure
that each strip E-W of building is distant from the next one the
minimum space required forthe main streets.

To make the neighborhood more diverse, your firm has decided that, the
buildings, instead of being aligned with the main streets, have to
have a front garden (in front of S) and one behind (behind N) of equal
depth. Similarly, where possible, the space between the side streets
and the buildings should be **evenly distributed** so that everyone
can have an E and a W garden of equal depth. Only those buildings that
face on the streets on the left and on the right side of the map do
not have gardens on that side.

You are provided with a txt file that contains data indicating which
buildings to put on the map.  The file contains on each line groups
of 5 integer values, followed by 1 comma and/or 0 (or more) spaces or
tabs. Each quintuple represents a building with:
  - width
  - height
  - intensity of R color channel
  - intensity of G color channel
  - intensity of B color channel

Each row contains at least one group of 5 positive integers related to
a building to be drawn. For each building you must draw a rectangle of
the given color and size.

Create the function ex(file_data, file_png, spacing) which:
  - reads the data from file_data
  - builds an image in PNG format of the map and saves it in the
    file_png file
  - returns the dimensions width, height of the map image

The map must have a black background and display all the buildings as follows:
  - the spacing argument indicates the number of pixels to be used for
    the space required for the external, main and secondary streets,
    i.e. the minimum spacing horizontally between rectangles; and
    vertically between rows of buildings
  - each building is represented by a rectangle described by a
    quintuple in the file
  - the buildings described on each line of the file must be
    drawn, vertically centered, on a strip in the E-W direction of the map
  - the buildings in the same strip must be equidistant horizontally
    from each other with a **minimum distance of pixel 'spacing'
    between one building and the next** so that all the the first
    buildings are on the edge of the left-vertical street;
    all the last buildings are on the edge of the right street.
    NOTE if the strip contains a single building, it must be drawn
    centered horizontally
  - each strip is at a minimum distance vertically to make room for
    the main road. NOTE the vertical distance is calculated between the
    two tallest buildings highest of two consecutive bands.
    The largest building in the first row is leaning against the
    edge of the upper E-W main street. 
    The larger building in the last row is leaning against the edge of the
    lower E-W main street.
  - the image has the minimum possible size, therefore:
     - there is at least one building in the first/last row at a
       pixel 'spacing' from the top/bottom edge
     - there is at least one strip that has the first and last building
       at pixel 'spacing' from the left/right edge
     - there is at least one E-W strip where buildings have non gardens
       on the E or W side

    NOTE: in drawing the buildings you can assume that the coordinates
          will always be integer (if they are not, you have made a
          mistake). 
    NOTE: Width and height of rectangles are all multiples of two.
'''

import images

def ex(file_dati, file_png, spacing):
    # place here your code
    pass

if __name__ == '__main__':
    # place here your personal tests
    pass
