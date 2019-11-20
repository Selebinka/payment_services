from flask import Flask

from flask import render_template, request, redirect
import random
import requests
from hashlib import sha256


app = Flask(__name__)

shop_id = '5'
secretKey = 'SecretKey01'
payway = 'payeer_rub'


@app.route('/', methods=['POST', 'GET'])
def handling():
    if request.method == 'POST':
        amount = request.form['summ']
        currency = request.form['currency']
        discription = request.form['discription']
        shop_order_id = str(random.randint(1,99999))
        
        if currency == 'EUR':
            currency = '978'
            keys_sorted = [amount, currency, shop_id, shop_order_id]
            sign = sign_gen(keys_sorted)
            return render_template('pay.html', 
                                    amount=amount, 
                                    currency=currency,
                                    shop_id=shop_id,
                                    sign=sign,
                                    shop_order_id=shop_order_id
                                )
        if currency == 'USD':
            currency = payer_currency = '840'
            keys_sorted = [currency, amount, payer_currency, shop_id, shop_order_id]
            sign = sign_gen(keys_sorted)
            data = {'payer_currency': payer_currency,
                    'shop_amount': amount, 
                    'shop_currency': currency, 
                    'shop_id': shop_id, 
                    'shop_order_id': shop_order_id,
                    'sign': sign
                }
            res_url = handlingBill(data)
            return redirect(res_url)

        if currency == 'RUB':
            currency = '643'
            keys_sorted = [amount, currency, payway, shop_id, shop_order_id]
            sign = sign_gen(keys_sorted)
            data = {"amount": amount,
                    "currency": currency,
                    "payway": payway,
                    "shop_id": shop_id,
                    "shop_order_id": shop_order_id,
                    "sign": sign
                }
            res_url = handlingInvoice(data)
            return res_url
            
    return render_template('index.html')

def sign_gen(data):
    str_gen = ":".join(data) + secretKey
    sign = sha256(str_gen.encode('utf-8')).hexdigest()
    return sign

def handlingBill(data):
    url = 'https://core.piastrix.com/bill/create'
    res = requests.post(url, json=data)
    result = res.json()['result']
    if result == True:
        url = res.json()['data']['url']
        return url
    
def handlingInvoice(data):
    url = 'https://core.piastrix.com/invoice/create'
    res = requests.post(url, json=data)
    result = res.json()['result']
    if result == True:
        method = res.json()['data']['method']
        action = res.json()['data']['url']
        m_curorderid =  res.json()['data']['data']['m_curorderid']
        m_historyid = res.json()['data']['data']['m_historyid']
        m_historytm =  res.json()['data']['data']['m_historytm']
        referer = res.json()['data']['data']['referer']
        return render_template('invoice.html',
                                method=method,
                                action=action,
                                m_curorderid=m_curorderid,
                                m_historyid=m_historyid,
                                m_historytm=m_historytm,
                                referer=referer
                        )


if __name__ == '__main__':
    app.run(debug=True)

