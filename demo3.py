# coding=gbk
import requests
from business import denglu

tk = denglu.test_dlxt()
print(tk)
url = 'http://192.168.0.21:9090/settlement/add'
heads = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
data = {"data": [{"id": 67253, "business_no": "XD23030035", "kp_business_no": "", "contract_amount": "3672.00",
                  "sales_amount": "3672.00", "drawer_time": 1678032000, "sales_id": 5, "sales_man": "罗利娟",
                  "customer_id": 1026, "customer_name": "上海鸣驭信息技术有限公司", "collection_period": 1680710400,
                  "overdue_days": -31, "receive_amount": "0.00", "not_receive_amount": "3672.00",
                  "invoice_amount": "0.00", "not_invoice_amount": "3672.00", "refund_amount": "0.00",
                  "receive_amount_month": "0.00", "settlement_amount": 0, "not_settlement_amount": "3572.00",
                  "is_cancel": 0, "ident": 2, "created_at": "2023-03-06 17:11:17", "updated_at": "2023-03-21 15:38:17",
                  "deleted_at": 0, "bill_amount": "100.00", "type": "sales", "not_bill_amount": "3572.00"},
                 {"id": 8, "purchase_order_code": "CD-20230227-0001", "voucher_abstract": "",
                  "purchase_amount": "18372.00", "purchase_time": 1677427200, "customer_id": 156,
                  "customer_name": "上海鸣驭信息技术有限公司", "purchase_user_id": 50, "purchase_user_name": "闫巧玲",
                  "remark": "", "invoice_time": 0, "invoice_amount": "0.00", "not_invoice_amount": "18372.00",
                  "payment_time": 0, "payment_amount": "0.00", "not_payment_amount": "18372.00",
                  "invoice_not_payment_amount": "0.00", "refund_amount": "0.00", "purchase_type": 0, "ident": 2,
                  "settlement_amount": 0, "not_settlement_amount": "18272.00", "created_at": "2023-02-27 10:09:33",
                  "updated_at": "2023-03-21 15:38:17", "deleted_at": 0, "type": "purchase", "bill_amount": "100.00",
                  "not_bill_amount": "18272.00"}],
        "sums": {"salesAmount": "0", "purashAmount": "0", "charAmount": "0.00"}}

r = requests.post(url=url, headers=heads, json=data)
re=r.json()
print(re)
