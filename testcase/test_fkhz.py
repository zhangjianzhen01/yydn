import requests, random, datetime
from business import denglu

tk = denglu.test_dlxt()

# 设置付款时间
fksj = datetime.date.today()
# 查询申请中付款单ID
ID = []


def test_cxsqz():
    global ID
    cx_url = 'http://192.168.0.21:9090/ApplyPayOrder?status=0&sortField=&sortOrder=&page=1&limit=10&apply_no=&pay_company_name=&down_amount_value[]=&down_amount_value[]=&down_time_type=&down_keywords_value='
    cx_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    r = requests.get(url=cx_url, headers=cx_head, )
    ID = r.json()['data'][0]['id']
    print(ID)


# 财务同意付款
def test_tyfk():
    tyfk_url = f'http://192.168.0.21:9090/ApplyPayOrderConfirm/{ID}'
    tyfk_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    r = requests.post(url=tyfk_url, headers=tyfk_head)
    print(r.json())


# 财务驳回申请
# def test_bhfk():
#     bhfk_url = f'http://192.168.0.21:9090/ApplyPayOrderReject/{ID}'
#     bhfk_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
#     bhfk_data = {"reject": "测试驳回"}
#
#     r = requests.post(url=bhfk_url, headers=bhfk_head, json=bhfk_data)
#     print(r.json())


# 查询付款方式及付款金额
fkfs = []
fkjine = []


def test_cxxq():
    global fkfs, fkjine
    cxxq_url = f'http://192.168.0.21:9090/ApplyPayOrder/{ID}'
    cxxq_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    r = requests.get(url=cxxq_url, headers=cxxq_head)
    fkfs = r.json()['data']['pay_type']
    fkjine = r.json()['data']['apply_amount']
    print(fkjine, fkfs,fksj)


# 财务付款
def test_fk():
    global fkfs, fkjine
    # 票据
    if fkfs == 3:
        url = f'http://192.168.0.21:9090/ApplyPayOrderDo/{ID}'
        head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
        data = {"before_amount": 0, "discount_amount": "", "is_discount": "0", "pay_type": "3", "bill_type": "1",
                "pay_company_name": "上海华胄网络科技有限公司", "pay_bank_name": "上海银行曹安支行",
                "pay_bank_no": "00070671090", "bill": [
                {"start_day": "", "end_day": "", "bill_day": f"{fksj}", "bill_no": "2233232", "bill_amount": fkjine,
                 "bill_url": "http://hzdefault-1304855126.cos.ap-nanjing.myqcloud.com/financial/1683368200000.png"}]}
        r = requests.post(url=url, headers=head, json=data)
        print(r.json())

    # 转账
    elif fkfs == 1:
        url = f'http://192.168.0.21:9090/ApplyPayOrderDo/{ID}'
        head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
        data = {"before_amount": 0, "discount_amount": 0, "is_discount": "0", "pay_amount": fkjine, "pay_type": "1",
                "pay_company_name": "上海华胄网络科技有限公司", "pay_bank_name": "上海银行曹安支行",
                "pay_bank_no": "00070671090", "pay_day": f"{fksj}", "VoucherUrl": [{"name": "png格式.png",
                                                                                       "url": "http://hzdefault-1304855126.cos.ap-nanjing.myqcloud.com/financial/1683509134000.png"}]}
        r = requests.post(url=url, headers=head, json=data)
        print(r.json())

    # 现金
    elif fkfs == 2:
        url = f'http://192.168.0.21:9090/ApplyPayOrderDo/{ID}'
        head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
        data = {"before_amount": 0, "discount_amount": 0, "is_discount": "0", "pay_amount": fkjine, "pay_type": "2",
                "pay_day": f"{fksj}"}
        r = requests.post(url=url, headers=head, json=data)
        print(r.json())

    else:
        print('出错啦')
