import requests
from bs4 import BeautifulSoup
import os

import telegram

# 토큰을 지정해서 bot을 선언해 줍시다! (물론 이 토큰은 dummy!)
bot = telegram.Bot(token='#')
# 우선 테스트 봇이니까 가장 마지막으로 bot에게 말을 건 사람의 id를 지정해줄게요.
# 만약 IndexError 에러가 난다면 봇에게 메시지를 아무거나 보내고 다시 테스트해보세요.
chat_id = bot.getUpdates()[-1].message.chat.id

# 파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get('https://www.yp21.go.kr/board/list.yangpyeong?boardId=BBS_0000035&menuCd=DOM_000000135007007001&contentsSid=1030')
req.encoding = 'utf-8'

html = req.text
soup = BeautifulSoup(html, 'html.parser')
posts = soup.select('td.txt-dot')
for li in posts:
    print(li.text)


with open(os.path.join(BASE_DIR, 'latest.txt'), 'r+') as f_read:
    before = f_read.readline()
    if before != latest:
        bot.sendMessage(chat_id=chat_id, text='새 글이 올라왔어요!')
    else: # 원래는 이 메시지를 보낼 필요가 없지만, 테스트 할 때는 봇이 동작하는지 확인차 넣어봤어요.
        bot.sendMessage(chat_id=chat_id, text='새 글이 없어요 ㅠㅠ')
    f_read.close()

with open(os.path.join(BASE_DIR, 'latest.txt'), 'w+') as f_write:
    f_write.write(latest)
    f_write.close()