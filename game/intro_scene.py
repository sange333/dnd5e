import time

def intro_scene():
    print("欢迎来到 DnD5e 文字冒险游戏!\n")
    time.sleep(1)
    print("你醒来时发现自己身处在一片黑暗的森林中，完全不记得自己是如何来到这里的。")
    print("有一条小路通向北方，附近的灌木丛中似乎有什么东西在动。")
    print("你想做什么?")
    print("1. 探索灌木丛")
    print("2. 沿着小路往北走")
    print("3. 等待并聆听\n")
    choice = input("请输入你选择的数字: ")
    
    return choice
