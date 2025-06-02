def knapsack_fracionado(itens, peso_max, volume_max=float('inf')):
    itens_ordenados = sorted(itens, key=lambda x: x['valor'] / x['peso'], reverse=True)
    
    carga_total = []
    valor_total = 0.0
    peso_usado = 0.0

    for item in itens_ordenados:
        if peso_usado >= peso_max:
            break

        peso_disponivel = peso_max - peso_usado
        proporcao = min(1, peso_disponivel / item['peso'])

        if proporcao > 0:
            carga_total.append({
                'nome': item['nome'],
                'proporcao': round(proporcao * 100, 2),
                'valor': round(item['valor'] * proporcao, 2)
            })
            peso_usado += item['peso'] * proporcao
            valor_total += item['valor'] * proporcao

    return {
        'carga': carga_total,
        'valor_total': round(valor_total, 2),
        'peso_usado': round(peso_usado, 2)
    }