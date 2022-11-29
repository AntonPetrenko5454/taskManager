from aiogram import types
from serviceController import ServiceController


def getServicesKeyboard():
    servicesKeyboard = types.InlineKeyboardMarkup(row_width=1)
    services = ServiceController.GetServices()
    for service in services:
        servicesKeyboard.add(types.InlineKeyboardButton(text=service[1],callback_data=f'service_{service[0]}'))
    return servicesKeyboard


