# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/3 19:18
@Auth ： d1rrick DanielGao.eth
@File ：autochat.py
@IDE ：vscode

"""
import requests
import datetime
import sys
import json
import random
import time
import re

class BATTLE:
    def __init__(self, authorization_list):
        self.authorization_list = authorization_list
        self.chanel_lists = {'ODM3MjMwNjgxMDU4MTgxMTUx.YL8alQ.xxx':['1026468902319964201'],
                'OTE4NzAyODkzMzA0MDA0NjA5.GDxijn.xxx':['1026468903410483251']
                }
        self.session_ids = {'ODM3MjMwNjgxMDU4MTgxMTUx.YL8alQ.xxx':'a9a9f46d9cfff21ea4996415',
                'OTE4NzAyODkzMzA0MDA0NjA5.GDxijn.xxx':'ad3a286c54d9d2cdb396471e5'
                }
        self.userids = {'ODM3MjMwNjgxMDU4MTgxMTUx.YL8alQ.xxx':'83723068',
                'OTE4NzAyODkzMzA0MDA0NjA5.GDxijn.xxx':'91870289330'
                }
        self.usernames = {'ODM3MjMwNjgxMDU4MTgxMTUx.YL8alQ.xxx':'name1#0471',
                'OTE4NzAyODkzMzA0MDA0NjA5.GDxijn.xxx':'name2#7357'
                }
        self.application_id = '980122372684251167'
        self.guild_id = '915445727600205844'
        self.EXIT = False

    def gen_context(self):
        context_list = [
            "兄弟们", "求求了，别肝了", "这个项目怎么样", "有人吗", "ARTIST是干嘛的啊", "GM bro",
            "牛逼", "反应不过来了", "有OAT奖励吗", "怎么样", "下午好啊", "家人们", "1", "牛的", "艺术家",
            "hi~", "项目牛逼", "干干干", "活跃起来", "一起死", "来吧", "太肝了", "银河都要笑了", "你们来自哪儿", "艺术品",
            "good project", "有啥好消息", "看下公告", "来自哪里？", "自我介绍下吧", "太好笑了", "very interesting", "it's funny", "i am tired",
            "我勒个去","血战到底","不要走，大战到天亮","这个项目很棒吧","加油，家人们","你们都好棒啊","想跟你们学技术","加油加油加油","粘贴复制就行了。。。"
        ]
        text = random.choice(context_list)
        return text
    
    
    def get_context(self,chanel_id):
        headr = {
            "Authorization": self.authorization,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
        }
        #chanel_id = random.choice(chanel_list)
        url = "https://discord.com/api/v9/channels/{}/messages?limit=8".format(
            chanel_id)
        res = requests.get(url=url, headers=headr)
        result = json.loads(res.content)
        result_list = []
        #print (result)
        c = 0
        for l in range(len(result)):
            context = result[l]
            if context['author']['username'] == 'Caviar':
                for embeds in context['embeds']:
                    if re.search('<@' + self.userid + '>, you have reached the limit', embeds['description']):
                        c+=1
                if c >= 2:
                    print ('cool down && exit')
                    self.EXIT = True
                for mentions in context['mentions']:
                    try:
                        if mentions['username'] == self.username.split('#')[0] and mentions['discriminator'] == self.username.split('#')[1]:
                            for embeds in context['embeds']:
                                if re.search('You need to react to', embeds['description']):
                                    #print ('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                                    print (embeds['description'])
                                    #https://discord.com/channels/915445727600205844/1026468902319964201/1031850822553837708
                                    #self.EXIT = True
                            result_list.append(context)
                            #self.EXIT = True
                            break
                    except:
                        continue
        #print (result_list)
        #sys.exit(0)
        return result_list
    
    
    def play(self):
        #chanel_lists = ['997064398600421387','997064400315891722','997064402316562442','997064403897819156','998510576743493672']
        #authorization_list = ['ODM3MjMwNjgxMDU4MTgxMTUx.YL8alQ.xxx', 'OTE4NzAyODkzMzA0MDA0NjA5.GDxijn.xxx']
        #authorization_list = ['ODM3MjMwNjgxMDU4MTgxMTUx.YL8alQ.xxx']
        for authorization in self.authorization_list:
            self.authorization = authorization
            self.session_id = self.session_ids.get(self.authorization)
            self.userid = self.userids.get(self.authorization)
            self.username = self.usernames.get(self.authorization)
            self.chanel_list = self.chanel_lists.get(self.authorization)
            chanel_list = [random.choice(self.chanel_list)]
            print (self.username + '@',chanel_list[0])
            header = {
                "Authorization": self.authorization,
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
            }
            parrten_num = {'Dear lord! What was that': 2, 'Make your choice':1, 'You need some cool down':None}
            out = []
            FLAG = 0
            s = 0
            special = 0
            for chanel_id in self.chanel_list:
                for i in range(1,100):
                    s = s + 1
                    if s > 1:
                        out = self.get_context(chanel_id)
                    else:
                        out = []
                        FLAG = 0
                    if out:
                        print (out[0])
                        mid = out[0]['id']
                        c_id = out[0]['channel_id']
                        title = out[0]['embeds'][0].get('title',None)
                        if not title:
                            description = out[0]['embeds'][0].get('description')
                            if re.search('You need to react to', description):
                                #❌ You need to react to �[this message](https://discord.com/channels/915445727600205844/1026468902319964201/1031853303472062484)� to go further
                                mid = description.split(')')[0].split('/')[6]
                                title = 'Make your choice ❌'
                                special = 1
                                s = 0
                        #components = out[0]['components']
                        nonce = "103041{}761106432".format(random.randrange(1000, 9900))
                        weizhi = random.choice(["dnd_roadmap_choice:" + self.userid + ":left","dnd_roadmap_choice:" + self.userid + ":right"])
                        for key,n in parrten_num.items():
                            FLAG = 0
                            if re.search(key, title):
                                FLAG = n
                                break
                    time.sleep(2)
                    if FLAG == None:
                        sys.exit(0)
                    if FLAG == 0:
                        msg = {
    
                            "content": "$go",
                            "nonce": "82329451214{}33232234".format(random.randrange(0, 1000)),
                            "tts": False
    
                            }
                        url = 'https://discord.com/api/v9/channels/{}/messages'.format(chanel_id)
                        try:
                            res = requests.post(url=url, headers=header,data=json.dumps(msg))
                        except Exception:
                            print(Exception)
                            continue
                    elif FLAG == 1:
                        msg = {
                            "type":3,
                            "nonce":nonce,
                            "guild_id":self.guild_id,
                            "channel_id":c_id,
                            "message_flags":0,
                            "message_id":mid,
                            "application_id":self.application_id,
                            "session_id":self.session_id,
                            "data":{"component_type":2,"custom_id":weizhi}
                           }
                    elif FLAG == 2:
                        msg = {
                            "type":3,
                            "nonce":nonce,
                            "guild_id":self.guild_id,
                            "channel_id":c_id,
                            "message_flags":0,
                            "message_id":mid,
                            "application_id":self.application_id,
                            "session_id":self.session_id,
                            "data":{"component_type":2,"custom_id":"retreat_from_giant_hunter:" + self.userid}
                           }
                    if special == 1:
                        msg1 = {
                            "type":3,
                            "nonce":nonce,
                            "guild_id":self.guild_id,
                            "channel_id":c_id,
                            "message_flags":0,
                            "message_id":mid,
                            "application_id":self.application_id,
                            "session_id":self.session_id,
                            "data":{"component_type":2,"custom_id":"retreat_from_giant_hunter:" + self.userid}
                            }
                    #https://discord.com/api/v9/interactions
                    if FLAG == 1 or FLAG == 2:
                        print (msg)
                        url = 'https://discord.com/api/v9/interactions'
                        try:
                            res = requests.post(url=url, headers=header,data=json.dumps(msg))
                            print (res.text)
                        except Exception:
                            print(Exception)
                            continue
                    time.sleep(1)
                    if special == 1:
                        url = 'https://discord.com/api/v9/interactions'
                        try:
                            res = requests.post(url=url, headers=header,data=json.dumps(msg1))
                            print (res.text)
                        except Exception:
                            print(Exception)
                            continue
                        special = 0
                    if self.EXIT and FLAG != 1:
                        sys.exit(0)
                    #i = i + 1
                    #sys.exit(0)
                    #out = get_context(chanel_id)
                    #time.sleep(sleep_time)
            # 取30秒到50之间的一个随机数，作为循环的间隔时间。
            time.sleep(random.randrange(1, 5))


if __name__ == '__main__':
   # while True:
   #     try:
   #         print('start')
   #         chat()
   #         break
   #         # 取180秒到240之间的一个随机数，作为机器人发送消息的间隔时间。
   #         sleeptime = random.randrange(15, 30)
   #         time.sleep(sleeptime)
   #     except:
   #         pass
   #     continue
    print ('start at:' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    #time.sleep(random.randrange(10, 115))
    #players = ['ODM3MjMwNjgxMDU4MTgxMTUx.YL8alQ.xxx','OTE4NzAyODkzMzA0MDA0NjA5.GDxijn.xxx']
    players = ['OTE4NzAyODkzMzA0MDA0NjA5.GDxijn.xxx']
    game = BATTLE(players)
    game.play()
