from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask import render_template, request, redirect, Response
from logging_config import logging_config
import logging.config

import random
from datetime import datetime
from modules.handling_req import handlingBill, handlingInvoice
from modules.sign_gen import sign_gen
from config import SHOP_ID, PAYWAY, Config
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models import *


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app,  db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def handling():
    try:
        amount = request.form['summ']
        currency = request.form['currency']
        discription = request.form['discription']
        shop_order_id = str(random.randint(1,99999))
        send_time = datetime.now().strftime('%H:%M:%S')
         
        p = Payments()
        p.currency = currency
        p.amount = amount
        p.discription = discription
        p.send_time = send_time
        p.shop_order_id = shop_order_id

        db.session.add(p)
        try:
            db.session.commit()
        except Exception as e:
            app.logger.exception('{}'.format(e))
            db.session.rollback()
            eprint(str(e))
            
        if currency == 'EUR':
            currency = '978'
            required_keys = {
                    'amount': amount, 
                    'currency': currency,  
                    'shop_id': SHOP_ID, 
                    'shop_order_id': shop_order_id
                }
            sign = sign_gen(required_keys)
            return render_template('pay.html', 
                                    amount=amount, 
                                    currency=currency,
                                    shop_id=SHOP_ID,
                                    sign=sign,
                                    shop_order_id=shop_order_id
                                )

        if currency == 'USD':
            currency = payer_currency = '840'
            required_keys = {
                    'shop_amount': amount, 
                    'shop_currency': currency,
                    'payer_currency': payer_currency,  
                    'shop_id': SHOP_ID, 
                    'shop_order_id': shop_order_id
                }
            sign = sign_gen(required_keys)
            required_keys.update({'sign': sign})
            res_url = handlingBill(required_keys)
            return redirect(res_url)

        if currency == 'RUB':
            currency = '643'
            required_keys = {
                "amount": amount,
                "currency": currency,
                "payway": PAYWAY,
                "shop_id": SHOP_ID,
                "shop_order_id": shop_order_id,
                }
            sign = sign_gen(required_keys)
            required_keys.update({"sign": sign})
            res_url = handlingInvoice(required_keys)
            return res_url

    except Exception as error:
        app.logger.exception('{}'.format(error))
        return Response(505, 'Internal Server Error')


if __name__ == '__main__':
    logging.config.dictConfig(logging_config)
    app.run()
    
    
