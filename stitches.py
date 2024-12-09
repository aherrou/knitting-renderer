from enum import Enum

class StitchType(Enum):
    '''Identifies whether the stitch is a standard stitch, an increase or a decrease'''
    NORMAL = 0
    INCREASE = 1
    DECREASE = 2 # or -1?

# when the thread going under stops
epsilon = 1

class Stitch:
    '''Class for representing stitches, drawing them and computing the garment shape they create'''

    def __init__(self, stype, fdraw):
        self.stype = stype
        self.f = fdraw


# Drawing the stitches

def str_coords(x,y):
    return str(x)+" "+str(y)

### Individual stitches

# maille à l'endroit
# toujours rentre dans un carré 12x12
def thread(x0, y0) :
    path1 = '''<path d="M '''+str_coords(x0, 4+y0)+" Q "+str_coords(4+x0, 4+y0)+" "+str_coords(4+x0, 12+y0)+" L "+str_coords(4+x0, 12+y0)+'''" 
    fill="none" stroke="black" stroke-width="2"/>'''

    path2='''
    <path d="M '''+ str_coords(12+x0, 4+y0)+" Q "+str_coords(8+x0, 4+y0)+" "+str_coords(8+x0, 12+y0)+" L "+str_coords(8+x0, 12+y0)+'''"
    fill="none" stroke="black" stroke-width="2"/>'''

    path3='''<path d="M '''+str_coords(4+x0, y0)+" C "+str_coords(x0+4, y0+4)+" "+str_coords(x0, 9+y0)+" "+str_coords(x0+6, 9+y0)+" S "+str_coords(x0+8, y0+4)+" "+str_coords(x0+8, y0)+'''"
    fill="none" stroke="black" stroke-width="2"/>'''

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

k = Stitch(StitchType.NORMAL, knit_stitch)

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

