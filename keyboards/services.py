from aiogram import types
from controllers.serviceController import ServiceController


def getServicesKeyboard(parent=0):
    servicesKeyboard = types.InlineKeyboardMarkup(row_width=1)
    services = ServiceController.GetServices(parent)
    if len(services) == 0:
        return None
    for service in services:
        servicesKeyboard.add(types.InlineKeyboardButton(text=service[1],callback_data=f'service_{service[0]}'))
    if parent != 0:
        servicesKeyboard.add(types.InlineKeyboardButton(text='Назад', callback_data=f'service_{ServiceController.GetServiceParent(parent)}'))
    return servicesKeyboard

