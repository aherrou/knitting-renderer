from random import choice
from math import atan, degrees
from stitches import *
import boilerplate


# with classes

# model = [[k, tk, yo]*3]*10

# exemple of model with increases
model1 = [[k]*6*2,
          [tk, yo, tk, tk, yo, tk]*2, 
          [k]*4*2,
          [tk, yo, tk, tk]*2,
          [k]*3*2]


def draw_model(model):
    '''Assembles the svg file corresponding to the model and writes it to /tmp/test.svg'''

    output = boilerplate.begin

    i=0
    j=0

    inc_prev = [0]*len(model1[0]) # we don't rotate the top-most row
    n_inc_total = 0
    
    for row in model:
        # array of the number of increases
        inc = []
        # current number of increases
        n_inc = 0 # number of increases in the row so far
        for stitch in row:
            if stitch.stype == StitchType.NORMAL:
                inc.append(n_inc) # add the rotation (which should be offset by half of the total rotation)
            else:
                n_inc += 1
            angle = 0
            if inc_prev[j] != 0:
                angle = degrees(atan(inc_prev[j]))
            output = output + stitch.f((j+n_inc_total/2)*12, i*12, angle) + "\n"
            j += 1

        output = output + "\n <!-- new row --> \n"
            
        print("Increases = ", inc)
        print("n_inc = ", n_inc)
        print("Increases of previous row = ", inc_prev)
        print("Total number of increases = ", n_inc_total)
        print()

        inc_prev = list(map(lambda x: x-n_inc/2, inc))
        n_inc_total += n_inc
                
        j = 0
        i += 1
        
    output = output+boilerplate.end

    return output

outfile = open(r"/tmp/test.svg", "w")

outfile.write(draw_model(model1))
outfile.close()
