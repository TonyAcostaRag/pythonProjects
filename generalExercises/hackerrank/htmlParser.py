import html.parser as htmlpsr


# create a subclass and override the handler methods
class MyHTMLParser(htmlpsr.HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Found a start tag  :", tag)

    def handle_endtag(self, tag):
        print("Found an end tag   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Found an empty tag :", tag)


parser = MyHTMLParser()
parser.feed("<html><head><title>HTML Parser - I</title></head>"
            + "<body><h1>HackerRank</h1><br /></body></html>")

