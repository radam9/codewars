# https://www.codewars.com/kata/59de1e2fe50813a046000124/train/python
# 5 Kyu
# Matching and Substituting

# My Solution
import re


def change(string, title, version):
    check_tel = re.search(r"\+1-\d{3}-\d{3}-\d{4}", string)
    check_ver = re.search(r": (\d+\.\d+)\n", string)
    if not check_tel or not check_ver:
        return "ERROR: VERSION or PHONE"
    check_ver = check_ver.group(1)
    if check_ver == "2.0":
        version = check_ver
    return f"Program: {title} Author: g964 Phone: +1-503-555-0090 Date: 2019-01-01 Version: {version}"


# Codewars Influenced Solution
import re


def change(string, title, version):
    try:
        re.search(r"\+1-\d{3}-\d{3}-\d{4}", string).group()
        check_ver = re.search(r"^Version\: (\d+\.\d+)$", string, re.M).group(1)
    except:
        return "ERROR: VERSION or PHONE"
    return f"Program: {title} Author: g964 Phone: +1-503-555-0090 Date: 2019-01-01 Version: {version if check_ver != '2.0' else check_ver}"