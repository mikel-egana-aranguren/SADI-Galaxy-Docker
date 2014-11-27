This is a "fork" of the tab2rdf tool from http://toolshed.g2.bx.psu.edu/view/sem4j/sparql_tools 

tab2rdf is a Galaxy tool that can convert tab files (3 columns) to RDF.

This version adds option for the user to define no base URI, ie all the entities of the tab file have their own URI. For example, one can add triples like this:

http://myurl.com#entity http://other_url_p http://foaf.com/my_friend


