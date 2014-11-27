
import sys
import rdflib
from operator import eq

def main(argv):

    g = rdflib.Graph()
    g.parse(argv[1])
    results = g.query(argv[2])
    render = argv[3]

    if (render == "html"):
        html_render(results)
    else:
        tab_render(results)
    
def html_render(results):
    print "<table>"
    print "<tr>"
    for key in results.bindings[1].keys():
        print "<td><b>" + key +"</b></td>"
    print "</tr>"
    for binding in results.bindings:
        print "<tr>"
        for value in binding.values():  
            if isinstance(value, rdflib.term.URIRef):
                print "<td><a href=\"" + value +"\">"+ value +"</a></td>"
            else:
                print "<td>"+ value +"</td>"
        print "</tr>"
    print "</table>"
    
def tab_render(results):
    for key in results.bindings[1].keys():
        print key + "\t",
    print "\n"
    for binding in results.bindings:
        for value in binding.values():  
            if isinstance(value, rdflib.term.URIRef):
                print value + "\t",
	    else:
		print value + "\t",	
	print "\n"

if __name__ == "__main__":
    main(sys.argv)
