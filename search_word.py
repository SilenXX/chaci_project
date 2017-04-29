import sys
import webbrowser
import urllib.request
import urllib.parse
import json
import sqlite3
from bs4 import BeautifulSoup

def main_display():
    print('------------------------------------------------------------------\n')
    print('\t\t\t命令说明\n')
    print('输入\tword + 单词\t进行单词查询\n')
    print('输入\tview\t\t用浏览器查看单词查询历史记录\n ')
    print('输入\texport\t\t导出单词查询历史记录到d:\\word_list.txt文件\n')
    print('输入\tquit\t\t退出本程序\n')
    print('------------------------------------------------------------------')


def export_word():
    url = "http://127.0.0.1:8000/record/"
    response = urllib.request.urlopen(url, timeout=3)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    result = []
    for line in soup.findAll('td'):
        result.append(line.string.split(' ')[0])
    f = open('d:/word_list.txt', 'w')
    for word in result:
        f.write('%s\n' % word)
    f.close()
    print('单词查询历史记录已成功导出到d:\\word_list.txt文件。')

def show_word():
    sys.path.append("libs")
    url = "http://127.0.0.1:8000/record/"
    webbrowser.open(url)
    print('单词查询历史已成功显示在浏览器中。')

def save_word(word):
    content = word
    url = "http://127.0.0.1:8000/record/add?word="
    response = urllib.request.urlopen(url + content)
        
def translation_word(word):
    content = word
    url = 'http://fanyi.youdao.com/openapi.do?keyfrom=shizutrans&key=1742896871&type=data&doctype=json&version=1.1&q='
    response = urllib.request.urlopen(url + content, timeout=3)
    html = response.read().decode('utf-8')
    target = json.loads(html)
    explains = target.get('basic').get('explains')
    print('\n%s' % word)
    for i in explains:
        print(i)
    save_word(word)



main_display()
while True:
    msg = input('\n请输入你的命令:\r\n')
    if msg == 'quit':
        break
    elif msg == 'view':
        show_word()
    elif msg == 'export':
        export_word()
    else:
        [order, word] = msg.split(' ')
        if order == 'word':
            translation_word(word)