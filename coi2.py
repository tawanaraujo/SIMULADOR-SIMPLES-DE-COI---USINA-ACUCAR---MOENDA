import pygame 

#estados importantes

funcionamento_motor = 'on', 'off', 'emergencia'
funcionamento_esteira = 'on', 'off', 'emergencia'
botao_ligado = 'on'
botao_desligado = 'off'
potencia = 10
animacao_ativa = False
mostrar_texto = False

#posições cana

x_cana = 0
y_cana = 0

#cores principais

vermelho = (200,0,0)
vermelho_escuro = (100,0,0)
azul = (0,0,255)
azul_escuro = (0,0,180)
amarelo = (200,200,0)
amarelo_escuro = (100,100,0)
verde = (0,200,0)
verde_escuro = (0,100,0)
cinza = (100,100,100)
cinza_escuro = (80,80,80)
cinza_escuro2 = (30,30,30)
branco = (255,255,255)

#rects dos 3 botões

botao_ligado_rect = pygame.Rect(39,590,70,70)
botao_desligado_rect = pygame.Rect(289,590,70,70)
botao_shut_rect = pygame.Rect(165,590,70,70)

#looping pricipal com janelas e eventos do jogo - BASE !!!!

pygame.init()
pygame.mixer.init()

#sons

motor1 = pygame.mixer.Sound('sons/motor1.mp3')
motor2 = pygame.mixer.Sound('sons/motor2.mp3')
motor2.set_volume(1.0)
som_on_off = pygame.mixer.Sound('sons/on.mp3')
som_shut = pygame.mixer.Sound('sons/shut.mp3')

#função de desenho de motores e esteiras etc

def desenhar_motor(surface, x, y,cor_motor, cor_grades):
    pygame.draw.rect(surface, cor_motor, (x, y, 150, 100), border_radius=10, width=0)          # motor corpo
    pygame.draw.rect(surface, cinza_escuro2, (x + 150, y + 40, 30, 20), border_radius=0)   # motor rotor
    pygame.draw.line(surface, cor_grades, (x, y + 20), (x + 149, y + 20), width=5)        # grades1
    pygame.draw.line(surface, cor_grades, (x, y + 80), (x + 149, y + 80), width=5)        # grades2
    pygame.draw.line(surface, cor_grades, (x, y + 50), (x + 149, y + 50), width=5)        # grades3
    pygame.draw.rect(surface, cinza_escuro, (x, y + 100, 150, 30), border_radius=8)      # base motor

def desenhar_motor_invertido(surface, x, y, cor_motor, cor_grades):
    pygame.draw.rect(surface, cor_motor, (x, y, 150, 100), border_radius=10, width=0)          # motor corpo
    pygame.draw.rect(surface, cinza_escuro2, (x - 30, y + 40, 30, 20), border_radius=0)   # motor rotor
    pygame.draw.line(surface, cor_grades, (x, y + 20), (x + 149, y + 20), width=5)        # grades1
    pygame.draw.line(surface, cor_grades, (x, y + 80), (x + 149, y + 80), width=5)        # grades2
    pygame.draw.line(surface, cor_grades, (x, y + 50), (x + 149, y + 50), width=5)        # grades3
    pygame.draw.rect(surface, cinza_escuro, (x, y + 100, 150, 30), border_radius=8)      # base motor

def desenhar_cana_esteira(surface, x_cana, y_cana):
    pygame.draw.rect(surface, verde, (x_cana, y_cana, 50,50), border_radius=10)

#fonte

fonte = pygame.font.SysFont('Arial', 24)

#looping do simulador

clock = pygame.time.Clock()
running = True
tela = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

while running:

    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            if botao_ligado_rect.collidepoint(event.pos):
                som_on_off.play()
                motor1.play()
                motor2.play(-1)
                animacao_ativa = not animacao_ativa
        mostrar_texto = False

        if event.button == 1:
            if botao_desligado_rect.collidepoint(event.pos):
                animacao_ativa = False
                mostrar_texto = False
                som_on_off.play()
                motor2.stop()
    

        if event.button == 1:
            if botao_shut_rect.collidepoint(event.pos):
                animacao_ativa = False
                mostrar_texto = not mostrar_texto
                som_on_off.play()
                som_shut.play(1)
                motor2.stop()
                
    if animacao_ativa:
        cor_motor = vermelho
        cor_grades = vermelho_escuro
        x_cana = x_cana + 5
        if x_cana >= 450:
            x_cana =  0   
        
    else:
        cor_motor = azul
        cor_grades = azul_escuro
    if mostrar_texto:
        cor_motor = amarelo
        cor_grades = amarelo_escuro
        
    tela.fill('black')

    #texto de titulo e tags de motores e moenda

    texto_titulo = fonte.render('SIMULADOR SIMPLIFICADO DE COI - USINA - MOEGA', True, branco)
    tela.blit(texto_titulo, (20,10)) #titulo

    emergencia_text = fonte.render('MOTORES DESLIGADOS EM MODO DE EMERGÊNCIA', True, amarelo)
    if mostrar_texto:
        tela.blit(emergencia_text, (20,50))

    texto_motor1 = fonte.render('MOTOR #1', True, branco)
    tela.blit(texto_motor1, (30,100)) #motor 1

    texto_motor2 = fonte.render('MOTOR #2', True, branco)
    tela.blit(texto_motor2, (30,310)) #motor 2

    texto_motor3 = fonte.render('MOTOR #3', True, branco)
    tela.blit(texto_motor3, (1210,585)) #motor 3

    texto_moega = fonte.render('MOEGA', True, branco)
    tela.blit(texto_moega, (950,12)) #moega

    #motores
    
    desenhar_motor(tela, 25, 150, cor_motor, cor_grades) #1
    desenhar_motor(tela, 25, 350, cor_motor, cor_grades) #2
    desenhar_motor_invertido (tela, 1200,620, cor_motor, cor_grades) #3

    #esteiras

    pygame.draw.rect(tela, cinza_escuro, (1020,50,150,700), width=0) #esteira1
    pygame.draw.rect(tela, cinza_escuro, (200,150,750,100), width=0) #esteira2
    pygame.draw.rect(tela, cinza_escuro, (200,350,750,100), width=0) #esteira3

    #esteira capas

    pygame.draw.rect(tela, verde_escuro, (200,150,50,100), width=0) #motor1
    pygame.draw.rect(tela, verde_escuro, (200,350,50,100), width=0) #motor2
    pygame.draw.rect(tela, verde_escuro, (1020,680,150,80), width=0) #motor3

    #moenda

    pygame.draw.rect(tela, verde, (750,50,500,500), width=0) #moenda_externa
    pygame.draw.rect(tela, verde_escuro, (775,70,450,450), width=0) #moenda_interna 

    #canas esteira

    pygame.draw.rect(tela, verde, (x_cana+250, y_cana+175, 50,50), border_radius=10) #1
    pygame.draw.rect(tela, verde, (x_cana+250, y_cana+375, 50,50), border_radius=10) #2
    
    #controle

    pygame.draw.rect(tela, cinza_escuro, (25,500,350,250), width=2) #painel externo
    pygame.draw.rect(tela, cinza, (37,510,325,225), width=0) #painel interno

    #botões on, off, emergencia e potencia

    pygame.draw.ellipse(tela, verde, (39,590,70,70), width=0) #on
    btn_on_txt = fonte.render('ON', True, branco) #botão on
    tela.blit(btn_on_txt, (54, 610))

    pygame.draw.ellipse(tela, vermelho, (289,590,70,70), width=0) #off
    btn_off_txt = fonte.render('OFF', True, branco) #botão off
    tela.blit(btn_off_txt, (304, 610))

    pygame.draw.ellipse(tela, amarelo, (165,590,70,70), width=0) #emergencia
    btn_shut_txt = fonte.render('SHUT', True, branco) #botão emergencia
    tela.blit(btn_shut_txt, (168, 610))

    pygame.draw.rect(tela, cinza_escuro, (75,540,250,25), width=0) #potencia barra
    btn_potencia_txt = fonte.render('POTÊNCIA', True, branco) #potencia barra
    tela.blit(btn_potencia_txt, (140, 512))

    pygame.draw.rect(tela, cinza_escuro2, (75,540,50,25), width=0) #potencia parte movel
    

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
