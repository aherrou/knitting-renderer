outfile = open(r"/tmp/test.svg", "w")

boilerplate_begin = '''<svg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'
         width='100%' height='100%' viewPort='0 0 1000 1000'>
         <!-- put some content in here -->'''

red_square = '''<rect x='0' y='0' width='100' height='100' fill='red'></rect>'''

boilerplate_end = '''
         </svg>
'''

# maille à l'endroit
knit_stitch = '''<path d="M 0 40 L 40 40 L 40 120" 
fill="transparent" stroke="black"/>
<path d="M 120 40 L 80 40 L 80 120"
fill="transparent" stroke="black"/>
<path d="M 40 0 L 30 80 L 90 80 L 80 0"
fill="transparent" stroke="black"/>'''

outfile.write(boilerplate_begin
              +knit_stitch
              +boilerplate_end)
