from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from controllers.service_controller import ServiceController


def getServicesKeyboard(callback,parent=0):
    servicesKeyboard = InlineKeyboardBuilder()
    services = ServiceController.GetServices(parent)
    if len(services) == 0:
        return None
    for service in services:
        servicesKeyboard.row(types.InlineKeyboardButton(text=service[1], callback_data=f'{callback}_service_{service[0]}'))

    if parent != 0:
        servicesKeyboard.row(types.InlineKeyboardButton(text=service[1], callback_data=f'{callback}_service'))
        servicesKeyboard.row(types.InlineKeyboardButton(text='Назад', callback_data=f'{callback}_service_{ServiceController.GetServiceParent(parent)}'))
    return servicesKeyboard.as_markup()
