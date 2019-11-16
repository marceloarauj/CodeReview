def main ():
    def embaralhar ():
        threading.Timer(card_shuffle.get_length() / 4, lambda: dar_cartas(39)).start()
    def dar_cartas (x):
        if x > 33: threading.Timer(card_shuffle.get_length() / 4, lambda: dar_cartas(x - 2)).start()
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    open_sans_regular_18 = pygame.font.Font("fontes/open_sans/regular.ttf", 18)
    card_shuffle = pygame.mixer.Sound("sons/card_shuffle.wav")
    tela = pygame.display.set_mode([800, 600], pygame.NOFRAME)
    tela_rect = tela.get_rect()
    pontuacao = "0 x 0"
    placar = passion_one_regular_40.render(pontuacao, True, [255, 255, 255], [0, 0, 0])
    placar_rect = placar.get_rect(centerx = tela_rect.centerx)
    relogio = pygame.time.Clock()
    rodando = True
    embaralhar()
    while rodando:
        for e in pygame.event.get():
    pygame.quit()
main()