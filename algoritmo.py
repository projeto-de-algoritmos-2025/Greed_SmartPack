def knapsack_fracionado(itens, peso_max, volume_max=float('inf')):
    itens_ordenados = sorted(itens, key=lambda x: x['valor'] / x['peso'], reverse=True)
    
    carga_total = []
    valor_total = 0.0
    peso_usado = 0.0