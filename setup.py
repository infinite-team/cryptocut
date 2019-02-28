from threading import Thread
import platform
#detect OS
#install tools for specific OS/distro
#copy files
if (platform.system()=="Darwin"):
    pass
if (platform.system()=="Windows"):
    pass
if (platform.system()=="Linux"):
    with open('/etc/os-release','r') as DistroInfoRead:
        DistroInfo = DistroInfoRead.read()
    DistroInfo = DistroInfo.split('\n')
    DistroInfo = DistroInfo[0:len(DistroInfo)-2]
    DistroInfoList=[]
    for i in DistroInfo:
        DistroInfoList.append([i.split('=')[0],i.split('=')[1]])
    #for i in Distr
    #ID_LIKE=arch
    for i in DistroInfoList:
        if (i[0]=="ID_LIKE"):
            if ("arch"==i[1]):
            if ("arch"==i[1]):

    #
    # ## package installer
    # #arch
    # if('arch' in DistroBase):
    #     thread = Thread(group=None, target=lambda:os.system("sudo pacman -Sy libnotify-bin wget xsel xclip"))
    #     thread.run()
    #     if(thread.is_alive()):
    #         print('packages not installed successfully :( \n see link for more information!')
    #     else:
    #         print('all done!')
    #
    # #debian
    # if('Debian' in DistroBase):
    #     thread = Thread(group=None, target=lambda:os.system("sudo pacman -Sy libnotify-bin wget xsel xclip"))
    #     thread.run()
    #     if(thread.is_alive()):
    #         print('packages not installed successfully :( \n see link for more information!')
    #     else:
    #         print('all done!')
