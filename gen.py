from random import choice 

outfile = open(r"/tmp/test.svg", "w")

boilerplate_begin = '''<svg version="1.1" xmlns='http://www.w3.org/2000/svg'
width='100%' height='100%' viewPort='0 0 10000 10000'>'''

defs = '''<defs>

<linearGradient id="gradienth1" x1="0%" y1="0%" x2="100%" y2="0%">
<stop offset="0%"   stop-color="#05a5"/>
<stop offset="100%" stop-color="#0a5"/>
</linearGradient>

<linearGradient id="gradienth2" x1="100%" y1="0%" x2="0%" y2="0%">
<stop offset="0%"   stop-color="#05a5"/>
<stop offset="100%" stop-color="#0a5"/>
</linearGradient>

<linearGradient id="gradientv" x1="0%" y1="100%" x2="0%" y2="0%">
<stop offset="0%"   stop-color="#05a0"/>
<stop offset="100%" stop-color="#0a5"/>
</linearGradient>

<style><![CDATA[
<!-- CSS goes here-->
]]></style>
</defs>
<!-- put some content in here -->
'''

boilerplate_end = '''
         </svg>
'''

epsilon = 1

def str_coords(x,y):
    return str(x)+" "+str(y)

### Individual stitches

# maille à l'endroit
# toujours rentre dans un carré 12x12
def thread(x0, y0) :
    path1 = '''<path d="M '''+str_coords(x0, 4+y0)+" Q "+str_coords(4+x0, 4+y0)+" "+str_coords(4+x0, 12+y0)+" L "+str_coords(4+x0, 12+y0)+'''" 
    fill="none" stroke="url(#gradienth1)" stroke-width="5"/>'''

    path2='''
    <path d="M '''+ str_coords(12+x0, 4+y0)+" Q "+str_coords(8+x0, 4+y0)+" "+str_coords(8+x0, 12+y0)+" L "+str_coords(8+x0, 12+y0)+'''"
    fill="none" stroke="url(#gradienth2)" stroke-width="5"/>'''

    path3='''<path d="M '''+str_coords(4+x0, y0)+" C "+str_coords(x0+4, y0+4)+" "+str_coords(x0, 9+y0)+" "+str_coords(x0+6, 9+y0)+" S "+str_coords(x0+8, y0+4)+" "+str_coords(x0+8, y0)+'''"
    fill="none" stroke="url(#gradientv)" stroke-width="5"/>'''

    return (path1+path2+path3)

# simpler display
def knit_stitch(x0, y0):
    # left strand
    path1 = '''<path d="M '''+str_coords(x0+12 - epsilon, y0 + epsilon)+" L "+str_coords(x0+6 + epsilon, y0+12 - epsilon)+'''" fill="none" stroke="black" stroke-width="2"/>
    '''
    # right strand
    path2 = '''<path d="M '''+str_coords(x0+6 - epsilon, y0+12 - epsilon)+" L "+str_coords(x0 + epsilon, y0+epsilon)+'''" fill="none" stroke="black" stroke-width="2"/>
    '''
    return path1+path2

def twisted_knit_stitch(x0, y0):
    path1 = '''<path d="M '''+str_coords(x0+12 - epsilon, y0 + epsilon)+" L "+str_coords(x0+6 - epsilon, y0+12 - epsilon)+'''" fill="none" stroke="black" stroke-width="2"/>
    '''
    path2 = '''<path d="M '''+str_coords(x0+6 + epsilon, y0+12 - epsilon)+" L "+str_coords(x0 + epsilon, y0+epsilon)+'''" fill="none" stroke="black" stroke-width="2"/>
    '''
    return path1+path2

def purl_stitch(x0, y0):
    path1= '''<path d="M '''+str_coords(x0 + 2, y0+6)+" Q "+str_coords(x0+6, y0)+" "+str_coords(x0+10, y0+6)+'''" fill="none" stroke="black" stroke-width="2"/>
    '''
    path2= '''<path d="M '''+str_coords(x0 + 4, y0+6)+" Q "+str_coords(x0+4, y0+9)+" "+str_coords(x0, y0+9)+'''" fill="none" stroke="black" stroke-width="2"/>
    '''
    path3= '''<path d="M '''+str_coords(x0 + 8, y0+6)+" Q "+str_coords(x0+8, y0+9)+" "+str_coords(x0+12, y0+9)+'''" fill="none" stroke="black" stroke-width="2"/>
    '''
    return path1+path2+path3

def yarn_over(x0, y0):
    path = '''<path d="M '''+str_coords(x0, y0)+" L "+str_coords(x0+12, y0)+'''" fill="none" stroke="black" stroke-width="2"/>'''
    return path

def m1l(x0, y0):
    path1 = '''<path d="M '''+str_coords(x0+4, y0)+" L "+str_coords(x0+6 - epsilon, y0+2 - epsilon)+'''" fill="none" stroke="black" stroke-width="2"/>
    '''
    path2 = '''<path d="M '''+str_coords(x0+8, y0)+" L "+str_coords(x0 + 4, y0+4)+'''" fill="none" stroke="black" stroke-width="2"/>
    '''
    path3 = '''<path d="M '''+str_coords(x0+8, y0+4)+" L "+str_coords(x0+6 + epsilon, y0+2 + epsilon)+'''" fill="none" stroke="black" stroke-width="2"/>
    '''
    return path1+path2+path3

def m1r(x0, y0):
    path1 = '''<path d="M '''+str_coords(x0+8, y0)+" L "+str_coords(x0+6 + epsilon, y0+2 - epsilon)+'''" fill="none" stroke="black" stroke-width="2"/>
    '''
    path2 = '''<path d="M '''+str_coords(x0+4, y0)+" L "+str_coords(x0 + 8, y0+4)+'''" fill="none" stroke="black" stroke-width="2"/>
    '''
    path3 = '''<path d="M '''+str_coords(x0+4, y0+4)+" L "+str_coords(x0+6 - epsilon, y0+2 + epsilon)+'''" fill="none" stroke="black" stroke-width="2"/>
    '''
    return path1+path2+path3

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
    
output = boilerplate_begin

# for i in range(0, 10):
#     for j in range(0, 10):
#         # if 1 == 0:
#         #     output = output + ribbing_2_2(i, j) + "\n"
#         # else:
#         #     output = output + rice(i, j) + "\n"
#         output = output + lace2(i, j) + "\n"
#         # output = output + twisted(i, j) + "\n"
#         # output = output + japanese_ribbing_1_1(i, j) + "\n"

model = [[knit_stitch, purl_stitch]*10,
         [knit_stitch, purl_stitch]*10,
         [m1r, yarn_over]*10]*5

i=0
j=0

for row in model:
    for stitch in row:
        output = output + stitch(i*12, j*12) + "\n"
        j = j+1
    j=0
    i = i+1

output = output+boilerplate_end

outfile.write(output)

# outfile.write(boilerplate_begin
#               +knit_stitch(0,0)
#               +knit_stitch(0,120)
#               +knit_stitch(120,0)
#               +knit_stitch(120,120)
#               +boilerplate_end)
