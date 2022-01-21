# encoding: utf-8
# cores no terminal

# Padrao ANSI: escape sequence
    # tudo dentro de ANSI comeca com uma \ e depois um codigo
# Sempre que quiser representar uma cor, usa-se o codigo:
# \033[style; text ; back m] -> respct: estilo, cor do texto, cor do fundo
# \033[0;33;44m # <- esse é o codigo de cor
    # codigos de estilo: tem apenas um algarismo
        # 0 - nenhum
        # 1 - bold
        # 4 - underline
        # 7 - negative
    # cores de texto: comecam com 3
        # 30, 31, 32, 33, 34, 35, 36, 37
    # back: comecam com 4
        # 40, 42, 42, 43, 44, 45, 46, 47

print('\033[31mOlá, Mundo!')
print('\033[1;31;40mOlá, Mundo!')
