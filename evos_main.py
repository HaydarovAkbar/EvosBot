from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from mtelegrambotlar.EvosBot.e_main import *


def main():
    Token = "1714235167:AAEKKFGhj6KmzFfdXbXvcC9Aw44ef-RrlRg"
    updater = Updater(Token, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler("start", start)

    help_handler = CommandHandler("help", help)
    text_handler = MessageHandler(Filters.text, start_main)

    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(text_handler)
    dispatcher.add_handler(CallbackQueryHandler(inline_query))

    updater.start_polling()


main()
#



# # # Python
# # Fibonachchi sonlarini chiqarish  (O'zidan oldingi 2 ta hadini yig'indisiga teng bo'lgan sonlar!)
#
# n = int(input("Fibonachchi sonlar ketma-ketligining chegarasini kiriting: "))
# a, b = 1, 1             # a va b ketma-ketlikning boshlang'ich sonlari
# result = [a,b]          #
# if n > 1:
#     while True:
#         c = a + b
#         if n < c:
#             break
#         result.append(c)
#         a, b = b, c
#     print(result)
# else:
#     print("!")


a = 1
b = 2











