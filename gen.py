from random import choice
from stitches import *
import boilerplate

outfile = open(r"/tmp/test.svg", "w")


### pattern functions

def ribbing_2_2(i, j):
    res = ""
    
    width_pattern = 4
    height_pattern = 1

    res = res+knit_stitch(0+i*12*width_pattern,0+j*12*height_pattern)
    res = res+knit_stitch(12+i*12*width_pattern,0+j*12*height_pattern)
    res = res+purl_stitch(2*12+i*12*width_pattern,0+j*12*height_pattern)
    res = res+purl_stitch(3*12+i*12*width_pattern,0+j*12*height_pattern)

    return res

def japanese_ribbing_1_1(i, j):
    res = ""
    
    width_pattern = 2
    height_pattern = 1

    res = res+twisted_knit_stitch(0+i*12*width_pattern,0+j*12*height_pattern)
    res = res+purl_stitch(12+i*12*width_pattern,0+j*12*height_pattern)

    return res

def twisted(i, j):
    res = ""
    
    width_pattern = 2
    height_pattern = 1

    res = res+knit_stitch(0+i*12*width_pattern,0+j*12*height_pattern)
    res = res+twisted_knit_stitch(12+i*12*width_pattern,0+j*12*height_pattern)

    return res


def rice(i, j):
    res = ""
    
    width_pattern = 2
    height_pattern = 2

    res = res+knit_stitch(0+i*12*width_pattern,0+j*12*height_pattern)
    res = res+purl_stitch(12+i*12*width_pattern,0+j*12*height_pattern)
    res = res+purl_stitch(0*12+i*12*width_pattern,12+j*12*height_pattern)
    res = res+knit_stitch(1*12+i*12*width_pattern,12+j*12*height_pattern)
    
    return res

def lace(i, j):
    res = ""
    
    width_pattern = 2
    height_pattern = 2

    res = res+knit_stitch(0+i*12*width_pattern,0+j*12*height_pattern)
    res = res+knit_stitch(12+i*12*width_pattern,0+j*12*height_pattern)
    res = res+knit_stitch(0*12+i*12*width_pattern,12+j*12*height_pattern)
    res = res+yarn_over(1*12+i*12*width_pattern,12+j*12*height_pattern)

    return res

def lace2(i, j):
    res = ""
    
    width_pattern = 2
    height_pattern = 2

    res = res+m1l(0+i*12*width_pattern,0+j*12*height_pattern)
    res = res+knit_stitch(12+i*12*width_pattern,0+j*12*height_pattern)
    res = res+knit_stitch(0*12+i*12*width_pattern,12+j*12*height_pattern)
    res = res+m1r(1*12+i*12*width_pattern,12+j*12*height_pattern)

    return res

### 
    
output = boilerplate.begin

# for i in range(0, 10):
#     for j in range(0, 10):
#         # if 1 == 0:
#         #     output = output + ribbing_2_2(i, j) + "\n"
#         # else:
#         #     output = output + rice(i, j) + "\n"
#         output = output + lace2(i, j) + "\n"
#         # output = output + twisted(i, j) + "\n"
#         # output = output + japanese_ribbing_1_1(i, j) + "\n"

model = [[knit_stitch, purl_stitch]*10, # highest line in the pattern 
         [twisted_knit_stitch, purl_stitch]*10]*5

i=0
j=0

for row in model:
    for stitch in row:
        output = output + stitch(j*12, i*12) + "\n"
        j = j+1
    j=0
    i = i+1

output = output+boilerplate.end

outfile.write(output)

# outfile.write(boilerplate.begin
#               +knit_stitch(0,0)
#               +knit_stitch(0,120)
#               +knit_stitch(120,0)
#               +knit_stitch(120,120)
#               +boilerplate.end)
