# coding=gbk
# ������
import requests, random, pymysql, allure
# business����
from business import logger, denglu

# �����¼token
tk = denglu.test_dlxt()
false = None
null = None

# ������
jine = random.randint(99, 399)
# �����޸Ľ��
xgjine = random.randint(99, 399)

# �ɹ�������
cgddh = 'CD-20210628-0003'

# ��Ʊ

# ���忪Ʊid
kaipiao = {'id': None}
kpid = kaipiao['id']
# ����������Ʊid
plkp = {'id': None}
plkpid = kaipiao['id']
# ����8λ�����Ʊ����
kphm = random.randint(99, 99999999)
# ����8λ�����Ʊ����
xgkphm = random.randint(99, 99999999)
# ���忪Ʊδ��˰���
hs = jine * 0.85
# ���忪Ʊ��˰���
whs = jine * 0.15
# ���忪Ʊ�޸�δ��˰���
xghs = xgjine * 0.85
# ���忪Ʊ�޸ĺ�˰���
xgwhs = xgjine * 0.15


@allure.feature('Ӧ������-�ӿ�')
@allure.story('������Ʊ')
def test_plkp():
    global tk, false, plkpid
    plkp_url = 'http://192.168.0.217:9901/PurchaseApInvoice'
    plkp_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    plkp_data = {"invoice_list": [{"invoice_total_amount": "23.00", "invoice_no": kphm, "invoice_company": "YG",
                                   "invoice_time": "2023-03-09T16:00:00.000Z", "invoice_type": 114,
                                   "invoice_type_name": "��ֵ˰ר�÷�Ʊ", "invoice_info": [
            {"invoice_amount": 20, "invoice_tax_amount": 3, "invoice_tax_rate": "15.00"}], "invoiceTypeList": [
            {"id": 112, "parent_id": 107, "dict_label": "N��", "dict_value": "", "dict_type": "ap_invoice_type",
             "dict_sort": 0, "dict_level": 1, "dict_img": "", "status": "1", "remark": null, "disabled": false,
             "creator_id": 1, "created_at": "2023-01-03 14:57:40", "updated_at": "2023-01-03 14:57:40",
             "deleted_at": 0}, {"id": 113, "parent_id": 107, "dict_label": "��ֵ˰��ͨ��Ʊ", "dict_value": "",
                                "dict_type": "ap_invoice_type", "dict_sort": 0, "dict_level": 1, "dict_img": "",
                                "status": "1", "remark": null, "disabled": false, "creator_id": 1,
                                "created_at": "2023-01-03 14:57:40", "updated_at": "2023-01-03 14:57:40",
                                "deleted_at": 0},
            {"id": 114, "parent_id": 107, "dict_label": "��ֵ˰ר�÷�Ʊ", "dict_value": "",
             "dict_type": "ap_invoice_type", "dict_sort": 0, "dict_level": 1, "dict_img": "", "status": "1",
             "remark": null, "disabled": false, "creator_id": 1, "created_at": "2023-01-03 14:57:40",
             "updated_at": "2023-01-03 14:57:40", "deleted_at": 0},
            {"id": 115, "parent_id": 107, "dict_label": "ȫ����Ʊ", "dict_value": "", "dict_type": "ap_invoice_type",
             "dict_sort": 0, "dict_level": 1, "dict_img": "", "status": "1", "remark": null, "disabled": false,
             "creator_id": 1, "created_at": "2023-01-03 14:57:40", "updated_at": "2023-01-03 14:57:40",
             "deleted_at": 0},
            {"id": 116, "parent_id": 107, "dict_label": "ȫ��רƱ", "dict_value": "", "dict_type": "ap_invoice_type",
             "dict_sort": 0, "dict_level": 1, "dict_img": "", "status": "1", "remark": null, "disabled": false,
             "creator_id": 1, "created_at": "2023-01-03 14:57:40", "updated_at": "2023-01-03 14:57:40",
             "deleted_at": 0}]}, {"invoice_total_amount": "34.00", "invoice_no": xgkphm,
                                  "invoice_time": "2023-03-08T16:00:00.000Z", "invoice_type": 119,
                                  "invoice_type_name": "��ֵ˰ר�÷�Ʊ", "invoice_info": [
            {"invoice_amount": 30, "invoice_tax_amount": 4, "invoice_tax_rate": "13.33"}], "invoice_company": "YT",
                                  "invoiceTypeList": [
                                      {"id": 117, "parent_id": 108, "dict_label": "N��", "dict_value": "",
                                       "dict_type": "ap_invoice_type", "dict_sort": 0, "dict_level": 1, "dict_img": "",
                                       "status": "1", "remark": null, "disabled": false, "creator_id": 1,
                                       "created_at": "2023-01-03 14:57:40", "updated_at": "2023-01-03 14:57:40",
                                       "deleted_at": 0},
                                      {"id": 118, "parent_id": 108, "dict_label": "��ֵ˰��ͨ��Ʊ", "dict_value": "",
                                       "dict_type": "ap_invoice_type", "dict_sort": 0, "dict_level": 1, "dict_img": "",
                                       "status": "1", "remark": null, "disabled": false, "creator_id": 1,
                                       "created_at": "2023-01-03 14:57:40", "updated_at": "2023-01-03 14:57:40",
                                       "deleted_at": 0},
                                      {"id": 119, "parent_id": 108, "dict_label": "��ֵ˰ר�÷�Ʊ", "dict_value": "",
                                       "dict_type": "ap_invoice_type", "dict_sort": 0, "dict_level": 1, "dict_img": "",
                                       "status": "1", "remark": null, "disabled": false, "creator_id": 1,
                                       "created_at": "2023-01-03 14:57:40", "updated_at": "2023-01-03 14:57:40",
                                       "deleted_at": 0},
                                      {"id": 120, "parent_id": 108, "dict_label": "ȫ����Ʊ", "dict_value": "",
                                       "dict_type": "ap_invoice_type", "dict_sort": 0, "dict_level": 1, "dict_img": "",
                                       "status": "1", "remark": null, "disabled": false, "creator_id": 1,
                                       "created_at": "2023-01-03 14:57:40", "updated_at": "2023-01-03 14:57:40",
                                       "deleted_at": 0},
                                      {"id": 121, "parent_id": 108, "dict_label": "ȫ��רƱ", "dict_value": "",
                                       "dict_type": "ap_invoice_type", "dict_sort": 0, "dict_level": 1, "dict_img": "",
                                       "status": "1", "remark": null, "disabled": false, "creator_id": 1,
                                       "created_at": "2023-01-03 14:57:40", "updated_at": "2023-01-03 14:57:40",
                                       "deleted_at": 0}]}], "remark": "����������Ʊ", "order_list": [
        {"customer_name": "�˳�����", "purchase_order_code": "3344", "invoice_amount": 25,
         "not_invoice_amount": "1232.00"},
        {"customer_name": "�˳�����", "purchase_order_code": "3242342", "invoice_amount": 32,
         "not_invoice_amount": "123213.00"}]}
    r = requests.post(url=plkp_url, headers=plkp_head, json=plkp_data)
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ���¿�ƱID
    plkp['id'] = r.json()['data']['id']
    plkpid = r.json()['data']['id']
    # ��ӡ���ؽ��
    req = r.json()
    print(req)


@allure.feature('Ӧ������-�ӿ�')
@allure.story('������Ʊ')
@allure.step('�޸�������Ʊ')
def test_xgplkp():
    global tk, false, plkpid
    xgplkp_url = f'http://192.168.0.217:9901/PurchaseApInvoice/{plkpid}'
    xgplkp_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    xgplkp_data = {"id": plkp['id'], "remark": "�����޸�������Ʊ", "creator_id": 1, "operate_id": 1, "ident": 2,
                   "invoice_list": [
                       {"id": 2468, "invoice_id": plkp['id'], "invoice_total_amount": "46.00", "invoice_no": "66666666",
                        "invoice_time": "2023-03-10", "invoice_company": "YT", "invoice_type": 118,
                        "invoice_type_name": "��ֵ˰��ͨ��Ʊ", "deleted_at": 0, "invoice_info": [
                           {"id": 2493, "invoice_item_id": 2468, "invoice_amount": 40, "invoice_tax_amount": 6,
                            "invoice_tax_rate": "15.00", "deleted_at": 0}], "invoice_company_name": "�Ź�",
                        "invoiceTypeList": [{"id": 117, "parent_id": 108, "dict_label": "N��", "dict_value": "",
                                             "dict_type": "ap_invoice_type", "dict_sort": 0, "dict_level": 1,
                                             "dict_img": "", "status": "1", "remark": null, "disabled": false,
                                             "creator_id": 1, "created_at": "2023-01-03 14:57:40",
                                             "updated_at": "2023-01-03 14:57:40", "deleted_at": 0},
                                            {"id": 118, "parent_id": 108, "dict_label": "��ֵ˰��ͨ��Ʊ",
                                             "dict_value": "", "dict_type": "ap_invoice_type", "dict_sort": 0,
                                             "dict_level": 1, "dict_img": "", "status": "1", "remark": null,
                                             "disabled": false, "creator_id": 1, "created_at": "2023-01-03 14:57:40",
                                             "updated_at": "2023-01-03 14:57:40", "deleted_at": 0},
                                            {"id": 119, "parent_id": 108, "dict_label": "��ֵ˰ר�÷�Ʊ",
                                             "dict_value": "", "dict_type": "ap_invoice_type", "dict_sort": 0,
                                             "dict_level": 1, "dict_img": "", "status": "1", "remark": null,
                                             "disabled": false, "creator_id": 1, "created_at": "2023-01-03 14:57:40",
                                             "updated_at": "2023-01-03 14:57:40", "deleted_at": 0},
                                            {"id": 120, "parent_id": 108, "dict_label": "ȫ����Ʊ", "dict_value": "",
                                             "dict_type": "ap_invoice_type", "dict_sort": 0, "dict_level": 1,
                                             "dict_img": "", "status": "1", "remark": null, "disabled": false,
                                             "creator_id": 1, "created_at": "2023-01-03 14:57:40",
                                             "updated_at": "2023-01-03 14:57:40", "deleted_at": 0},
                                            {"id": 121, "parent_id": 108, "dict_label": "ȫ��רƱ", "dict_value": "",
                                             "dict_type": "ap_invoice_type", "dict_sort": 0, "dict_level": 1,
                                             "dict_img": "", "status": "1", "remark": null, "disabled": false,
                                             "creator_id": 1, "created_at": "2023-01-03 14:57:40",
                                             "updated_at": "2023-01-03 14:57:40", "deleted_at": 0}]},
                       {"id": 2469, "invoice_id": plkp['id'], "invoice_total_amount": "68.00", "invoice_no": "55555555",
                        "invoice_time": "2023-03-09", "invoice_company": "YT", "invoice_type": 119,
                        "invoice_type_name": "��ֵ˰ר�÷�Ʊ", "deleted_at": 0, "invoice_info": [
                           {"id": 2494, "invoice_item_id": 2469, "invoice_amount": 60, "invoice_tax_amount": 8,
                            "invoice_tax_rate": "13.33", "deleted_at": 0}], "invoice_company_name": "۫ͨ",
                        "invoiceTypeList": [{"id": 117, "parent_id": 108, "dict_label": "N��", "dict_value": "",
                                             "dict_type": "ap_invoice_type", "dict_sort": 0, "dict_level": 1,
                                             "dict_img": "", "status": "1", "remark": null, "disabled": false,
                                             "creator_id": 1, "created_at": "2023-01-03 14:57:40",
                                             "updated_at": "2023-01-03 14:57:40", "deleted_at": 0},
                                            {"id": 118, "parent_id": 108, "dict_label": "��ֵ˰��ͨ��Ʊ",
                                             "dict_value": "", "dict_type": "ap_invoice_type", "dict_sort": 0,
                                             "dict_level": 1, "dict_img": "", "status": "1", "remark": null,
                                             "disabled": false, "creator_id": 1, "created_at": "2023-01-03 14:57:40",
                                             "updated_at": "2023-01-03 14:57:40", "deleted_at": 0},
                                            {"id": 119, "parent_id": 108, "dict_label": "��ֵ˰ר�÷�Ʊ",
                                             "dict_value": "", "dict_type": "ap_invoice_type", "dict_sort": 0,
                                             "dict_level": 1, "dict_img": "", "status": "1", "remark": null,
                                             "disabled": false, "creator_id": 1, "created_at": "2023-01-03 14:57:40",
                                             "updated_at": "2023-01-03 14:57:40", "deleted_at": 0},
                                            {"id": 120, "parent_id": 108, "dict_label": "ȫ����Ʊ", "dict_value": "",
                                             "dict_type": "ap_invoice_type", "dict_sort": 0, "dict_level": 1,
                                             "dict_img": "", "status": "1", "remark": null, "disabled": false,
                                             "creator_id": 1, "created_at": "2023-01-03 14:57:40",
                                             "updated_at": "2023-01-03 14:57:40", "deleted_at": 0},
                                            {"id": 121, "parent_id": 108, "dict_label": "ȫ��רƱ", "dict_value": "",
                                             "dict_type": "ap_invoice_type", "dict_sort": 0, "dict_level": 1,
                                             "dict_img": "", "status": "1", "remark": null, "disabled": false,
                                             "creator_id": 1, "created_at": "2023-01-03 14:57:40",
                                             "updated_at": "2023-01-03 14:57:40", "deleted_at": 0}]}], "order_list": [
            {"id": 3970, "invoice_id": plkp['id'], "purchase_order_code": "3344", "invoice_amount": 50, "deleted_at": 0,
             "customer_name": "�˳�����", "not_invoice_amount": "1207.00"},
            {"id": 3971, "invoice_id": plkp['id'], "purchase_order_code": "3242342", "invoice_amount": 64,
             "deleted_at": 0,
             "customer_name": "�˳�����", "not_invoice_amount": "123181.00"}], "creator_name": "Admin",
                   "operate_name": "Admin"}
    r = requests.put(url=xgplkp_url, headers=xgplkp_head, json=xgplkp_data)
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡ���ؽ��
    req = r.json()
    print(req)


@allure.feature('Ӧ������-�ӿ�')
@allure.story('������Ʊ')
@allure.step('ɾ��������Ʊ')
def test_scplkp():
    scplkp_url = f'http://192.168.0.217:9901/PurchaseApInvoice/{plkpid}'
    scplkp_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    r = requests.delete(url=scplkp_url, headers=scplkp_head)
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡ���ؽ��
    req = r.json()
    print(req)


@allure.feature('Ӧ������-�ӿ�')
@allure.story('������Ʊ')
@allure.step('��ѯ������Ʊ������¼')
def test_cxplkp():
    global plkpid
    # �������ݿ�
    connect = pymysql.connect(host='192.168.0.226', user='root', password='CLd8T8TWt58ypaxd', db='hz_erp_test')
    if connect:
        print('���ӳɹ�')
    # ����һ���α����
    yf = connect.cursor()
    # ��ȷ��ѯ������־
    sql_rz = f"select invoice_id,`type` from hz_erp_test.hz_purchase_ap_invoice_log where invoice_id ={plkpid}"
    # ִ�в�ѯ���
    yf.execute(sql_rz)
    # ��ȡ���
    rz = yf.fetchall()
    # ��ӡ���ؽ��
    print(rz)
    yf.close()


@allure.feature('Ӧ������-�ӿ�')
@allure.story('��Ʊ')
@allure.step('���뿪Ʊ')
def test_sqkp():
    global tk, false, kpid
    kp_url = 'http://192.168.0.217:9901/PurchaseApInvoice'
    kp_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    kp_data = {"invoice_list": [{"invoice_total_amount": jine, "invoice_no": kphm, "invoice_company": "HZ",
                                 "invoice_time": "2023-03-05T16:00:00.000Z", "invoice_type": 85,
                                 "invoice_type_name": "��ֵ˰��ͨ��Ʊ", "invoice_info": [
            {"invoice_amount": hs, "invoice_tax_amount": whs, "invoice_tax_rate": "13.00"}], "invoiceTypeList": [
            {"id": 84, "parent_id": 106, "dict_label": "N��", "dict_value": "", "dict_type": "ap_invoice_type",
             "dict_sort": 0, "dict_level": 1, "dict_img": "", "status": "1", "remark": null, "disabled": false,
             "creator_id": 1, "created_at": "2022-12-28 10:52:01", "updated_at": "2022-12-28 10:52:01",
             "deleted_at": 0}, {"id": 85, "parent_id": 106, "dict_label": "��ֵ˰��ͨ��Ʊ", "dict_value": "",
                                "dict_type": "ap_invoice_type", "dict_sort": 0, "dict_level": 1, "dict_img": "",
                                "status": "1", "remark": null, "disabled": false, "creator_id": 1,
                                "created_at": "2022-12-28 10:52:01", "updated_at": "2022-12-28 10:52:01",
                                "deleted_at": 0},
            {"id": 86, "parent_id": 106, "dict_label": "��ֵ˰ר�÷�Ʊ", "dict_value": "",
             "dict_type": "ap_invoice_type", "dict_sort": 0, "dict_level": 1, "dict_img": "", "status": "1",
             "remark": null, "disabled": false, "creator_id": 1, "created_at": "2022-12-28 10:52:01",
             "updated_at": "2022-12-28 10:52:01", "deleted_at": 0},
            {"id": 110, "parent_id": 106, "dict_label": "ȫ����Ʊ", "dict_value": "", "dict_type": "ap_invoice_type",
             "dict_sort": 0, "dict_level": 1, "dict_img": "", "status": "1", "remark": null, "disabled": false,
             "creator_id": 1, "created_at": "2023-01-03 14:57:40", "updated_at": "2023-01-03 14:57:40",
             "deleted_at": 0},
            {"id": 111, "parent_id": 106, "dict_label": "ȫ��רƱ", "dict_value": "", "dict_type": "ap_invoice_type",
             "dict_sort": 0, "dict_level": 1, "dict_img": "", "status": "1", "remark": null, "disabled": false,
             "creator_id": 1, "created_at": "2023-01-03 14:57:40", "updated_at": "2023-01-03 14:57:40",
             "deleted_at": 0}]}], "remark": "���Կ�Ʊ", "order_list": [
        {"customer_name": "�˳�������Ϣ��ҵ�ɷ����޹�˾", "purchase_order_code": cgddh,
         "invoice_amount": jine, "not_invoice_amount": "200600.00"}]}
    r = requests.post(url=kp_url, headers=kp_head, json=kp_data)
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ���¿�ƱID
    kaipiao['id'] = r.json()['data']['id']
    kpid = r.json()['data']['id']
    # ��ӡ���ؽ��
    req = r.json()
    print(req)


@allure.feature('Ӧ������-�ӿ�')
@allure.story('��Ʊ')
@allure.step('�޸Ŀ�Ʊ')
def test_xgkp():
    global tk, false, kpid
    xgkp_url = f'http://192.168.0.217:9901/PurchaseApInvoice/{kpid}'
    xgkp_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    xgkp_data = {"id": kaipiao['id'], "remark": "�����޸Ŀ�Ʊ", "creator_id": 1, "operate_id": 1, "ident": 2,
                 "invoice_list": [
                     {"id": kaipiao['id'], "invoice_id": kaipiao['id'], "invoice_total_amount": "226.00",
                      "invoice_no": xgkphm,
                      "invoice_time": "2023-03-06", "invoice_company": "HZ", "invoice_type": 85,
                      "invoice_type_name": "��ֵ˰��ͨ��Ʊ", "deleted_at": 0, "invoice_info": [
                         {"id": 4, "invoice_item_id": 4, "invoice_amount": xgwhs, "invoice_tax_amount": xghs,
                          "invoice_tax_rate": "13.00", "deleted_at": 0}], "invoice_company_name": "����",
                      "invoiceTypeList": [
                          {"id": 84, "parent_id": 106, "dict_label": "N��", "dict_value": "",
                           "dict_type": "ap_invoice_type",
                           "dict_sort": 0, "dict_level": 1, "dict_img": "", "status": "1", "remark": null,
                           "disabled": false,
                           "creator_id": 1, "created_at": "2022-12-28 10:52:01", "updated_at": "2022-12-28 10:52:01",
                           "deleted_at": 0},
                          {"id": 85, "parent_id": 106, "dict_label": "��ֵ˰��ͨ��Ʊ", "dict_value": "",
                           "dict_type": "ap_invoice_type", "dict_sort": 0, "dict_level": 1, "dict_img": "",
                           "status": "1", "remark": null, "disabled": false, "creator_id": 1,
                           "created_at": "2022-12-28 10:52:01", "updated_at": "2022-12-28 10:52:01",
                           "deleted_at": 0},
                          {"id": 86, "parent_id": 106, "dict_label": "��ֵ˰ר�÷�Ʊ", "dict_value": "",
                           "dict_type": "ap_invoice_type", "dict_sort": 0, "dict_level": 1, "dict_img": "",
                           "status": "1",
                           "remark": null, "disabled": false, "creator_id": 1, "created_at": "2022-12-28 10:52:01",
                           "updated_at": "2022-12-28 10:52:01", "deleted_at": 0},
                          {"id": 110, "parent_id": 106, "dict_label": "ȫ����Ʊ", "dict_value": "",
                           "dict_type": "ap_invoice_type",
                           "dict_sort": 0, "dict_level": 1, "dict_img": "", "status": "1", "remark": null,
                           "disabled": false,
                           "creator_id": 1, "created_at": "2023-01-03 14:57:40", "updated_at": "2023-01-03 14:57:40",
                           "deleted_at": 0},
                          {"id": 111, "parent_id": 106, "dict_label": "ȫ��רƱ", "dict_value": "",
                           "dict_type": "ap_invoice_type",
                           "dict_sort": 0, "dict_level": 1, "dict_img": "", "status": "1", "remark": null,
                           "disabled": false,
                           "creator_id": 1, "created_at": "2023-01-03 14:57:40", "updated_at": "2023-01-03 14:57:40",
                           "deleted_at": 0}]}], "order_list": [
            {"id": kaipiao['id'], "invoice_id": kaipiao['id'], "purchase_order_code": cgddh,
             "invoice_amount": xgjine, "deleted_at": 0,
             "customer_name": "�˳�������Ϣ��ҵ�ɷ����޹�˾", "not_invoice_amount": "200487.00"}],
                 "creator_name": "Admin",
                 "operate_name": "Admin"}
    r = requests.put(url=xgkp_url, headers=xgkp_head, json=xgkp_data)
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡ���ؽ��
    req = r.json()
    print(req)


@allure.feature('Ӧ������-�ӿ�')
@allure.story('��Ʊ')
@allure.step('ɾ����Ʊ')
def test_scfp():
    scfp_url = f'http://192.168.0.217:9901/PurchaseApInvoice/{kpid}'
    scfp_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    r = requests.delete(url=scfp_url, headers=scfp_head)
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡ���ؽ��
    req = r.json()
    print(req)


@allure.feature('Ӧ������-�ӿ�')
@allure.story('��Ʊ')
@allure.step('��ѯ��Ʊ������¼')
def test_cxfp():
    global kpid
    # �������ݿ�
    connect = pymysql.connect(host='192.168.0.226', user='root', password='CLd8T8TWt58ypaxd', db='hz_erp_test')
    if connect:
        print('���ӳɹ�')
    # ����һ���α����
    yf = connect.cursor()
    # ��ȷ��ѯ������־
    sql_rz = f"select invoice_id,`type` from hz_erp_test.hz_purchase_ap_invoice_log where invoice_id ={kpid}"
    # ִ�в�ѯ���
    yf.execute(sql_rz)
    # ��ȡ���
    rz = yf.fetchall()
    # ��ӡ���ؽ��
    print(rz)
    yf.close()


# ������������id
plfk = {'id': None}
plfkid = kaipiao['id']


@allure.feature('Ӧ������-�ӿ�')
@allure.story('��������')
@allure.step('������������')
def test_plfk():
    global tk, false, plfkid
    plfk_url = 'http://192.168.0.217:9901/PurchaseApPayment'
    plfk_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    plfk_data = {"payment_list": [
        {"payment_total_amount": 23, "payment_time": "2023-03-09T16:00:00.000Z", "payment_mode": 58,
         "payment_mode_name": "�Ź��Ϻ�����"}], "remark": "������������", "order_list": [
        {"customer_name": "�˳�����", "usable_pre_payment_amount": 0, "purchase_order_code": "3344",
         "payment_amount": 11, "pre_payment_amount": 0, "offset_amount": 0, "not_payment_amount": "1232.00"},
        {"customer_name": "�˳�����", "usable_pre_payment_amount": 0, "purchase_order_code": "3242342",
         "payment_amount": 12, "pre_payment_amount": 0, "offset_amount": 0, "not_payment_amount": "123213.00"}]}
    r = requests.post(url=plfk_url, headers=plfk_head, json=plfk_data)
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ���¿�ƱID
    plfk['id'] = r.json()['data']['id']
    plfkid = r.json()['data']['id']
    # ��ӡ���ؽ��
    req = r.json()
    print(req)


@allure.feature('Ӧ������-�ӿ�')
@allure.story('��������')
@allure.step('�޸���������')
def test_xgplfk():
    global tk, false, plfkid
    xgplfk_url = f'http://192.168.0.217:9901/PurchaseApPayment/{plfkid}'
    xgplfk_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    xgplfk_data = {"id": plfk['id'], "remark": "�����޸���������", "creator_id": 1, "operate_id": 1, "ident": 2,
                   "payment_list": [{"id": 2044, "payment_id": plfk['id'], "payment_time": "2023-03-07T16:00:00.000Z",
                                     "payment_total_amount": 25, "payment_mode": 60,
                                     "payment_mode_name": "���н�������", "deleted_at": 0}], "order_list": [
            {"id": 3734, "payment_id": plfk['id'], "purchase_order_code": "3344", "payment_amount": 12,
             "pre_payment_amount": 0, "offset_amount": "0.00", "deleted_at": 0, "customer_name": "�˳�����",
             "not_payment_amount": "1232.00", "usable_pre_payment_amount": 0},
            {"id": 3735, "payment_id": plfk['id'], "purchase_order_code": "3242342", "payment_amount": 13,
             "pre_payment_amount": 0, "offset_amount": "0.00", "deleted_at": 0, "customer_name": "�˳�����",
             "not_payment_amount": "123213.00", "usable_pre_payment_amount": 0}], "creator_name": "Admin",
                   "operate_name": "Admin"}
    r = requests.put(url=xgplfk_url, headers=xgplfk_head, json=xgplfk_data)
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡ���ؽ��
    req = r.json()
    print(req)


@allure.feature('Ӧ������-�ӿ�')
@allure.story('��������')
@allure.step('ɾ����������')
def test_scplfk():
    scplfk_url = f'http://192.168.0.217:9901/PurchaseApPayment/{plfkid}'
    scplfk_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    r = requests.delete(url=scplfk_url, headers=scplfk_head)
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡ���ؽ��
    req = r.json()
    print(req)


@allure.feature('Ӧ������-�ӿ�')
@allure.story('��������')
@allure.step('��ѯ�������������¼')
def test_cxplfk():
    global plfkid
    # �������ݿ�
    connect = pymysql.connect(host='192.168.0.226', user='root', password='CLd8T8TWt58ypaxd', db='hz_erp_test')
    if connect:
        print('���ӳɹ�')
    # ����һ���α����
    yf = connect.cursor()
    # ��ȷ��ѯ������־
    sql_rz = f"select payment_id,`type` from hz_erp_test.hz_purchase_ap_payment_log where payment_id ={plfkid}"
    # ִ�в�ѯ���
    yf.execute(sql_rz)
    # ��ȡ���
    rz = yf.fetchall()
    # ��ӡ���ؽ��
    print(rz)
    yf.close()


# ����
# ���帶��id
fukuan = {'id': None}
fkid = fukuan['id']


@allure.feature('Ӧ������-�ӿ�')
@allure.story('����')
@allure.step('���븶��')
def test_fk():
    global tk, fkid
    fk_url = 'http://192.168.0.217:9901/PurchaseApPayment'
    fk_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    fk_data = {"payment_list": [
        {"payment_total_amount": jine, "payment_time": "2023-03-05T16:00:00.000Z", "payment_mode": 58,
         "payment_mode_name": "�Ź��Ϻ�����"}], "remark": "���Ը���", "order_list": [
        {"customer_name": "�˳�������Ϣ��ҵ�ɷ����޹�˾", "not_payment_amount": "200600.00", "offset_amount": 0,
         "pre_payment_amount": 0, "usable_pre_payment_amount": 0, "purchase_order_code": cgddh,
         "payment_amount": jine}]}
    r = requests.post(url=fk_url, headers=fk_head, json=fk_data)
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ���¸���ID
    fukuan['id'] = r.json()['data']['id']
    fkid = r.json()['data']['id']
    req = r.json()
    # ��ӡ���ؽ��
    print(req)


@allure.feature('Ӧ������-�ӿ�')
@allure.story('����')
@allure.step('�޸ĸ���')
def test_xgfk():
    global tk, false, fkid
    xgfk_url = f'http://192.168.0.217:9901/PurchaseApPayment/{fkid}'
    xgfk_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    xgfk_data = {"id": fukuan['id'], "remark": "", "creator_id": 1, "operate_id": 1, "ident": 2, "payment_list": [
        {"id": fukuan['id'], "payment_id": 5, "payment_time": "2023-03-06", "payment_total_amount": xgjine,
         "payment_mode": 62,
         "payment_mode_name": "����΢������", "deleted_at": 0}], "order_list": [
        {"id": fukuan['id'], "payment_id": 5, "purchase_order_code": cgddh, "payment_amount": xgjine,
         "pre_payment_amount": 0, "offset_amount": "0.00", "deleted_at": 0,
         "customer_name": "�˳�������Ϣ��ҵ�ɷ����޹�˾", "not_payment_amount": "200600.00",
         "usable_pre_payment_amount": 0}], "creator_name": "Admin", "operate_name": "Admin"}
    r = requests.put(url=xgfk_url, headers=xgfk_head, json=xgfk_data)
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡ���ؽ��
    req = r.json()
    print(req)


@allure.feature('Ӧ������-�ӿ�')
@allure.story('����')
@allure.step('ɾ������')
def test_scfk():
    scfp_url = f'http://192.168.0.217:9901/PurchaseApPayment/{fkid}'
    scfp_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    r = requests.delete(url=scfp_url, headers=scfp_head)
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡ���ؽ��
    req = r.json()
    print(req)


@allure.feature('Ӧ������-�ӿ�')
@allure.story('����')
@allure.step('��ѯ���������¼')
def test_cxfk():
    global fkid
    # �������ݿ�
    connect = pymysql.connect(host='192.168.0.226', user='root', password='CLd8T8TWt58ypaxd', db='hz_erp_test')
    if connect:
        print('���ӳɹ�')
    # ����һ���α����
    yf = connect.cursor()
    # ��ȷ��ѯ������־
    sql_rz = f"select payment_id,`type` from hz_erp_test.hz_purchase_ap_payment_log where payment_id ={fkid}"
    # ִ�в�ѯ���
    yf.execute(sql_rz)
    # ��ȡ���
    rz = yf.fetchall()
    # ��ӡ���ؽ��
    print(rz)
    yf.close()


# �ۿ�
# �����ۿ�id
zhekou = {'id': None}
zkid = zhekou['id']


@allure.feature('Ӧ������-�ӿ�')
@allure.story('�ۿ�')
@allure.step('�����ۿ�')
def test_zk():
    global zkid
    # �ۿ�URL
    zk_url = 'http://192.168.0.217:9901/PurchaseApDiscount'
    # �ۿ�����ͷ
    zk_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {tk}"}
    # �ۿ�������
    zk_data = {"discount_amount": jine, "stop_amount": "", "remark": "�����ۿ�",
               "purchase_order_code": cgddh}
    # �ۿ�����
    r = requests.post(url=zk_url, json=zk_data, headers=zk_header)
    # ��ȡ�ۿ۶���id���µ��б�
    zhekou['id'] = r.json()['data']['id']
    zkid = r.json()['data']['id']
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡjson��������
    print(r.json())
    # �����տ�ɹ�����
    assert r.json()['message'] == 'success'


@allure.feature('Ӧ������-�ӿ�')
@allure.story('�ۿ�')
@allure.step('�޸��ۿ�')
def test_xgzk():
    global zkid
    # �޸��ۿ�URL
    xgzk_url = f'http://192.168.0.217:9901/PurchaseApDiscount/{zkid}'
    # �޸��ۿ�����ͷ
    xgzk_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {tk}"}
    # �޸��ۿ�������
    xgzk_data = {"id": zhekou['id'], "purchase_order_code": cgddh, "discount_amount": xgjine,
                 "remark": "�����޸��ۿ�",
                 "creator_id": 1, "operate_id": 1, "ident": 2, "creator_name": "Admin", "operate_name": "Admin"}
    # �޸��ۿ�����
    r = requests.put(url=xgzk_url, json=xgzk_data, headers=xgzk_header)
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡjson��������
    print(r.json())


@allure.feature('Ӧ������-�ӿ�')
@allure.story('�ۿ�')
@allure.step('ɾ���ۿ�')
def test_sczk():
    # ɾ���ۿ�URL
    sczk_url = f'http://192.168.0.217:9901/PurchaseApDiscount/{zkid}'
    # ɾ���ۿ�����ͷ
    sczk_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {tk}"}
    # ɾ���ۿ�����
    r = requests.delete(url=sczk_url, headers=sczk_header)
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡjson��������
    print(r.json())


@allure.feature('Ӧ������-�ӿ�')
@allure.story('�ۿ�')
@allure.step('��ѯ�ۿ۲�����¼')
def test_cxzk():
    global zkid
    # �������ݿ�
    connect = pymysql.connect(host='192.168.0.226', user='root', password='CLd8T8TWt58ypaxd', db='hz_erp_test')
    if connect:
        print('���ӳɹ�')
    # ����һ���α����
    yf = connect.cursor()
    # ��ȷ��ѯ������־
    sql_rz = f"select discount_id,`type` from hz_erp_test.hz_purchase_ap_discount_log where discount_id ={zkid}"
    # ִ�в�ѯ���
    yf.execute(sql_rz)
    # ��ȡ���
    rz = yf.fetchall()
    # ��ӡ���ؽ��
    print(rz)
    yf.close()


# ��ֹ
# ������ֹid
zhongzhi = {'id': None}
zzid = zhongzhi['id']


@allure.feature('Ӧ������-�ӿ�')
@allure.story('��ֹ')
@allure.step('������ֹ')
def test_zz():
    global zzid
    # ��ֹURL
    zz_url = 'http://192.168.0.217:9901/PurchaseApStop'
    # ��ֹ����ͷ
    zz_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {tk}"}
    # ��ֹ������
    zz_data = {"purchase_order_code": cgddh, "stop_amount": jine, "remark": "������ֹ"}
    # ��ֹ����
    r = requests.post(url=zz_url, json=zz_data, headers=zz_header)
    # ��ȡ��ֹ����id���µ��б�
    zhongzhi['id'] = r.json()['data']['id']
    zzid = r.json()['data']['id']
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡjson��������
    print(r.json())
    # ������ֹ�ɹ�����
    assert r.json()['message'] == 'success'


@allure.feature('Ӧ������-�ӿ�')
@allure.story('��ֹ')
@allure.step('�޸���ֹ')
def test_xgzz():
    global zzid
    # �޸���ֹURL
    xgzz_url = f'http://192.168.0.217:9901/PurchaseApStop/{zzid}'
    # �޸���ֹ����ͷ
    xgzz_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {tk}"}
    # �޸���ֹ������
    xgzz_data = {"id": zhongzhi['id'], "purchase_order_code": cgddh, "stop_amount": xgjine,
                 "remark": "�����޸���ֹ",
                 "creator_id": 1, "operate_id": 1, "ident": 2, "creator_name": "Admin", "operate_name": "Admin"}
    # �޸���ֹ����
    r = requests.put(url=xgzz_url, json=xgzz_data, headers=xgzz_header)
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡjson��������
    print(r.json())


@allure.feature('Ӧ������-�ӿ�')
@allure.story('��ֹ')
@allure.step('ɾ����ֹ')
def test_sczz():
    # ɾ����ֹURL
    sczz_url = f'http://192.168.0.217:9901/PurchaseApStop/{zzid}'
    # ɾ����ֹ����ͷ
    sczz_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {tk}"}
    # ɾ����ֹ����
    r = requests.delete(url=sczz_url, headers=sczz_header)
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡjson��������
    print(r.json())


@allure.feature('Ӧ������-�ӿ�')
@allure.story('��ֹ')
@allure.step('��ѯ��ֹ������¼')
def test_cxzz():
    global zzid
    # �������ݿ�
    connect = pymysql.connect(host='192.168.0.226', user='root', password='CLd8T8TWt58ypaxd', db='hz_erp_test')
    if connect:
        print('���ӳɹ�')
    # ����һ���α����
    yf = connect.cursor()
    # ��ȷ��ѯ������־
    sql_rz = f"select stop_id,`type` from hz_erp_test.hz_purchase_ap_stop_log where stop_id ={zzid}"
    # ִ�в�ѯ���
    yf.execute(sql_rz)
    # ��ȡ���
    rz = yf.fetchall()
    # ��ӡ���ؽ��
    print(rz)
    yf.close()


# δ˰
# ����δ˰id
weishui = {'id': None}
wsid = weishui['id']


@allure.feature('Ӧ������-�ӿ�')
@allure.story('δ˰')
@allure.step('����δ˰')
def test_ws():
    global wsid
    # δ˰URL
    ws_url = 'http://192.168.0.217:9901/PurchaseApNoTax'
    # δ˰����ͷ
    ws_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {tk}"}
    # δ˰������
    ws_data = {"purchase_order_code": cgddh, "no_tax_amount": jine, "remark": "����δ˰"}
    # δ˰����
    r = requests.post(url=ws_url, json=ws_data, headers=ws_header)
    # ��ȡ��ֹ����id���µ��б�
    weishui['id'] = r.json()['data']['id']
    wsid = r.json()['data']['id']
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡjson��������
    print(r.json())
    # ����δ˰�ɹ�����
    assert r.json()['message'] == 'success'


@allure.feature('Ӧ������-�ӿ�')
@allure.story('δ˰')
@allure.step('�޸�δ˰')
def test_xgws():
    global wsid, weishui
    # �޸�δ˰URL
    xgws_url = f'http://192.168.0.217:9901/PurchaseApNoTax/{wsid}'
    # �޸�δ˰����ͷ
    xgws_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {tk}"}
    # �޸�δ˰������
    xgws_data = {"id": weishui['id'], "purchase_order_code": cgddh, "no_tax_amount": xgjine,
                 "remark": "���Ա༭δ˰",
                 "creator_id": 1, "operate_id": 1, "creator_name": "Admin", "operate_name": "Admin"}
    # �޸�δ˰����
    r = requests.put(url=xgws_url, json=xgws_data, headers=xgws_header)
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡjson��������
    print(r.json())


@allure.feature('Ӧ������-�ӿ�')
@allure.story('δ˰')
@allure.step('ɾ��δ˰')
def test_scws():
    # ɾ����ֹURL
    scws_url = f'http://192.168.0.217:9901/PurchaseApNoTax/{wsid}'
    # ɾ����ֹ����ͷ
    scws_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {tk}"}
    # ɾ����ֹ����
    r = requests.delete(url=scws_url, headers=scws_header)
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡjson��������
    print(r.json())


@allure.feature('Ӧ������-�ӿ�')
@allure.story('δ˰')
@allure.step('��ѯδ˰������¼')
def test_cxws():
    global wsid
    # �������ݿ�
    connect = pymysql.connect(host='192.168.0.226', user='root', password='CLd8T8TWt58ypaxd', db='hz_erp_test')
    if connect:
        print('���ӳɹ�')
    # ����һ���α����
    yf = connect.cursor()
    # ��ȷ��ѯ������־
    sql_rz = f"select no_tax_id,`type` from hz_erp_test.hz_purchase_ap_no_tax_log where no_tax_id ={wsid}"
    # ִ�в�ѯ���
    yf.execute(sql_rz)
    # ��ȡ���
    rz = yf.fetchall()
    # ��ӡ���ؽ��
    print(rz)
    yf.close()


# Ԥ������
# ����������Ӽ���Ԥ������
yfk = random.randint(-199, 399)


@allure.feature('Ӧ������-�ӿ�')
@allure.story('Ԥ����')
@allure.step('Ԥ������')
def test_yfk():
    # Ԥ����URL
    yfk_url = 'http://192.168.0.217:9901/PurchaseApCustomerPre'
    # Ԥ��������ͷ
    yfk_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {tk}"}
    # Ԥ����������
    yfk_data = {"total_pre_payment_amount": "", "customer_name": "�㽭�콡Զ���Ƽ����޹�˾", "payment_mode": 65,
                "payment_mode_name": "�����ֽ�", "payment_time": "2023-02-28", "pre_payment_amount": yfk,
                "remark": "��������Ԥ����"}
    # Ԥ��������
    r = requests.post(url=yfk_url, json=yfk_data, headers=yfk_header)
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡjson��������
    print(r.json())
    # ����Ԥ�������ɹ�����
    assert r.json()['message'] == 'success'
