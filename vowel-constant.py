print("......Monk on Hills......")
myfirst_varb=input("enter the word:")
vowels=['a', 'e', 'i', 'o', 'u']
consonant=['b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 's', 't', 'v', 'x', 'z','h','r','w','y']


def test():
    for el in myfirst_varb:
        if el*2 in myfirst_varb:
            pipe=el
            print(el,end='', flush=True)
            print(el.replace(pipe,"||"),end='', flush=True)
        elif el in vowels:
            html = el
            print (el,end='', flush=True)
            f = el.replace(html, '\\')
            print(f,end='', flush=True)

        elif el in consonant:
            print(el,end='', flush=True)
            html2 = el
            f2 = el.replace(html2, str('/'))
            print(f2,end='', flush=True)
        else:
            print(el,end='', flush=True)




test()
