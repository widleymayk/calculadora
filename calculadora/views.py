from django.shortcuts import render

# Vou criar a função para exibir a calculadora
def exibir_calculadora(request):
    resultado = None #Variavel para armazenar o resultado                               # return render(request, 'calculadora/index.html') # Renderiza o arquivo HTML.
    if request.method == "POST": # Verifica se o método da requisição é POST
        try:
         #Realiza a coleta de números e operação escolhida pelo usuário.
            numero1 =  float(request.POST.get('numero1'))
            numero2 = float(request.POST.get('numero2'))
            operacao = request.POST.get('operacao')

                #Realiza a operação de acordo com  a escolha do usuário.
            if operacao == 'adicao':
                resultado = numero1 + numero2
            elif operacao =='subtracao':
                resultado = numero1 - numero2
            elif operacao =='multiplicacao':
                resultado = numero1 * numero2
            elif operacao == 'divisao':
                resultado = numero1 / numero2
                 
                #excessao de cálculo para divisão por zero.
        except (ValueError , ZeroDivisionError):
            resultado = 'Valores inválidos. Digite apenas números.'

                #renderiza a página com o resultado.  
    return render(request, 'calculadora/index.html',{'resultado':resultado}) # Retorna o resultado para a view.
                    
