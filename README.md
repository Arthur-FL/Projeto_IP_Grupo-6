# 🛡️ CINgurando a Base 
CINgurando a Base é um jogo do estilo Tower Defense 2D desenvolvido por alunos do Centro de Informática da UFPE como projeto da disciplina de Introdução à Programação. O jogo combina movimentação do jogador, coleta de moedas e posicionamento estratégico de defesas para evitar que inimigos atinjam a base.  

## 👥 Membros da Equipe  
- Arthur Fernandes (afol)
- Gabriel Rio (grtc)  
- Janderson (jfs6)
- José Guilherme (jgtn) 
- Rafael Nobrega (rdn)
- Wilhyã Pedro (wpn)

## 🏗️ Arquitetura do Projeto 
O projeto está organizado em módulos Python, seguindo o paradigma de Orientação a Objetos. A estrutura foi pensada para manter o código modular, reutilizável e de fácil manutenção.  

O ponto de entrada do jogo é o arquivo main_game.py, que inicia o loop principal e gerencia a interação entre todos os outros módulos. Nele está contida a classe game, responsável por:  
- Inicializar a tela do jogo e carregar os grupos de sprites.  
- Controlar o estado geral do jogo (em execução, pausado, menu, game over, vitória etc.).  
- Coordenar a atualização e renderização dos objetos na tela.  
- Gerenciar entradas do usuário, como colocar defesas, iniciar novas ondas, ou ativar a visualização de debug.  
- Lidar com o sistema de ondas de inimigos.  
- Desenhar os elementos do HUD, como vida, moedas e número da onda.  

Cada componente do jogo foi separado em seu próprio arquivo para manter a clareza e facilitar futuras expansões.  

### 📁Projeto_IP_Grupo-6:  
│  
└─── coin.py # Gerencia as moedas do jogo (drop, coleta etc.)  
│  
└─── collide_detector.py # Define distância entre defesa e camino dos inimigos  
│  
└─── defenses.py # Define o comportamento e atributos da defesa  
│  
└─── enemy.py # Controla a movimentação e lógica dos inimigos  
│  
└─── jogo.py # Tela inicial e lógica de transição de estados  
│  
└─── main_game.py # Loop principal do jogo e integração dos módulos  
│  
└─── mapa.py # Representa o mapa e o caminho dos inimigos  
│  
└─── player.py # Movimentação do jogador  
│  
└─── random_drops.py # Sistema de geração aleatória de itens (como vida, escudos etc.)  
│  
└─── Assets # Imagens e recursos gráficos utilizados no jogo  
│       Blue_evil_eye_tp.png.png        
│       Cthulhu_eye_base_tp.png.png      
│       Cthulhu_eye_base_tp.png.png    
│       Green_evil_eye_tp.png.png    
│       Red_evil_eye_tp.png.png     
│       Inimigo1.png  
│       Inimigo2.png   
│       Inimigo3.png  
│       arrow.png   
│       arrow_1.png   
│       coin.png    
│       enemy1.png   
│       enemy1.webp   
│       fire.png    
│       fox_archer_left.png    
│       fox_archer_left_red.png   
│       fox_archer_left_yellow.png    
│       fox_warrior.png      
│       fox_warrior_left.png    
│       fox_warrior_left_blue.png    
│       fox_warrior_left_red.png    
│       fox_warrior_left_yellow.png    
│       game_over (1).png    
│       game_over.png    
│       heart.png    
│       pathtd.png   
│       player.png    
│       raposa_direita.png    
│       raposa_esquerda.png    
│       shield.png    
│       slash.png    
│       slash_1.png    
│       tornado.png    
│       win_screen.png     
│  
└───pycache # Arquivos compilados automaticamente pelo Python  
│       health_drop.cpython-312.pyc     
│       mapa.cpython-312.pyc    
│       enemy.cpython-312.pyc   
│       enemy.cpython-313.pyc   
│       mapa.cpython-313.pyc   

 ## 🛠️ Ferramentas Utilizadas  

 ### 1. Python  
 Foi a linguagem base utilizada para todo o desenvolvimento do jogo. Facilitou a implementação de conceitos da disciplina como laços, listas, condicionais e orientação a objetos.  

### 2. Pygame  
Responsável por toda a parte gráfica, controle de sprites, detecção de colisões, controle do teclado, reprodução de som e gerenciamento da tela de jogo. Tornou o desenvolvimento do jogo possível de forma simples e eficiente.  

### 3. VSCode / PyCharm  
Foram usados para escrever, testar e depurar o código do jogo. Ajudaram a manter a organização e produtividade da equipe durante o desenvolvimento.  

### 4. GitHub   
Permitiu que todos os membros contribuíssem com o código de forma organizada, evitando conflitos e mantendo o histórico de alterações. Útil para armazenar, compartilhar e manter o projeto atualizado entre os integrantes.  

### 5. Discord e WhatsApp  
Serviram como canais principais para organização, alinhamento das tarefas, troca de ideias, feedback e tomada de decisões em grupo.  

## 🧩 Conceitos da Disciplina Aplicados 
- Condicionais:usados para verificar teclas pressionadas e lógica de comportamento de sprites.  
- Laços de repetição: loops principais e atualização de sprites.  
- Listas: controle dos grupos de sprites (pygame.sprite.Group()).  
- Funções: criação de funcionalidades como colisão (player_collide, point_near_path, etc.).  
- Tuplas: usadas para coordenadas e dimensões (ex: Vector2).  
- Dicionários: usados para carregar defesas com diferentes atributos (defense_data).  
- Orientação a Objetos: estrutura base de todo o jogo, com classes como Player, Coin, Defense, etc.  

## ⚔️ Desafios Enfrentados  

### 📚 Maior desafio técnico:  
Compreender como integrar os conceitos de Programação Orientada a Objetos (POO) com os comandos específicos do Pygame.  
Durante o desenvolvimento, percebemos que dominar apenas os fundamentos de POO não era suficiente — era necessário entender como essa estrutura podia ser aplicada de forma eficiente dentro da lógica do Pygame, especialmente na organização de sprites, atualizações de estado e detecção de eventos.  
👉 Como lidamos com isso: Buscamos exemplos, tutoriais, discutimos entre o grupo e fizemos testes práticos para entender as possibilidades da biblioteca. Aos poucos, fomos refatorando nosso código para aproveitar melhor os benefícios da POO.  

### 📉 Maior erro de processo:  
Iniciar o desenvolvimento sem uma divisão clara de tarefas nem planejamento detalhado.  
No começo, a empolgação em "colocar a mão no código" nos levou a começar o projeto rapidamente, mas sem uma estratégia definida. Isso resultou em  falta de alinhamento sobre o que cada membro deveria estar fazendo.  
👉 Como lidamos com isso: Após identificar o problema, nos reunimos (via Discord e WhatsApp) para reorganizar as pendencias. Esse replanejamento melhorou a produtividade e o fluxo de trabalho do grupo.  

## 🎓 Lições Aprendidas  
- Como usar Pygame para desenvolver jogos 2D interativos.  
- A importância de organizar bem o código em módulos e classes.  
- Como aplicar conceitos fundamentais da programação em um projeto real.  
- Testar aos poucos economiza tempo.  

## 🕹️ Funcionamento do Jogo  
O jogo é do tipo Tower Defense 2D, onde o jogador deve proteger a base posicionando defesas no mapa para impedir que inimigos avancem. Abaixo estão os controles e as principais mecânicas:  

### 🎮 Controles:  
- W, A, S, D – Movimentam o personagem para cima, esquerda, baixo e direita, respectivamente.  
- ESC – Pausa e despausa o jogo.  
- TAB – Ativa uma "debug view" que exibe informações como: Vida dos inimigos, Alcance das torres... 
- Teclas numéricas de 1 a 5 – Selecionam os diferentes tipos de defesas disponíveis para serem posicionadas no mapa.  

### 💰 Itens Coletáveis:  
- Moeda 🪙 – Ao passar por cima de moedas, o jogador as coleta automaticamente. As moedas servem como recurso para comprar e posicionar defesas.  
- Vida ❤️ – Recupera pontos de vida do jogador. Fundamental para evitar a derrota.  
- Escudo 🛡️ – Concede proteção temporária. Enquanto o escudo estiver ativo, o jogador não sofre dano ao ser atingido por inimigos.  

### 🧠 Lógica do Jogo:  
- O jogador deve se mover pelo mapa coletando recursos e posicionando defesas em locais estratégicos.  
- Ganha o jogo se conseguir preencher completamente o mapa com defesas sobrevivendoa todos os ataques e ainda possuir pontos de vida.  
- Perde o jogo se os pontos de vida do jogador chegarem a zero antes do mapa estar totalmente defendido.  

Essa dinâmica exige que o jogador equilibre bem movimentação, coleta de recursos e posicionamento tático, garantindo que os inimigos não consigam atravessar a base.  

## 🎮 Instruções de Execução  
Siga os passos abaixo para executar o jogo CINgurando a Base no seu computador:  

### 1. Baixar um editor de código (VSCode ou PyCharm)  
Você precisa de um ambiente para editar e executar o código. Recomendamos uma das opções abaixo:  

#### 👉 Visual Studio Code (VSCode)  
- Acesse: https://code.visualstudio.com/  
- Clique em Download for Windows/Linux/Mac e instale.  
- Após a instalação, abra o VSCode.
- 
#### 👉 PyCharm (da JetBrains)  
- Acesse: https://www.jetbrains.com/pycharm/  
- Clique em Download e escolha a versão Community (gratuita).  
- Instale e abra o PyCharm. 
 
### 2. Instalar o Python (se ainda não tiver)  
- Acesse: https://www.python.org/downloads/  
- Clique em Download Python 3.x.x. (versão atual 3.13.2)  
- Durante a instalação, marque a opção "Add Python to PATH" antes de clicar em "Install Now".  

#### Para verificar se instalou corretamente:  
- Abra o terminal (Prompt de Comando ou Terminal do VSCode) e digite:  
```brash 
python --version 
``` 
- Deve aparecer algo como: Python 3.x.x  
 
### 3. Instalar a biblioteca Pygame  
Com o Python instalado, você precisa instalar o Pygame, que é usado para criar o jogo.  

No terminal, digite:  
```brash 
pip install pygame 
``` 

### 4. Baixar os arquivos do jogo 
Você pode obter os arquivos do jogo de duas maneiras:  

#### 🔽 A) Clonar o repositório (se estiver no GitHub)  

No terminal:  
git clone https://github.com/Arthur-FL/Projeto_IP_Grupo-6  

#### 📁 B) Baixar como .ZIP  
- Acesse o repositório (ex: GitHub).  
- Clique em Code > Download ZIP.  
- Extraia o ZIP para uma pasta local.  

### 5. Executar o jogo  
- Abra a pasta do jogo no VSCode ou PyCharm.  
- Localize o arquivo main_game.py.  
- Execute com o botão de Run (executar) no editor ou via terminal com:  
```brash 
python main_game.py 
``` 

O jogo será iniciado em uma janela. Divirta-se defendendo sua base! 

 
