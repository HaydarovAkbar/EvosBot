from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from mtelegrambotlar.EvosBot.evos_postgras import EvosPostgras

evo = EvosPostgras().selectCategory()

keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton("🍔" + evo[0][1] + "🌯", callback_data="zakas1"),
     InlineKeyboardButton("🍵" + evo[1][1] + "☕️", callback_data="zakas2")],
    [InlineKeyboardButton("🍹" + evo[2][1] + "🧉", callback_data="zakas3"),
     InlineKeyboardButton("🍕" + evo[3][1] + "🥮", callback_data="zakas4")],
    [InlineKeyboardButton("🍰" + evo[4][1] + "🎂", callback_data="zakas5"),
     InlineKeyboardButton("Orqaga🚫🚫", callback_data="zakas6")]
])

avo = EvosPostgras().selectProduct(3)
bao = EvosPostgras().selectProduct(1)
chao = EvosPostgras().selectProduct(2)
bach = EvosPostgras().selectProduct(4)
chaa = EvosPostgras().selectProduct(5)

batton3 = InlineKeyboardMarkup([
    [InlineKeyboardButton("🍹 " + avo[0][1] + "  " + str(avo[0][2]) + " so'm", callback_data="task1")],
    [InlineKeyboardButton("🍷 " + avo[1][1] + "  " + str(avo[1][2]) + " so'm", callback_data="task2")],
    [InlineKeyboardButton("🧉 " + avo[2][1] + "  " + str(avo[2][2]) + " so'm", callback_data="task3")],
    [InlineKeyboardButton("🍹🚫 Oqraga", callback_data="ras")]
])

batton2 = InlineKeyboardMarkup([
    [InlineKeyboardButton("☕️ " + chao[0][1] + " " + str(chao[0][2]) + "so'm", callback_data="rask1")],
    [InlineKeyboardButton("🍵 " + chao[1][1] + " " + str(chao[1][2]) + "so'm", callback_data="rask2")],
    [InlineKeyboardButton("☕️🍵 " + chao[2][1] + " " + str(chao[2][2]) + "so'm", callback_data="rask3")],
    [InlineKeyboardButton("☕🚫 Orqaga", callback_data="ras")]
])

batton1 = InlineKeyboardMarkup([
    [InlineKeyboardButton("🍔  " + bao[0][1] + "  " + str(bao[0][2]) + " so'm", callback_data="taskk1")],
    [InlineKeyboardButton("🌮  " + bao[1][1] + "  " + str(bao[1][2]) + " so'm", callback_data="taskk2")],
    [InlineKeyboardButton("🥪  " + bao[2][1] + "  " + str(bao[2][2]) + " so'm", callback_data="taskk3")],
    [InlineKeyboardButton("🌭  " + bao[3][1] + "  " + str(bao[3][2]) + " so'm", callback_data="taskk4")],
    [InlineKeyboardButton("🍔  " + bao[4][1] + "  " + str(bao[4][2]) + " so'm", callback_data="taskk5")],
    [InlineKeyboardButton("🌮  " + bao[5][1] + "  " + str(bao[5][2]) + " so'm", callback_data="taskk6")],
    [InlineKeyboardButton("🥪  " + bao[6][1] + "  " + str(bao[6][2]) + " so'm", callback_data="taskk7")],
    [InlineKeyboardButton("🌭  " + bao[7][1] + "  " + str(bao[7][2]) + " so'm", callback_data="taskk8")],
    [InlineKeyboardButton("🍔  " + bao[8][1] + "  " + str(bao[8][2]) + " so'm", callback_data="taskk9")],
    [InlineKeyboardButton("🌮  " + bao[9][1] + "  " + str(bao[9][2]) + " so'm", callback_data="taskk10")],
    [InlineKeyboardButton("🥪  " + bao[10][1] + "  " + str(bao[10][2]) + " so'm", callback_data="taskk11")],
    [InlineKeyboardButton("🌭  " + bao[11][1] + "  " + str(bao[11][2]) + " so'm", callback_data="taskk12")],
    [InlineKeyboardButton("🍔🚫 Oqraga", callback_data="ras")],
])
batton4 = InlineKeyboardMarkup([
    [InlineKeyboardButton("🍕 " + bach[0][1] + "  " + str(bach[0][2]) + "so'm", callback_data="raskk1")],
    [InlineKeyboardButton("🍕 " + bach[1][1] + "  " + str(bach[1][2]) + "so'm", callback_data="raskk2")],
    [InlineKeyboardButton("🍕🚫 Orqaga", callback_data="ras")]
])
batton5 = InlineKeyboardMarkup([
    [InlineKeyboardButton("🎂 " + chaa[0][1] + "  " + str(chaa[0][2]) + "so'm", callback_data="ras1")],
    [InlineKeyboardButton("🍰 " + chaa[1][1] + "  " + str(chaa[1][2]) + "so'm", callback_data="ras2")],
    [InlineKeyboardButton("🍮 " + chaa[2][1] + "  " + str(chaa[2][2]) + "so'm", callback_data="ras3")],
    [InlineKeyboardButton("🎂🍰🍮 🚫 Orqaga", callback_data="ras")]
])
battont = ReplyKeyboardMarkup([["🇺🇿 Tilni o'zgartirish 🇺🇿"],
                              ["🇷🇺 Пeрeвод на русский язик 🇷🇺"],
    ["🚫Orqaga🚫"]
], resize_keyboard=True)
batton = ReplyKeyboardMarkup([
                               ["🚫Orqaga🚫"]
                               ], resize_keyboard=True)

start_key = ReplyKeyboardMarkup([
    ["🚗 Evos Zakas 🛒"],
    ["🛒 Buyurtmalarim 🛍", "✍️Fikr bildirish  📝"],
    ["⚙️Sozlamalar "]
], resize_keyboard=True)

datas = {
    "task1": "Coco-Cola",
    "task2": "Fanta",
    "task3": "Pepsi",
    "rask1": "qora choy",
    "rask2": "limon choy",
    "rask3": "student choy",
    "taskk1": "bonus lavash",
    "taskk2": "lavash",
    "taskk3": "xogi",
    "taskk4": "Big xogi",
    "taskk5": "Big gamburger",
    "taskk6": "cheeseburger",
    "taskk7": "Xotdog",
    "taskk8": "Big Xotdog",
    "taskk9": "Big lavash",
    "taskk10": "student lavash",
    "taskk11": "student gamburger",
    "taskk12": "salat",
    "raskk1": "pizza",
    "raskk2": "gushtli pizza",
    "ras1": "pirojni",
    "ras2": "shokoladli pirojni",
    "ras3": "Big perojni",
}
liss = ["task1", "task2", "task3","task4", "rask1", "rask2",
        "rask3","rask4", "raskk2","raskk3", "taskk1", "taskk2", "taskk3",
        "taskk4", "taskk5", "taskk6", "taskk7", "taskk8",
        "taskk9", "taskk10", "taskk11", "taskk12","taskk13", "raskk1",
        "raskk2","raskk3", "ras1", "ras2", "ras3","ras"]

suzlar = ["akbar", "Akbar", "Zur", "zur", "yaxshi","gap yo","👍","😂","zo'r","Zo'r"]

yomon = ["zaybal", "zzz", "kim bu", "nima", "jinni", "ee", "jala", "dalba", "uchr", "xuy","axmoq","🖕","Zaybal","Zzz","Ee","Jinni","Axmoq"]

yaxshi = ["Sizga faxxriyy yorliq beramiz!😂", "Bilimdonmisiz deyman😏","O'ylab ko'radigan masala buu"
          "shuni qayerdadir eshitgandayman", "Ha man ushaman😁", "Tanimayman!😝","Rahmat😎","🤠Sizga bitta lavash sovg'a mani hisobimdan🤝"]

gaplar = ["Eee asabimga tegma🥴", "😡🤬San uzi kimsan tushinmadim",
          "Asabimga tegurse hoz uchasan🚀", "ee avval yozishni o'rgan xop😹",
          "sanga gapirganni foydasi yo😏👊", "👊Bo'ldi qilasanmi yommi!","😈Hoz telfoninga buzib kirib mazeni qochiraman🤡"]



# # Python
# # n gacha bo'lgan tub sonlarni chiqarishni Filter methodi bilan ishlashni ko'ramiz
#
# n = 145
# # Funksiyaga malum bir son keladi uni bo'luvchilar sonini topamiz
# def tubSon(number):                # number = 12
#     count = 0
#     for i in range(1,number+1):    # 1 dan 13 gacha sonlarni qaytaradi 13 kirmaydi!
#         if number % i == 0:        # 12 ni oraliqdagi har bir songa bo'lib ko'ramiz
#             count += 1             # buluvchilarni sanab boramiz
#     if count == 2:                 # Agar buluvchilar soni 2 ga teng bulsa damak tub son
#         return True                # Tub son bulsa True qiymat qaytar deymiz
#
# # (range(2,12) 2 dan 11 gacha sonlarni tuplam kurinishida ifodalaydi)
# # Filter methodi 2 va 11 oraligidan har bir sonni tubSon funksiyasida tekshiradi
#
# tub_sonlar = list(filter(tubSon, range(2,n)))    # Agar True bulsa sonni qaytaradi
# print(tub_sonlar)
















