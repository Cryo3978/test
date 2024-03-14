#designed by Shuheng Chen, Tianjin University.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

#储存result.txt之处
filepath="res/result.txt"
directory=os.path.dirname(filepath)

#执行时请设置好环境变量
driver = webdriver.Chrome()
def store_current_price(date,type):
    #字典转换
    if type in samples_dict:
        type=samples_dict[type]
    else:
        print("The type you provide is not typical, plz double check!")

    driver.get("https://www.boc.cn/sourcedb/whpj/")
    #Explicit Waits
    try:
        search1=WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.NAME,"erectDate"))
        )
        search2=WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.NAME,"nothing"))
        )
        option=WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.NAME,"pjname"))
        )
        search_btn=WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[onclick='executeSearch()']"))
        )
    except Exception as e:
        print(e)

#设置具体查询
    search1.clear()
    search1.send_keys(date)
    search2.clear()
    search2.send_keys(date)
    option.send_keys(type)
    search_btn.click()
    print("search successfully")

    # 定位到类名为 'odd' 的 <tr> 中的第三个 <td>，也就是现汇卖出价
    try:
        price=WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "tr.odd td:nth-child(3)"))
        )
    except Exception as e:
        print(e)

    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

    # 写入内容
    with open(filepath, 'w', encoding="utf-8") as file:
        content=date+type+"参考现汇卖出价:"+price.text
        file.write(content)
        print("successfully store")
    file.close()
    driver.quit()

#转换字典
samples_dict = {
    "USD": "美元",
    "EUR": "欧元",
    "JPY": "日元",
    "GBP": "英镑",
    "AUD": "澳大利亚元",
    "CAD": "加拿大元",
    "CHF": "瑞士法郎",
    "CNY": "人民币",
    "SEK": "瑞典克朗",
    "NZD": "新西兰元",
    "MXN": "墨西哥比索",
    "SGD": "新加坡元",
    "HKD": "港币",
    "NOK": "挪威克朗",
    "KRW": "韩元",
    "TRY": "土耳其里拉",
    "RUB": "俄罗斯卢布",
    "INR": "印度卢比",
    "BRL": "巴西雷亚尔",
    "ZAR": "南非兰特",
    "DKK": "丹麦克朗",
    "PLN": "波兰兹罗提",
    "TWD": "新台币",
    "THB": "泰铢",
    "IDR": "印尼盾",
    "HUF": "匈牙利福林",
    "CZK": "捷克克朗",
    "ILS": "以色列新谢克尔",
    "CLP": "智利比索",
    "PHP": "菲律宾比索",
    "AED": "阿联酋迪拉姆",
    "COP": "哥伦比亚比索",
    "SAR": "沙特里亚尔",
    "MYR": "马来西亚林吉特",
    "RON": "罗马尼亚列伊",
    "VND": "越南盾",
    "BDT": "孟加拉塔卡",
    "UAH": "乌克兰格里夫纳",
    "PEN": "秘鲁新索尔",
    "EGP": "埃及镑",
    "NGN": "尼日利亚奈拉",
    "PKR": "巴基斯坦卢比",
    "DZD": "阿尔及利亚第纳尔",
    "KES": "肯尼亚先令",
    "ARS": "阿根廷比索",
    "QAR": "卡塔尔里亚尔",
    "CZK": "捷克克朗",
    "LYD": "利比亚第纳尔",
    "JOD": "约旦第纳尔",
    "OMR": "阿曼里亚尔",
    "RSD": "塞尔维亚第纳尔",
    "UZS": "乌兹别克斯坦索姆",
    "BGN": "保加利亚列弗",
    "KHR": "柬埔寨瑞尔",
    "LKR": "斯里兰卡卢比",
    "MVR": "马尔代夫卢非亚",
    "NPR": "尼泊尔卢比",
    "AMD": "亚美尼亚德拉姆",
    "MNT": "蒙古图格里克",
    "IRR": "伊朗里亚尔",
    "LBP": "黎巴嫩镑",
    "YER": "也门里亚尔",
    "QAR": "卡塔尔里亚尔",
    "ISK": "冰岛克朗",
    "JMD": "牙买加元",
    "FJD": "斐济元",
    "XPF": "太平洋法郎",
    "MOP": "澳门元",
    "SBD": "所罗门群岛元",
    "ETB": "埃塞俄比亚比尔",
    "MGA": "马达加斯加阿里亚里",
    "BWP": "博茨瓦纳普拉",
    "GHS": "加纳塞地",
    "NAD": "纳米比亚元",
    "PAB": "巴拿马巴波亚",
    "BBD": "巴巴多斯元"
}

#测试用例
date="2024-03-13"
type="JPY"
store_current_price(date,type)


