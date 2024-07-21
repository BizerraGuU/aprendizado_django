from django.db import models
from django.conf import settings 

class Room (models.Model):

    #toda sala de chat precisa de um moderador

    user = models.ForeignKey(
        #adicionando os usuario
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    title = models.CharField(max_length=200) 
    # definidindo o tamanho maximo do titulo
    messages = models.ManyToManyField('Message')
    #apenas para evitar eventuais erros, fora adicionado uma string
    created_at = models.DateTimeField(auto_now_add=True)
    #registrar data e hora da publicação


class Message(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    text = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
