import os

import requests

if __name__ == '__main__':

    '''验证代理是否存在'''
    respond=requests.post("http://127.0.0.1:30713/is_exist")
    print(respond.text)
    print("Divide---------------------------------------------------------------------\n\n\n")
    respond=requests.post("http://127.0.0.1:30713/get_all_versions")
    print(respond.text)
    print("Divide---------------------------------------------------------------------\n\n\n")
    respond=requests.post("http://127.0.0.1:30713/get_LiteLoader_list",data={"Version":"1.12.2"})
    print(respond.json())
    print("Divide---------------------------------------------------------------------\n\n\n")
    respond=requests.post("http://127.0.0.1:30713/get_forge_list",data={"Version":"1.12.2"})
    print(respond.json())
    print("Divide---------------------------------------------------------------------\n\n\n")
    respond=requests.post("http://127.0.0.1:30713/get_forge_supported_list")
    #print(respond.json())
    print("Divide---------------------------------------------------------------------\n\n\n")
    respond=requests.post("http://127.0.0.1:30713/get_optifine_list",data={"Version":"1.12.2"})
    print(respond.json())
    print("Divide---------------------------------------------------------------------\n\n\n")
    respond=requests.post("http://127.0.0.1:30713/get_java_list")
    print(respond.json())
    print("Divide---------------------------------------------------------------------\n\n\n")

    path=os.getcwd()+"\\"
    path="D:\\GolangFiles\\RedStoneGameCache\\"

    # respond=requests.post("http://127.0.0.1:30713/download",data={"MCVersion":"1.7.10","VersionName":"1.7.10","RetryTimes":5,"DownloadSource":2,"WorkPath":path})
    # respond=requests.post("http://127.0.0.1:30713/execute",data={"MCVersion":"1.7.10","VersionName":"1.7.10","UserName":"StarDream","RetryTimes":5,"DownloadSource":2,"JavaPath":"'D:\\JavaJDK\\bin\\java.exe' ","WorkPath":path})
    # respond=requests.post("http://127.0.0.1:30713/download",data={"MCVersion":"1.12.2","VersionName":"1.12.2","RetryTimes":10,"DownloadSource":2,"WorkPath":path})
    # respond=requests.post("http://127.0.0.1:30713/execute",data={"MCVersion":"1.12.2","VersionName":"1.12.2","UserName":"StarDream","RetryTimes":10,"DownloadSource":2,"JavaPath":"'D:\\JavaJDK\\bin\\java.exe' ","WorkPath":path})
    # respond=requests.post("http://127.0.0.1:30713/download",data={"MCVersion":"1.14.4","VersionName":"1.14.4","RetryTimes":5,"DownloadSource":2,"WorkPath":path})
    # respond=requests.post("http://127.0.0.1:30713/execute",data={"MCVersion":"1.14.4","VersionName":"1.14.4","UserName":"StarDream","RetryTimes":5,"DownloadSource":2,"JavaPath":"'D:\\JavaJDK\\bin\\java.exe' ","WorkPath":path})
    #respond=requests.post("http://127.0.0.1:30713/download",data={"MCVersion":"1.16","VersionName":"1.16","RetryTimes":5,"DownloadSource":2,"WorkPath":path})
    #respond=requests.post("http://127.0.0.1:30713/execute",data={"MCVersion":"1.16","VersionName":"1.16","UserName":"StarDream","RetryTimes":5,"DownloadSource":2,"JavaPath":"'D:\\JavaJDK\\bin\\java.exe' ","WorkPath":path})
    #respond=requests.post("http://127.0.0.1:30713/download",data={"MCVersion":"1.18.2","VersionName":"1.18.2","RetryTimes":5,"DownloadSource":2,"WorkPath":path})
    #respond=requests.post("http://127.0.0.1:30713/execute",data={"MCVersion":"1.18.2","VersionName":"1.18.2","UserName":"StarDream","RetryTimes":5,"DownloadSource":2,"JavaPath":"'D:\\JavaJDK\\bin\\java.exe' ","WorkPath":path})
    # respond=requests.post("http://127.0.0.1:30713/download",data={"MCVersion":"1.19.2","VersionName":"1.19.2","RetryTimes":5,"DownloadSource":2,"WorkPath":path})
    # respond=requests.post("http://127.0.0.1:30713/execute",data={"MCVersion":"1.19.2","VersionName":"1.19.2","UserName":"StarDream","RetryTimes":5,"DownloadSource":2,"JavaPath":"'D:\\JavaJDK\\bin\\java.exe' ","WorkPath":path})
    respond=requests.post("http://127.0.0.1:30713/java_list")
    print(respond.text)
    respond=requests.post("http://127.0.0.1:30713/adduser_offline",{"UserName":"Tester"})
    print(respond.text)
    respond=requests.post("http://127.0.0.1:30713/Select_user",{"UserName":"Tester"})
    print(respond.text)
    print("Divide---------------------------------------------------------------------\n\n\n")
