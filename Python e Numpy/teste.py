import pywhatkit

fone = '+5582998090956'
message = 'teste de script para mandar mensagem whats'
hour = 15
minutes = 23

pywhatkit.sendwhatmsg(fone, message, hour, minutes)
print('mensagem enviada com sucesso')