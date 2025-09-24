define bk = Character("書上的文字")

label survive:
    q "決定要在教室度過這個夜晚了，有種不安的感覺"

    q "總之先看看這本筆記吧"

    jump readcover


label readcover:
menu:
    q "......"
    "封面":
        q "上面貼著一張便條"
        bk "如果你沒有在本教室過夜的打算，請不要翻開此書，假設你打開了，請無論如何都要待到隔天早晨才能離開"
        jump readcover
    "鎖":
        q "這鎖還蠻牢固的，旁邊有一把鑰匙，要打開嗎？"
        menu:
            "打開":
                "(鎖打開了)"
                q "有股不安感......"
                jump readcoverover
            "還是等等吧":
                jump readcover
                

label readcoverover:
    q "書被打開了，霍，還挺多條目的"
    menu:
        "扉頁":
            bk "挖喔，我得鼓勵一下有勇氣的你，但是在情緒價值前提醒一下，請立刻去把門和燈都給關上喔"
            bk ""
        "電腦病毒"
        "ENTER"
