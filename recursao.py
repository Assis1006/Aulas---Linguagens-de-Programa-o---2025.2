def fatorial(num:int) -> int:
    """
    Calcula o fatoria de num.

    Parameters
    ----------
    num : int
        Número para cálculo.

    Returns
    -------
    int
        Fatorial de num.

    """
    if num <= 1:
        return 1
    
    return num * fatorial(num - 1) # Recursão: método que resolve a si próprio. Resolve o problema aos poucos.
# Nesse caso, se tentarmos o fatorial de 10, a função irá fazer: 10*fatorial(9), depois 10*9*fatorial(8) e assim por diante.
# A recursão funciona como um "while", parando somente quando chegar no caso 10*9*...*2*fatorial(1). O fatorial(1) quebra o "loop", retornando 1.
# Exemplo de recursão com Fibonacci:
# def f(n):
    #if n = 1: return 1
    #if n = 0: return 1
    #return f(n-1) + f(n-2)
    
# Testes "caixa preta": rodamos o código esperando um certo retorno, se o retorno foi o esperado deu certo, se não, não. Nesse caso não tentamos entender o que ocorreu no código.
