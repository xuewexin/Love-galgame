# ======================================
# Ren'Py 剧本：林砚线主线剧情（扩展版 — 好感度放大版）
# 说明：保留 define player = Character("[player_name]") 及你原始名字输入方式
# 注：已放大好感度变化区间并添加注释（# +X / -X 好感）
# ======================================

# init python:
#     # 安卓安全键盘 hack（8.4.1）
#     if renpy.android:
#         import android
#         def android_safe_input(prompt, length=32):
#             # 调用安卓安全键盘
#             # TYPE_CLASS_TEXT | TYPE_TEXT_VARIATION_PASSWORD = 129
#             android.set_text_type(129)
#             text = renpy.input(prompt, length=length)
#             android.set_text_type(1)  # 恢复普通键盘
#             return text

default lin_yan_affection = 0
default secret_affection = 0
default unlocked_memory = False

define player = Character("[player_name]")
define l = Character("林研", color="#e74c3c", image="linyan")

# -------------------
# 立绘
# -------------------
image linyan base = "images/character/linyan_base.png"
image linyan shy = "images/character/linyan_shy.png"
image linyan surprised = "images/character/linyan_surprised.png"
image linyan sad = "images/character/linyan_sad.png"
image linyan winter = "images/character/linyan_winter.png"
image linyan desperate = "images/character/linyan_desperate.png"

# -------------------
# 背景
# -------------------
image bg library = "images/scene/library.png"
image bg bookmarket = "images/scene/bookmarket.png"
image bg bookmarket_rain = "images/scene/bookmarket_rain.png"
image bg building = "images/scene/building_snow.png"
image bg cliff = "images/scene/cliff_snow.png"
image bg station = "images/scene/station_winter.png"
image bg foreign = "images/scene/foreign_town.png"
image bg back = "images/scene/Renp.png"

# -------------------
# 音效 / 背景音乐
# -------------------
define sound_rain = "sound/1.wav"
define sound_page_flip = "sound/2.mp3"
define sound_footsteps = "sound/3.wav"
define sound_paper_drop = "sound/4.wav"
define sound_heartbeat = "sound/5.wav"
define sound_bell = "sound/6.mp3"

define bgm_library = "sound/library_bgm.mp3"
define bgm_market = "sound/market_bgm.wav"
define bgm_snow = "sound/snow_bgm.mp3"
define bgm_tension = "sound/tension_bgm.mp3"
define bgm_soft = "sound/library_bgm.mp3"

# 放在 script 开头或 init 块
screen show_affection():
    text "好感度: [lin_yan_affection]" size 24 color "#231ac9" align (0.9, 0.05)

# ===============================
# 游戏入口（保留你原有的 player_name 输入写法）
# ===============================
label start:
    play music bgm_library fadein 1.0 loop
    show screen show_affection
    scene bg back with fade
    python:
        player_name = renpy.input("你的名字是什么？(默认：叶萧凡)", length=32)
        player_name = player_name.strip()
        if not player_name:
            player_name = "叶萧凡"
    scene black with fade
    jump chapter1

# ===============================
# 第一章：图书馆初遇与回忆（大幅扩展）
# ===============================
label chapter1:
    $ renpy.music.set_volume(0.8, channel="music")
    # 低语音效调至 80%，无过渡（立即生效）
    $ renpy.music.set_volume(1.2, channel="sound")
    play music bgm_library fadein 1.0 loop
    scene bg library with fade
    show linyan base at right with dissolve

    "[player_name]" "午后的图书馆，阳光透过百叶窗洒在书架上，空气里弥漫着纸墨香。"
    play sound sound_page_flip
    "[player_name]" "我注意到林砚蹲在文学区的角落，指尖轻触书页，神情专注，像是沉浸在自己的世界里。"

    "[player_name]" "(他每一次翻页的动作都仿佛有节奏，像是与周围世界隔绝，只剩下书与心。)"
    "[player_name]" "(我走近，发现他眼神专注，眉间微蹙，仿佛在思索书中的每一句话。)"
    "[player_name]" "(我轻轻吸了口气，试图靠近又怕打扰他……心跳不断加速。)"

    # 新增：环顾图书馆细节
    "[player_name]" "(图书馆里有人低声讨论着诗歌，有学生伏案写着论文，有人戴着耳机，像与世界隔离。)"
    "[player_name]" "(书架间有一道被阳光染成金色的缝隙，光线刚好落在他的发梢上。)"
    play sound sound_footsteps fadein 0.3

    # 延展对话与互动 — 增加内心、延长过程
    menu:
        "温和开口：你指尖沾到灰了，需要纸巾吗？":
            "[player_name]" "你指尖沾到灰了，需要纸巾吗？"
            show linyan surprised at right with dissolve
            l "！阿..谢谢你…你认识我？……"
            "[player_name]" "上周看到你抄川端康成的语录，我就记住了。"
            $ lin_yan_affection += 10   # +10 好感（主动关心，幅度放大）

            "[player_name]" "(他说话时声音低低的，带着一点点不自信的温柔。)"
            "[player_name]" "(我想把更多话说出口，却又怕声调破坏了这一刻的美好。)"

            menu:
                "递书给他，轻声邀请":
                    "[player_name]" "这本给你，我可以等新书。"
                    show linyan shy at right with dissolve
                    l "不，不用了……你真细心。"
                    $ lin_yan_affection += 15  # +15 好感（直接亲密动作）
                    "[player_name]" "下周去旧书市场吧，我想多了解你。"
                    l "好…好的。"
                    $ lin_yan_affection += 10  # +10 好感（约定下一次见面）
                    $ secret_affection += 2    # +2 隐藏好感（亲密触碰）
                    play sound sound_paper_drop

                    "[player_name]" "(我把书递过去时手微微颤抖，指尖碰到他的那一刻，仿佛有火花冒出。)"
                    "[player_name]" "(他看向我的眼神短促但真诚，像是一盏灯亮在深巷里。)"

                    # 增加短分支延展：一起找那本书的出处
                    menu:
                        "询问书的来历":
                            "[player_name]" "这书我在旧书摊上淘到的，封面很旧但字很干净。"
                            l "（仔细端详）我也喜欢这种旧书的味道。"
                            $ lin_yan_affection += 6   # +6 好感（共同话题）
                            "[player_name]" "(我们俩就这样聊起了书的来历，话题从作者延伸到各自的生活。)"
                        "把书放回书架":
                            "[player_name]" "我还是放回原位吧，给别人也留点惊喜。"
                            l "（略显惋惜）好吧，下次你要提醒我。"
                            $ lin_yan_affection += 0   # +0 好感（中性选择）

                "坦诚心意，略带挑逗":
                    "[player_name]" "其实我一直在看你，每次你认真看书的样子，都让我心痒难耐。"
                    show linyan shy at right with dissolve
                    l "（耳尖泛红，低头捏衣角）你…你说的是真的？"
                    $ lin_yan_affection += 18   # +18 好感（强烈挑逗）
                    $ secret_affection += 2     # +2 隐藏好感
                    "[player_name]" "我想靠近，感受你的呼吸。"
                    l "（微微咬唇，心跳加速）"
                    play sound sound_heartbeat

                    "[player_name]" "(空气中弥漫着微妙的紧张与甜蜜，让人难以呼吸。)"
                    "[player_name]" "(我想延长这一瞬间，但又害怕过于激烈让他退缩。)"

        "直接靠近，低声耳语":
            "[player_name]" "（走近他耳边，低声）你看书的样子真迷人。"
            show linyan surprised at right with dissolve
            l "（呼吸急促，轻轻后退）你…你说什么呢？"
            $ lin_yan_affection += 12   # +12 好感（大胆亲近）
            $ secret_affection += 3     # +3 隐藏好感（强烈亲密）

            "[player_name]" "(他的脸颊微微泛红，我的心也跟着暖了起来。)"
            "[player_name]" "(我知道这话有些冒失，但他的眼神里的惊讶又让我觉得值得。)"

    # 进一步延长：图书馆静默段落 + 暧昧细节
    "[player_name]" "(我们并肩走过一排排旧书，纸页的摩擦声像古老的节拍。)"
    "[player_name]" "(他偶尔抬头，眼里有着刚才谈话之后若有若无的期待。)"
    play sound sound_page_flip

    # 新增小事件：管理员提醒图书馆即将闭馆，延长相处时间
    "[player_name]" "(忽然，图书馆管理员用低沉的嗓音提醒闭馆时间。)"
    play sound sound_bell
    "[player_name]" "(我们知道要散场了，但仿佛被这种仪式感拉得更近。)"
    menu:
        "提出下次见面计划":
            "[player_name]" "今晚有读书会，下次一起去怎么样？"
            $ lin_yan_affection += 10   # +10 好感（主动约定）
            l "（眼睛闪亮）好啊，如果你愿意。"
            "[player_name]" "(我鼓起勇气留下了联系方式，也许这只是一个开始。)"
        "从容告别":
            "[player_name]" "那我先走了，回头见。"
            $ lin_yan_affection -= 3    # -3 好感（礼貌但冷淡）
            l "（轻声）回头见。"
            "[player_name]" "(离开时心里却盘算着如何再制造偶遇的机会。)"

    scene black with fade
    stop music fadeout 1.0
    jump chapter2

# ===============================
# 第二章：旧书市场与游玩喜悦（大幅扩展）
# ===============================
label chapter2:
    $ renpy.music.set_volume(1.2, channel="music")
    $ renpy.music.set_volume(1.2, channel="sound")
    play music bgm_market fadein 1.0 loop
    scene bg bookmarket with fade
    show linyan base at right with dissolve

    "[player_name]" "旧书市场藏在老巷深处，纸墨混合桂花香，空气温暖而湿润。"
    play sound sound_footsteps
    "[player_name]" "(摊主的笑声像陈年葡萄酒，带着甜味也带着点酸楚。)"
    "[player_name]" "(我与林砚并肩走着，偶尔手指轻触，心跳不断加速。)"

    # 扩展剧情：逛摊、讨价还价、共同寻找珍本
    "[player_name]" "(我们在摊位间停留，翻看装帧斑驳的书页。)"
    menu:
        "提议一起找一本特定的书":
            "[player_name]" "我记得有一本我们都喜欢的诗集，想一起找找看吗？"
            $ lin_yan_affection += 8    # +8 好感（主动提议共同寻找）
            l "（眼里有光）好啊，我们一起找。"
            "[player_name]" "(我们像小孩般在书堆里翻找，偶尔互相交换意见。)"
            play sound sound_page_flip

            # 小支线：找到书或错过
            menu:
                "找到了那本书":
                    "[player_name]" "就是这本！"
                    $ lin_yan_affection += 10  # +10 好感（共同找到，亲密感提升）
                    l "(他小心翼翼地翻开，仿佛在翻阅一段旧时光。)"
                "没找到，但交换了彼此收藏":
                    "[player_name]" "没找到，不过你愿意交换你喜欢的那本给我吗？"
                    $ lin_yan_affection += 6   # +6 好感（交换收藏，意愿亲近）
                    l "(羞涩地点头)好。"

        "听他讲书里的某个段落":
            l "（指着一段）这里写得很好，像是在说我们这样的某一刻。"
            "[player_name]" "(听他朗读时，声音像温暖的秋风拂过心湖。)"
            $ lin_yan_affection += 6    # +6 好感（被声音打动）

        "默默注视，享受当下":
            "[player_name]" "(我只是看着他，注意他的每个动作，像捕捉一个难得的画面。)"
            $ lin_yan_affection += 4    # +4 好感（静默观察，温柔）

    $ renpy.music.set_volume(0, channel="music")
    $ renpy.music.set_volume(2, channel="sound")
    # 突然下雨，雨中戏份延长（更多细节）
    scene bg bookmarket_rain with fade
    stop music fadeout 1.0
    play sound sound_rain fadein 1.0 loop
    "[player_name]" "雨突然落下，我将他护在伞下，肩膀微微相碰，气息交错."
    "[player_name]" "(伞下的世界像一个小小的岛屿，雨声将市声隔绝，只剩我们.)"

    menu:
        "递伞并靠近":
            "[player_name]" "(我把伞倾向他)这样雨不会打湿你。"
            $ lin_yan_affection += 15   # +15 好感（浪漫靠近）
            show linyan shy at right with dissolve
            l "（低声）谢谢你……你的手很暖。"
            play sound sound_heartbeat
            "[player_name]" "(他的手指无意触碰我的掌心，像是写下一个无声的誓言。)"
            $ secret_affection += 2     # +2 隐藏好感

            "[player_name]" "(我们在雨中慢慢走，脚步与雨声合成一首缓慢的歌。)"
            "[player_name]" "(他讲了小时候在雨中躲雨的事，我回忆起类似的傍晚，我们相视而笑.)"

        "牵手告白":
            "[player_name]" "(按住他的手，深情看着他)不管世俗怎么看，我都想和你在一起。"
            $ lin_yan_affection += 20   # +20 好感（重大亲密宣言）
            $ secret_affection += 3     # +3 隐藏好感（强烈）
            show linyan shy at right with dissolve
            l "（泪滑落，轻轻握紧）我也是…也是啊，[player_name]君。"
            play sound sound_heartbeat

        "沉默陪伴":
            "[player_name]" "(我不说话，只牵着伞，与他并肩走在潮湿的巷子。)"
            $ lin_yan_affection += 8    # +8 好感（温柔陪伴）
            "[player_name]" "(沉默像棉被，温柔地将我们包裹。)"

    # 小冲突 + 温柔化解（增加戏剧张力）
    "[player_name]" "(有人在旁边嘲讽，但我们选择忽视.)"
    menu:
        "回击":
            "[player_name]" "别理他们，我们知道什么是真实的。"
            $ lin_yan_affection += 6    # +6 好感（保护行为提升好感）
            l "（握紧你的手）你总是那么勇敢。"
            "[player_name]" "(我心里燃起一股保护欲，想把他护在身后。)"
        "离开":
            "[player_name]" "我们走吧，换个安静的地方。"
            $ lin_yan_affection += 2    # +2 好感（转移到安全的选择）
            l "（点头）好，我们走。"
            "[player_name]" "(我们离开了喧嚣，雨和书摊的香味伴着脚步渐远。)"

    stop sound fadeout 1.0
    stop music fadeout 1.0
    scene black with fade
    jump chapter3

# ===============================
# 第三章：冬日抉择与情感极限（大幅扩展）
# ===============================
label chapter3:
    $ renpy.music.set_volume(0.6, channel="music")
    $ renpy.music.set_volume(1.2, channel="sound")
    play music bgm_snow fadein 1.0 loop
    scene bg building with fade
    show linyan winter at right with dissolve

    "[player_name]" "初冬的雪如约而至，寒风中我们面临人生与爱情的抉择。"
    "[player_name]" "(雪花打在脸上，却比不上心中悸动的冷。)"
    l "家里的人说，如果我再和你联系，就不认我了……"
    "[player_name]" "(他的声音低沉，却让我感到一种深深的无助和脆弱。)"
    l "大家都在议论我们……[player_name]君，我们是不是错了？"
    "[player_name]" "错的不是我们，而是不理解爱情的人。"
    "[player_name]" "(我握紧拳头，决心要保护他，不让世俗左右我们的心。)"

    # 增加对话回合与家长来电支线
    menu:
        "坚定反抗舆论":
            "[player_name]" "我不在乎别人怎么说，我只在乎你。"
            $ lin_yan_affection += 20   # +20 好感（坚定保护）
            $ unlocked_memory = True
            l "（泪水滑落，却笑着紧握我的手）你…总让我安心。"
            play sound sound_heartbeat

            # 家人来电延展
            "[player_name]" "(这时他的手机震动，是家里的来电，我看见他一瞬的犹豫。)"
            menu:
                "建议接听并平静谈话":
                    "[player_name]" "你可以接，但我陪着你。"
                    l "（点头）好的。"
                    play music bgm_tension fadeout 0.5
                    $ lin_yan_affection += 8  # +8 好感（理智应对增加信任）
                    "[player_name]" "(通话中，你温柔地说明我们的关系，他母亲的语气虽然严厉，但有了迟疑。)"
                "建议先不接，先稳住情绪":
                    "[player_name]" "先别急着接，我们现在需要彼此。"
                    $ lin_yan_affection += 4  # +4 好感（情感依靠）
                    l "（靠在你肩上）谢谢你。"
                    "[player_name]" "(他的信任像灯光，照亮我胸中的黑暗.)"

        "温柔退让":
            "[player_name]" "别担心，我们慢慢来，我会陪你。"
            $ lin_yan_affection += 12   # +12 好感（耐心与承诺）
            l "（低头轻颤，心底松口气）"
            "[player_name]" "(我更愿意用时间和耐心去换得他的安全感，而非一时的冲突.)"

            # 规划未来支线
            "[player_name]" "(我们讨论是否要暂时低调，怎样安排未来的学习和见面，让彼此都有退路和希望。)"
            $ lin_yan_affection += 6    # +6 好感（共同规划带来安全感）

        "回避冲突":
            "[player_name]" "去别的地方吧，远离目光。"
            $ lin_yan_affection += 4    # +4 好感（保护但不对抗）
            l "（偷偷看我，内心波动）"
            "[player_name]" "(他微微颤抖的手让我不忍放手，决定带他走向更安静的巷道.)"

        "大胆表白，靠近唇边":
            "[player_name]" "不管世界怎么看，我只想和你贴近，感受你的呼吸。"
            $ lin_yan_affection += 25   # +25 好感（关键性重大表白）
            $ secret_affection += 3     # +3 隐藏好感（极强亲密）
            show linyan shy at right with dissolve
            l "（脸红心跳加速，轻轻咬唇）我也是…一直是。"
            play sound sound_heartbeat
            "[player_name]" "(他的心跳和我的交错，仿佛整个世界只剩下彼此.)"

    # 决策后延展：街角的争论、私语与承诺
    "[player_name]" "(我们在一个临时停靠的站台停下，白雪在灯下像散落的纸片.)"
    "[player_name]" "(我看着他，他看着我，我们都在沉默中寻找着力量.)"

    # 最后情绪铺垫（更多心理描写）
    "[player_name]" "(如果这是终局，我愿用一生来证明我们的选择是值得的.)"
    "[player_name]" "(如果这是开始，我想让每一天都值得铭记.)"

    # ===============================
    # 平衡后的结局判断（扩大区间）
    # ===============================
    if lin_yan_affection >= 110 or secret_affection >= 9:
        jump ending1   # 雪落殉情（极致爱情）
    elif lin_yan_affection >= 85:
        jump ending2   # 远走他乡（深厚情感）
    elif lin_yan_affection >= 60:
        jump ending3   # 离别亦或开始（理性与矛盾）
    elif lin_yan_affection >= 35:
        jump ending4   # 苦命鸳鸯（失衡的牵绊）
    else:
        jump ending5   # 移情别恋（冷漠或分离）

# ===============================
# 结局（优化为点击跳转）
# ===============================
label ending1:
    scene bg cliff with dissolve
    show linyan winter at right with dissolve
    "[player_name]" "雪花落在肩头，我们紧紧相拥，往日种种涌来。"
    l "我爱你，[player_name]君。"
    "[player_name]" "我也爱你，苦命鸳鸯。"
    stop music fadeout 2.0
    scene black with fade
    call screen final_text1
    $ renpy.pause(0.1, hard=True)  # 确保 screen 已显示
    scene black with fade
    jump end_scene

label ending2:
    scene bg foreign with dissolve
    show linyan base at right with dissolve
    "[player_name]" "在陌生的土地，我们仍能彼此温暖。"
    l "嗯，[player_name]君，我会一直陪你。"
    stop music fadeout 2.0
    scene black with fade
    call screen final_text2
    jump end_scene

label ending3:
    scene bg station with dissolve
    show linyan winter at right with dissolve
    "[player_name]" "暂时分开吧……至少我需要理清思绪。"
    l "往日种种…你真的舍得离开我吗？"
    stop music fadeout 2.0
    scene black with fade
    call screen final_text3
    jump end_scene

label ending4:
    scene bg station with dissolve
    show linyan sad at right with dissolve
    "[player_name]" "……也许我们不适合彼此。"
    l "风雪中的离别，成了心底永远的遗憾…"
    stop music fadeout 2.0
    scene black with fade
    call screen final_text4
    jump end_scene

label ending5:
    scene bg station with dissolve
    show linyan desperate at right with dissolve
    "[player_name]" "错过了太多机会……"
    l "往日种种……你真的不关心我了吗？"
    stop music fadeout 2.0
    scene black with fade
    call screen final_text5
    jump end_scene

# ===============================
# 终章
# ===============================
label end_scene:
    scene black with fade
    call screen over 
    return

screen over():
    text "故事终章：爱情本无错" size 30 color "#cccccc" align (0.5, 0.4)
    text "错的是不被理解的世俗，不过是对苦命鸳鸯罢了……" size 30 color "#cccccc" align (0.5, 0.5)
    text "愿天下有情人终成眷属" size 30 color "#cccccc" align (0.5, 0.6)
    text "游戏结束，感谢游玩~~~" size 30 color "#cccccc" align (0.5, 0.7)
    text "---作者：薛文欣" size 30 color "#cccccc" align (0.7, 0.8)
    key "mouseup_1" action Return()

# ===============================
# 结局显示 screen（修改为点击任意位置即可关闭并跳转）
# ===============================
screen final_text1():
    text "结局一：雪落殉情" size 40 color "#ffffff" align (0.5, 0.4)
    text "世俗的偏见如同坚冰，无法融化。" size 30 color "#cccccc" align (0.5, 0.5)
    text "你们选择用最决绝的方式，守护彼此的爱情，永远定格在雪落的瞬间。" size 30 color "#cccccc" align (0.5, 0.6)
    text "【点击继续】" size 28 color "#aaaaaa" align (0.5, 0.85)
    key "mouseup_1" action Return()

screen final_text2():
    text "结局二：远走他乡" size 40 color "#ffffff" align (0.5, 0.4)
    text "为了相守，你们选择逃离世俗的偏见。" size 30 color "#cccccc" align (0.5, 0.5)
    text "在陌生的土地上，没有家人的祝福，没有朋友的理解，却有彼此不离不弃的陪伴。" size 30 color "#cccccc" align (0.5, 0.6)
    text "【点击继续】" size 28 color "#aaaaaa" align (0.5, 0.85)
    key "mouseup_1" action Return()

screen final_text3():
    text "结局三：离别亦或开始" size 40 color "#ffffff" align (0.5, 0.4)
    text "是否是真正的离别？" size 30 color "#cccccc" align (0.5, 0.5)
    text "只要爱在，将来总会相见吧。" size 30 color "#cccccc" align (0.5, 0.6)
    text "【点击继续】" size 28 color "#aaaaaa" align (0.5, 0.85)
    key "mouseup_1" action Return()

screen final_text4():
    text "结局四：苦命鸳鸯" size 40 color "#ffffff" align (0.5, 0.4)
    text "世俗的压力太过沉重，你们终究向现实妥协。" size 30 color "#cccccc" align (0.5, 0.5)
    text "风雪中的离别，成了彼此心中永远的遗憾，只剩下无尽的思念与牵挂。" size 30 color "#cccccc" align (0.5, 0.6)
    text "【点击继续】" size 28 color "#aaaaaa" align (0.5, 0.85)
    key "mouseup_1" action Return()

screen final_text5():
    text "结局五：移情别恋" size 40 color "#ffffff" align (0.5, 0.4)
    text "做一个世俗所谓的正常人吗？" size 30 color "#cccccc" align (0.5, 0.5)
    text "那样还算是真正的爱吗？" size 30 color "#cccccc" align (0.5, 0.6)
    text "【点击继续】" size 28 color "#aaaaaa" align (0.5, 0.85)
    key "mouseup_1" action Return()
