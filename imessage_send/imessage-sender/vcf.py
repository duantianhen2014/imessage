import sys
import os
import re

def csv2vcf_android(csv_filename, encoding='utf-8'):
    """csv格式文件转换为安卓适用的vcf格式文件"""
    # 1.读取csv文件
    with open(csv_filename, 'r', encoding='utf-8') as f:
        ftext_list = f.readlines()
        f.close()
    # 2.将cvs转换为vcf格式
    vcards = ''
    for line in ftext_list[1:]:
        tel_numbers = ''
        name_tel_list = line.strip().split(',')
        if name_tel_list[0]:
            tel_name = name_tel_list[0]  # 姓名
            org = name_tel_list[1]       # 单位
            for tel in name_tel_list[2:]:  # 电话
                tel_numbers += f'TEL;CELL:{tel}\n'
            vcard = f'BEGIN:VCARD\nN:{tel_name}\nORG:{org}\n{tel_numbers}END:VCARD\n'
            vcards += vcard
    # 3.保存转换后的vcf格式文件
    (fpath, temp_fname) = os.path.split(csv_filename)
    (fname, fextension) = os.path.splitext(temp_fname)
    with open(f'{fpath}{fname}_android.vcf', "w", encoding=encoding) as f:
        try:
            f.write(vcards)
        finally:
            f.close()

def csv2vcf_ios(csv_filename, encoding='utf-8'):
    """csv格式文件转换为ios适用vcf格式文件"""
    # 1.读取csv文件
    with open(csv_filename, 'r', encoding='utf-8') as f:
        ftext_list = f.readlines()
        f.close()
    # 2.将cvs转换为vcf格式
    vcards = ''
    for line in ftext_list[1:]:
        #tel_numbers = ''
        name_tel_list = line.strip().split(',')
        if name_tel_list[0]:
            tel_name = name_tel_list[0]  # 姓名
            xing = tel_name[0]   # 姓
            ming = tel_name[1:]  # 名
            #print(xing,ming,len(ming))
            org = name_tel_list[1]  # 单位
            short_tel = name_tel_list[2]
            long_tel = name_tel_list[3]
            vcard = f'BEGIN:VCARD\nVERSION:3.0\nN:{xing};{ming};;;\nFN:{ming} {xing}\nORG:{org};\nTEL;TYPE=CELL;TYPE=pref;TYPE=VOICE:{long_tel}\nTEL;TYPE=WORK;TYPE=VOICE:{short_tel}\nPRODID:-//Apple Inc.//iCloud Web Address Book 2021B82//EN\nREV:2020-11-26T19:51:27Z\nEND:VCARD\n'
            vcards += vcard
    # 3.保存转换后的vcf格式文件
    (fpath, temp_fname) = os.path.split(csv_filename)
    (fname, fextension) = os.path.splitext(temp_fname)
    with open(f'{fpath}{fname}_ios.vcf', "w", encoding=encoding) as f:
        try:
            f.write(vcards)
        finally:
            f.close()



filename = sys.argv[1]
# csv2vcf_android(filename)
csv2vcf_ios(filename)