def calcular_limite(renda: float) -> float:
    """Calcula o limite de crédito a partir da renda."""
    if renda < 0:
        raise ValueError("renda não pode ser negativa")
    return renda * 0.25
