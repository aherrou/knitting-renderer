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

def str_coords(x,y):
    return str(x)+" "+str(y)

# maille à l'endroit
# toujours rentre dans un carré 120x120
def knit_stitch(x0, y0) :
    path1 = '''<path d="M '''+str_coords(x0, 40+y0)+" Q "+str_coords(40+x0, 40+y0)+" "+str_coords(40+x0, 120+y0)+" L "+str_coords(40+x0, 120+y0)+'''" 
    fill="transparent" stroke="url(#gradienth1)" stroke-width="5"/>'''

    path2='''
    <path d="M '''+ str_coords(120+x0, 40+y0)+" Q "+str_coords(80+x0, 40+y0)+" "+str_coords(80+x0, 120+y0)+" L "+str_coords(80+x0, 120+y0)+'''"
    fill="transparent" stroke="url(#gradienth2)" stroke-width="5"/>'''

    path3='''<path d="M '''+str_coords(40+x0, y0)+" C "+str_coords(x0+40, y0+40)+" "+str_coords(x0, 90+y0)+" "+str_coords(x0+60, 90+y0)+" S "+str_coords(x0+80, y0+40)+" "+str_coords(x0+80, y0)+'''"
    fill="transparent" stroke="url(#gradientv)" stroke-width="5"/>'''

    return (path1+path2+path3)

output = boilerplate_begin

for i in range(0, 10):
    for j in range(0, 10):
        output = output+knit_stitch(0+i*120,0+j*120)

output = output+boilerplate_end

outfile.write(output)

# outfile.write(boilerplate_begin
#               +knit_stitch(0,0)
#               +knit_stitch(0,120)
#               +knit_stitch(120,0)
#               +knit_stitch(120,120)
#               +boilerplate_end)
