import requests
from bs4 import BeautifulSoup

''' 認識BeautifulSoup的基本功能
主要會講解巡覽網頁結構
也就是怎麼樣找到一個網頁元件
的parent, children跟siblings '''

def main():
    resp = requests.get('http://newmedia.tw/aiarts/table.html')
    soup = BeautifulSoup(resp.text, 'html.parser')

    # 計算課程平均人數  
    # 我們關心的是tbody下面的每一列  也就是每一個tr的第三個欄位  第三個td，因為它存放了人數的資訊
    # 取得所有課程人數: 方法一, 使用 index
    prices = []   #首先我們先用一個list去存  我們即將取得的人數的資訊
    # 再來我們去找到那一張表格  找到那張表格的下面的tbody  之後再去找tbody下面全部的row，全部的tr  先存在rows裡面
    rows = soup.find('table', 'table').tbody.find_all('tr')  

    ''' 接著我們對每一列去巡覽
        巡覽的方式是
        我們對於每一列去找它全部的td
        那我們需要的是第三欄
        那BeautifulSoup跟Python的index是從零開始
        所以第三欄就是索引2，就是index 2 '''

    '''  我們找到它全部的td
        然後取得它第三欄
        也就是index為2的文字，就是我們的價錢
        在這邊你也可以把價錢印出來看看
        對那找到價錢之後
        再把它放進去我們的price的list裡面
        最後再把它平均
        就是把它加起來再除以list的長度
        就是課程的平均價錢
        所以它執行的結果會像是這個樣子
        它把每一個欄位價錢欄位的值
        都取出來之後做平均 '''
    for row in rows:
        price = row.find_all('td')[2].text
        prices.append(int(price))
    print(sum(prices)/len(prices))


    # 取得所有課程人數: 方法二, <a> 的 parent (<td>) 的 previous_sibling
    # 人數一個欄位  其實很靠近這一個a這一個超連結的欄位
    prices = []
    links = soup.find_all('a')
    for link in links:   # 對每一個超連結
        price = link.parent.previous_sibling.text  
        # 先找到它的parent parent就是它所在的那一個欄位 那一個td，然後那一個td的前一個td
        # previous sibling就是人數所在的欄位 text就是人數本身
        prices.append(int(price))
    print(sum(prices) / len(prices))


    ''' 接著
        怎麼樣來取得這一個網頁全部的資訊
        以及怎麼樣取得網頁元件的屬性
        也就是說這一個表格有六列
        每一列有四欄
        那第四欄是一個超連結跟一個圖片
        我們希望把每一列的文字
        課程名稱、對象人數都印出來
        而且它的超連結跟它的圖片網址
        的來源也印出來 '''
 
    # 取得每一列所有欄位資訊: find_all('td') or row.children
    rows = soup.find('table', 'table').tbody.find_all('tr')
     #首先一樣把每一列都找出來 先找到表格本身，再找tbody
     #再找每一列，存到rows裡面

    for row in rows: # 對於每一列，我們要找到它全部的欄位
        all_tds = row.find_all('td')  # 方法一: find_all('td)
      # all_tds = [td for td in row.children]  # 方法二: 找出 row (tr) 所有的直接 (下一層) children
      # 以下執行時會報錯, 因為最後一列的 <a> 沒有 'href' 屬性  會有exception
      # print(all_tds[0].text, all_tds[1].text, all_tds[2].text, all_tds[3].a['href'], all_tds[3].a.img['src'])

       
       

        # 可以改成這樣子的寫法  我們在取得這個屬性之前  先檢查它是不是存在  
        # 檢查的方法就是用.attribute()這個function         
        # 取得 href 屬性前先檢查其是否存在
        if 'href' in all_tds[3].a.attrs: # 這個function回傳的會是一個dictionary 
                                         # 那我們檢查href這個key 有沒有在它的attribute的dictionary裡面
            href = all_tds[3].a['href']  # 如果有在的話就直接取用它的值 
        else:
            href = None                  # 那如果不在的話就設為None
        print(all_tds[0].text, all_tds[1].text, all_tds[2].text, href, all_tds[3].a.img['src'])


    ''' 複習一下
        stripped_strings方法
        也就是要怎麼樣把這一些
        把這一個表格這六列的文字都印出來
        我們可以看到它每一列這些文字都
        分別被這三個欄位這三個td的tag夾住
        所以stripped_strings就可以把這三個字串
        每一列的這三個字串
        都幫我們把它切分出來 '''


    # 取得每一列所有欄位文字資訊: stripped_strings
    rows = soup.find('table', 'table').tbody.find_all('tr')
    for row in rows:
        print([s for s in row.stripped_strings])

if __name__ == '__main__':
    main()
