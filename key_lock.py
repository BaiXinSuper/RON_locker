import autopy,time,psutil,datetime,math
print('开源地址： https://github.com/BaiXinSuper/RON_locker')
print('解决RON鼠标锁定的屌毛弱智问题')
nix_progress_id=0
while 1:
    #print(psutil.pids())
    for i in psutil.pids() :
        if psutil.Process(i).name()=='ReadyOrNot.exe' or psutil.Process(i).name()=='ReadyOrNot-Win64-Shipping.exe':
            nix_progress_id=i
            break
    if nix_progress_id:
        break
    time.sleep(10)
def init():
    global yu
    yu=input(f'边界阈值 推荐 3-10 (注意不可大于或等于{min(int(autopy.screen.size()[0]),int(autopy.screen.size()[1]))})\n')
    try:
        yu=int(yu)
        if yu>=min(int(autopy.screen.size()[0]),int(autopy.screen.size()[1])):
            init()
        elif yu>=50:
            ll=input('你确定要这样吗？这可有点大哦~可能会有点影响你的设置或者开始游戏的哦~~ y/n\n')
            if ll=='y' or ll=='Y':
                ll=input('你确定要这样吗？这是最后一次忠告！！ y/n\n')
                if ll=='y' or ll=='Y':
                    print('我可真劝不住你')
                    pass
                else:
                    init()
            else:
                init()
    except:
        init()
print(f'发现进程ID：{nix_progress_id}')
print(f'屏幕分辨率:{int(autopy.screen.size()[0])}x{int(autopy.screen.size()[1])} (可能会有误，但是不会影响使用)')
init()
print('软件已启动')
print('打游戏看鼠标不顺眼？我也是')
while nix_progress_id:
    if autopy.mouse.location()[0] >= autopy.screen.size()[0]-yu or autopy.mouse.location()[1] >= autopy.screen.size()[1]-yu:
        print(f'[{str(datetime.datetime.now())[:-7:]}]鼠标出现移位错误{autopy.mouse.location()}')
        autopy.mouse.move(autopy.screen.size()[0]/2,autopy.screen.size()[1]/2)
    elif autopy.mouse.location()[0] <= yu or autopy.mouse.location()[1] <= yu:
        print(f'[{str(datetime.datetime.now())[:-7:]}]鼠标出现移位错误{autopy.mouse.location()}')
        autopy.mouse.move(autopy.screen.size()[0]/2,autopy.screen.size()[1]/2)
    time.sleep(0.005)
    if psutil.pid_exists(nix_progress_id):
        try:
            if psutil.Process(nix_progress_id).name()=='ReadyOrNot.exe' or psutil.Process(nix_progress_id).name()=='ReadyOrNot-Win64-Shipping.exe':
                pass
            else:
                input('游戏已关闭，回车退出软件')
                exit(0)
        except:
            input('游戏已关闭，回车退出软件')
            exit(0)
    else:
        input('游戏已关闭，回车退出软件')
        exit(0)
