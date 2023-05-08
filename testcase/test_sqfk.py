import requests, random, datetime
from business import denglu

tk = denglu.test_dlxt()

# 设置采购订单号变量
cgddh = '34357424'
# 随机付款方式
fkfs_list = [1, 2, 3]
fk_fs = random.choice(fkfs_list)

# 随机付款金额
fk_jine = random.randint(1, 99)
# 随机修改金额
fk_xgjine = random.randint(1, 88)

# 获取当前日期
time = datetime.date.today()
# 当前日期加一周
fk_sj = time + datetime.timedelta(days=7)
# 修改日期
fk_xgsj = time + datetime.timedelta(days=9)

# 查询订单金额
ddjine = []


def test_wfjine():
    global ddjine
    cx_url = f'http://192.168.0.21:9090/PurchaseOrder/ChooseList?page=1&limit=10&warehousing_type=&warehousing_status=&supply_unit=&purchase_order_code[]={cgddh}&voucher_abstract='
    cx_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    r = requests.get(url=cx_url, headers=cx_head, )
    ddjine = r.json()['data'][0]['purchase_total_amount']
    print(ddjine)


# 采购申请付款单
def test_sqfk():
    sqfk_url = 'http://192.168.0.21:9090/ApplyPayOrder'
    sqfk_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    sqfk_data = {"type": "batch",
                 "list": [{"item": [{"purchase_order_code": cgddh, "this_amount": fk_jine}], "total_amount": ddjine,
                           "apply_amount": fk_jine, "plan_time": f"{fk_sj}", "pay_type": fk_fs,
                           "collect_customer": "测试换货结算客户", "collect_bank": "招商银行",
                           "collect_bank_no": "574587342837432", "remark": "测试采购申请付款"}]}

    r = requests.post(url=sqfk_url, headers=sqfk_head, json=sqfk_data)
    print(r.json())


# 查询最新申请付款单ID
ID = []


def test_cxdsh():
    global ID
    cx_url = 'http://192.168.0.21:9090/ApplyPayOrder?page=1&limit=10&collect_customer=&apply_no=&status=0&is_pay=&invoice_status=&warehousing_status=&down_time_type=&purchase_order_code=&voucher_abstract='
    cx_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    r = requests.get(url=cx_url, headers=cx_head, )
    ID = r.json()['data'][0]['id']
    print(ID)


# 修改付款申请
def test_xgfk():
    xgfk_url = f'http://192.168.0.21:9090/ApplyPayOrder/{ID}'
    xgfk_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    xgfk_data = {"item": [{"purchase_order_code": cgddh, "this_amount": fk_xgjine}], "total_amount": ddjine,
                 "apply_amount": fk_xgjine, "plan_time": f"{fk_xgsj}", "collect_customer": "测试换货结算客户",
                 "collect_bank": "招商银行", "collect_bank_no": "574587342837432", "pay_type": fk_fs}

    r = requests.put(url=xgfk_url, headers=xgfk_head, json=xgfk_data)
    print(r.json())
    print(fk_xgjine)

# 取消申请付款单
def test_qxfk():
    qxfk_url = f'http://192.168.0.21:9090/ApplyPayOrderCancel/{ID}'
    qxfk_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}

    r = requests.post(url=qxfk_url, headers=qxfk_head)
    print(r.json())
