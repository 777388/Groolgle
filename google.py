import sys
from optparse import OptionParser
def Main():
    parser = OptionParser()
    parser.add_option("-1", "--it", dest='it', help="intext:", action='store')
    parser.add_option("-2", "--i", dest='i', help="intitle:", action='store')
    parser.add_option("-3", "--ai", dest='ai', help="allinurl:", action='store')
    parser.add_option("-4", "--iu", dest='iu', help="inurl:", action='store')
    parser.add_option("-5", "--aiu", dest='aiu', help="allinurl:", action='store')
    parser.add_option("-6", "--f", dest='f', help="filetype:", action='store')
    parser.add_option("-7", "--ait", dest='ait', help="allintext:", action='store')
    parser.add_option("-8", "--s", dest='s', help="site:", action='store')
    parser.add_option("-9", "--l", dest='l', help="link:", action='store')
    parser.add_option("-A", "--ia", dest='ia', help="inanchor:", action='store')
    parser.add_option("-B", "--n", dest='n', help="numrange:", action='store')
    parser.add_option("-C", "--d", dest='d', help="daterange:", action='store')
    parser.add_option("-D", "--a", dest='a', help="author:", action='store')
    parser.add_option("-E", "--g", dest='g', help="group:", action='store')
    parser.add_option("-F", "--is", dest='iss', help="insubject:", action='store')
    parser.add_option("-G", "--m", dest='m', help="msgid:", action='store')
    parser.add_option("-I", "--c", dest='cac', help="cache:", action='store')
    parser.add_option("-L", "--ind", dest='ind', help="intitle:\"index of\"", action='append')
    parser.add_option("-M", "--sea", dest="sea", help="regular search", action='store', default=sys.argv[-1])
    (options, args) = parser.parse_args()
    if options.sea == None:
        parser.print_help()
        exit(0)
    else:
        response = ""
        if options.it != None:
            it = " intext:"+options.it+" &"
            response += it
        if options.i != None:
            i = " intitle:"+options.i+" &"
            response += i
        if options.ai != None:
            ai = " allinurl:"+options.ai+" &"
            response += ai
        if options.iu != None:
            iu = " inurl:"+options.iu+" &"
            response += iu
        if options.aiu != None:
            aiu = " allinurl:"+options.aiu+" &"
            response += aiu
        if options.f != None:
            f = " filetype:"+options.f+" &"
            response += f
        if options.ait != None:
            ait = " allintext:"+options.ait+" &"
            response += ait
        if options.s != None:
            s = " site:"+options.s+" &"
            response += s
        if options.l != None:
            l = " link:"+options.l+" &"
            response += l
        if options.ia != None:
            ia = " inanchor:"+options.ia+" &"
            response += ia
        if options.n != None:
            n = " numrange:"+options.n+" &"
            response += n
        if options.d != None:
            d = " daterange:"+options.d+" &"
            response += d
        if options.g != None:
            g = " group:"+options.g+" &"
            response += g
        if options.iss != None:
            iss = " insubject:"+options.iss+" &"
            response += iss
        if options.m != None:
            m = " msgid:"+options.msgid+" &"
            response += m
        if options.cac != None:
            c = " cache:"+options.cac+" &"
            response += c      
        if options.ind != None:
            ind = " intitle:\"index of\""
            response += ind
        if options.sea != None:
            sea = " "+options.sea
            response += sea
        x = 256
        for v in range(0, x, 10):
            print("site:***"+str(v)+" | site:***"+str(v+1)+" | site:***"+str(v+2)+" | site:***"+str(v+3)+" | site:***"+str(v+4)+" | site:***"+str(v+5)+" | site:***"+str(v+6)+" | site:***"+str(v+7)+" | site:***"+str(v+8)+" | site:***"+str(v+9)+" | site:***"+str(v+10)+" &"+response)
            print()
        
        print(response)

if __name__ == '__main__':
    Main()
    
