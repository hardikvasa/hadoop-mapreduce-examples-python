#!/usr/bin/env python
import sys

#Finding 'Next Link' on a given web page
def get_next_link(s):
    start_link = s.find("href=")
    if start_link == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_quote = s.find('"', start_link)
        end_quote = s.find('"',start_quote+1)
        link = str(s[start_quote+1:end_quote])
        return link, end_quote

#Getting all links with the help of 'get_next_links'
def get_all_links(page):
    links = []
    while True:
        link, end_link = get_next_link(page)
        if link == "no_links":
            break
        else:
            links.append(link)      #Append all the links in the list named 'Links'
            #time.sleep(0.1)
            page = page[end_link:]
    return links

##Main Program
for line in sys.stdin:
    line = line.strip()   #remove white spaces

    if 'wgArticleId' in line:
        key = 'Articles'
        value = 1
        print( "%s\t%d" % (key, value) )
    else:
        links = get_all_links(line)
        for j in links:
            if 'href=' in line:
                s = line.find('href')
                if '.jpg' in line or '.png' in line or '.svg' in line or '.gif' in line or '.jpeg' in line or '.tiff' in line or '.xcf' in line:
                    key = 'Image Links'
                    value = 1
                    print( "%s\t%d" % (key, value) )
                elif 'en.wikipedia.org' in line or '/w/' in line:
                    key = 'Internal but Irrelevant'
                    value = 1
                    print( "%s\t%d" % (key, value) )
                elif '.wikipedia.org' in line:
                    key = 'Non-English Wikipedia Link'
                    value = 1
                    print( "%s\t%d" % (key, value) )
                elif 'wikimedia.org' in line or 'wikimediafoundation.org' in line:
                    key = 'Organizational Link'
                    value = 1
                    print( "%s\t%d" % (key, value) )
                elif '/wiki/' in line[s+6:s+15]:
                    key = 'Internal Link'
                    value = 1
                    print( "%s\t%d" % (key, value) )
                else:
                    key = 'External Link'
                    value = 1
                    print( "%s\t%d" % (key, value) )
            else:
                pass
