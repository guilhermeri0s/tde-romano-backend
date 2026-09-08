import re


class ErroDeValidacao(Exception):
    """Erro de dado inválido informado pelo usuário."""
    pass


PADRAO_EMAIL = re.compile(r"^[^@\s]+@[^@\s]+\.[A-Za-z]{2,}$")


def texto_obrigatorio(valor, campo, minimo=2, maximo=100):
    if valor is None:
        raise ErroDeValidacao(f"O campo '{campo}' é obrigatório.")

    valor = valor.strip()

    if not valor:
        raise ErroDeValidacao(f"O campo '{campo}' é obrigatório e não pode ficar em branco.")
    if len(valor) < minimo:
        raise ErroDeValidacao(f"O campo '{campo}' deve ter no mínimo {minimo} caracteres.")
    if len(valor) > maximo:
        raise ErroDeValidacao(f"O campo '{campo}' deve ter no máximo {maximo} caracteres.")

    return valor


def email_obrigatorio(valor, campo="e-mail"):
    valor = texto_obrigatorio(valor, campo, minimo=5, maximo=120)

    if not PADRAO_EMAIL.match(valor):
        raise ErroDeValidacao(f"O campo '{campo}' não contém um endereço válido (exemplo: nome@dominio.com).")

    return valor.lower()


def telefone_obrigatorio(valor, campo="telefone"):
    valor = texto_obrigatorio(valor, campo, minimo=8, maximo=20)
    digitos = re.sub(r"\D", "", valor)

    if len(digitos) < 10 or len(digitos) > 11:
        raise ErroDeValidacao(f"O campo '{campo}' deve conter DDD + número (10 ou 11 dígitos).")

    return digitos


def decimal_positivo(valor, campo):
    valor = texto_obrigatorio(str(valor), campo, minimo=1, maximo=20)
    valor = valor.replace("R$", "").replace(" ", "").replace(",", ".")

    try:
        numero = float(valor)
    except ValueError:
        raise ErroDeValidacao(f"O campo '{campo}' deve ser um número (exemplo: 19,90).")

    if numero <= 0:
        raise ErroDeValidacao(f"O campo '{campo}' deve ser maior que zero.")

    return round(numero, 2)


def inteiro_nao_negativo(valor, campo):
    valor = texto_obrigatorio(str(valor), campo, minimo=1, maximo=10)

    try:
        numero = int(valor)
    except ValueError:
        raise ErroDeValidacao(f"O campo '{campo}' deve ser um número inteiro.")

    if numero < 0:
        raise ErroDeValidacao(f"O campo '{campo}' não pode ser negativo.")

    return numero