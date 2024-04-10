import app.keyboards as kb


from aiogram.utils import markdown
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart


from app.database.requests import set_user
from app.database.requests import get_item_by_id



router = Router()



@router.message(CommandStart())
@router.callback_query(F.data == 'to_main')
async def cmd_start(message: Message | CallbackQuery):
    url = ''
    if isinstance(message, Message):
        await message.delete()
        await set_user(message.from_user.id)
        await message.answer(f'{markdown.hide_link(url)}Добро пожаловать в <b>SHOP MORTALA</b>\n\n<b>У нас самые доступные цены</b>\n<b>И множество игр на выбор</b>\n\n<b>Нажимай и покупай</b>',
                         reply_markup=kb.main)
    else:
        await message.message.answer(f'{markdown.hide_link(url)}Добро пожаловать в <b>SHOP MORTALA</b>\n<b>У нас самые доступные цены</b>\n<b>И множество игр на выбор</b>',
                                        reply_markup=kb.main)






@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'id: {message.photo[-1].file_id}')

@router.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
    await callback.message.edit_text(f'︎Выбери игру из списка, <b>{callback.from_user.full_name}</b>︎︎︎',
    reply_markup=await kb.categories())



@router.callback_query(F.data.startswith('category_'))
async def category(callback: CallbackQuery):
    await callback.answer('Вы выбрали')
    await callback.message.edit_text(text='︎👇<b>Выберите товар</b>︎👇',
                                  reply_markup=await kb.items(callback.data.split('_')[1]))


# @router.callback_query(F.data.startswith('item_'))
# async def category(callback: CallbackQuery):
#     item = await get_item_by_id(callback.data.split('_')[1])
#     await callback.answer('🔥Вы выбрали🔥')
#     await callback.message.answer_photo(photo=item.photo, caption=f'{item.name}\n{item.price}\n\n{item.description}',
#     reply_markup=kb.to_main)


@router.callback_query(F.data.startswith('item_'))
async def category(callback: CallbackQuery):
    item = await get_item_by_id(callback.data.split('_')[1])
    await callback.answer('')
    await callback.message.answer_photo(photo=item.photo, caption=f'<b>{item.name}</b>\nЦена: 💲<b>{item.description}</b>💲\n\nДля оплаты отправьте артикул владельцу: @zxc11095\nАртикул: <b>{item.price}</b>',
                                     reply_markup=kb.to_main)



# @router.callback_query(F.data == 'vladelec')
# async def vladelec(callback: CallbackQuery):
#     await callback.answer('')
#     await callback.message.edit_text(
#         f'︎<b>У нас в магазине только один владелец</b>\n\n<b>По рекламе, сотрудничеству к нему</b>\n\n@zxc11095',
#                                   reply_markup=kb.to_main)


@router.callback_query(F.data.startswith('vladelec'))
async def vladelec(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(text=f'︎<b>У нас в магазине только один владелец</b>'
                                       f'\n\n<b>По рекламе, сотрудничеству к нему</b>\n\n->->->@zxc11095',
                                  reply_markup=kb.to_main)



@router.callback_query(F.data == 'otz')
async def otz(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('<b>Отзывы здесь:</b>\n\n@OtzivyIMMORTAL',
                                  reply_markup=kb.to_main)

@router.message(F.text)
async def tetx(message: Message):
    await message.answer(f'Добро пожаловать в <b>SHOP MORTALA</b>',
                         reply_markup=kb.main)




