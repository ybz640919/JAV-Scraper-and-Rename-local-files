# -*- coding:utf-8 -*-
import re, os, requests
# from traceback import format_exc

# 功能：请求各大jav网站和arzon的网页
# 参数：网址url，请求头部header/cookies，代理proxy
# 返回：网页html，请求头部


#################################################### javlibrary ########################################################
# 搜索javlibrary，或请求javlibrary上jav所在网页，返回html
def get_library_html(url, proxy):
    for retry in range(10):
        try:
            if proxy:
                rqs = requests.get(url, proxies=proxy, timeout=(6, 7))
            else:
                rqs = requests.get(url, timeout=(6, 7))
        except requests.exceptions.ProxyError:
            # print(format_exc())
            print('    >通过局部代理失败，重新尝试...')
            continue
        except:
            # print(format_exc())
            print('    >打开网页失败，重新尝试...')
            continue
        rqs.encoding = 'utf-8'
        rqs_content = rqs.text
        # print(rqs_content)
        if re.search(r'JAVLibrary', rqs_content):        # 得到想要的网页，直接返回
            return rqs_content
        else:                                         # 代理工具返回的错误信息
            print('    >打开网页失败，空返回...重新尝试...')
            continue
    print('>>请检查你的网络环境是否可以打开：', url)
    os.system('pause')

