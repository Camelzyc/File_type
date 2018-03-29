#判断文件类型
fileName=input("请输入你的文件名:")
number=fileName.rfind(".")
print(fileName[number+1:])
