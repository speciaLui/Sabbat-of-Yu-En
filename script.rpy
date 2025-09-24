# 遊戲腳本位於此檔案。

# 宣告該遊戲使用的角色。 color 參數
# 為角色的名稱著色。


define xv = Character("???")

define q = Character("齊拉奈")

define y = Character("海町宇恩")

define flag=0



# 遊戲從這裡開始。

# image book:
#     "#020202"
#     "xysize" = (800,600)

# label start:

#     # 隱藏對話框
#     window hide

#     # 更換背景或設為空白底
#     show book

#     # 顯示全頁文字（可多行）
#     show text """
#     第一章：命運的齒輪

#     從前從前，在遙遠的東方，有一座被迷霧籠罩的山谷。
#     那裡居住著一群被世人遺忘的守護者——他們守護著千年古卷的秘密。

#     傳說中，只有命中注定的人才能揭開古卷的真面目……

#     """ at truecenter with dissolve

#     pause  # 等待玩家點擊繼續

#     return

    
label start:
    jump book_scene

init python:
    book_pages = [
        "第一章：命運的齒輪\n\n從前從前，在遙遠的東方……",
        "第二章：古卷的守護者\n\n……他們守護著千年古卷的秘密。\n傳說中，只有命中注定的人……",
        "第三章：尾聲\n\n故事未完，翻頁見分曉。"
    ]

screen book_page(pages, page=0):
    tag book
    modal True
    zorder 100

    frame:
        xalign 0.5
        yalign 0.5
        xsize 800
        ysize 600
        background Solid("#da5700")
        padding 20

        vbox:
            spacing 10

            # 主要文字區（用 xmaximum 限制寬度，避免跑出框外）
            text pages[page]:
                xmaximum 760
                xalign 0.0
                size 28
                color "#000"
                line_spacing 6

            null height 20

            # 分頁控制列
            hbox:
                xalign 0.5
                spacing 24

                # 上一頁：只有在 page > 0 時才顯示可按的按鈕
                if page > 0:
                    textbutton "上一頁" action SetScreenVariable("page", page-1)
                else:
                    # 顯示不可按的文字（可自訂顏色使其看起來 disabled）
                    text "上一頁" color "#888" xminimum 80

                # 動態頁碼
                text "第 [page+1] / [len(pages)] 頁"

                # 下一頁：非最後頁則翻下一頁；最後一頁則結束（Return）
                if page < len(pages)-1:
                    textbutton "下一頁" action SetScreenVariable("page", page+1)
                else:
                    textbutton "下一頁" action Return()

    # 鍵盤支援（並用 min/max 保險地 clamp 到合法範圍）
    key "K_RIGHT" action SetScreenVariable("page", min(page+1, len(pages)-1))
    key "K_LEFT"  action SetScreenVariable("page", max(page-1, 0))
    key "K_ESCAPE" action Return()

label book_scene:
    call screen book_page(book_pages)
    "你已離開書頁閱讀器。"
    return



    
