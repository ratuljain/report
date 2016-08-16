from bs4 import BeautifulSoup


def consolidateToHTML():
    HTMLsoup = BeautifulSoup(open("C:/Users/rjain1/PycharmProjects/report/DailyRep/res_files/sheet001.htm"),
                             'html.parser')
    CSSsoup = BeautifulSoup(open("C:/Users/rjain1/PycharmProjects/report/DailyRep/res_files/stylesheet.css"),
                            'html.parser')

    for tag in HTMLsoup.find_all('script'):
        tag.replaceWith('')

    HTMLsoup.head.style.append(CSSsoup)

    html = HTMLsoup.prettify("utf-8")
    with open("output.html", "wb") as file:
        file.write(html)

    print "HTML CSS consolidated"

# consolidateToHTML()
