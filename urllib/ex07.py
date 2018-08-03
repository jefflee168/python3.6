#!/usr/bin/env python3
# coding: utf-8 

import requests

headers = {
    'Cookie': '.CNBlogsCookie=B84E9FD1BE3945CB62D02B217C83B43A62DF988F57DE6AD1300F3471F5D9C4548457B79931E00EA819E30D7EC0A4810FD50AC7234F3E1ADFBD99838E229667A74701D1419E94B352DC290232E97A0EF28B3E32D1; .Cnblogs.AspNetCore.Cookies=CfDJ8FHXRRtkJWRFtU30nh_M9mDa4uAfPbfdl_-USz5vZHuiAS_Zm5EElpSLjSLHz3sYMcsz_hL-AWpz_4OTsvghQzNsr9tvFcf4CTACAbtqYeOpgAm1odEUITsi5sYtTmmPJWeJo10q1o6uknxYS51n3TBLINFsr3qzECb8NVZrMPeJB--nnEPLBKOfGoUkpNBa7ximXenrDntjoGbRXFPxTecuvYzKTiiABh2M0L2ITHCzQxP0uwfCSxn-w1iZi-9GzHy_Q4rfcqC0oyIvUaDxxd4Ng-CKIN7YermF3OlVVHo3VlAu6iogYldgBgU2lnRROA',
    'Host': 'www.cnblogs.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}

r = requests.get('https://www.cnblogs.com', headers=headers)
print(r.text)
