from flask import Flask

from flask import render_template, request, redirect
import random
from sing_gen import sign_gen
from handling_req import handlingBill ,handlingInvoice
from config import SHOP_ID, PAYWAY


app = Flask(__name__)

@app.route('/', methods=['POST'])
def handling():

    amount = request.form['summ']
    currency = request.form['currency']
    discription = request.form['discription']
    shop_order_id = str(random.randint(1,99999))

    # payment_handlers = {
    #         "USD": usd_payment,
    #         "EUR": eur_payment,
    #         "RUB": rur_payment
    #     }

    if currency == 'EUR':
        currency = '978'
        keys_sorted = [amount, currency, SHOP_ID, shop_order_id]
        sign = sign_gen(keys_sorted)
        return render_template('pay.html', 
                                amount=amount, 
                                currency=currency,
                                shop_id=SHOP_ID,
                                sign=sign,
                                shop_order_id=shop_order_id
                            )
    if currency == 'USD':
        currency = payer_currency = '840'
        keys_sorted = [currency, amount, payer_currency, SHOP_ID, shop_order_id]
        sign = sign_gen(keys_sorted)
        data = {'payer_currency': payer_currency,
                'shop_amount': amount, 
                'shop_currency': currency, 
                'shop_id': SHOP_ID, 
                'shop_order_id': shop_order_id,
                'sign': signg
            }
        res_url = handlingBill(data)
        return redirect(res_url)

    if currency == 'RUB':
        currency = '643'
        keys_sorted = [amount, currency, PAYWAY, SHOP_ID, shop_order_id]
        sign = sign_gen(keys_sorted)
        data = {"amount": amount,
                "currency": currency,
                "payway": PAYWAY,
                "shop_id": SHOP_ID,
                "shop_order_id": shop_order_id,
                "sign": sign
            }
        res_url = handlingInvoice(data)
        return res_url

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

