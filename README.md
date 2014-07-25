markright
===========

####Not just another markup language.

Markright is pictured as superset of SGML, HTML, XML and similar markup languages, which are ugly, and hard to read and maintain.
This unpleasant markups for humans (but so pleasant for machines) are eye eaters when you're editing it.

Overview
--------

Markright is not replacement for markdown, instead it enables embedding it in markright document.
Others languages are also embeddable from markright's part of document or from filesystem or URL as well.


Why all this hassle?
--------

Some reasons why markright is usable:

  * it is easier to type markright then html or xml, because it uses only the most common brackets (parentheses), among all of the variations.
  * avoid much characters which makes typing harder (chevrons, quotations, slashes...)
  * enables to slice parts of code into blocks which can be edited separately, and included when markright is converting to (X,HT)ML or SVG
  

###Shebang

    #!/usr/bin/markright
    
###Coding (python style)

    # -*- coding: utf-8 -*-

##Synthax by example


Markright interpreter will convert:

    Meta ( http-equiv Content-Type, content text/html; charset=UTF-8 ) meta
    
to html:
    
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    

...or:

    Title Atarado,, title
    
to:

    <title>Atarado</title>
    

...or html comment :

    .-  REQUIRED CSS FILES  -.
    
to:

    <!-- REQUIRED CSS FILES -->
    

...or tag with atributes:

    Link ( rel stylesheet, type text/css, href http://www.atarado.com/wp-content/style.css, media screen ) link

to:

    <link rel="stylesheet" type="text/css" href="http://www.atarado.com/Tesla/style.css" media="screen" />


...or tag with attributes and content :

    A ( href http://www.atarado.com/contact-us/ ) Contact Us,, a
    
to:

    <a href="http://www.atarado.com/contact-us/">Contact Us</a>


...or literal phrase:

    ,,<!DOCTYPE html...blah...blah...xhtml1-strict.dtd">,,
to:

    <!DOCTYPE html...blah...blah...xhtml1-strict.dtd">





###Licence

(c) 2014, Aleksa and Bartul Bralic

Markright is available for use under the MIT software license.
