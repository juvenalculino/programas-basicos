from cores import verde, vermelho, amarelo, magenta

perguntas = {
    "pergunta 1: ": {
        'pergunta': 'Quanto é 5 * 42?',
        'resposta': {'a': '205', 'b': '195', 'c': '210', 'd': '250'},
        'correta': 'c',
    },
    "pergunta 2: ": {
        'pergunta': 'Quanto é 18 / 2?',
        'resposta': {'a': '7', '4': '10', 'c': '3', 'd': '9'},
        'correta': 'd',
    },
}
print()
resposta_correta = 0
qtd_perguntas = len(perguntas)

# Retorna os valores e os itens da pergunta
for p_valor, p_item in perguntas.items():
    vermelho(f'{p_valor} {p_item["pergunta"]}')
    print('-' * 28)
    verde('Respostas:\n')
    # Retorna o valor e o item da resposta
    for r_valor, r_item in p_item['resposta'].items():
        magenta(f'[{r_valor}]: {r_item}')
    # input
    usuario_escolhe = input('\n\u001b[32mEscolha sua opção:\u001b[0m ').lower()
    if usuario_escolhe == p_item['correta']:
        # Se a resposta estiver correta incrementa 1
        resposta_correta += 1
        verde('\nÓtimo, você acertou!!!\n')
        # Aqui há uma pequena modificação, caso esteja no singular ou no plural
        if resposta_correta == 1:
            verde(f'você acertou {resposta_correta}. questão\n')
        else:
            verde(f'você acertou {resposta_correta} questões.\n')
    else:
        vermelho('\nErrou, na proxima você consegue!\n')
# Retorna a porcentagem do acerto
porcentagem_acerto = resposta_correta / qtd_perguntas * 100
amarelo(f'Sua porentagem de acerto é de {porcentagem_acerto}%')
