
import  urllib.request as ur
import re
import requests
token = '5750144758:AAH1CvSZ0NJIIzROH3WB1ruWSxi0etz6D1U'
url = f'https://api.telegram.org/bot{token}/getUpdates'
dolor_api = 'https://dapi.p3p.repl.co/api/?currency=usd'
bitcoin_api = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR'
class bot:
    def __init__(self,url,token,dolar_api,bitcoin_api):
        self.url = url
        self.token = token
        self.dolar_api = dolar_api
        self.bitcoin_api = bitcoin_api
    def price_bitcoin(self):
        dolar_price_dict = ur.urlopen(self.bitcoin_api)
        data_read = str(dolar_price_dict.read())
        print(data_read)
        data_return = re.findall('"USD":[0-9]+|"JPY":[0-9]+|"EUR":[0-9]+',data_read)
        print(data_return)
        self.a = ''
        for i in data_return:
            self.a+=f'{i}\n'
        return self.a


    def price_dolar(self):
        dolar_price_dict = ur.urlopen(self.dolar_api)
        data_read = str(dolar_price_dict.read())
        #print(data_read)
        find_price = re.findall('"Price":"[0-9]+"',data_read)
        #print(find_price)
        find_price1 = find_price[0]
        #print(find_price1)
        find_price2 = re.findall('[0-9]+',find_price1)
        #print(find_price2)
        find_price3 = find_price2[0]
        #print(find_price3)
        return find_price3


    def bot(self):
        request = ur.urlopen(self.url)
        data = str(request.read())
        #print(type(data))
        message_id = re.findall('"message_id":[0-9]+',data)
        chat_id = re.findall('"chat":{"id":[0-9]+',data)
        text = re.findall('"text":"[a-z]+"|"text":"/[a-z]+|"text":"Dolar"',data)
        print(len(message_id))
        print(message_id)
        print("--------------------------")
        print(len(chat_id))
        print(chat_id)
        print("-----------------------------")
        print(len(text))
        print(text)
        print("------------------------------")
        print("start_bot..........................")
        while True:
            request_betwin = ur.urlopen(self.url)
            data_betwin = str(request_betwin.read())
            new_message_id = re.findall('"message_id":[0-9]+',data_betwin)
            new_chat_id = re.findall('"chat":{"id":[0-9]+', data_betwin)
            text_betwin = re.findall('"text":"[a-z]+"|"text":"/[a-z]+"|text":"Dolar', data_betwin)
            print(new_message_id)
            print('--------------------------------')
            print(new_chat_id)
            print('----------------------------')
            print(text_betwin)
            print('------------------------------')
            len_for = len(new_message_id)
            for i in range(0,len_for):
                try:
                      if (new_chat_id[i] == chat_id[i])and(new_message_id[i] == message_id[i])and(text_betwin[i] == text[i]):
                           pass
                except:
                    print("new_message")
                    chat_id_post_str = new_chat_id[i]
                    chat_id_post_number_l = re.findall('[0-9]+',chat_id_post_str)
                    chat_id_post_number = int(chat_id_post_number_l[0])
                    text_read = str(text_betwin[i])
                    text_start = 'hellow\nwelcome\nthis bot for a price of currency,gold,USD\nfore show Instructions\nsend */help*'
                    text_help='dolar_price:dolar\nbitcoin:bit'
                    if text_read == '"text":"/start"':
                        requests.get(f'https://api.telegram.org/bot{self.token}/sendmessage?chat_id={chat_id_post_number}&text={text_start}')
                    if text_read == '"text":"/help"':
                        requests.get(f'https://api.telegram.org/bot{self.token}/sendmessage?chat_id={chat_id_post_number}&text={text_help}')
                    if text_read == '"text":"dolar"':
                        requests.get(f'https://api.telegram.org/bot{self.token}/sendmessage?chat_id={chat_id_post_number}&text=price:{self.price_dolar()}')
                    if text_read == '"text":"bit"':
                        requests.get(f'https://api.telegram.org/bot{self.token}/sendmessage?chat_id={chat_id_post_number}&text={self.price_bitcoin()}$')

                    elif (text_read != '"text":"/start"') or ( text_read != '"text":"/help"') or(text_read == '"text":"/dolar"'):
                        requests.get(
                            f'https://api.telegram.org/bot{self.token}/sendmessage?chat_id={chat_id_post_number}&text=pleseType')
                    message_id.append(new_message_id[i])
                    chat_id.append(new_chat_id[i])
                    text.append(text_read)




if __name__ == "__main__":
    x = bot(url,token,dolor_api,bitcoin_api)
    x.bot()