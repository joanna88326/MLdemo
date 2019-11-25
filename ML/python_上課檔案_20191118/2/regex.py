import requests
import re
from bs4 import BeautifulSoup

 
# 現在要做的事情是 把全部h tag所夾住的文字，把它印出來

def main():
    resp = requests.get('http://newmedia.tw/aiarts/blog.html')
    soup = BeautifulSoup(resp.text, 'html.parser')

    # 找出所有 'h' 開頭的標題文字  不用regular expression 的寫法
    titles = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']) # 把h4 tag或是h6 tag裡面 夾住的文字都找出來
    for title in titles:
        print(title.text.strip())

    # 利用 regex 找出所有 'h' 開頭的標題文字
    for title in soup.find_all(re.compile('h[1-6]')):
        print(title.text.strip())

    ''' 用regular expression的話，它寫起來會比較簡潔
        我們一樣用find_all()去找全部的tag，符合的tag的名字，只是這個tag的名字
        我們傳入一個regular expression，這個regular expression要用
        re.complile()這個function  去做出一個regular expression的物件
        那你想要的字串的規則就放在 complie 的引數裡面
        那在這邊我們放進去的規則是，h開頭的字串，而且它可以是h1、h2一直到h6
        寫法就是h[1-6]
        這樣子它的效果，跟我們前一個程式是一模一樣的 '''

    # 找出所有 .png 結尾的圖片 不用regular expression 的寫法
    imgs = soup.find_all('img')
    for img in imgs:
        if 'src' in img.attrs:
            if img['src'].endswith('.png'):
                print(img['src'])
    
    ''' 把全部的image tag找出來， 找出來之後先確定 src在image的attribute裡面
        那而且image src的值就是圖片的網址 又是.png結尾的話，我們就把它印出來 '''

    # 利用 regex 找出所有 .png 結尾的圖片
    for img in soup.find_all('img', {'src': re.compile('\.png$')}):
        print(img['src'])

        ''' 用regular expression來做的話 一樣是用soup.find_all()去找
            第一個我們送進去的是img tag  是tag的名字
            第二個在attribute的部分
            用正規的寫法，也就是key是src value必須要符合regular expression
            在這邊regular expression的寫法是.png結尾的圖片
            因為"."在regular expression裡面是特殊字元，所以要表示"."的時候要多加一個反斜線
            所以\.png$，這個$的符號代表的是  以前面這個字串結尾的意思
            所以\.png$就是.png結尾的字串的意思
            只要img tag，然後它的src符合我這一個表示式，這個字串的規則就會被印出來 '''

    # 找出所有 .png 結尾且含 'beginner' 的圖片  不用regular expression 的寫法
    imgs = soup.find_all('img')
    for img in imgs:
        if 'src' in img.attrs:
            if 'beginner' in img['src'] and img['src'].endswith('.png'):
                print(img['src'])

    ''' 先把全部的img tag找出來
        第一個當然是確認src有在attribute裡面，第二個是beginner這個字串在它的檔名裡面
        而且這個檔名是用png來結尾，這樣子執行的結果就只會剩下第一個
        第一張圖片它的檔名、它的來源才符合我們的規定 '''

    # 利用 regex 找出所有 .png 結尾且含 'beginner' 的圖片
    for img in soup.find_all('img', {'src': re.compile('beginner.*\.png$')}):
        print(img['src'])

    ''' 傳入的regular expression的字串，把它分開來看
        第一個部分是.png結尾，跟上一個範例一樣沒有問題
        那第二個是字串檔名裡面，必須要含有beginner這個字串
        那在beginner這個字串跟png結尾的中間，可以出現長度是0或者是1的任何字
        "."就是代表任何字，那"*"就是代表長度是0或者是1
        所以這樣子寫的話，執行的結果跟之前的範例是一樣的
        它可以找出檔名裡面含有beginner，然後結尾是.png的字串 '''


if __name__ == '__main__':
    main()
