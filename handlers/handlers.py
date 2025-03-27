import os

from aiogram import types, Router, F
from aiogram.types import FSInputFile

from handlers.keyboards import kurslarimiz, start_buttons

router = Router()


asilbek = FSInputFile(os.path.join(os.path.dirname(__file__), "images", 'img_2.png'))
shohruh = FSInputFile(os.path.join(os.path.dirname(__file__), "images", 'img_8.png'))
habibulloh = FSInputFile(os.path.join(os.path.dirname(__file__), "images",   'img_7.png'))

mentorlar = [
    [asilbek, "Asilbek Mamadaliyev"],
    [shohruh, "Shohruh Abdurahmonov"],
    [habibulloh, "Habibulloh Nuriddinov"],
]



@router.message(F.text == "Kompaniya haqida")
async def kompaniya_haqida(message: types.Message):
    image = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img.png"))
    text = "8 yillik tajriba, 2000 mingdan ortiq o'quvchilar va tajribali mantorlar ega"
    await message.answer_photo(caption=text, photo=image)

@router.message(F.text == "Kontraktlar/Manzil")
async def kontraktlar_manzil(message: types.Message):
    image = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_3.png"))
    text = ("📞 -> +998 777 74 77"
            "📍 -> Toshkent shahri, Shayhontohur tum,"
            "Chorsu, Xadra, Zarqaynar 3-uy")
    await message.answer_photo(caption=text, photo=image)

@router.message(F.text == "Bizning Mentorlar")
async def mentorlara_btn(message: types.Message):
    for mentor in mentorlar:
        await message.answer_photo(photo=mentor[0], caption=mentor[1])

@router.message(F.text == "Kurslarimiz")
async def kurslarimiz_btn(message: types.Message):
    await message.answer(text="Bizning kuslarimiz", reply_markup=kurslarimiz)

@router.message(F.text == "Python Junior")
async def python(message: types.Message):
    image = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_6.png"))
    text = ("Python - Mantiqiy fikrlash va dasturlash asoslari")
    await message.answer_photo(caption=text, photo=image)

@router.message(F.text == "Frontend Junior")
async def python(message: types.Message):
    image = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_9.png"))
    text = ("Frondent - bu veb-ishlanmalarni yaratishda"
            " foydalanuvchi ko'radigan va o'zaro aloqada bo'ladigan qismini ifodalaydi.")
    await message.answer_photo(caption=text, photo=image)

@router.message(F.text == "Robototexnika")
async def python(message: types.Message):
    image = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_5.png"))
    text = ("Robototexnika — bu robotlar va avtomatlashtirilgan tizimlarni"
            "yaratish, ishlab chiqish va qo‘llash bilan shug‘ullanuvchi fan va texnologiyalar majmuasidir..")
    await message.answer_photo(caption=text, photo=image)

@router.message(F.text == "Scratch")
async def python(message: types.Message):
    image = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_4.png"))
    text = ("Scratch — bu bolalar va yosh dasturchilar uchun mo'ljallangan"
            " vizual dasturlash tili va platformasidir..")
    await message.answer_photo(caption=text, photo=image)

@router.message(F.text == "🔙Ortga")
async def python(message: types.Message):
    await message.answer("Siz ortga qaytdingiz", reply_markup=start_buttons)

@router.message(F.text == "Kontaktlar/Manzil")
async def get_contact(msg: types.Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_3.png"))
    text = "Bu yerda siz manzil tanlab olishingiz mumkin"
    await msg.answer_photo(photo=img, caption=text)
