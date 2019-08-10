#from webcrawl.bugsmusic import BugsCrawler
from webcrawl.Controller import Controller as cr

if __name__ == '__main__':
    print('a : 국회 크롤링')
    print('b : 국회 크롤링')
    print('0 : 종료')
    flag = input()
    if(flag == 'a'):
        url = 'http://likms.assembly.go.kr/bill/billDetail.do?billId=PRC_R1N9J0N1X0Y9A1O8S3R5Z3J3K9O8N7'
    elif(flag == 'b'):
        url = 'https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20190810&charthour=11'
    elif (flag == '0')
        break
        
    cr.exec(flag, url)
