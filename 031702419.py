# -*- coding: utf-8 -*-
import json
import re

def gettelnum(s):       #获得电话号码
    res = re.search(r'\d{11}', s)
    if res == None:
        return ""
    return res.group(0)

def getprovince(s):      ##获得省
    res = re.search(("(.*?省)|(.*?自治区)|上海市|北京市|天津市|重庆市"), s)
    if res != None:
        l = len(res.group(0))
    if res == None or l > 5:
        if s[0:3] == "黑龙江":
            return "黑龙江"
        if s[0:3] == "内蒙古":
            return "内蒙古"
        else:
            return s[0:2]
    return res.group(0)

def getcity(s):            #获得城镇
    res = re.search("(.*?自治州)|(.*?[市])", s)
    if res != None:
        l = len(res.group(0))
    if res == None or l > 7:
        for i in CITIES:
            if s[0:2] in i:
                return i
        return ""
    return res.group(0)

def getcounty(s):            #获得县
    #print(s)
    res = re.search("(.*?自治旗)|(.*?[县区市旗])", s)
    if res == None:
        #print("_____________________")
        for i in AREAS:
            if s[0:2] in i:
                return i
        return ""
    return res.group(0)

def gettown(s):         #获得城镇
    res = re.search("(.*?街道)|(.*?[镇乡])", s)
    if res == None:
        return ""
    return res.group(0)

def getroad(s): #获得路
    res = re.search("(.*?[路街巷道])", s)
    if res == None:
        return ""
    return res.group(0)

def getdoornum(s):                         #获得门牌号
    res = re.search("(.*?[号])", s)
    if res == None:
        return ""
    return res.group(0)

CITIES=['乌鲁木齐', '克拉玛依', '拉萨 ', '银川', '石嘴山', '吴忠', '固原', '中卫', '呼和浩特', '包头', '乌海', '赤峰', '通辽', '鄂尔多斯', '呼伦贝尔', '巴彦淖尔', '乌兰察布', '南宁', '柳州', '桂林', '梧州', '北海', '崇左', '来宾', '贺州', '玉林', '百色', '河池', '钦州', '防城港', '贵港', '哈尔滨', '大庆', '齐齐哈尔', '佳木斯', '鸡西', '鹤岗', '双鸭山', '牡丹江', '伊春', '七台河', '黑河', '绥化', '长春', '吉林', '四平', '辽源', '通化', '白山', '松原', '白城', '沈阳', '大连', '鞍山', '抚顺', '本溪', '丹东', '锦州', '营口', '阜新', '辽阳', '盘锦', '铁岭', '朝阳', '葫芦岛', '石家庄', '唐山', '邯郸', '秦皇岛', '保定', '张家口', '承德', '廊坊', '沧州', '衡水', '邢台', '济南', '青岛', '淄博', '枣庄', '东营', '烟台', '潍坊', '济宁', '泰安', '威海', '日照', '莱芜', '临沂', '德州', '聊城', '菏泽', '滨州', '南京', '镇江', '常州', '无锡', '苏州', '徐州', '连云港', '淮安', '盐城', '扬州', '泰州', '南通', '宿迁', '合肥', '蚌埠', '芜湖', '淮南', '亳州', '阜阳', '淮北', '宿州', '滁州', '安庆', '巢湖', '马鞍山', '宣城', '黄山', '池州', '铜陵', '杭州', '嘉兴', '湖州', '宁波', '金华', '温州', '丽水', '绍兴', '衢州', '舟山', '台州', '福州', '厦门', '泉州', '三明', '南平', '漳州', '莆田', '宁德', '龙岩', '广州', '深圳', '汕头', '惠州', '珠海', '揭阳', '佛山', '河源', '阳江', '茂名', '湛江', '梅州', '肇庆', '韶关', '潮州', '东莞', '中山', '清远', '江门', '汕尾', '云浮', '海口', '三亚', '昆明', '曲靖', '玉溪', '保山', '昭通', '丽江', '普洱', '临沧', '贵阳', '六盘水', '遵义', '安顺', '成都', '绵阳', '德阳', '广元', '自贡', '攀枝花', '乐山', '南充', '内江', '遂宁', '广安', '泸州', '达州', '眉山', '宜宾', '雅安', '资阳', '长沙', '株洲', '湘潭', '衡阳', '岳阳', '郴州', '永州', '邵阳', '怀化', '常德', '益阳', '张家界', '娄底 ', '武汉', '襄樊', '宜昌', '黄石', '鄂州', '随州', '荆州', '荆门', '十堰', '孝感', '黄冈', '咸宁', '郑州', '洛阳', '开封', '漯河', '安阳', '新乡', '周口', '三门峡', '焦作', '平顶山', '信阳', '南阳', '鹤壁', '濮阳', '许昌', '商丘', '驻马店', '太原', '大同', '忻州', '阳泉', '长治', '晋城', '朔州', '晋中', '运城', '临汾', '吕梁', '西安', '咸阳', '铜川', '延安', '宝鸡', '渭南', '汉中', '安康', '商洛', '榆林', '兰州', '天水', '平凉', '酒泉', '嘉峪关', '金昌', '白银', '武威', '张掖', '庆阳', '定西', '陇南', '西宁', '南昌', '九江', '赣州', '吉安', '鹰潭', '上饶', '萍乡', '景德镇', '新余', '宜春', '抚州','延边朝鲜族自治州', '恩施土家族苗族自治州', '湘西土家族苗族自治州', '临夏回族自治州', '甘南藏族自治州', '甘孜藏族自治州', '凉山彝族自治州', '阿坝藏族羌族自治州', '黔东南苗族侗族自治州', '黔南布依族苗族自治州', '黔西南布依族苗族自治州', '昌吉回族自治州', '伊犁哈萨克自治州', '博尔塔拉蒙古自治州', '巴音郭楞蒙古自治州', '黄南藏族自治州', '海北藏族自治州', '海南藏族自治州', '果洛藏族自治州', '玉树藏族自治州', '海西蒙古族藏族自治州', '迪庆藏族自治州', '楚雄彝族自治州', '大理白族自治州', '怒江傈僳族自治州', ' 西双版纳傣族自治州', '文山壮族苗族自治州', '德宏傣族景颇族自治州', '红河哈尼族彝族自治州', '克孜勒苏柯尔克孜自治州']
AREAS = ['东城区', '西城区', '朝阳区', '丰台区', '石景山区', '海淀区', '门头沟区', '房山区', '通州区', '顺义区', '昌平区', '大兴区', '怀柔区',
 '平谷区', '密云区', '延庆区', '和平区', '河东区', '河西区', '南开区', '河北区', '红桥区', '东丽区', '西青区']
S = input()
A = S[0]
S = S[2:]
RESULT = S.split(",")
NAME = RESULT[0]
NOWS = RESULT[1]
TELNUM = gettelnum(NOWS)
NOWS = NOWS.replace(TELNUM, "", 1)
NOWS = NOWS.replace(".", "", 1)

PROVINCE = getprovince(NOWS)
if PROVINCE in ('北京', '上海', '天津', '重庆'):
    PROVINCE = PROVINCE
    NOWS = NOWS.replace(PROVINCE, PROVINCE + "市", 1)
elif PROVINCE in ('北京市', '上海市', '天津市', '重庆市'):
    PROVINCE = PROVINCE[0:2]
elif PROVINCE == "广西":
    NOWS = NOWS.replace(PROVINCE, "", 1)
    PROVINCE = PROVINCE + "壮族自治区"
elif PROVINCE == "新疆":
    NOWS = NOWS.replace(PROVINCE, "", 1)
    PROVINCE = PROVINCE + "维吾尔自治区"
elif PROVINCE == "宁夏":
    NOWS = NOWS.replace(PROVINCE, "", 1)
    PROVINCE = PROVINCE + "回族自治区"
elif PROVINCE == "内蒙古":
    NOWS = NOWS.replace(PROVINCE , "", 1)
    PROVINCE = PROVINCE + "自治区"
elif PROVINCE == "西藏":
    NOWS = NOWS.replace(PROVINCE, "", 1)
    PROVINCE = PROVINCE + "自治区"
elif PROVINCE[-1] != "省" and PROVINCE[-1] != "区":           #province = 黑龙江 福建
    NOWS = NOWS.replace(PROVINCE, "", 1)
    PROVINCE = PROVINCE + "省"
else:
    NOWS = NOWS.replace(PROVINCE, "", 1)

CITY = getcity(NOWS)

if CITY != "":
    NOWS = NOWS.replace(CITY, "", 1)
    if (CITY[-1] != "市") and (CITY[-3:-1] != "自治"):
        #print(city[-3:-1])
        CITY = CITY+"市"
        #print(CITY)


COUNTY = getcounty(NOWS)
if COUNTY != "":
    L = len(COUNTY)
    if COUNTY[-1] == NOWS[L-1]:
        NOWS = NOWS.replace(COUNTY, "", 1)
    else:
        NOWS = NOWS.replace(COUNTY[:-1], "", 1)
        #print(county[:-1])
TOWN = gettown(NOWS)
NOWS = NOWS.replace(TOWN, "", 1)
DETAIADDR = NOWS

ROAD = getroad(NOWS)
NOWS = NOWS.replace(ROAD, "", 1)

DOORNUM = getdoornum(NOWS)
NOWS = NOWS.replace(DOORNUM, "", 1)

DICT = {}
DICT["姓名"] = NAME
DICT["手机"] = TELNUM
ADDRLIST = []
if A == '1':
    ADDRLIST.append(PROVINCE)
    ADDRLIST.append(CITY)
    ADDRLIST.append(COUNTY)
    ADDRLIST.append(TOWN)
    ADDRLIST.append(DETAIADDR)
else:
    ADDRLIST.append(PROVINCE)
    ADDRLIST.append(CITY)
    ADDRLIST.append(COUNTY)
    ADDRLIST.append(TOWN)
    ADDRLIST.append(ROAD)
    ADDRLIST.append(DOORNUM)
    ADDRLIST.append(NOWS)
DICT["地址"] = ADDRLIST

#print(DICT)
print(json.dumps(DICT))