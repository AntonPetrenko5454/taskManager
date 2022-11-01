from aiogram import types, Dispatcher


'''

def registerHandlersBotInfo(dp: Dispatcher):
    dp.register_callback_query_handler(userInfoButtonClick, lambda call: call.data == 'userInfoButton_click', state='*')
    dp.register_callback_query_handler(historyTaskButtonClick, lambda call: call.data == 'historyTaskButton_click', state='*')
    dp.register_callback_query_handler(userInfoButtonClick, lambda call: call.data == 'userInfoButton_click', state='*')
    dp.register_callback_query_handler(backUserInfoButtonClick, lambda call: call.data == 'backUserInfoButton_click', state='*')


@dp.callback_query_handler(text='botInfoButton_click')
async def botInfoButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Тут вы можете прочитать информацию о боте или оставить пожелание/отзыв',
                                 reply_markup=botInfoKeyboard)
    await call.answer()


@dp.callback_query_handler(text='writeWishBotButton_click')
async def botWriteWishButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Тут вы можете написать пожелания, которые вы хотели бы видеть в нашем боте',
                                 reply_markup=botInfoWishKeyboard)
    await call.answer()


@dp.callback_query_handler(text='seeReviewBotButton_click')
async def botSeeReviewButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Отзывы: \n', reply_markup=botInfoReviewWriteKeyboard)
    await call.answer()


@dp.callback_query_handler(text='writeReviewBotButton_click')
async def botWriteReviewButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Тут вы можете оставить отзыв об функциональности бота ',
                                 reply_markup=botInfoReviewWriteKeyboard)
    await call.answer()


@dp.callback_query_handler(text='backBotInfoButton_click')
async def backBotInfoButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Тут вы можете прочитать информацию о боте или оставить пожелание/отзыв',
                                 reply_markup=botInfoKeyboard)
    await call.answer()

'''