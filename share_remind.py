"""
作者：Mr.Feng
功能：股票提醒系统
版本：V3.0
时间：2019/07/14
"""
import tushare as ts
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class Share:
    def __init__(self, code, buy, sale):
        self.code = code
        self.buy = buy
        self.sale = sale

    def buy_sale_decision(self):
        data_now = ts.get_realtime_quotes(self.code)  # 获取实时分笔数据,参考tushare主页介绍
        name = data_now.loc[0][0]  # 股票名字
        price = float(data_now.loc[0][3])  # 当前价格
        data_date = data_now.loc[0][30]  # 日期
        data_time = data_now.loc[0][31]  # 时间
        describe = '股票名字: ' + name + '当前价格: ' + str(price) + '日期: '+data_date + '时间: ' + data_time
        print(describe)

        # print('股票名字：',name,'当前价格：',price,'日期:',data_date,'时间：',data_time)

        if price <= self.buy:
            print('达到买点，买进！')
            send_email('达到买点', describe)
        elif price >= self.sale:
            print('达到卖点，卖出！')
            send_email('达到卖点', describe)
        else:
            print('拿着不动!')


def send_email(subject, content):
    msg_from = 'feng_jie324@sina.com'  # 发送方邮箱
    pwd = '*************'  # 邮箱密码
    msg_to = '2478177109@qq.com'  # 接收方邮箱
    # 构造邮件
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = Header('ShareAlert<feng_jie324@sina.com>')
    msg['To'] = msg_to

    """发送邮件"""

    try:
        ss = smtplib.SMTP('smtp.sina.com', 25)
        ss.login(msg_from, pwd)
        ss.sendmail(msg_from, msg_to, msg.as_string())
        print('发送成功!')
    except Exception as e:
        print('发送失败！ 详情：', e)


def main():
    share1 = Share('sh', 2900, 3000)
    share2 = Share('399363', 3250, 4500)
    share3 = Share('cyb', 1200, 2500)
    share_list = [share1, share2, share3]
    while 1 > 0:
        for share in share_list:
            share.buy_sale_decision()
        print('-----------------------------------------------------------------------------------')
        time.sleep(30)


if __name__ == '__main__':
    main()

