from datetime import datetime

def getime():
    res=""
    par=str(datetime.now()).split(' ')
    YMD=par[0]
    HMS=par[1]
    YMD_par=YMD.split('-')
    M=YMD_par[1]
    D=YMD_par[2]
    res=res+M+'月'+D+'日 '+HMS[0:5]
    return res
print(getime())