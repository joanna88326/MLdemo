import requests
from bs4 import BeautifulSoup


def main():
    resp = requests.get('http://newmedia.tw/aiarts/blog.html')
    soup = BeautifulSoup(resp.text, 'html.parser')

    # 取得第一篇 blog (h4)
    print(soup.find('h4'))
    print(soup.h4)  # 與上一行相等

    # 取得第一篇 blog 主標題  
    print(soup.h4.a.text)

    # 取得所有 blog 主標題, 使用 tag      用tag name去locate網頁元件的方式
    main_titles = soup.find_all('h4')
    for title in main_titles:
        print(title.a.text)

    # 取得所有 blog 主標題, 使用 class   
    # 以下寫法皆相同:   (attribute的寫法有好幾個)
    # soup.find_all('h4', 'card-title')
    # soup.find_all('h4', {'class': 'card-title'})
    # soup.find_all('h4', class_='card-title')  
                               # 因為class在Python裡面是保留字所以你不能夠直接寫class等於card-title   
                               # 你寫的時候class要多加一個底線
    main_titles = soup.find_all('h4', 'card-title')  #約定俗成的寫法
  # main_titles = soup.find_all('', 'card-title')  #tag 留白  會列出全部
    for title in main_titles:
        print(title.a.text)

    # 使用 key=value 取得元件  (第二個寫法我們也很常常用  id去定位所在的元件)
    print(soup.find(id='mac-p'))
  # print(soup.find(id='mac-p').text)    我們要取得這個字的部分跟這一個字的部分  我們就是用text去取得
  # print(soup.find(id='mac-p').text.strip())    
    ''' 當你打text的時候就可以
        取得這個p element下面包含的全部的文字
        那你會看到它output的結果
        會有一些換行符號跟空白
        它就幫你忠實的保留下來
        但有的時候我們並不需要這一些空白或是
        換行符號所以我們會用strip()這一個function
        去把字串前後的空白跟換行符號去掉 '''



    # 當 key 含特殊字元時, 使用 dict 取得元件
    # print(soup.find(data-foo='mac-foo'))  # 會導致 SyntaxError  '-' 是特殊字元
    print(soup.find('', {'data-foo': 'mac-foo'}))



    ''' 取得所有Blog Post的文字
        也就是說這邊有六篇文章
        我們想要做的事情是把一篇一篇文章
        依照它文章的順序，把它的文章的類型
        它的大標題小標題超連結的文字
        依序的把它印出來 '''


    # 取得各篇 blog 的所有文字
    divs = soup.find_all('div', 'content')
    for div in divs:
        # 方法一, 使用 text (會包含許多換行符號)(這方式會保留很多換行符號跟空白  混亂)
        #print(div.text)

        # 方法二, 使用 tag 定位  (每一個div下面找h6然後再把它的text印出來 印出來的時候記得  把它的前後空白或是換行符號都去掉)
        #print(div.h6.text.strip(), div.h4.a.text.strip(), div.p.text.strip())

        # 方法三, 使用 .stripped_strings

        print(div.stripped_strings)

        ''' BeautifulSoup
            內建的取得文字字串的方式
            就是所謂的stripped_strings
            那stripped_strings會把這一個網頁
            元件下面全部的字串
            被所謂的子標籤夾住的字串
            一個一個的幫你分開
            幫你分開之後再幫你把
            前後的空白跟換行符號去掉
            所以我們可以直接用.stripped_strings
            去取得這一個div下面全部的文字
            全部的文字包含了這個div下面有h6
            有這個文字跟這個文字
            跟這個文字跟這個文字
            所以它分別被四個tag所包住
            所以stripped_strings會幫你把這四段文字切開
            不過當你執行的時候你會發現
            它回傳的是你看不懂的物件的表示方式
            因為stripped_strings它回傳的
            是一個iterator object
            iterator物件必須要去iterate它
            去巡覽它之後，你才能夠取得它的值
             '''

      
        ''' 所以我們會這樣子去寫
            對於它回傳的物件
            我們會一個一個回去看
            如果你一個一個去看它，再把它印出來
            那你就會發現，它的確就是那些文字 
            一個字會印一行 '''

        ''' 
        for s in div.stripped_strings:
            print(s)
        '''


        print([s for s in div.stripped_strings])

        ''' 有一個比較簡便的方式
            就是我們可以把
            它回傳的字串放在一個list裡面
            之後再處理會比較方便
            我們做法是
            去巡覽它回傳的這個iterator object
            那巡覽的每一個結果把它放到一個list裡面
            這個時候你再去把它印出來
            就可以看出它字的內容 '''

if __name__ == '__main__':
    main()
