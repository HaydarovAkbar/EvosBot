import datetime
from mtelegrambotlar.EvosBot.evosBattons import *
from mtelegrambotlar.EvosBot.evos_postgras import EvosPostgras
import random

# --------------------------
bott = """Bu bot orqali siz tez va oson tanavvul  qilishingiz yoki Bot haqida malumotlarga ega bo'lishingiz mumkin!\n
        🚗Yetkazib berish: Yetkazib berish bizning hisobimizdan(Shahar ichida) Faqatgina belgilangan miqdorda savdo qilgan mijozlar uchun!!!😏\n
        🎁Chegirma :Doimiy mijozlarimizga va hurmatli mehmonlarga chegirmalar bor\n
        👨‍💻Dasturchi :@Akbar_TUIT,Kelishilgan narxlarda sizni ham shunaqa BOTingiz bo'lishi mumkin!"""
# --------------------------

datee = datetime.datetime.now()
date = datee.strftime("%Y/%m/%d %H:%M")


def inline_quers(update, context):
    try:
        query = update.callback_query
        if query.data == "ras":
            return zakas(update, context)
        evos = EvosPostgras()
        a = update.effective_chat.id
        vs = datas.get(query.data, query.data)
        evos.insertBuylist(a, vs, date, 1)
        query.edit_message_text(text="eeee hazillashdim 😆\n"
                                     "Xafa bo'lish yuq!")
    except Exception as e:
        return e

def inline_query(update, context):
    try:
        query = update.callback_query
        if query.data == "zakas3":
            query.edit_message_text(text=f"<b>Quyidagi</b> kategoriyalardan birini tanlang👇", parse_mode="HTML",
                                    reply_markup=batton3)
        if query.data == "zakas1":
            query.edit_message_text(text=f"<b>Quyidagi</b> kategoriyalardan birini tanlang👇", parse_mode="HTML",
                                    reply_markup=batton1)
        if query.data == "zakas2":
            query.edit_message_text(text=f"<b>Quyidagi</b> kategoriyalardan birini tanlang👇", parse_mode="HTML",
                                    reply_markup=batton2)
        if query.data == "zakas4":
            query.edit_message_text(text=f"<b>Quyidagi</b> kategoriyalardan birini tanlang👇", parse_mode="HTML",
                                    reply_markup=batton4)
        if query.data == "zakas5":
            query.edit_message_text(text=f"<b>Quyidagi</b> kategoriyalardan birini tanlang👇", parse_mode="HTML",
                                    reply_markup=batton5)
        if query.data == "zakas6":
            query.edit_message_text(text=f"!")
            return yanaa(update, context)
        if query.data in liss:
            return inline_quers(update, context)
    except Exception as e:
        return e

def bot_date(update, context):
    keyboard = ReplyKeyboardMarkup([
        ["Orqaga🚫"]
    ], resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"Botni ishga tushirilgan vaqti 🕒👇 \n\n📅 <b> yil/oy/kun soat </b>: {date}",
                             parse_mode="HTML", reply_markup=keyboard)


def bot_haqida(update, context):
    keyboard = ReplyKeyboardMarkup([
        ["Orqaga🚫"]
    ], resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id, text=bott, reply_markup=keyboard)


def start(update, context):
    user = update.message.from_user.first_name

    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Assalomu alaykum <b> {user} </b> \n"
                                                                    f"<b>Akbar</b>ni botiga xush kelibsiz😁\n"
                                                                    f"Bot haqida yoki biror yordam kerak bo'lsa"
                                                                    f" /help ni bosing!", parse_mode="HTML",
                             reply_markup=start_key)


def yanaa(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"<b>Quyidagi</b> kategoriyalardan birini tanlang👇", parse_mode="HTML",
                             reply_markup=start_key)


def help(update, context):
    keyboard = ReplyKeyboardMarkup([
        ["🤖 Bot haqida 🤖"],
        ["📅 Ishga tushirilgan vaqt 🕒", "🛒 Buyurtmaga o'tish"],
        ["💬 Bot haqida Fikr 📥"]
    ], resize_keyboard=True)

    context.bot.send_message(chat_id=update.effective_chat.id, text=f"👇 Quyidagilardan birini tanlang 👇\n",
                             reply_markup=keyboard)


def bot_haqida_fikr(update, context):
    user = update.message.from_user.first_name
    keyboard = ReplyKeyboardMarkup([
        ["Orqaga🚫"]
    ], resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"<b> {user} </b> Agar biror bir kamchilik yoki takliflaringiz"
                                  f" bo'lsa qoldirishingiz mumkin, Biz buni albatta ko'rib "
                                  f"chiqamiz", parse_mode="HTML", reply_markup=keyboard)


def rahmat(update, context):
    keyboard = ReplyKeyboardMarkup([
        ["🤖 Bot haqida 🤖"],
        ["📅 Ishga tushirilgan vaqt 🕒"],
        ["💬 Bot haqida Fikr 📥"]
    ], resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id, text="fikringiz uchun rahmat", reply_markup=keyboard)


def til_uzgartirish(update, context):
    text = update.message.text
    if text == "🇺🇿 Tilni o'zgartirish 🇺🇿":
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="O'zbek tilida turiptiku, nimasini o'zgartimoqchisiz!🤦‍")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Hozircha Rus tilini bilmayman😔,yaqinda qo'shiladi bu ham😊")


def takrorla(update, context):
    try:
        user = update.message.from_user
        text = update.message.text
        if text in "🇺🇿 Tilni o'zgartirish 🇺🇿 🇷🇺 Пeрeвод на русский язик 🇷🇺":
            return til_uzgartirish(update, context)
        elif "salom" in text:
            gaplar_suz = "Shu serSalom odamlani yoqtirmaymanda😤"
            context.bot.send_message(chat_id=update.effective_chat.id, text=f"<b>{user.first_name}</b> {gaplar_suz}",
                                     parse_mode="HTML")
        elif text.lower() == "tushinmadim" or text == "?" or text.lower() == "nimaga":
            gaplar_suz = "nime tushinmesa😬"
            context.bot.send_message(chat_id=update.effective_chat.id, text=f"<b>{user.first_name}</b> {gaplar_suz}",
                                     parse_mode="HTML")
        elif text in suzlar:
            yaxshi_suz = random.choices(yaxshi)[0]
            context.bot.send_message(chat_id=update.effective_chat.id, text=f"<b>{user.first_name}</b> {yaxshi_suz}",
                                     parse_mode="HTML")
        elif text in yomon:
            gaplar_suz = random.choices(gaplar)[0]
            context.bot.send_message(chat_id=update.effective_chat.id, text=f"<b>{user.first_name}</b> {gaplar_suz}",
                                     parse_mode="HTML")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text=f"<b>{update.message.text}</b>",
                                     parse_mode="HTML")
            context.bot.send_message(chat_id=758934089,
                                     text=f"{user.first_name}:@{user.username} foydalanuvchi sizga quyidagi xabarni qoldirdi \n📝{update.message.text}")
    except Exception as e:
        return

a = 1


def zakas(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('D:\Zako_New_project\yangi_New\mtelegrambotlar\EvosBot\EVOS Hammasi.jpg', "rb"),
                           reply_markup=batton)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"👇<b>Quyidagi</b> Categroyalardan birini tanlang😋!",
                             parse_mode="HTML", reply_markup=keyboard)


def buyurtma(update, context):
    b = update.effective_chat.id
    evoss = EvosPostgras().selectbuy(b)
    buyurtmalar = ""
    if evoss:
        for i in evoss:
            buyurtmalar += "(" + i[1] + " " + i[2] + "),  \n"
    else:
        buyurtmalar = "Siz haligacha bizdan savdo qilmabsiz NIMAGA???🤨"
    user = update.message.from_user.first_name
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f" <b>{user}</b> 🛍🛒sizni buyurtmalaringiz:📋\n\n {buyurtmalar}", parse_mode="HTML",
                             reply_markup=batton)


def evosFikr(update, context):
    user = update.message.from_user.first_name
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"<b>{user}</b>! Sizni fikringiz biz "
                                                                    f"\nuchun unchalik muhim emas!!!",
                             parse_mode="HTML", reply_markup=batton)


def sozlamalar(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"👇Quyidagilardan birini tanlang👇!\nTanlamasangiz ham mayli 😂",
                             parse_mode="HTML", reply_markup=battont)


def start_main(update, context):
    try:
        text = update.message.text
        if text in ["🚗 Evos Zakas 🛒", "🛒 Buyurtmalarim 🛍", "✍️Fikr bildirish  📝", "⚙️Sozlamalar"]:
            if text == "🚗 Evos Zakas 🛒":
                return zakas(update, context)
            if text == "🛒 Buyurtmalarim 🛍":
                return buyurtma(update, context)
            if text == "✍️Fikr bildirish  📝":
                return evosFikr(update, context)
            if text == "⚙️Sozlamalar":
                return sozlamalar(update, context)
        else:
            if text == "🛒 Buyurtmaga o'tish":
                return start(update, context)
            if text == "zakas1":
                return rahmat(update, context)
            if text == "🤖 Bot haqida 🤖":
                return bot_haqida(update, context)
            if text == "📅 Ishga tushirilgan vaqt 🕒":
                return bot_date(update, context)
            if text == "💬 Bot haqida Fikr 📥":
                return bot_haqida_fikr(update, context)
            if text == "Orqaga🚫":
                return help(update, context)
            if text == "🚫Orqaga🚫":
                user = update.message.from_user.first_name
                context.bot.send_message(chat_id=update.effective_chat.id, text=f"<b> {user} </b>! \n"
                                                                                f"<b>Akbar</b>ni botiga xush kelibsiz😁\n"
                                                                                f"Bot haqida yoki biror yordam kerak bo'lsa"
                                                                                f" /help ni bosing!", parse_mode="HTML",
                                         reply_markup=start_key)
            else:
                return takrorla(update, context)
    except Exception as e:
        return