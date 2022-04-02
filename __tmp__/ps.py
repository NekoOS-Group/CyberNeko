from xml.etree import ElementTree as ET

tree = ET.parse('api.html')
root = tree.getroot()

li = [list() for i in range(13)]

def get_text(x):
    v = ""
    for y in x:
        v += get_text(y)
    if x.text != None:
        v += x.text
    if x.tail != None:
        v += x.tail
    return v

def detect_type(x):
    if x.find(' or ') >= 0:
        return str([detect_type(y) for y in x.split(' or ')]).replace("'", '')
    if x.find('Array') >= 0:
        print(x)
        return "[%s]" % x.split('Array')[0].strip()
    if x.find('Int') >= 0:
        return 'int'
    if x.find('Str') >= 0:
        return 'str'
    if x.find('Bool') >= 0 or x.find('True') >= 0:
        return 'bool'
    if x.find('Float') >= 0:
        return 'float'
    return x.strip()

def isOptional(x):
    s = get_text(x[2])
    if s.find('Optional') >= 0:
        return True
    else:
        return False

def getType(x):
    return detect_type( get_text(x[1]) )

def getName(x):
    return x[0].text

f = open('functions.txt', "w")
g = open('classes.txt', "w")
h = open('classdefine.txt', "w")

def generate_function(name, x):
    s = []
    for y in x:
        if not isOptional(y):
            s.append( getName(y) )
    if len(s) > 0:
        f.write( "    def %s(self, %s, **argv) :\n" % ( name, (', '.join(s)) ) )
    else:
        f.write( "    def %s(self, **argv) :\n" % name )
    f.write( "        params_table = {\n" )
    for y in x:
        f.write( "            %-25s : %s,\n" % ( "'%s'" % getName(y), getType(y) ) )
    f.write( "        }\n" )
    for y in x:
        if not isOptional(y):
            f.write( "        argv['%s'] = %s\n" % (getName(y), getName(y)) )
    f.write( "        comfirm_params( params_table, argv )\n" )
    f.write( "        return post(self, '%s', argv)\n\n" % name )
    
def generate_class(name, x):
    h.write( "class %s(tgtype): pass\n" % name )
    g.write( "%s.__type__table__ = {\n" % name )
    for y in x:
        g.write( "%35s: %s,\n" % ( "'%s' " % getName(y), getType(y) ) )
    g.write( "}\n\n" )

def dfs(x, deep):
    if x.tag=='table':
        v = x.getchildren()[0][0][0].text
        v = "Class " if v == 'Field' else 'Function '
        t = v.strip()
        name = ""
        for y in range(-1,-5,-1):
            if li[deep][y].tag == 'h4':
                name = get_text( li[deep][y][0] )
                print( v + name )
                break
        for y in x[1]:
            s = getType(y) + " " + getName(y) + " "
            if isOptional(y):
                s = "[%s]" %s
            print( "  " + s )
        if t == 'Function':
            generate_function( name, x[1] )
        if t == 'Class':
            generate_class( name, x[1] )
    li[deep].append(x)
    for v in x:
        dfs(v, deep + 1)

dfs(root,0)
