# coding=gbk
# 公共库
import requests, random, pymysql
# business代码
from business import logger, denglu

# 定义登录token
tk = denglu.test_dlxt()
false = None
null = None

# 定义金额
jine = random.randint(99, 399)
# 定义修改金额
xgjine = random.randint(99, 399)

# 采购订单号
cgddh = 'CD-20210628-0003'

# 开票

# 定义开票id
kaipiao = {'id': None}
kpid = kaipiao['id']
# 定义8位随机开票号码
kphm = random.randint(99, 99999999)
# 定义8位随机开票号码
xgkphm = random.randint(99, 99999999)
# 定义开票未含税金额
hs = jine * 0.85
# 定义开票含税金额
whs = jine * 0.15
# 定义开票修改未含税金额
xghs = xgjine * 0.85
# 定义开票修改含税金额
xgwhs = xgjine * 0.15


def test_kp():
    global tk, false, kpid
    kp_url = 'http://192.168.0.217:9901/PurchaseApInvoice'
    kp_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    kp_data = {"invoice_list": [{"invoice_total_amount": jine, "invoice_no": kphm, "invoice_company": "HZ",
                                 "invoice_time": "2023-03-05T16:00:00.000Z", "invoice_type": 85,
                                 "invoice_type_name": "增值税普通发票", "invoice_info": [
            {"invoice_amount": hs, "invoice_tax_amount": whs, "invoice_tax_rate": "13.00"}], "invoiceTypeList": [
            {"id": 84, "parent_id": 106, "dict_label": "N类", "dict_value": "", "dict_type": "ap_invoice_type",
             "dict_sort": 0, "dict_level": 1, "dict_img": "", "status": "1", "remark": null, "disabled": false,
             "creator_id": 1, "created_at": "2022-12-28 10:52:01", "updated_at": "2022-12-28 10:52:01",
             "deleted_at": 0}, {"id": 85, "parent_id": 106, "dict_label": "增值税普通发票", "dict_value": "",
                                "dict_type": "ap_invoice_type", "dict_sort": 0, "dict_level": 1, "dict_img": "",
                                "status": "1", "remark": null, "disabled": false, "creator_id": 1,
                                "created_at": "2022-12-28 10:52:01", "updated_at": "2022-12-28 10:52:01",
                                "deleted_at": 0},
            {"id": 86, "parent_id": 106, "dict_label": "增值税专用发票", "dict_value": "",
             "dict_type": "ap_invoice_type", "dict_sort": 0, "dict_level": 1, "dict_img": "", "status": "1",
             "remark": null, "disabled": false, "creator_id": 1, "created_at": "2022-12-28 10:52:01",
             "updated_at": "2022-12-28 10:52:01", "deleted_at": 0},
            {"id": 110, "parent_id": 106, "dict_label": "全电普票", "dict_value": "", "dict_type": "ap_invoice_type",
             "dict_sort": 0, "dict_level": 1, "dict_img": "", "status": "1", "remark": null, "disabled": false,
             "creator_id": 1, "created_at": "2023-01-03 14:57:40", "updated_at": "2023-01-03 14:57:40",
             "deleted_at": 0},
            {"id": 111, "parent_id": 106, "dict_label": "全电专票", "dict_value": "", "dict_type": "ap_invoice_type",
             "dict_sort": 0, "dict_level": 1, "dict_img": "", "status": "1", "remark": null, "disabled": false,
             "creator_id": 1, "created_at": "2023-01-03 14:57:40", "updated_at": "2023-01-03 14:57:40",
             "deleted_at": 0}]}], "remark": "测试开票", "order_list": [
        {"customer_name": "浪潮电子信息产业股份有限公司", "purchase_order_code": cgddh,
         "invoice_amount": jine, "not_invoice_amount": "200600.00"}]}
    r = requests.post(url=kp_url, headers=kp_head, json=kp_data)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 更新开票ID
    kaipiao['id'] = r.json()['data']['id']
    kpid = r.json()['data']['id']
    # 打印返回结果
    req = r.json()
    print(req)


# 修改发票
def test_xgkp():
    global tk, false, kpid
    xgkp_url = f'http://192.168.0.217:9901/PurchaseApInvoice/{kpid}'
    xgkp_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    xgkp_data = {"id": kaipiao['id'], "remark": "测试修改开票", "creator_id": 1, "operate_id": 1, "ident": 2,
                 "invoice_list": [
                     {"id": kaipiao['id'], "invoice_id": kaipiao['id'], "invoice_total_amount": "226.00",
                      "invoice_no": xgkphm,
                      "invoice_time": "2023-03-06", "invoice_company": "HZ", "invoice_type": 85,
                      "invoice_type_name": "增值税普通发票", "deleted_at": 0, "invoice_info": [
                         {"id": 4, "invoice_item_id": 4, "invoice_amount": xgwhs, "invoice_tax_amount": xghs,
                          "invoice_tax_rate": "13.00", "deleted_at": 0}], "invoice_company_name": "华胄",
                      "invoiceTypeList": [
                          {"id": 84, "parent_id": 106, "dict_label": "N类", "dict_value": "",
                           "dict_type": "ap_invoice_type",
                           "dict_sort": 0, "dict_level": 1, "dict_img": "", "status": "1", "remark": null,
                           "disabled": false,
                           "creator_id": 1, "created_at": "2022-12-28 10:52:01", "updated_at": "2022-12-28 10:52:01",
                           "deleted_at": 0},
                          {"id": 85, "parent_id": 106, "dict_label": "增值税普通发票", "dict_value": "",
                           "dict_type": "ap_invoice_type", "dict_sort": 0, "dict_level": 1, "dict_img": "",
                           "status": "1", "remark": null, "disabled": false, "creator_id": 1,
                           "created_at": "2022-12-28 10:52:01", "updated_at": "2022-12-28 10:52:01",
                           "deleted_at": 0},
                          {"id": 86, "parent_id": 106, "dict_label": "增值税专用发票", "dict_value": "",
                           "dict_type": "ap_invoice_type", "dict_sort": 0, "dict_level": 1, "dict_img": "",
                           "status": "1",
                           "remark": null, "disabled": false, "creator_id": 1, "created_at": "2022-12-28 10:52:01",
                           "updated_at": "2022-12-28 10:52:01", "deleted_at": 0},
                          {"id": 110, "parent_id": 106, "dict_label": "全电普票", "dict_value": "",
                           "dict_type": "ap_invoice_type",
                           "dict_sort": 0, "dict_level": 1, "dict_img": "", "status": "1", "remark": null,
                           "disabled": false,
                           "creator_id": 1, "created_at": "2023-01-03 14:57:40", "updated_at": "2023-01-03 14:57:40",
                           "deleted_at": 0},
                          {"id": 111, "parent_id": 106, "dict_label": "全电专票", "dict_value": "",
                           "dict_type": "ap_invoice_type",
                           "dict_sort": 0, "dict_level": 1, "dict_img": "", "status": "1", "remark": null,
                           "disabled": false,
                           "creator_id": 1, "created_at": "2023-01-03 14:57:40", "updated_at": "2023-01-03 14:57:40",
                           "deleted_at": 0}]}], "order_list": [
            {"id": kaipiao['id'], "invoice_id": kaipiao['id'], "purchase_order_code": cgddh,
             "invoice_amount": xgjine, "deleted_at": 0,
             "customer_name": "浪潮电子信息产业股份有限公司", "not_invoice_amount": "200487.00"}],
                 "creator_name": "Admin",
                 "operate_name": "Admin"}
    r = requests.put(url=xgkp_url, headers=xgkp_head, json=xgkp_data)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印返回结果
    req = r.json()
    print(req)


# 删除发票
def test_scfp():
    scfp_url = f'http://192.168.0.217:9901/PurchaseApInvoice/{kpid}'
    scfp_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    r = requests.delete(url=scfp_url, headers=scfp_head)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印返回结果
    req = r.json()
    print(req)


# 查询发票操作记录
def test_cxfp():
    global kpid
    # 连接数据库
    connect = pymysql.connect(host='192.168.0.226', user='root', password='CLd8T8TWt58ypaxd', db='hz_erp_test')
    if connect:
        print('连接成功')
    # 创建一个游标对象
    yf = connect.cursor()
    # 精确查询操作日志
    sql_rz = f"select invoice_id,`type` from hz_erp_test.hz_purchase_ap_invoice_log where invoice_id ={kpid}"
    # 执行查询语句
    yf.execute(sql_rz)
    # 获取结果
    rz = yf.fetchall()
    # 打印返回结果
    print(rz)
    yf.close()


# 付款
# 定义付款id
fukuan = {'id': None}
fkid = fukuan['id']


def test_fk():
    global tk, fkid
    fk_url = 'http://192.168.0.217:9901/PurchaseApPayment'
    fk_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    fk_data = {"payment_list": [
        {"payment_total_amount": jine, "payment_time": "2023-03-05T16:00:00.000Z", "payment_mode": 58,
         "payment_mode_name": "优果上海银行"}], "remark": "测试付款", "order_list": [
        {"customer_name": "浪潮电子信息产业股份有限公司", "not_payment_amount": "200600.00", "offset_amount": 0,
         "pre_payment_amount": 0, "usable_pre_payment_amount": 0, "purchase_order_code": cgddh,
         "payment_amount": jine}]}
    r = requests.post(url=fk_url, headers=fk_head, json=fk_data)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 更新付款ID
    fukuan['id'] = r.json()['data']['id']
    fkid = r.json()['data']['id']
    req = r.json()
    # 打印返回结果
    print(req)


# 修改付款
def test_xgfk():
    global tk, false, fkid
    xgfk_url = f'http://192.168.0.217:9901/PurchaseApPayment/{fkid}'
    xgfk_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    xgfk_data = {"id": fukuan['id'], "remark": "", "creator_id": 1, "operate_id": 1, "ident": 2, "payment_list": [
        {"id": fukuan['id'], "payment_id": 5, "payment_time": "2023-03-06", "payment_total_amount": xgjine,
         "payment_mode": 62,
         "payment_mode_name": "华胄微众银行", "deleted_at": 0}], "order_list": [
        {"id": fukuan['id'], "payment_id": 5, "purchase_order_code": cgddh, "payment_amount": xgjine,
         "pre_payment_amount": 0, "offset_amount": "0.00", "deleted_at": 0,
         "customer_name": "浪潮电子信息产业股份有限公司", "not_payment_amount": "200600.00",
         "usable_pre_payment_amount": 0}], "creator_name": "Admin", "operate_name": "Admin"}
    r = requests.put(url=xgfk_url, headers=xgfk_head, json=xgfk_data)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印返回结果
    req = r.json()
    print(req)


# 删除付款
def test_scfk():
    scfp_url = f'http://192.168.0.217:9901/PurchaseApPayment/{fkid}'
    scfp_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    r = requests.delete(url=scfp_url, headers=scfp_head)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印返回结果
    req = r.json()
    print(req)


# 查询付款操作记录
def test_cxfk():
    global fkid
    # 连接数据库
    connect = pymysql.connect(host='192.168.0.226', user='root', password='CLd8T8TWt58ypaxd', db='hz_erp_test')
    if connect:
        print('连接成功')
    # 创建一个游标对象
    yf = connect.cursor()
    # 精确查询操作日志
    sql_rz = f"select payment_id,`type` from hz_erp_test.hz_purchase_ap_payment_log where payment_id ={fkid}"
    # 执行查询语句
    yf.execute(sql_rz)
    # 获取结果
    rz = yf.fetchall()
    # 打印返回结果
    print(rz)
    yf.close()
