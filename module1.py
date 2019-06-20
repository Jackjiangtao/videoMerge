import urllib.request
from bs4 import BeautifulSoup
import os
 
def Download(url,picAlt,name):
    path = 'D:\\pythonDemo____________爬虫____________\\'+picAlt+'\\'
    if not os.path.exists(path):#判断系统是否存在该路径，不存在则创建
        os.makedirs(path)
    urllib.request.urlretrieve( url, '{0}{1}.jpg'.format(path, name))  # ，下载图片保存在本地
 
header = {
    "User-Agent":'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
 
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive'
    """
        用户代理(User-Agent):用于伪装程序不是爬虫，让服务器以为你是一个正常用户。
            是一种向访问网站提供你所使用的浏览器类型、操作系统及版本、CPU 类型、浏览器渲染引擎、浏览器语言、浏览器插件等信息的标识。
            UA字符串在每次浏览器 HTTP 请求时发送到服务器
    """
}
def run(targetUrl, beginNUM ,endNUM):
    req = urllib.request.Request(url=targetUrl,headers=header)
    response = urllib.request.urlopen(req)#这里的req可看成一种更为高级的URL
    html = response.read().decode('gb2312','ignore')#解码 得到这个网页的html源代码：这个网站的编码使用的是GB2312格式，更常见的网站编码格式应该是UTF-8了吧
    soup = BeautifulSoup(html, 'html.parser')#将得到的HTML代码使用python自带的解析器（也可以使用lxml解析器，性能会更好，本代码从简
    Divs = soup.find_all('div',attrs={'id':'big-pic' })#使得条件唯一，找到我们想要下载的目标。这里语法是bs，主流的解析搜索方式有：bs，xpath和正则 ，小白还是用bs吧
    nowpage = soup.find('span',attrs={'class':'nowpage'}).get_text()#获取当前页码
    totalpage= soup.find('span',attrs={'class':'totalpage'}).get_text()#获取所有页
    if beginNUM ==endNUM :#跳出条件
        return
    for div in Divs:#遍历所有大图所在的div,其实只有一个元素。因为前面使用的是find_all()方法得到的是集合，所以这要遍历了。有点不太实用 因为与照顾到语法使用全面的意思
        beginNUM = beginNUM+1
 
        if div.find("a") is None :#如果这张图片没有下一张图片的链接
            print("没有下一张了")
            return
        elif div.find("a")['href'] is None or div.find("a")['href']=="":#有链接，但是是 空链接
            print("没有下一张了None")
            return
        print("=====================================================下载信息：总进度：",beginNUM,"/",endNUM," ，正在下载套图：(",nowpage,"/",totalpage,")====================================")
 
        if int(nowpage)<int(totalpage):#nowpage，totalpage是str类型；（如果不转换成int来比较的话，totalPage是字符串“12”无法与‘1’‘2’这些单个字符的字符串比较）
            nextPageLink ="http://www.mmonly.cc/mmtp/qcmn/" +(div.find('a')['href'])
        elif int(nowpage)==int(totalpage):
            nextPageLink = (div.find('a')['href'])
 
        picLink = (div.find('a').find('img')['src'])#本网站大图的SRC属性是下一张图片的链接
        picAlt = (div.find('a').find('img'))['alt']#图片的名字alt属性
        print('下载的图片链接:',picLink)
        print('套图名：[ ', picAlt , ' ] ')
        print('开始下载...........')
        Download(picLink,picAlt, nowpage)
        print("下载成功！")
        print('下一页链接:',nextPageLink)
        run(nextPageLink,beginNUM ,endNUM)#递归
        return
 
#################################main 函数########################################
if __name__ == '__main__':
    #可以是这个网站（http://www.mmonly.cc/mmtp/qcmn/）下的任意一个网址（如下）开始爬取，means爬取的起点（）
    # targetUrl ="http://www.mmonly.cc/mmtp/qcmn/258345_2.html"
    # targetUrl ="http://www.mmonly.cc/mmtp/qcmn/259676_8.html"
    targetUrl ="http://www.mmonly.cc/mmtp/qcmn/237269.html"
    run(targetUrl,beginNUM=0,endNUM=60)#设置下载图片数量：endNUM-beginNUM 数字相减为总数量
    print("【【【【       OVER！        】】】】】")