import os
import logging
import random
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes
from abjad import *

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_markup = InlineKeyboardMarkup(thekeyboard())
	await update.message.reply_text(text =f"Merhaba **{message.from_user.first_name }** \n\n"
	"__Ben bir ebced hesaplama botuyum, farklı ebced tablolarına dayanan\n"
	"hesaplar yapabiliyorum. Sahur Özel'in Ebced Hesaplayan Makrolarını\n"
	"kullanırım. Kullandığım makrolar LibreOffice Calc, Microsoft Excel,\n"
	"Google E-tablolar ve Web uygulamalarınızda web tarayıcınızda da\n"
	"kullanılabilir. [github.com/metatronslove/abjad](https://github.com/metatronslove/abjad) adresinden\n"
	"VBA, Python, JS, Google Apps Script kodu örnekleri indirilebilir.\n"
	"Makro örnekleri, ebced tablolarını ayrıntılı açıklayan kodlardır.\n"
	"Yeterince ekran klavye uygulaması geliştirildiği için ebced hesabı\n"
	"yaptığını idda eden Arapça ekran klavye uygulamalarından değildir.__\n"
	, reply_to_message_id = message.message_id 
	, parse_mode="markdown"
	, "Ne yapmak istiyorsunuz ?"
	, reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    fqdata = float(query.data)
    if fqdata in [21, 60, 93, 111, 115, 119]: start()
    elif fqdata in [1, 2]:
		reply_markup = InlineKeyboardMarkup(ebced(fqdata))
		await query.edit_message_text(text =f"Sayın **{message.from_user.first_name }** \n\n"
		"__Ebced hesaplarken, Arapça için mağribi ve frekans dahil tüm\n"
		"tablolara göre hesap yaptırabilirsiniz Türkçe ve İbranice için\n"
		"sadece ebced tablolarını seçebilirsiniz.__"
		, reply_to_message_id = message.message_id
		, parse_mode="markdown"
		, "/nLütfen tablo seçin:"
		, reply_markup=reply_markup)
	elif fqdata in range(8, 20):
		reply_markup = InlineKeyboardMarkup(shadda(fqdata))
		await query.edit_message_text(text =f"Sayın **{message.from_user.first_name }** \n\n"
		"__Şeddeyle yazılan harfleri tek ya da çift hesaplatabilirsiniz.\n"
		"Girilen metin şedde içermiyorsa seçiminiz sonucu değiştirmez.__"
		, reply_to_message_id = message.message_id
		, parse_mode="markdown"
		, "/nTek veya çift hesaplamayı seçin:"
		, reply_markup=reply_markup)
	elif fqdata in range(22, 34):
	elif fqdata in range(34, 46):		
	elif fqdata in range(47, 59):
		reply_markup = InlineKeyboardMarkup(shadda(fqdata))
		await query.edit_message_text(text =f"Sayın **{message.from_user.first_name }** \n\n"
		"__Şeddeyle yazılan harfleri tek ya da çift hesaplatabilirsiniz.\n"
		"Girilen metin şedde içermiyorsa seçiminiz sonucu değiştirmez.__"
		, reply_to_message_id = message.message_id
		, parse_mode="markdown"
		, "/nTek veya çift hesaplamayı seçin:"
		, reply_markup=reply_markup)
	elif fqdata in range(61, 73):
	elif fqdata in range(73, 85):
	elif fqdata == 3:
		reply_markup = InlineKeyboardMarkup(nature(fqdata))
		await query.edit_message_text(text =f"Sayın **{message.from_user.first_name }** \n\n"
		"__Arapça için farklı islamî okült ustaları harflerin tabiatları\n"
		"için farklı sınıflandırmalar kullanmışlar. Kayda geçen tasnifler\n"
		"burada örneklendirildi. Türk ve İbranî alfabeleri için ustalar\n"
		"nasıl tasnif ettiyse benzetimle sınıflandırmalar yapıldı.__\n"
		, reply_to_message_id = message.message_id
		, parse_mode="markdown"
		, "/nLütfen tasnif yöntemi seçin:"
		, reply_markup=reply_markup)
	elif fqdata in range(86, 92):
		reply_markup = InlineKeyboardMarkup(shadda(fqdata))
		await query.edit_message_text(text =f"Sayın **{message.from_user.first_name }** \n\n"
		"__Şeddeyle yazılan harfleri tek ya da çift hesaplatabilirsiniz.\n"
		"Girilen metin şedde içermiyorsa seçiminiz sonucu değiştirmez.__"
		, reply_to_message_id = message.message_id
		, parse_mode="markdown"
		, "/nTek veya çift hesaplamayı seçin:"
		, reply_markup=reply_markup)
	elif fqdata in range(94, 100):
	elif fqdata in range(100, 106):
	elif fqdata == 4:
		reply_markup = InlineKeyboardMarkup(sayioku(fqdata))
		await query.edit_message_text(text =f"Sayın **{message.from_user.first_name }** \n\n"
		"__Arapça,  Türkçe  ve İ branice olarak girdiğiniz sayının ebced\n"
		"hesabında,  bast usûlü hesabında  ve harflerin unsur tasnifinde\n"
		"kullanabileceğiniz istintakını yani nutkedilişini alabilirsiniz__\n"
		"Trilyonlu sayılara kadar elbette..."
		, reply_to_message_id = message.message_id
		, parse_mode="markdown"
		, "/nLütfen okuma dilini seçin:"
		, reply_markup=reply_markup)
	elif fqdata in range(107, 110):
	elif fqdata == 5:
		reply_markup = InlineKeyboardMarkup(hadim(fqdata))
		await query.edit_message_text(text =f"Sayın **{message.from_user.first_name }** \n\n"
		"__Hadim ismi  hesaplanırken  harf olarak  okunacak sayılar 1000 ve\n"
		"daha büyük sayılar olduğunda hadim isminin ebced değeri eşitliği\n"
		"sona erer  ve  düzeltme çabası için 1000 değerine  eşit harf ile\n"
		"çarpımı mantığı üzerine iki farklı  yaygın seçenekde olduğu gibi\n"
		"hesaplanır.  Gruplandırarak  yapılan  okumada binler, milyonlar,\n"
		"milyarlar ve trilyonlar için  tek sefer 1000'le çarpım öngörülür\n"
		"gruplandırmadan  yapılan  okumada  binden büyük her basamak için\n"
		"1000 harfi  çarpım  şeklinde eklenir.  Gruplandırılan hadim ismi\n"
		"gruplandırılmayan  isimden  hem  daha kısa görünür  hem de ebced\n"
		"değeri daha küçük olur.__"
		, reply_to_message_id = message.message_id
		, parse_mode="markdown"
		, "/nLütfen hesaplama modu seçin:"
		, reply_markup=reply_markup)
	elif fqdata == 112:
	elif fqdata == 113:
	elif fqdata == 6:
		reply_markup = InlineKeyboardMarkup(shadda(fqdata))
		await query.edit_message_text(text =f"Sayın **{message.from_user.first_name }** \n\n"
		"__Şeddeyle yazılan harfleri tek ya da çift hesaplatabilirsiniz.\n"
		"Girilen metin şedde içermiyorsa seçiminiz sonucu değiştirmez.__"
		, reply_to_message_id = message.message_id
		, parse_mode="markdown"
		, "/nTek veya çift hesaplamayı seçin:"
		, reply_markup=reply_markup)
	elif fqdata == 116:
	elif fqdata == 117:
	elif fqdata in [7, 20, 46, 59, 85, 92, 106, 110, 114, 118]:
		reply_markup = InlineKeyboardMarkup(thekeyboard())
		await query.edit_message_text(text =f"Sayın **{message.from_user.first_name }** \n\n"
		+ helperofhelpers(fqdata)
		, reply_to_message_id = message.message_id
		, parse_mode="markdown"
		, "/nNe yapmak istiyorsunuz ?"
		, reply_markup=reply_markup)

def thekeyboard(queries):
    keyboard = [
        [
            InlineKeyboardButton("Ebced Hesapla", callback_data="1"),
            InlineKeyboardButton("Bast Et", callback_data="2"),
            InlineKeyboardButton("Anasır Tasnif Et", callback_data="3")
        ],
        [
            InlineKeyboardButton("Sayı Nutket", callback_data="4"),
            InlineKeyboardButton("Hadim İsmine Çevir", callback_data="5"),
            InlineKeyboardButton("Harfleri Say", callback_data="6")
        ],
        [
			InlineKeyboardButton("Nümerolojik", callback_data="121"),
			InlineKeyboardButton("Ebced Bağlantıları", callback_data="120"),
			InlineKeyboardButton("Bot Yardım", callback_data="7")]
    ]
	return keyboard	
	

def ebced(queries):
    if queries == 1: cbdatam = 8
    elif queries == 2: cbdatam = 47
    ebced_keyboard = [
		[
			InlineKeyboardButton("Asgarî Ebced", callback_data=str(cbdatam)),
			InlineKeyboardButton("Sağir Ebced", callback_data=str(cbdatam+1)),
			InlineKeyboardButton("Kebir Ebced", callback_data=str(cbdatam+2)),
			InlineKeyboardButton("Ekber Ebced", callback_data=str(cbdatam+3))
		],
		[
			InlineKeyboardButton("Asgarî Mağribi", callback_data=str(cbdatam+4)),
			InlineKeyboardButton("Sağir Mağribi", callback_data=str(cbdatam+5)),
			InlineKeyboardButton("Kebir Mağribi", callback_data=str(cbdatam+6)),
			InlineKeyboardButton("Ekber Mağribi", callback_data=str(cbdatam+7))
		],
		[
			InlineKeyboardButton("Asgarî Frekans", callback_data=str(cbdatam+8)),
			InlineKeyboardButton("Sağir Frekans", callback_data=str(cbdatam+9)),
			InlineKeyboardButton("Kebir Frekans", callback_data=str(cbdatam+10)),
			InlineKeyboardButton("Ekber Frekans", callback_data=str(cbdatam+11))
		],
		[
			InlineKeyboardButton("Bot Yardım", callback_data=str(cbdatam+12)),
			InlineKeyboardButton("Önceki", callback_data=str(cbdatam+13))
		]
	]
	return ebced_keyboard	

def nature(queries)
    if queries == 3: cbdatam = 86
    nature_keyboard = [
		[
			InlineKeyboardButton("Muhiyyiddin ibni Arabî", callback_data=str(cbdatam)),
			InlineKeyboardButton("Ahmed El Buni", callback_data=str(cbdatam+1)),
			InlineKeyboardButton("Süleyman El Hüseyni", callback_data=str(cbdatam+2)),
			InlineKeyboardButton("Yaygın benimsenen", callback_data=str(cbdatam+3)),
			InlineKeyboardButton("Türk Alfabesi", callback_data=str(cbdatam+4)),
			InlineKeyboardButton("İbranî Alfabesi", callback_data=str(cbdatam+5))
		],
		[
			InlineKeyboardButton("Bot Yardım", callback_data=str(cbdatam+6)),
			InlineKeyboardButton("Önceki", callback_data=str(cbdatam+7))
		]
	]
	return nature_keyboard

def sayioku(queries):
    if queries == 4: cbdatam = 107
    sayioku_keyboard = [
		[
			InlineKeyboardButton("Arapça", callback_data=str(cbdatam)),
			InlineKeyboardButton("İbranice", callback_data=str(cbdatam+1)),
			InlineKeyboardButton("Türkçe", callback_data=str(cbdatam+2))
		],
		[
			InlineKeyboardButton("Bot Yardım", callback_data=str(cbdatam+3)),
			InlineKeyboardButton("Önceki", callback_data=str(cbdatam+4))
		]
	]
	return sayioku_keyboard
	
def hadim(queries):
    if queries == 5: 
		cbdatam = 112
		sayioku_keyboard = [
			[
				InlineKeyboardButton("Grupla", callback_data=str(cbdatam)),
				InlineKeyboardButton("Gruplama", callback_data=str(cbdatam+1))
			],
			[
				InlineKeyboardButton("Bot Yardım", callback_data=str(cbdatam+2)),
				InlineKeyboardButton("Önceki", callback_data=str(cbdatam+3))
			]
		]
    if queries == 5: 
		cbdatam = 112
		sayioku_keyboard = [
			[
				InlineKeyboardButton("Grupla", callback_data=str(cbdatam)),
				InlineKeyboardButton("Gruplama", callback_data=str(cbdatam+1))
			],
			[
				InlineKeyboardButton("Bot Yardım", callback_data=str(cbdatam+2)),
				InlineKeyboardButton("Önceki", callback_data=str(cbdatam+3))
			]
		]
	return sayioku_keyboard
	
def numerolojik(queries):
	if queries == 121: cbdatam = 666
	numerolog_keyboard = [
		[
			InlineKeyboardButton("Gruplayarak", callback_data=str(cbdatam)),
			InlineKeyboardButton("Gruplamadan", callback_data=str(cbdatam+1))
		],
		[
			InlineKeyboardButton("Bot Yardım", callback_data=str(cbdatam+2)),
			InlineKeyboardButton("Önceki", callback_data=str(cbdatam+3))
		]
	]
	return numerolog_keyboard

def shadda(queries):
	queries = float(query.data)
	if queries in range(8, 20):
		cbdatam = 46
		previous = 1
		single = 14
		twice = 26
    elif queries in range(47, 59):
		cbdatam = 85
		previous = 2
		single = 14
		twice = 26
	elif queries in range(87, 93):
		cbdatam = 107
		previous = 3
		single = 8
		twice = 14
	elif queries == 6:
		cbdatam = 118
		previous = 119
		single = 110
		twice = 111
	shadda_keyboard = [
		[
			InlineKeyboardButton("Tek hesapla", callback_data=str(queries + single)),
			InlineKeyboardButton("Çift hesapla", callback_data=str(queries + twice))
		],
		[
			InlineKeyboardButton("Bot Yardım", callback_data=str(cbdatam)),
			InlineKeyboardButton("Önceki", callback_data=str(previous))
		]
	]
	return shadda_keyboard
	
def helperofhelpers(queries):
	if queries in [7, 20, 46, 59, 85, 92, 106, 110, 114, 118]:

def randomgreetings(previousgreeting):
	
	greetings = ["","",""]
	
	return newgreeting		

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Use /start to test this bot.")
    

def main() -> None:
    application = Application.builder().token("TOKEN").build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("başlat", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("yardım", help_command))
    application.run_polling()

if __name__ == "__main__": main()
