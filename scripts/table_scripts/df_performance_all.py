from data7project.scripts.table_scripts.tools.append_tables_buckets import *

df = Append_All('data7-engineering-project')
df = df.append_all('Academy')


def ih_pull():
    ih_pull = df.filter(
        ["name", "IH_W1", "IH_W2", "IH_W3", "IH_W4", "IH_W5", "IH_W6", "IH_W7", "IH_W8", "IH_W9", "IH_W10"])
    return ih_pull


def is_pull():
    is_pull = df.filter(
        ["name", "IS_W1", "IS_W2", "IS_W3", "IS_W4", "IS_W5", "IS_W6", "IS_W7", "IS_W8", "IS_W9", "IS_W10"])
    return is_pull


def pv_pull():
    pv_pull = df.filter(
        ["name", "PV_W1", "PV_W2", "PV_W3", "PV_W4", "PV_W5", "PV_W6", "PV_W7", "PV_W8", "PV_W9", "PV_W10"])
    return pv_pull


def ps_pull():
    ps_pull = df.filter(
        ["name", "PS_W1", "PS_W2", "PS_W3", "PS_W4", "PS_W5", "PS_W6", "PS_W7", "PS_W8", "PS_W9", "PS_W10"])
    return ps_pull


def sd_pull():
    sd_pull = df.filter(
        ["name", "SD_W1", "SD_W2", "SD_W3", "SD_W4", "SD_W5", "SD_W6", "SD_W7", "SD_W8", "SD_W9", "SD_W10"])
    return sd_pull


def sa_pull():
    sa_pull = df.filter(
        ["name", "SA_W1", "SA_W2", "SA_W3", "SA_W4", "SA_W5", "SA_W6", "SA_W7", "SA_W8", "SA_W9", "SA_W10"])
    return sa_pull

print(df)