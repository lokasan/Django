from django.shortcuts import render
def main(request):
    return render(request, 'mainapp/index.html', context={'menu':{'main': 'Главная', 'catalogue': 'Каталог', 'contacts': 'Контакты'}, 'page': 'Главная'})
    

def catalogue(request):
    return render(request, 'mainapp/catalogue/index.html', context={'menu':{'main': 'Главная', 'catalogue': 'Каталог', 'contacts': 'Контакты'}, 'page': 'Каталог'})
    

def contacts(request):
    return render(request, 'mainapp/contacts/index.html', context={'placeholder': {'name': 'ivan', 'email': 'mail@gmail.com', 'theme': 'покупка монитора'}, 'menu':{'main': 'Главная', 'catalogue': 'Каталог', 'contacts': 'Контакты'}, 'page': 'Контакты'})

def monitor(request):
	return render(request, r'mainapp/catalogue/monitor/Eizo ColorEdge CG318-4K/CG318-4K.html', context={'menu':{'main': 'Главная', 'catalogue': 'Каталог', 'contacts': 'Контакты'}})
# Create your views here.

# Create your views here.
