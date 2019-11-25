import requests
from bs4 import BeautifulSoup

def main():
    resp = requests.get('http://newmedia.tw/aiarts/index.html')
    print(resp.status_code)
    input()
    ''' 我們加入一個input()
        這個input()就是中斷程式的執行
        等待使用者的輸入
        之後才會繼續執行
        所以我們就是對每一個output
        我們都加一個中斷
        這樣我們會比較方便去看它的內容 '''

    print(resp.text)
    input()

    soup = BeautifulSoup(resp.text, 'html.parser')
    print(soup)    
    input()

    print(soup.find('h1'))
    input()

    print(soup.find('h1').text)

if __name__ == '__main__':
    main()

''' 
我們要跟網站溝通
我們用的是requests.get()
requests這個library
.get()這個方法
那把網址放入.get()的引數之後
它就會回傳一個response物件
那response物件有很多屬性可以取用
那我們最關心的是它的文字屬性
就是resp.text
這個屬性的內容
因為它就是網頁的內容
那我們把網頁再用beautifulSoup這個lib去parse
所以我們把文字內容放進來
再指定我們要用的parser
之後beautifulSoup就會回傳一個
它自己定義的獨特的物件
soup的物件
那這個soup的物件支援很多的方法
我們可以用find()去找出這個網頁裡面的tag
那找到tag之後我們再用.text
把這個tag裡面夾住的文字把它取出來
所以它執行的結果就會像是這樣子
我們一開始可以用run去執行
你run過一次之後它就會出現在這上面
所以我們執行它
我們可以看到的確這個爬蟲
已經把這個網頁的標題
它的head取出來了
'''