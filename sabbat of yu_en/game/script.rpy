# 遊戲腳本位於此檔案。

# 宣告該遊戲使用的角色。 color 參數
# 為角色的名稱著色。


define xv = Character("???")

define en = Character("宇恩")

define cn = Character("楚南")

image en_pose = "images/yuen@5.png"

# 遊戲從這裡開始。

label start:

    # 顯示背景。 預設情況下，它使用佔位符，但您可以
    # 將檔案（名為 "bg room.png" 或 "bg room.jpg"）新增至
    # images 目錄來顯示它。

    scene bg room

    # 這顯示了一個角色精靈。 使用了佔位符，但您可以
    # 透過將名為 "eileen happy.png" 的檔案
    # 新增至 images 目錄來取代它。

    

    # 這些顯示對話行。

    "那一天，我在農場高中醒來"

    "那是一個風光明媚的夜晚，我本應於床上酣睡"

    "但是現在......為甚麼我在凌晨3點出現在教室呢？"

    xv "阿拉阿拉，這不是我們敬愛的蕭楚南同學嗎？"

    show en_pose

    cn "......宇恩？"

    en "heheheha"

    # 遊戲結束。

    return
