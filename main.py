from telebot import TeleBot,types
token='7305119953:AAECq6ZBPIhe0JKo1Pq_x1cF9TjQCE6kJ8A'
bot=TeleBot(token)
@bot.message_handler(content_types=['text'])
def main(m):
	
	commands=m.text
	if m.chat.type =="private":
		if commands =="/start":
			bot.reply_to(m,"hello")
	if m.chat.type == 'supergroup':
		if commands=='تشغيل':
			bot.reply_to(m,'  تم تفعيل المجموعة')
bot.polling()