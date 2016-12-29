import urllib.request    
import socket    
import re    
import sys    
import os    
targetDir = "./Douban/picture/"
def testFile(path):    
    if not os.path.isdir(targetDir):    
        os.mkdir(targetDir)    
    pos = path.rindex('/')    
    t = os.path.join(targetDir, path[pos+1:])    
    return t    
if __name__ == "__main__":  #程序运行入口  
    weburl = "http://www.douban.com/"  
    webheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}   
    req = urllib.request.Request(url=weburl, headers=webheaders)  #构造请求报头  
    webpage = urllib.request.urlopen(req)  #发送请求报头  
    contentBytes = webpage.read()
    contentBytes = contentBytes.decode('UTF-8')
    #print(contentBytes)
    #print('______________')
    for link, t in set(re.findall(r'(https:[^\s]*?(jpg|png|gif))', contentBytes)):  #正则表达式查找所有的图片  
        print(link) 
        print(t)
        try:   
            urllib.request.urlretrieve(link, testFile(link)) #下载图片  
        except:  
            print('失败') #异常抛出 
'''
https://img3.doubanio.com/view/dianpu_product_item/medium/public/p377790.jpg
jpg
https://img1.doubanio.com/view/ark_article_cover/large/public/28925118.jpg
jpg
https://img3.doubanio.com/icon/g292021-3.jpg
jpg
https://img3.doubanio.com/view/site/small/public/4ff788daaa1b9d4.jpg
jpg
https://img1.doubanio.com/view/event_poster/small/public/53fe391ad8dc9c9.jpg
jpg
https://img1.doubanio.com/view/ark_article_cover/large/public/27947849.jpg
jpg
https://img3.doubanio.com/view/site/small/public/41a05c67f29d832.jpg
jpg
https://img3.doubanio.com/img/songlist/large/493827-4.jpg
jpg
https://img3.doubanio.com/view/dianpu_shop_icon/medium/public/9d03efbf705887d.jpg
jpg
https://img1.doubanio.com/spic/s29157729.jpg
jpg
https://img3.doubanio.com/view/dianpu_product_item/medium/public/p209660.jpg
jpg
https://img1.doubanio.com/view/movie_poster_cover/spst/public/p2406638957.jpg
jpg
https://img3.doubanio.com/img/songlist/large/13802226-1.jpg
jpg
https://img3.doubanio.com/icon/g24177-1.jpg
jpg
https://img3.doubanio.com/view/dianpu_product_item/medium/public/p458880.jpg
jpg
https://img3.doubanio.com/spic/s29164091.jpg
jpg
https://img1.doubanio.com/icon/g149062-18.jpg
jpg
https://img3.doubanio.com/view/site/small/public/a5ede27ce1dc914.jpg
jpg
https://img3.doubanio.com/icon/g201401-1.jpg
jpg
https://img3.doubanio.com/view/site/small/public/26da380abd71ddd.jpg
jpg
https://img3.doubanio.com/img/songlist/large/11986-1.jpg
jpg
https://img5.doubanio.com/view/dianpu_shop_icon/medium/public/169b1b76356f636.jpg
jpg
https://img3.doubanio.com/spic/s29212232.jpg
jpg
https://img3.doubanio.com/spic/s29219435.jpg
jpg
https://img3.doubanio.com/img/files/file-1423193113.png
png
https://img3.doubanio.com/view/dianpu_product_item/medium/public/p270364.jpg
jpg
https://img1.doubanio.com/img/files/file-1478594087.jpg
jpg
https://img3.doubanio.com/icon/g13266-32.jpg
jpg
https://img1.doubanio.com/view/photo/albumcover/public/p2302848198.jpg
jpg
https://img3.doubanio.com/view/dianpu_shop_icon/medium/public/5f1ed6b928e7434.jpg
jpg
https://img3.doubanio.com/pics/icon/jubao.png
png
https://img3.doubanio.com/view/site/small/public/5fb52fdcb25f763.jpg
jpg
https://img3.doubanio.com/icon/g16533-1.jpg
jpg
https://img5.doubanio.com/view/ark_article_cover/large/public/15077436.jpg
jpg
https://img5.doubanio.com/view/movie_poster_cover/spst/public/p2404720316.jpg
jpg
https://img3.doubanio.com/view/movie_poster_cover/spst/public/p2390687452.jpg
jpg
https://img3.doubanio.com/view/event_poster/small/public/fd23d4a3d20bb70.jpg
jpg
https://img3.doubanio.com/f/sns/1f6d8a4cb8c89de5d931a3d4e3276a7221c3c0d9/pics/sns/anony_home/ypy_qr.jpg
jpg
https://img3.doubanio.com/f/sns/0c708de69ce692883c1310053c5748c538938cb0/pics/sns/anony_home/icon_qrcode_green.png
png
https://img3.doubanio.com/view/movie_poster_cover/spst/public/p2394573821.jpg
jpg
https://img5.doubanio.com/view/dianpu_product_item/medium/public/p521646.jpg
jpg
https://img3.doubanio.com/img/songlist/large/1338534-1.jpg
jpg
https://img3.doubanio.com/view/ark_article_cover/large/public/28784360.jpg
jpg
https://img3.doubanio.com/icon/g536786-2.jpg
jpg
https://img1.doubanio.com/icon/g48758-8.jpg
jpg
https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif
gif
https://img3.doubanio.com/spic/s29228455.jpg
jpg
https://img3.doubanio.com/view/ark_article_cover/large/public/28472864.jpg
jpg
https://img3.doubanio.com/view/dianpu_shop_icon/medium/public/7f37444b0a6a0e2.jpg
jpg
https://img3.doubanio.com/view/event_poster/small/public/3142d9ff8cbd6f1.jpg
jpg
https://img3.doubanio.com/view/movie_poster_cover/spst/public/p2402859930.jpg
jpg
https://img3.doubanio.com/icon/g10503-10.jpg
jpg
https://img1.doubanio.com/view/movie_poster_cover/spst/public/p2395733377.jpg
jpg
https://img1.doubanio.com/view/event_poster/small/public/44f627f5635cf3a.jpg
jpg
https://img1.doubanio.com/mpic/s29232827.jpg
jpg
https://img3.doubanio.com/pics/biaoshi.gif
gif
https://img3.doubanio.com/f/sns/1cad523e614ec4ecb6bf91b054436bb79098a958/pics/sns/anony_home/doubanapp_qrcode.png
png
https://img1.doubanio.com/view/dianpu_product_item/medium/public/p509169.jpg
jpg
https://img3.doubanio.com/pics/new_menu.gif
gif
https://img1.doubanio.com/spic/s29232368.jpg
jpg
https://img1.doubanio.com/view/movie_poster_cover/spst/public/p2402705389.jpg
jpg
https://img3.doubanio.com/icon/g12087-4.jpg
jpg
https://img5.doubanio.com/img/files/file-1431585796.jpg
jpg
https://img5.doubanio.com/spic/s29149466.jpg
jpg
https://img3.doubanio.com/view/photo/albumcover/public/p2406945274.jpg
jpg
https://img5.doubanio.com/icon/g116210-6.jpg
jpg
https://img1.doubanio.com/view/ark_article_cover/large/public/25750679.jpg
jpg
https://img3.doubanio.com/spic/s29245350.jpg
jpg
https://img1.doubanio.com/icon/g13784-7.jpg
jpg
https://www.douban.com/pics/blank.gif
gif
https://img3.doubanio.com/view/photo/albumcover/public/p2401835611.jpg
jpg
https://img1.doubanio.com/view/movie_poster_cover/spst/public/p2397337958.jpg
jpg
https://img3.doubanio.com/view/ark_article_cover/large/public/27819391.jpg
jpg
https://img3.doubanio.com/view/photo/albumcover/public/p2180461505.jpg
jpg
'''