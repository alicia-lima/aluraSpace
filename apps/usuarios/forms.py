from django import forms

''' Cria uma Classe de formulario de Login com nome e senha:
    label são as informações que aparecem antes do Input 
    [required = True] é um bool de preenchimento necessário 
    max_lengt são os caractér máximo de um Input 
    widget permite a edição de alguns caracteres do input 

    forms.Form - Cria um formulário do zero 

'''

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex. João Silva"
            }
        )
    )
    senha=forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget= forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite sua senha"
            }
        )
    )

class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label="Nome de Cadastro",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex. João Silva"
            }
        )
    )
    email=forms.EmailField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex. joãosilva@xpto.com"
            }
        )
    )
    senha_1=forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget= forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite sua senha"
            }
        )
    )
    senha_2=forms.CharField(
        label="Confirme sua senha",
        required=True,
        max_length=70,
        widget= forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite sua senha novamente"
            }
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")

        #verifica se existe algo em nome e tira os espaços, verifica se há espaços e devolve nomes 
        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("Espaços não são permitidos neste campo")
            else: 
                return nome
        return nome 

    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get('senha_1')
        senha_2 = self.cleaned_data.get('senha_2')

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('Senhas não são iguais')
            else:
                return senha_2
        