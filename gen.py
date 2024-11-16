outfile = open(r"/tmp/test.svg", "w")

boilerplate_begin = '''<svg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'
         width='100%' height='100%' viewPort='0 0 1000 1000'>
         <!-- put some content in here -->'''

red_square = '''<rect x='0' y='0' width='100' height='100' fill='red'></rect>'''

boilerplate_end = '''
         </svg>
'''

# maille à l'endroit
# toujours rentre dans un carré 120x120
def knit_stitch(x0, y0) :
    path1 = '''<path d="M '''+str(x0)+" "+str(40+y0)+" H "+str(40+x0)+" V "+str(120+y0)+'''" 
    fill="transparent" stroke="black" stroke-width="5"/>'''
    path2='''
    <path d="M '''+ str(120+x0)+" "+str(40+y0)+" H "+str(80+x0)+" V "+str(120+y0)+'''"
    fill="transparent" stroke="black" stroke-width="5"/>'''
    path3='''<path d="M '''+str(40+x0)+" "+str(y0)+" L "+str(30+x0)+" "+str(80+y0)+" H "+str(90+x0)+" L "+str(80+x0)+" "+str(y0)+'''"
    fill="transparent" stroke="black" stroke-width="5"/>'''
    return (path1 +path2+path3)

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
