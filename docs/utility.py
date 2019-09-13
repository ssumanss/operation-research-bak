from fractions import Fraction
from IPython.display import Markdown, display, HTML


def printmd(string):
    display(Markdown(string))

def printhtml(string):
    display(HTML(string))
    
def fancy_output(res, maximize=False):
    data = ''
    for i in res.x:
        data += str(Fraction(i)) + ','

    if maximize:
        optimal = (-1) * res.fun
    else:
        optimal = res.fun
        
    printmd('The value of optimal is $' + str(Fraction(optimal)) + '$ at ' + '$(' + data[:-1] + ')$')