# coding=gbk
# 公共库
import requests, random, pymysql, allure
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
# 定义批量开票id
plkp = {'id': None}
plkpid = kaipiao['id']
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


@allure.feature('应付汇总-接口')
@allure.story('批量开票')
def test_plkp():
    global tk, false, plkpid
    plkp_url = 'http://192.168.0.217:9901/PurchaseApInvoice'
    plkp_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    plkp_data = {"invoice_list": [{"invoice_total_amount": "23.00", "invoice_no": kphm, "invoice_company": "YG",
                                   "invoice_time": "2023-03-09T16:00:00.000Z", "invoice_type": 114,
                                   "invoice_type_name": "增值税专用发票", "invoice_info": [
            {"invoice_amount": 20, "invoice_tax_amount": 3, "invoice_tax_rate": "15.00"}], "invoiceTypeList": [
            {"id": 112, "parent_id": 107, "dict_label": "N类", "dict_value": "", "dict_type": "ap_invoice_type",
             "dict_sort": 0, "dict_level": 1, "dict_img": "", "status": "1", "remark": null, "disabled": false,
             "creator_id": 1, "created_at": "2023-01-03 14:57:40", "updated_at": "2023-01-03 14:57:40",
             "deleted_at": 0}, {"id": 113, "parent_id": 107, "dict_label": "增值税普通发票", "dict_value": "",
                                "dict_type": "ap_invoice_type", "dict_sort": 0, "dict_level": 1, "dict_img": "",
                                "status": "1", "remark": null, "disabled": false, "creator_id": 1,
                                "created_at": "2023-01-03 14:57:40", "updated_at": "2023-01-03 14:57:40",
                                "deleted_at": 0},
            {"id": 114, "parent_id": 107, "dict_label": "增值税专用发票", "dict_value": "",
             "dict_type": "ap_invoice_type", "dict_sort": 0, "dict_level": 1, "dict_img": "", "status": "1",
             "remark": null, "disabled": false, "creator_id": 1, "created_at": "2023-01-03 14:57:40",
             "updated_at": "2023-01-03 14:57:40", "deleted_at": 0},
            {"id": 115, "parent_id": 107, "dict_label": "全电普票", "dict_value": "", "dict_type": "ap_invoice_type",
             "dict_sort": 0, "dict_level": 1, "dict_img": "", "status": "1", "remark": null, "disabled": false,
             "creator_id": 1, "created_at": "2023-01-03 14:57:40", "updated_at": "2023-01-03 14:57:40",
             "deleted_at": 0},
            {"id": 116, "parent_id": 107, "dict_label": "全电专票", "dict_value": "", "dict_type": "ap_invoice_type",
             "dict_sort": 0, "dict_level": 1, "dict_img": "", "status": "1", "remark": null, "disabled": false,
             "creator_id": 1, "created_at": "2023-01-03 14:57:40", "updated_at": "2023-01-03 14:57:40",
             "deleted_at": 0}]}, {"invoice_total_amount": "34.00", "invoice_no": xgkphm,
                                  "invoice_time": "2023-03-08T16:00:00.000Z", "invoice_type": 119,
                                  "invoice_type_name": "增值税专用发票", "invoice_info": [
            {"invoice_amount": 30, "invoice_tax_amount": 4, "invoice_tax_rate": "13.33"}], "invoice_company": "YT",
                                  "invoiceTypeList": [
                                      {"id": 117, "parent_id": 108, "dict_label": "N类", "dict_value": "",
                                       "dict_type": "ap_invoice_type", "dict_sort": 0, "dict_level": 1, "dict_img": "",
                                       "status": "1", "remark": null, "disabled": false, "creator_id": 1,
                                       "created_at": "2023-01-03 14:57:40", "updated_at": "2023-01-03 14:57:40",
                                       "deleted_at": 0},
                                      {"id": 118, "parent_id": 108, "dict_label": "增值税普通发票", "dict_value": "",
                                       "dict_type": "ap_invoice_type", "dict_sort": 0, "dict_level": 1, "dict_img": "",
                                       "status": "1", "remark": null, "disabled": false, "creator_id": 1,
                                       "created_at": "2023-01-03 14:57:40", "updated_at": "2023-01-03 14:57:40",
                                       "deleted_at": 0},
                                      {"id": 119, "parent_id": 108, "dict_label": "增值税专用发票", "dict_value": "",
                                       "dict_type": "ap_invoice_type", "dict_sort": 0, "dict_level": 1, "dict_img": "",
                                       "status": "1", "remark": null, "disabled": false, "creator_id": 1,
                                       "created_at": "2023-01-03 14:57:40", "updated_at": "2023-01-03 14:57:40",
                                       "deleted_at": 0},
                                      {"id": 120, "parent_id": 108, "dict_label": "全电普票", "dict_value": "",
                                       "dict_type": "ap_invoice_type", "dict_sort": 0, "dict_level": 1, "dict_img": "",
                                       "status": "1", "remark": null, "disabled": false, "creator_id": 1,
                                       "created_at": "2023-01-03 14:57:40", "updated_at": "2023-01-03 14:57:40",
                                       "deleted_at": 0},
                                      {"id": 121, "parent_id": 108, "dict_label": "全电专票", "dict_value": "",
                                       "dict_type": "ap_invoice_type", "dict_sort": 0, "dict_level": 1, "dict_img": "",
                                       "status": "1", "remark": null, "disabled": false, "creator_id": 1,
                                       "created_at": "2023-01-03 14:57:40", "updated_at": "2023-01-03 14:57:40",
                                       "deleted_at": 0}]}], "remark": "测试批量开票", "order_list": [
        {"customer_name": "浪潮北京", "purchase_order_code": "3344", "invoice_amount": 25,
         "not_invoice_amount": "1232.00"},
        {"customer_name": "浪潮北京", "purchase_order_code": "3242342", "invoice_amount": 32,
         "not_invoice_amount": "123213.00"}]}
    r = requests.post(url=plkp_url, headers=plkp_head, json=plkp_data)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 更新开票ID
    plkp['id'] = r.json()['data']['id']
    plkpid = r.json()['data']['id']
    # 打印返回结果
    req = r.json()
    print(req)


@allure.feature('应付汇总-接口')
@allure.story('批量开票')
@allure.step('修改批量开票')
def test_xgplkp():
    global tk, false, plkpid
    xgplkp_url = f'http://192.168.0.217:9901/PurchaseApInvoice/{plkpid}'
    xgplkp_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    xgplkp_data = {"id": plkp['id'], "remark": "测试修改批量开票", "creator_id": 1, "operate_id": 1, "ident": 2,
                   "invoice_list": [
                       {"id": 2468, "invoice_id": plkp['id'], "invoice_total_amount": "46.00", "invoice_no": "66666666",
                        "invoice_time": "2023-03-10", "invoice_company": "YT", "invoice_type": 118,
                        "invoice_type_name": "增值税普通发票", "deleted_at": 0, "invoice_info": [
                           {"id": 2493, "invoice_item_id": 2468, "invoice_amount": 40, "invoice_tax_amount": 6,
                            "invoice_tax_rate": "15.00", "deleted_at": 0}], "invoice_company_name": "优果",
                        "invoiceTypeList": [{"id": 117, "parent_id": 108, "dict_label": "N类", "dict_value": "",
                                             "dict_type": "ap_invoice_type", "dict_sort": 0, "dict_level": 1,
                                             "dict_img": "", "status": "1", "remark": null, "disabled": false,
                                             "creator_id": 1, "created_at": "2023-01-03 14:57:40",
                                             "updated_at": "2023-01-03 14:57:40", "deleted_at": 0},
                                            {"id": 118, "parent_id": 108, "dict_label": "增值税普通发票",
                                             "dict_value": "", "dict_type": "ap_invoice_type", "dict_sort": 0,
                                             "dict_level": 1, "dict_img": "", "status": "1", "remark": null,
                                             "disabled": false, "creator_id": 1, "created_at": "2023-01-03 14:57:40",
                                             "updated_at": "2023-01-03 14:57:40", "deleted_at": 0},
                                            {"id": 119, "parent_id": 108, "dict_label": "增值税专用发票",
                                             "dict_value": "", "dict_type": "ap_invoice_type", "dict_sort": 0,
                                             "dict_level": 1, "dict_img": "", "status": "1", "remark": null,
                                             "disabled": false, "creator_id": 1, "created_at": "2023-01-03 14:57:40",
                                             "updated_at": "2023-01-03 14:57:40", "deleted_at": 0},
                                            {"id": 120, "parent_id": 108, "dict_label": "全电普票", "dict_value": "",
                                             "dict_type": "ap_invoice_type", "dict_sort": 0, "dict_level": 1,
                                             "dict_img": "", "status": "1", "remark": null, "disabled": false,
                                             "creator_id": 1, "created_at": "2023-01-03 14:57:40",
                                             "updated_at": "2023-01-03 14:57:40", "deleted_at": 0},
                                            {"id": 121, "parent_id": 108, "dict_label": "全电专票", "dict_value": "",
                                             "dict_type": "ap_invoice_type", "dict_sort": 0, "dict_level": 1,
                                             "dict_img": "", "status": "1", "remark": null, "disabled": false,
                                             "creator_id": 1, "created_at": "2023-01-03 14:57:40",
                                             "updated_at": "2023-01-03 14:57:40", "deleted_at": 0}]},
                       {"id": 2469, "invoice_id": plkp['id'], "invoice_total_amount": "68.00", "invoice_no": "55555555",
                        "invoice_time": "2023-03-09", "invoice_company": "YT", "invoice_type": 119,
                        "invoice_type_name": "增值税专用发票", "deleted_at": 0, "invoice_info": [
                           {"id": 2494, "invoice_item_id": 2469, "invoice_amount": 60, "invoice_tax_amount": 8,
                            "invoice_tax_rate": "13.33", "deleted_at": 0}], "invoice_company_name": "郢通",
                        "invoiceTypeList": [{"id": 117, "parent_id": 108, "dict_label": "N类", "dict_value": "",
                                             "dict_type": "ap_invoice_type", "dict_sort": 0, "dict_level": 1,
                                             "dict_img": "", "status": "1", "remark": null, "disabled": false,
                                             "creator_id": 1, "created_at": "2023-01-03 14:57:40",
                                             "updated_at": "2023-01-03 14:57:40", "deleted_at": 0},
                                            {"id": 118, "parent_id": 108, "dict_label": "增值税普通发票",
                                             "dict_value": "", "dict_type": "ap_invoice_type", "dict_sort": 0,
                                             "dict_level": 1, "dict_img": "", "status": "1", "remark": null,
                                             "disabled": false, "creator_id": 1, "created_at": "2023-01-03 14:57:40",
                                             "updated_at": "2023-01-03 14:57:40", "deleted_at": 0},
                                            {"id": 119, "parent_id": 108, "dict_label": "增值税专用发票",
                                             "dict_value": "", "dict_type": "ap_invoice_type", "dict_sort": 0,
                                             "dict_level": 1, "dict_img": "", "status": "1", "remark": null,
                                             "disabled": false, "creator_id": 1, "created_at": "2023-01-03 14:57:40",
                                             "updated_at": "2023-01-03 14:57:40", "deleted_at": 0},
                                            {"id": 120, "parent_id": 108, "dict_label": "全电普票", "dict_value": "",
                                             "dict_type": "ap_invoice_type", "dict_sort": 0, "dict_level": 1,
                                             "dict_img": "", "status": "1", "remark": null, "disabled": false,
                                             "creator_id": 1, "created_at": "2023-01-03 14:57:40",
                                             "updated_at": "2023-01-03 14:57:40", "deleted_at": 0},
                                            {"id": 121, "parent_id": 108, "dict_label": "全电专票", "dict_value": "",
                                             "dict_type": "ap_invoice_type", "dict_sort": 0, "dict_level": 1,
                                             "dict_img": "", "status": "1", "remark": null, "disabled": false,
                                             "creator_id": 1, "created_at": "2023-01-03 14:57:40",
                                             "updated_at": "2023-01-03 14:57:40", "deleted_at": 0}]}], "order_list": [
            {"id": 3970, "invoice_id": plkp['id'], "purchase_order_code": "3344", "invoice_amount": 50, "deleted_at": 0,
             "customer_name": "浪潮北京", "not_invoice_amount": "1207.00"},
            {"id": 3971, "invoice_id": plkp['id'], "purchase_order_code": "3242342", "invoice_amount": 64,
             "deleted_at": 0,
             "customer_name": "浪潮北京", "not_invoice_amount": "123181.00"}], "creator_name": "Admin",
                   "operate_name": "Admin"}
    r = requests.put(url=xgplkp_url, headers=xgplkp_head, json=xgplkp_data)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印返回结果
    req = r.json()
    print(req)


@allure.feature('应付汇总-接口')
@allure.story('批量开票')
@allure.step('删除批量开票')
def test_scplkp():
    scplkp_url = f'http://192.168.0.217:9901/PurchaseApInvoice/{plkpid}'
    scplkp_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    r = requests.delete(url=scplkp_url, headers=scplkp_head)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印返回结果
    req = r.json()
    print(req)


@allure.feature('应付汇总-接口')
@allure.story('批量开票')
@allure.step('查询批量开票操作记录')
def test_cxplkp():
    global plkpid
    # 连接数据库
    connect = pymysql.connect(host='192.168.0.226', user='root', password='CLd8T8TWt58ypaxd', db='hz_erp_test')
    if connect:
        print('连接成功')
    # 创建一个游标对象
    yf = connect.cursor()
    # 精确查询操作日志
    sql_rz = f"select invoice_id,`type` from hz_erp_test.hz_purchase_ap_invoice_log where invoice_id ={plkpid}"
    # 执行查询语句
    yf.execute(sql_rz)
    # 获取结果
    rz = yf.fetchall()
    # 打印返回结果
    print(rz)
    yf.close()


@allure.feature('应付汇总-接口')
@allure.story('开票')
@allure.step('申请开票')
def test_sqkp():
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


@allure.feature('应付汇总-接口')
@allure.story('开票')
@allure.step('修改开票')
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


@allure.feature('应付汇总-接口')
@allure.story('开票')
@allure.step('删除开票')
def test_scfp():
    scfp_url = f'http://192.168.0.217:9901/PurchaseApInvoice/{kpid}'
    scfp_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    r = requests.delete(url=scfp_url, headers=scfp_head)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印返回结果
    req = r.json()
    print(req)


@allure.feature('应付汇总-接口')
@allure.story('开票')
@allure.step('查询开票操作记录')
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


# 定义批量付款id
plfk = {'id': None}
plfkid = kaipiao['id']


@allure.feature('应付汇总-接口')
@allure.story('批量付款')
@allure.step('申请批量付款')
def test_plfk():
    global tk, false, plfkid
    plfk_url = 'http://192.168.0.217:9901/PurchaseApPayment'
    plfk_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    plfk_data = {"payment_list": [
        {"payment_total_amount": 23, "payment_time": "2023-03-09T16:00:00.000Z", "payment_mode": 58,
         "payment_mode_name": "优果上海银行"}], "remark": "测试批量付款", "order_list": [
        {"customer_name": "浪潮北京", "usable_pre_payment_amount": 0, "purchase_order_code": "3344",
         "payment_amount": 11, "pre_payment_amount": 0, "offset_amount": 0, "not_payment_amount": "1232.00"},
        {"customer_name": "浪潮北京", "usable_pre_payment_amount": 0, "purchase_order_code": "3242342",
         "payment_amount": 12, "pre_payment_amount": 0, "offset_amount": 0, "not_payment_amount": "123213.00"}]}
    r = requests.post(url=plfk_url, headers=plfk_head, json=plfk_data)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 更新开票ID
    plfk['id'] = r.json()['data']['id']
    plfkid = r.json()['data']['id']
    # 打印返回结果
    req = r.json()
    print(req)


@allure.feature('应付汇总-接口')
@allure.story('批量付款')
@allure.step('修改批量付款')
def test_xgplfk():
    global tk, false, plfkid
    xgplfk_url = f'http://192.168.0.217:9901/PurchaseApPayment/{plfkid}'
    xgplfk_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    xgplfk_data = {"id": plfk['id'], "remark": "测试修改批量付款", "creator_id": 1, "operate_id": 1, "ident": 2,
                   "payment_list": [{"id": 2044, "payment_id": plfk['id'], "payment_time": "2023-03-07T16:00:00.000Z",
                                     "payment_total_amount": 25, "payment_mode": 60,
                                     "payment_mode_name": "华胄建设银行", "deleted_at": 0}], "order_list": [
            {"id": 3734, "payment_id": plfk['id'], "purchase_order_code": "3344", "payment_amount": 12,
             "pre_payment_amount": 0, "offset_amount": "0.00", "deleted_at": 0, "customer_name": "浪潮北京",
             "not_payment_amount": "1232.00", "usable_pre_payment_amount": 0},
            {"id": 3735, "payment_id": plfk['id'], "purchase_order_code": "3242342", "payment_amount": 13,
             "pre_payment_amount": 0, "offset_amount": "0.00", "deleted_at": 0, "customer_name": "浪潮北京",
             "not_payment_amount": "123213.00", "usable_pre_payment_amount": 0}], "creator_name": "Admin",
                   "operate_name": "Admin"}
    r = requests.put(url=xgplfk_url, headers=xgplfk_head, json=xgplfk_data)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印返回结果
    req = r.json()
    print(req)


@allure.feature('应付汇总-接口')
@allure.story('批量付款')
@allure.step('删除批量付款')
def test_scplfk():
    scplfk_url = f'http://192.168.0.217:9901/PurchaseApPayment/{plfkid}'
    scplfk_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    r = requests.delete(url=scplfk_url, headers=scplfk_head)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印返回结果
    req = r.json()
    print(req)


@allure.feature('应付汇总-接口')
@allure.story('批量付款')
@allure.step('查询批量付款操作记录')
def test_cxplfk():
    global plfkid
    # 连接数据库
    connect = pymysql.connect(host='192.168.0.226', user='root', password='CLd8T8TWt58ypaxd', db='hz_erp_test')
    if connect:
        print('连接成功')
    # 创建一个游标对象
    yf = connect.cursor()
    # 精确查询操作日志
    sql_rz = f"select payment_id,`type` from hz_erp_test.hz_purchase_ap_payment_log where payment_id ={plfkid}"
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


@allure.feature('应付汇总-接口')
@allure.story('付款')
@allure.step('申请付款')
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


@allure.feature('应付汇总-接口')
@allure.story('付款')
@allure.step('修改付款')
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


@allure.feature('应付汇总-接口')
@allure.story('付款')
@allure.step('删除付款')
def test_scfk():
    scfp_url = f'http://192.168.0.217:9901/PurchaseApPayment/{fkid}'
    scfp_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    r = requests.delete(url=scfp_url, headers=scfp_head)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印返回结果
    req = r.json()
    print(req)


@allure.feature('应付汇总-接口')
@allure.story('付款')
@allure.step('查询付款操作记录')
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


# 折扣
# 定义折扣id
zhekou = {'id': None}
zkid = zhekou['id']


@allure.feature('应付汇总-接口')
@allure.story('折扣')
@allure.step('申请折扣')
def test_zk():
    global zkid
    # 折扣URL
    zk_url = 'http://192.168.0.217:9901/PurchaseApDiscount'
    # 折扣请求头
    zk_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {tk}"}
    # 折扣请求体
    zk_data = {"discount_amount": jine, "stop_amount": "", "remark": "测试折扣",
               "purchase_order_code": cgddh}
    # 折扣请求
    r = requests.post(url=zk_url, json=zk_data, headers=zk_header)
    # 获取折扣订单id更新到列表
    zhekou['id'] = r.json()['data']['id']
    zkid = r.json()['data']['id']
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印json返回数据
    print(r.json())
    # 设置收款成功断言
    assert r.json()['message'] == 'success'


@allure.feature('应付汇总-接口')
@allure.story('折扣')
@allure.step('修改折扣')
def test_xgzk():
    global zkid
    # 修改折扣URL
    xgzk_url = f'http://192.168.0.217:9901/PurchaseApDiscount/{zkid}'
    # 修改折扣请求头
    xgzk_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {tk}"}
    # 修改折扣请求体
    xgzk_data = {"id": zhekou['id'], "purchase_order_code": cgddh, "discount_amount": xgjine,
                 "remark": "测试修改折扣",
                 "creator_id": 1, "operate_id": 1, "ident": 2, "creator_name": "Admin", "operate_name": "Admin"}
    # 修改折扣请求
    r = requests.put(url=xgzk_url, json=xgzk_data, headers=xgzk_header)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印json返回数据
    print(r.json())


@allure.feature('应付汇总-接口')
@allure.story('折扣')
@allure.step('删除折扣')
def test_sczk():
    # 删除折扣URL
    sczk_url = f'http://192.168.0.217:9901/PurchaseApDiscount/{zkid}'
    # 删除折扣请求头
    sczk_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {tk}"}
    # 删除折扣请求
    r = requests.delete(url=sczk_url, headers=sczk_header)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印json返回数据
    print(r.json())


@allure.feature('应付汇总-接口')
@allure.story('折扣')
@allure.step('查询折扣操作记录')
def test_cxzk():
    global zkid
    # 连接数据库
    connect = pymysql.connect(host='192.168.0.226', user='root', password='CLd8T8TWt58ypaxd', db='hz_erp_test')
    if connect:
        print('连接成功')
    # 创建一个游标对象
    yf = connect.cursor()
    # 精确查询操作日志
    sql_rz = f"select discount_id,`type` from hz_erp_test.hz_purchase_ap_discount_log where discount_id ={zkid}"
    # 执行查询语句
    yf.execute(sql_rz)
    # 获取结果
    rz = yf.fetchall()
    # 打印返回结果
    print(rz)
    yf.close()


# 终止
# 定义终止id
zhongzhi = {'id': None}
zzid = zhongzhi['id']


@allure.feature('应付汇总-接口')
@allure.story('终止')
@allure.step('申请终止')
def test_zz():
    global zzid
    # 终止URL
    zz_url = 'http://192.168.0.217:9901/PurchaseApStop'
    # 终止请求头
    zz_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {tk}"}
    # 终止请求体
    zz_data = {"purchase_order_code": cgddh, "stop_amount": jine, "remark": "测试终止"}
    # 终止请求
    r = requests.post(url=zz_url, json=zz_data, headers=zz_header)
    # 获取终止订单id更新到列表
    zhongzhi['id'] = r.json()['data']['id']
    zzid = r.json()['data']['id']
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印json返回数据
    print(r.json())
    # 设置终止成功断言
    assert r.json()['message'] == 'success'


@allure.feature('应付汇总-接口')
@allure.story('终止')
@allure.step('修改终止')
def test_xgzz():
    global zzid
    # 修改终止URL
    xgzz_url = f'http://192.168.0.217:9901/PurchaseApStop/{zzid}'
    # 修改终止请求头
    xgzz_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {tk}"}
    # 修改终止请求体
    xgzz_data = {"id": zhongzhi['id'], "purchase_order_code": cgddh, "stop_amount": xgjine,
                 "remark": "测试修改终止",
                 "creator_id": 1, "operate_id": 1, "ident": 2, "creator_name": "Admin", "operate_name": "Admin"}
    # 修改终止请求
    r = requests.put(url=xgzz_url, json=xgzz_data, headers=xgzz_header)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印json返回数据
    print(r.json())


@allure.feature('应付汇总-接口')
@allure.story('终止')
@allure.step('删除终止')
def test_sczz():
    # 删除终止URL
    sczz_url = f'http://192.168.0.217:9901/PurchaseApStop/{zzid}'
    # 删除终止请求头
    sczz_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {tk}"}
    # 删除终止请求
    r = requests.delete(url=sczz_url, headers=sczz_header)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印json返回数据
    print(r.json())


@allure.feature('应付汇总-接口')
@allure.story('终止')
@allure.step('查询终止操作记录')
def test_cxzz():
    global zzid
    # 连接数据库
    connect = pymysql.connect(host='192.168.0.226', user='root', password='CLd8T8TWt58ypaxd', db='hz_erp_test')
    if connect:
        print('连接成功')
    # 创建一个游标对象
    yf = connect.cursor()
    # 精确查询操作日志
    sql_rz = f"select stop_id,`type` from hz_erp_test.hz_purchase_ap_stop_log where stop_id ={zzid}"
    # 执行查询语句
    yf.execute(sql_rz)
    # 获取结果
    rz = yf.fetchall()
    # 打印返回结果
    print(rz)
    yf.close()


# 未税
# 定义未税id
weishui = {'id': None}
wsid = weishui['id']


@allure.feature('应付汇总-接口')
@allure.story('未税')
@allure.step('申请未税')
def test_ws():
    global wsid
    # 未税URL
    ws_url = 'http://192.168.0.217:9901/PurchaseApNoTax'
    # 未税请求头
    ws_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {tk}"}
    # 未税请求体
    ws_data = {"purchase_order_code": cgddh, "no_tax_amount": jine, "remark": "测试未税"}
    # 未税请求
    r = requests.post(url=ws_url, json=ws_data, headers=ws_header)
    # 获取终止订单id更新到列表
    weishui['id'] = r.json()['data']['id']
    wsid = r.json()['data']['id']
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印json返回数据
    print(r.json())
    # 设置未税成功断言
    assert r.json()['message'] == 'success'


@allure.feature('应付汇总-接口')
@allure.story('未税')
@allure.step('修改未税')
def test_xgws():
    global wsid, weishui
    # 修改未税URL
    xgws_url = f'http://192.168.0.217:9901/PurchaseApNoTax/{wsid}'
    # 修改未税请求头
    xgws_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {tk}"}
    # 修改未税请求体
    xgws_data = {"id": weishui['id'], "purchase_order_code": cgddh, "no_tax_amount": xgjine,
                 "remark": "测试编辑未税",
                 "creator_id": 1, "operate_id": 1, "creator_name": "Admin", "operate_name": "Admin"}
    # 修改未税请求
    r = requests.put(url=xgws_url, json=xgws_data, headers=xgws_header)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印json返回数据
    print(r.json())


@allure.feature('应付汇总-接口')
@allure.story('未税')
@allure.step('删除未税')
def test_scws():
    # 删除终止URL
    scws_url = f'http://192.168.0.217:9901/PurchaseApNoTax/{wsid}'
    # 删除终止请求头
    scws_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {tk}"}
    # 删除终止请求
    r = requests.delete(url=scws_url, headers=scws_header)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印json返回数据
    print(r.json())


@allure.feature('应付汇总-接口')
@allure.story('未税')
@allure.step('查询未税操作记录')
def test_cxws():
    global wsid
    # 连接数据库
    connect = pymysql.connect(host='192.168.0.226', user='root', password='CLd8T8TWt58ypaxd', db='hz_erp_test')
    if connect:
        print('连接成功')
    # 创建一个游标对象
    yf = connect.cursor()
    # 精确查询操作日志
    sql_rz = f"select no_tax_id,`type` from hz_erp_test.hz_purchase_ap_no_tax_log where no_tax_id ={wsid}"
    # 执行查询语句
    yf.execute(sql_rz)
    # 获取结果
    rz = yf.fetchall()
    # 打印返回结果
    print(rz)
    yf.close()


# 预付款变更
# 定义随机增加减少预付款金额
yfk = random.randint(-199, 399)


@allure.feature('应付汇总-接口')
@allure.story('预付款')
@allure.step('预付款变更')
def test_yfk():
    # 预付款URL
    yfk_url = 'http://192.168.0.217:9901/PurchaseApCustomerPre'
    # 预付款请求头
    yfk_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {tk}"}
    # 预付款请求体
    yfk_data = {"total_pre_payment_amount": "", "customer_name": "浙江天健远见科技有限公司", "payment_mode": 65,
                "payment_mode_name": "华胄现金", "payment_time": "2023-02-28", "pre_payment_amount": yfk,
                "remark": "测试新增预付款"}
    # 预付款请求
    r = requests.post(url=yfk_url, json=yfk_data, headers=yfk_header)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印json返回数据
    print(r.json())
    # 设置预付款变更成功断言
    assert r.json()['message'] == 'success'
