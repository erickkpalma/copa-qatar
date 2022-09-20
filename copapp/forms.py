from django import forms
from django.core.mail.message import EmailMessage

class ContatoForms(forms.Form):

    email = forms.EmailField()
    nome = forms.CharField(label='Nome')
    assunto = forms.CharField(label='Assunto', max_length=50)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):

        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'\nEmail: {email}\nNome: {nome}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject='Email enviado',
            body=conteudo,
            from_email='erick.palma93@outlook.com',
            to=['erick.palma93@outlook.com',],
            headers={'Reply-To': email}

        )
        mail.send()


class PesquisaForm(forms.Form):

    pesq = forms.CharField(max_length=20, label='Nome do time..')
