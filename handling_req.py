from flask import render_template
import requests

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