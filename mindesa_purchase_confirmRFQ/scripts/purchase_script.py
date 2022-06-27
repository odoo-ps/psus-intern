# -*- coding: utf-8 -*-


from operator import mod
from xmlrpc import client
url = "http://localhost:8069"
db = "mindesa"
username = "admin"
password = "admin"

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version())

uid = common.authenticate(db,username,password,{})
print(uid)

models = client.ServerProxy("{}/xmlrpc/2/object".format(url))

model_access = models.execute_kw(db,uid,password,
                                'purchase.order', 'check_access_rights',
                                ['write'], {'raise_exception':False})

print(model_access)

draft_quotes=models.execute_kw(db,uid,password,'purchase.order', 'search', [[['state', '=','draft'],
                                                                            ['partner_id','=','Mindesa SAPI de CV'],
                                                                            ['user_id','=','OdooBot']]])
print(draft_quotes)

#if_confirmed = models.execute_kw(db,uid,password,'purchase.order','action_rfq_send',[draft_quotes])


