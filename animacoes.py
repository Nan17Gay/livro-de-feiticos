import pygame

def animar_lumos():
    pygame.init()
    tela = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Feitiço: Lumos")

    PRETO = (0, 0, 0)
    MARROM = (139, 69, 19)
    AMARELO = (255, 255, 0)

    clock = pygame.time.Clock()
    luz_acesa = False
    tempo_troca = 1000
    ultimo_tempo = pygame.time.get_ticks()

    rodando = True
    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

        agora = pygame.time.get_ticks()
        if agora - ultimo_tempo > tempo_troca:
            luz_acesa = not luz_acesa
            ultimo_tempo = agora

        tela.fill(PRETO)
        pygame.draw.line(tela, MARROM, (200, 300), (300, 200), 8)
        if luz_acesa:
            pygame.draw.circle(tela, AMARELO, (300, 200), 20)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def animar_expelliarmus():
    pygame.init()
    tela = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Feitiço: Expelliarmus")

    PRETO = (0, 0, 0)
    VERMELHO = (255, 0, 0)
    BRANCO = (255, 255, 255)

    clock = pygame.time.Clock()
    raio_expansao = 0
    raio_max = 40
    pos_x = 50
    raio_pulsar = 10

    rodando = True
    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

        tela.fill(PRETO)

        # Desenha o raio vermelho que avança até a borda da tela
        if pos_x < 600:
            pos_x += 15
        pygame.draw.line(tela, VERMELHO, (50, 200), (min(pos_x, 600), 200), 6)

        # Depois do raio, um círculo branco que pulsa
        if pos_x >= 600:
            raio_expansao += 1
            if raio_expansao > raio_max:
                raio_expansao = 10
            pygame.draw.circle(tela, BRANCO, (600, 200), raio_expansao)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def animar_alohomora():
    pygame.init()
    tela = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Feitiço: Alohomora")

    PRETO = (0, 0, 0)
    CINZA = (169, 169, 169)
    AMARELO = (255, 255, 0)

    clock = pygame.time.Clock()
    deslocamento = 0
    max_desloc = 120
    sentido = 1  # 1 para abrir, -1 para fechar

    rodando = True
    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

        tela.fill(PRETO)

        porta_rect = pygame.Rect(250 + deslocamento, 150, 100, 150)
        pygame.draw.rect(tela, CINZA, porta_rect)
        pygame.draw.circle(tela, AMARELO, (porta_rect.right - 20, porta_rect.centery), 15)

        deslocamento += sentido * 5
        if deslocamento >= max_desloc or deslocamento <= 0:
            sentido *= -1

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


def animar_expecto_patronum():
    pygame.init()
    tela = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Feitiço: Expecto Patronum")

    PRETO = (0, 0, 0)
    BRANCO = (255, 255, 255)
    CINZA_CLARO = (200, 200, 200)

    clock = pygame.time.Clock()

    # Pontos para o patrono em forma simples
    pontos = [(300, 150), (320, 170), (340, 150), (360, 170), (350, 200), (310, 200)]

    rodando = True
    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

        tela.fill(PRETO)
        pygame.draw.polygon(tela, BRANCO, pontos)
        pygame.draw.circle(tela, CINZA_CLARO, (320, 160), 10)
        pygame.draw.circle(tela, CINZA_CLARO, (340, 160), 10)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


def animar_protego():
    pygame.init()
    tela = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Feitiço: Protego")

    PRETO = (0, 0, 0)
    AZUL_CLARO = (100, 150, 255)

    clock = pygame.time.Clock()
    raio = 10
    aumentando = True

    rodando = True
    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

        tela.fill(PRETO)

        if aumentando:
            raio += 2
            if raio >= 100:
                aumentando = False
        else:
            raio -= 2
            if raio <= 10:
                aumentando = True

        pygame.draw.circle(tela, AZUL_CLARO, (300, 200), raio, 5)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


def animar_stupefy():
    pygame.init()
    tela = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Feitiço: Stupefy")

    PRETO = (0, 0, 0)
    VERMELHO = (255, 0, 0)
    BRANCO = (255, 255, 255)

    clock = pygame.time.Clock()
    pos_x = 50
    raio_expansao = 0
    raio_max = 50
    explosao = False

    rodando = True
    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

        tela.fill(PRETO)

        if not explosao:
            pos_x += 20
            pygame.draw.line(tela, VERMELHO, (50, 200), (min(pos_x, 600), 200), 10)
            if pos_x >= 600:
                explosao = True
        else:
            raio_expansao += 2
            if raio_expansao > raio_max:
                raio_expansao = 10
            pygame.draw.circle(tela, BRANCO, (600, 200), raio_expansao)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def executar_animacao(nome_feitico):
    funcoes = {
        "lumos": animar_lumos,
        "expelliarmus": animar_expelliarmus,
        "alohomora": animar_alohomora,
        "expecto patronum": animar_expecto_patronum,
        "protego": animar_protego,
        "stupefy": animar_stupefy
    }
    func = funcoes.get(nome_feitico)
    if func:
        func()
    else:
        print("Animação para este feitiço ainda não implementada.")