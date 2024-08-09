import requests
import gradio as gr
def do(text):
    s=0
    if text=='銀行買入':
        s=2
    elif text=='銀行賣出':
        s=3
    else:
        return '請正確輸入喔!'
        exit()
    ans=[]
    url='https://rate.bot.com.tw/xrt/flcsv/0/day'
    thing=requests.get(url)
    thing.encoding='utf-8'
    txt=thing.text
    time=txt.split('\n')
    for i in time:
        try:
            k=i.split(',')
            ans.append(k[0]+':'+k[s])
            #return k[0]+':'+k[s]
        except:
            return ans
            break 
iface=gr.Interface(fn=do,
                title='台灣銀行爬蟲',
                description='請輸入您要提取的東西(銀行買入或銀行賣出)(兩者都是現今匯率)(資料來源:台灣銀行)',
                inputs='text',
                outputs='text'
                   )
iface.launch(share=True)


  