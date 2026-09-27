import json, os, html

with open('extracted_slides.json', 'r', encoding='utf-8') as f:
    slides_data = json.load(f)

# Podcasts Script Transcripts by Lesson
podcasts_scripts = {
    1: "Olá, bem-vindo ao podcast da Aula 1 de Smart Grids! Sou a Professora Bia. Nesta aula introdutória, exploramos a transição das redes elétricas tradicionais unidirecionais para as Redes Inteligentes (Smart Grids). Discutimos o papel da infraestrutura de medição avançada AMI, os sistemas SCADA e a automação de self-healing para reestabelecer o fornecimento de energia em questão de segundos!",
    2: "Olá! Neste episódio do podcast da Aula 2, analisamos os Algoritmos Genéticos (AG). Vimos como os operadores de Seleção por Roleta, Crossover e Mutação evoluem uma população de soluções candidatas para resolver o problema de Alocação Ótima de Unidades de Medição Fasorial (PMUs), garantindo 100% de observabilidade com o menor custo possível.",
    3: "Bem-vindo ao podcast da Aula 3 sobre Evolução Diferencial! Sou a Professora Bia. Explicamos como a ED utiliza vetores de diferença ponderados pelo fator de escala F e a taxa de recombinação CR para mutar soluções contínuas e aplicar a Seleção Gulosa, otimizando a redução de perdas energéticas com extrema velocidade.",
    4: "Olá! No podcast da Aula 4, mergulhamos na Inteligência em Enxame! Estudamos o algoritmo PSO, que imita o vôo de bandos de pássaros, e o algoritmo ACO, baseado no comportamento de formigas reais, aplicados ao roteamento otimizado de dados de telemetria em redes PLC e cabos de fibra óptica OPGW.",
    5: "Bem-vindo ao podcast da Aula 5 sobre Estimação de Estado! Explicamos o algoritmo clássico dos Mínimos Quadrados Ponderados (WLS). Vimos como ele filtra o ruído das medições convencionais e das PMUs, permitindo detectar e rejeitar maus dados (Bad Data) através do teste do Qui-Quadrado.",
    6: "Olá! Neste episódio da Aula 6, discutimos a Operação em Baixa Tensão e a Reconfiguração de Redes de Distribuição. Aprendemos como a alteração do status de chaves seccionadoras e tie-switches permite aliviar sobrecargas e minimizar perdas I²R, respeitando estritamente a restrição de radialidade da rede.",
    7: "Bem-vindo ao podcast da Aula 7! Abordamos a Geração Distribuída solar e eólica, a operação de Microgrids em modo conectado ou ilhado, e o conceito de Virtual Power Plants (VPPs) agregando pequenos recursos distribuídos via software com suporte da metaheurística VNS.",
    8: "Olá! No podcast da Aula 8, apresentamos os sistemas HEMS para Smart Homes! Discutimos a otimização multi-objetivo com o algoritmo NSGA-II, gerando a Fronteira de Pareto para equilibrar de forma ótima a redução do custo da conta de luz e o conforto térmico do usuário.",
    9: "Bem-vindo ao podcast da Aula 9 sobre Redes Neurais Profundas! Explicamos a aplicação de arquiteturas LSTM e CNN para extração automática de atributos em séries temporais de consumo elétrico, realizando a previsão de carga a curto prazo (STLF) e a detecção de furtos de energia.",
    10: "Olá! Neste podcast da Aula 10, exploramos Big Data Science em Smart Grids! Analisamos os 5 V's (Volume, Velocidade, Variedade, Veracidade e Valor) aplicados aos petabytes de dados de medidores inteligentes AMI com processamento em tempo real via Spark Streaming."
}

# SVG Vector Diagrams for each lesson
svg_figures = {
    1: '''
    <svg viewBox="0 0 800 240" style="width:100%;height:auto;background:var(--surface2);border-radius:14px;border:1px solid var(--border);padding:10px;">
      <text x="400" y="25" text-anchor="middle" fill="var(--accent)" font-weight="bold" font-size="14" font-family="Orbitron">ARQUITETURA DA SMART GRID vs. REDE TRADICIONAL</text>
      <rect x="50" y="60" width="120" height="70" rx="8" fill="rgba(0,243,255,0.15)" stroke="var(--accent)" stroke-width="2"/>
      <text x="110" y="95" text-anchor="middle" fill="var(--text)" font-size="12" font-weight="bold">SUBESTAÇÃO</text>
      <text x="110" y="115" text-anchor="middle" fill="var(--gold)" font-size="10">SCADA / Telemetria</text>
      <line x1="170" y1="95" x2="330" y2="95" stroke="var(--accent)" stroke-width="3" stroke-dasharray="5,5"/>
      <circle cx="330" cy="95" r="18" fill="var(--surface)" stroke="var(--success)" stroke-width="2"/>
      <text x="330" y="100" text-anchor="middle" fill="var(--success)" font-size="10" font-weight="bold">CHAVE</text>
      <line x1="348" y1="95" x2="510" y2="95" stroke="var(--accent)" stroke-width="3"/>
      <rect x="510" y="60" width="110" height="70" rx="8" fill="rgba(255,183,0,0.15)" stroke="var(--gold)" stroke-width="2"/>
      <text x="565" y="95" text-anchor="middle" fill="var(--text)" font-size="12" font-weight="bold">MEDIDOR AMI</text>
      <text x="565" y="115" text-anchor="middle" fill="var(--accent)" font-size="10">Leitura Bidirecional</text>
      <rect x="670" y="60" width="100" height="70" rx="8" fill="rgba(0,255,102,0.15)" stroke="var(--success)" stroke-width="2"/>
      <text x="720" y="95" text-anchor="middle" fill="var(--text)" font-size="12" font-weight="bold">SOLAR PV</text>
      <text x="720" y="115" text-anchor="middle" fill="var(--success)" font-size="10">Geração Distribuída</text>
      <path d="M 620 85 L 660 85 M 650 80 L 660 85 L 650 90 M 660 105 L 620 105 M 630 100 L 620 105 L 630 110" fill="none" stroke="var(--gold)" stroke-width="2"/>
      <text x="400" y="185" text-anchor="middle" fill="var(--muted)" font-size="12">Rede Digitalizada com Comunicação Bidirecional em Tempo Real e Self-Healing</text>
    </svg>
    ''',
    2: '''
    <svg viewBox="0 0 800 220" style="width:100%;height:auto;background:var(--surface2);border-radius:14px;border:1px solid var(--border);padding:10px;">
      <text x="400" y="25" text-anchor="middle" fill="var(--accent)" font-weight="bold" font-size="14" font-family="Orbitron">OPERADORES DO ALGORITMO GENÉTICO (CROSSOVER & MUTAÇÃO)</text>
      <text x="80" y="65" fill="var(--muted)" font-size="11" font-weight="bold">Pai 1:</text>
      <rect x="130" y="50" width="220" height="24" rx="4" fill="rgba(0,243,255,0.2)" stroke="var(--accent)"/>
      <text x="240" y="66" text-anchor="middle" fill="var(--text)" font-family="monospace" font-weight="bold">[ 1  1  0  1 | 0  0  1 ]</text>
      <text x="80" y="105" fill="var(--muted)" font-size="11" font-weight="bold">Pai 2:</text>
      <rect x="130" y="90" width="220" height="24" rx="4" fill="rgba(255,0,85,0.2)" stroke="var(--accent-pink)"/>
      <text x="240" y="106" text-anchor="middle" fill="var(--text)" font-family="monospace" font-weight="bold">[ 0  0  1  0 | 1  1  0 ]</text>
      <path d="M 370 80 L 420 80" stroke="var(--gold)" stroke-width="3"/>
      <text x="395" y="70" text-anchor="middle" fill="var(--gold)" font-size="10">Crossover</text>
      <text x="440" y="85" fill="var(--success)" font-size="11" font-weight="bold">Filho Crossover:</text>
      <rect x="540" y="70" width="220" height="24" rx="4" fill="rgba(0,255,102,0.2)" stroke="var(--success)"/>
      <text x="650" y="86" text-anchor="middle" fill="var(--text)" font-family="monospace" font-weight="bold">[ 1  1  0  1 | 1  1  0 ]</text>
      <text x="440" y="145" fill="var(--accent-pink)" font-size="11" font-weight="bold">Após Mutação:</text>
      <rect x="540" y="130" width="220" height="24" rx="4" fill="rgba(255,0,85,0.3)" stroke="var(--accent-pink)"/>
      <text x="650" y="146" text-anchor="middle" fill="var(--text)" font-family="monospace" font-weight="bold">[ 1  1  0  0*| 1  1  0 ]</text>
      <text x="400" y="195" text-anchor="middle" fill="var(--muted)" font-size="11">Cromossomo de Alocação de PMUs: 1 = PMU instalada na barra, 0 = Sem PMU</text>
    </svg>
    ''',
    3: '''
    <svg viewBox="0 0 800 220" style="width:100%;height:auto;background:var(--surface2);border-radius:14px;border:1px solid var(--border);padding:10px;">
      <text x="400" y="25" text-anchor="middle" fill="var(--accent)" font-weight="bold" font-size="14" font-family="Orbitron">VETOR MUTANTE NA EVOLUÇÃO DIFERENCIAL: v_i = x_r1 + F * (x_r2 - x_r3)</text>
      <circle cx="150" cy="140" r="6" fill="var(--accent)"/>
      <text x="140" y="160" fill="var(--accent)" font-weight="bold" font-size="12">x_r1 (Base)</text>
      <circle cx="350" cy="140" r="6" fill="var(--gold)"/>
      <text x="350" y="160" fill="var(--gold)" font-weight="bold" font-size="12">x_r2</text>
      <circle cx="350" cy="70" r="6" fill="var(--accent-pink)"/>
      <text x="350" y="60" fill="var(--accent-pink)" font-weight="bold" font-size="12">x_r3</text>
      <line x1="350" y1="70" x2="350" y2="140" stroke="var(--gold)" stroke-width="2" stroke-dasharray="4,4"/>
      <text x="375" y="105" fill="var(--gold)" font-size="11">(x_r2 - x_r3)</text>
      <line x1="150" y1="140" x2="520" y2="70" stroke="var(--success)" stroke-width="3"/>
      <circle cx="520" cy="70" r="8" fill="var(--success)"/>
      <text x="535" y="75" fill="var(--success)" font-weight="bold" font-size="13">v_i (Vetor Mutante)</text>
      <text x="400" y="195" text-anchor="middle" fill="var(--muted)" font-size="11">Fator de Escala F dimensiona a perturbação no espaço de busca contínuo</text>
    </svg>
    ''',
    4: '''
    <svg viewBox="0 0 800 220" style="width:100%;height:auto;background:var(--surface2);border-radius:14px;border:1px solid var(--border);padding:10px;">
      <text x="400" y="25" text-anchor="middle" fill="var(--gold)" font-weight="bold" font-size="14" font-family="Orbitron">OTIMIZAÇÃO EM ENXAME (PSO & ACO) PARA ROTEAMENTO DE DADOS</text>
      <circle cx="120" cy="80" r="10" fill="var(--accent)"/>
      <text x="120" y="105" text-anchor="middle" fill="var(--accent)" font-size="11">Partícula 1</text>
      <circle cx="150" cy="160" r="10" fill="var(--accent)"/>
      <text x="150" y="185" text-anchor="middle" fill="var(--accent)" font-size="11">Partícula 2</text>
      <circle cx="400" cy="90" r="12" fill="var(--gold)"/>
      <text x="400" y="70" text-anchor="middle" fill="var(--gold)" font-weight="bold" font-size="11">pbest (Melhor Individual)</text>
      <circle cx="680" cy="120" r="16" fill="var(--success)"/>
      <text x="680" y="155" text-anchor="middle" fill="var(--success)" font-weight="bold" font-size="12">gbest (Global Best / SCADA)</text>
      <path d="M 130 80 Q 260 50 388 90" stroke="var(--accent)" stroke-width="2" fill="none" stroke-dasharray="4,4"/>
      <path d="M 412 90 Q 540 100 664 120" stroke="var(--gold)" stroke-width="3" fill="none"/>
      <text x="400" y="200" text-anchor="middle" fill="var(--muted)" font-size="11">Partículas convergem para o nó de menor latência e custo via atração social e cognitiva</text>
    </svg>
    ''',
    5: '''
    <svg viewBox="0 0 800 220" style="width:100%;height:auto;background:var(--surface2);border-radius:14px;border:1px solid var(--border);padding:10px;">
      <text x="400" y="25" text-anchor="middle" fill="var(--accent)" font-weight="bold" font-size="14" font-family="Orbitron">FLUXOGRAMA DA ESTIMAÇÃO DE ESTADO WLS (MÍNIMOS QUADRADOS PONDERADOS)</text>
      <rect x="50" y="70" width="140" height="60" rx="8" fill="rgba(255,0,85,0.15)" stroke="var(--accent-pink)" stroke-width="2"/>
      <text x="120" y="98" text-anchor="middle" fill="var(--text)" font-size="11" font-weight="bold">Medições (z)</text>
      <text x="120" y="115" text-anchor="middle" fill="var(--accent-pink)" font-size="10">UTRs & PMUs com Ruído</text>
      <line x1="190" y1="100" x2="260" y2="100" stroke="var(--accent)" stroke-width="3"/>
      <rect x="260" y="70" width="280" height="60" rx="8" fill="rgba(0,243,255,0.15)" stroke="var(--accent)" stroke-width="2"/>
      <text x="400" y="95" text-anchor="middle" fill="var(--accent)" font-size="12" font-weight="bold">ALGORITMO ESTIMADOR WLS</text>
      <text x="400" y="115" text-anchor="middle" fill="var(--text)" font-size="10">Minimiza J(x) = Σ (z_i - h_i(x))² / σ²</text>
      <line x1="540" y1="100" x2="610" y2="100" stroke="var(--success)" stroke-width="3"/>
      <rect x="610" y="70" width="140" height="60" rx="8" fill="rgba(0,255,102,0.15)" stroke="var(--success)" stroke-width="2"/>
      <text x="680" y="98" text-anchor="middle" fill="var(--text)" font-size="11" font-weight="bold">Estado Estimado (x)</text>
      <text x="680" y="115" text-anchor="middle" fill="var(--success)" font-size="10">Tensões (V) e Ângulos (θ)</text>
      <text x="400" y="185" text-anchor="middle" fill="var(--muted)" font-size="11">Permite o Teste de Resíduos para Rejeição de Maus Dados (Bad Data)</text>
    </svg>
    ''',
    6: '''
    <svg viewBox="0 0 800 220" style="width:100%;height:auto;background:var(--surface2);border-radius:14px;border:1px solid var(--border);padding:10px;">
      <text x="400" y="25" text-anchor="middle" fill="var(--accent-pink)" font-weight="bold" font-size="14" font-family="Orbitron">RECONFIGURAÇÃO DE REDE DE DISTRIBUIÇÃO (TIE-SWITCHES & RADIALIDADE)</text>
      <rect x="60" y="60" width="100" height="50" rx="6" fill="rgba(0,243,255,0.2)" stroke="var(--accent)"/>
      <text x="110" y="90" text-anchor="middle" fill="var(--text)" font-size="11" font-weight="bold">Alimentador A</text>
      <line x1="160" y1="85" x2="350" y2="85" stroke="var(--accent)" stroke-width="3"/>
      <circle cx="250" cy="85" r="10" fill="var(--success)"/>
      <text x="250" y="110" text-anchor="middle" fill="var(--success)" font-size="10">NC (Fechada)</text>
      <circle cx="400" cy="85" r="14" fill="var(--surface)" stroke="var(--accent-pink)" stroke-width="3"/>
      <text x="400" y="90" text-anchor="middle" fill="var(--accent-pink)" font-size="10" font-weight="bold">S1</text>
      <text x="400" y="115" text-anchor="middle" fill="var(--accent-pink)" font-size="10">NO (Tie-Switch)</text>
      <line x1="450" y1="85" x2="640" y2="85" stroke="var(--gold)" stroke-width="3"/>
      <circle cx="550" cy="85" r="10" fill="var(--success)"/>
      <text x="550" y="110" text-anchor="middle" fill="var(--success)" font-size="10">NC (Fechada)</text>
      <rect x="640" y="60" width="100" height="50" rx="6" fill="rgba(255,183,0,0.2)" stroke="var(--gold)"/>
      <text x="690" y="90" text-anchor="middle" fill="var(--text)" font-size="11" font-weight="bold">Alimentador B</text>
      <text x="400" y="185" text-anchor="middle" fill="var(--muted)" font-size="11">Abertura e fechamento coordenados garantem a redução de perdas I²R mantendo a estrutura radial</text>
    </svg>
    ''',
    7: '''
    <svg viewBox="0 0 800 220" style="width:100%;height:auto;background:var(--surface2);border-radius:14px;border:1px solid var(--border);padding:10px;">
      <text x="400" y="25" text-anchor="middle" fill="var(--gold)" font-weight="bold" font-size="14" font-family="Orbitron">ARQUITETURA DE MICROGRID & USINA VIRTUAL DE ENERGIA (VPP)</text>
      <rect x="60" y="60" width="120" height="60" rx="8" fill="rgba(255,183,0,0.2)" stroke="var(--gold)" stroke-width="2"/>
      <text x="120" y="95" text-anchor="middle" fill="var(--text)" font-size="12" font-weight="bold">SOLAR PV</text>
      <rect x="240" y="60" width="120" height="60" rx="8" fill="rgba(0,255,102,0.2)" stroke="var(--success)" stroke-width="2"/>
      <text x="300" y="95" text-anchor="middle" fill="var(--text)" font-size="12" font-weight="bold">BATERIA BESS</text>
      <rect x="420" y="60" width="120" height="60" rx="8" fill="rgba(0,243,255,0.2)" stroke="var(--accent)" stroke-width="2"/>
      <text x="480" y="95" text-anchor="middle" fill="var(--text)" font-size="12" font-weight="bold">CARGAS / HEMS</text>
      <rect x="600" y="60" width="140" height="60" rx="8" fill="rgba(157,78,221,0.2)" stroke="var(--accent-purple)" stroke-width="2"/>
      <text x="670" y="88" text-anchor="middle" fill="var(--text)" font-size="12" font-weight="bold">REDE PRINCIPAL</text>
      <text x="670" y="105" text-anchor="middle" fill="var(--accent-purple)" font-size="10">Disjuntor de Ilhamento</text>
      <path d="M 120 120 L 400 170 M 300 120 L 400 170 M 480 120 L 400 170 M 670 120 L 400 170" stroke="var(--gold)" stroke-width="2" stroke-dasharray="4,4"/>
      <circle cx="400" cy="170" r="22" fill="var(--surface)" stroke="var(--gold)" stroke-width="2"/>
      <text x="400" y="175" text-anchor="middle" fill="var(--gold)" font-weight="bold" font-size="11">VPP</text>
      <text x="400" y="210" text-anchor="middle" fill="var(--muted)" font-size="10">O sistema alterna entre modo conectado e ilhado garantindo a resiliência energética</text>
    </svg>
    ''',
    8: '''
    <svg viewBox="0 0 800 220" style="width:100%;height:auto;background:var(--surface2);border-radius:14px;border:1px solid var(--border);padding:10px;">
      <text x="400" y="25" text-anchor="middle" fill="var(--accent-pink)" font-weight="bold" font-size="14" font-family="Orbitron">FRONTEIRA DE PARETO MULTI-OBJETIVO (HEMS + NSGA-II)</text>
      <line x1="100" y1="170" x2="700" y2="170" stroke="var(--muted)" stroke-width="2"/>
      <text x="400" y="200" text-anchor="middle" fill="var(--muted)" font-size="11">Objetivo 1: Custo da Energia Elétrica (R$)</text>
      <line x1="100" y1="170" x2="100" y2="50" stroke="var(--muted)" stroke-width="2"/>
      <text x="45" y="110" text-anchor="middle" fill="var(--muted)" font-size="11" transform="rotate(-90 45 110)">Objetivo 2: Desconforto</text>
      <path d="M 140 60 Q 200 150 650 160" stroke="var(--accent-pink)" stroke-width="4" fill="none"/>
      <circle cx="160" cy="72" r="7" fill="var(--gold)"/>
      <text x="210" y="70" fill="var(--gold)" font-size="10" font-weight="bold">Conforto Máximo (Custo Alto)</text>
      <circle cx="340" cy="142" r="7" fill="var(--accent)"/>
      <text x="360" y="130" fill="var(--accent)" font-size="10" font-weight="bold">Ponto de Equilíbrio HEMS</text>
      <circle cx="600" cy="158" r="7" fill="var(--success)"/>
      <text x="600" y="145" fill="var(--success)" font-size="10" font-weight="bold">Economia Máxima</text>
      <text x="500" y="75" fill="var(--muted)" font-size="11">Soluções Não-Dominadas (NSGA-II)</text>
    </svg>
    ''',
    9: '''
    <svg viewBox="0 0 800 220" style="width:100%;height:auto;background:var(--surface2);border-radius:14px;border:1px solid var(--border);padding:10px;">
      <text x="400" y="25" text-anchor="middle" fill="var(--accent)" font-weight="bold" font-size="14" font-family="Orbitron">ARQUITETURA DE REDE NEURAL PROFUNDA (LSTM) PARA PREVISÃO DE CARGA</text>
      <circle cx="120" cy="70" r="14" fill="rgba(0,243,255,0.2)" stroke="var(--accent)" stroke-width="2"/>
      <circle cx="120" cy="115" r="14" fill="rgba(0,243,255,0.2)" stroke="var(--accent)" stroke-width="2"/>
      <circle cx="120" cy="160" r="14" fill="rgba(0,243,255,0.2)" stroke="var(--accent)" stroke-width="2"/>
      <text x="120" y="195" text-anchor="middle" fill="var(--muted)" font-size="11">Entrada (Histórico)</text>
      <rect x="260" y="55" width="100" height="120" rx="10" fill="rgba(157,78,221,0.2)" stroke="var(--accent-purple)" stroke-width="2"/>
      <text x="310" y="110" text-anchor="middle" fill="var(--text)" font-weight="bold" font-size="12">CAMADA 1</text>
      <text x="310" y="130" text-anchor="middle" fill="var(--accent-purple)" font-size="10">128 Células LSTM</text>
      <rect x="460" y="55" width="100" height="120" rx="10" fill="rgba(255,0,85,0.2)" stroke="var(--accent-pink)" stroke-width="2"/>
      <text x="510" y="110" text-anchor="middle" fill="var(--text)" font-weight="bold" font-size="12">CAMADA 2</text>
      <text x="510" y="130" text-anchor="middle" fill="var(--accent-pink)" font-size="10">64 Células LSTM</text>
      <circle cx="680" cy="115" r="18" fill="rgba(0,255,102,0.2)" stroke="var(--success)" stroke-width="2"/>
      <text x="680" y="120" text-anchor="middle" fill="var(--success)" font-weight="bold" font-size="12">STLF</text>
      <text x="680" y="155" text-anchor="middle" fill="var(--success)" font-size="11">Previsão de Carga (kW)</text>
      <line x1="134" y1="115" x2="260" y2="115" stroke="var(--accent)" stroke-width="2"/>
      <line x1="360" y1="115" x2="460" y2="115" stroke="var(--accent-purple)" stroke-width="2"/>
      <line x1="560" y1="115" x2="662" y2="115" stroke="var(--accent-pink)" stroke-width="2"/>
    </svg>
    ''',
    10: '''
    <svg viewBox="0 0 800 220" style="width:100%;height:auto;background:var(--surface2);border-radius:14px;border:1px solid var(--border);padding:10px;">
      <text x="400" y="25" text-anchor="middle" fill="var(--success)" font-weight="bold" font-size="14" font-family="Orbitron">PIPELINE DE BIG DATA ANALYTICS & DETECÇÃO DE ANOMALIAS</text>
      <rect x="50" y="65" width="140" height="70" rx="8" fill="rgba(0,243,255,0.15)" stroke="var(--accent)" stroke-width="2"/>
      <text x="120" y="95" text-anchor="middle" fill="var(--text)" font-weight="bold" font-size="12">MEDIDORES AMI</text>
      <text x="120" y="115" text-anchor="middle" fill="var(--accent)" font-size="10">Petabytes de Leituras</text>
      <line x1="190" y1="100" x2="270" y2="100" stroke="var(--accent)" stroke-width="3"/>
      <rect x="270" y="65" width="260" height="70" rx="8" fill="rgba(255,183,0,0.15)" stroke="var(--gold)" stroke-width="2"/>
      <text x="400" y="95" text-anchor="middle" fill="var(--gold)" font-weight="bold" font-size="12">SPARK STREAMING</text>
      <text x="400" y="115" text-anchor="middle" fill="var(--text)" font-size="10">Processamento dos 5 V's em Tempo Real</text>
      <line x1="530" y1="100" x2="610" y2="100" stroke="var(--success)" stroke-width="3"/>
      <rect x="610" y="65" width="140" height="70" rx="8" fill="rgba(0,255,102,0.15)" stroke="var(--success)" stroke-width="2"/>
      <text x="680" y="95" text-anchor="middle" fill="var(--text)" font-weight="bold" font-size="12">ANALYTICS & FRAUDE</text>
      <text x="680" y="115" text-anchor="middle" fill="var(--success)" font-size="10">Alarmes de Anomalia</text>
      <text x="400" y="185" text-anchor="middle" fill="var(--muted)" font-size="11">Monitoramento de Volume, Velocidade, Variedade, Veracidade e Valor</text>
    </svg>
    '''
}

# Simulators Code for each Aula
simulators = {
    1: '''
      <div class="sim-controls">
        <div class="control-box"><label>Carga Total (MW):</label><input type="number" id="simLoad" value="15" min="1" max="50" onchange="runSim1()"></div>
        <div class="control-box"><label>Densidade AMI (%):</label><input type="range" id="simAmi" value="80" min="0" max="100" oninput="runSim1()"><span id="amiVal" style="color:var(--accent)">80%</span></div>
        <div class="control-box"><label>Modo de Operação:</label><select id="simMode" onchange="runSim1()"><option value="smart">Smart Grid (Automação & Self-Healing)</option><option value="trad">Rede Tradicional (Manual)</option></select></div>
      </div>
      <div class="sim-display">
        <h3 style="color:var(--accent);margin-bottom:12px;" id="simResTitle">Resultado do Evento de Falta</h3>
        <p id="simResText">Clique para calcular...</p>
        <div style="display:flex;justify-content:space-around;margin-top:20px;">
          <div><div style="font-size:1.8rem;font-weight:800;color:var(--gold)" id="resTime">0.5s</div><div style="font-size:0.78rem;color:var(--muted)">Tempo de Restauração</div></div>
          <div><div style="font-size:1.8rem;font-weight:800;color:var(--success)" id="resRestored">92%</div><div style="font-size:0.78rem;color:var(--muted)">Clientes Reestabelecidos</div></div>
        </div>
      </div>
      <script>
      function runSim1() {
        const load = parseFloat(document.getElementById('simLoad').value);
        const ami = parseFloat(document.getElementById('simAmi').value);
        const mode = document.getElementById('simMode').value;
        document.getElementById('amiVal').innerText = ami + '%';
        if (mode === 'smart') {
          document.getElementById('simResTitle').innerText = '⚡ Restauração Automática (Smart Grid)';
          document.getElementById('simResText').innerText = 'Falta isolada com sucesso! As chaves automáticas religaram o trecho saudável em segundos.';
          document.getElementById('resTime').innerText = (1.5 - (ami / 200)).toFixed(2) + 's';
          document.getElementById('resRestored').innerText = Math.round(85 + (ami * 0.14)) + '%';
        } else {
          document.getElementById('simResTitle').innerText = '⚠️ Interrupção Manual (Rede Tradicional)';
          document.getElementById('simResText').innerText = 'Equipe de campo precisa ser deslocada fisicamente até a subestação.';
          document.getElementById('resTime').innerText = '1h 45min';
          document.getElementById('resRestored').innerText = '0%';
        }
      }
      runSim1();
      </script>
    ''',
    2: '''
      <div class="sim-controls">
        <div class="control-box"><label>População:</label><input type="number" id="gaPop" value="30" min="10" max="100"></div>
        <div class="control-box"><label>Taxa de Crossover (%):</label><input type="number" id="gaCross" value="80" min="50" max="100"></div>
        <div class="control-box"><label>Taxa de Mutação (%):</label><input type="number" id="gaMut" value="5" min="1" max="30"></div>
        <div class="control-box"><label>Gerações Máximas:</label><input type="number" id="gaGen" value="50" min="10" max="200"></div>
      </div>
      <button class="btn-run" onclick="runGA()">⚡ Executar Algoritmo Genético</button>
      <div class="sim-display" style="margin-top:20px;">
        <div style="display:flex;justify-content:space-between;align-items:center;">
          <span style="font-weight:700;color:var(--accent);">Geração Atual: <span id="curGen">0</span> / <span id="maxGen">50</span></span>
          <span style="font-weight:700;color:var(--success);">Melhor Aptidão (Fitness): <span id="bestFit">—</span></span>
        </div>
        <div style="background:var(--surface2);height:10px;border-radius:5px;overflow:hidden;margin:12px 0;">
          <div id="gaProgress" style="height:100%;width:0%;background:linear-gradient(90deg, var(--accent), var(--accent-pink));transition:width 0.1s;"></div>
        </div>
        <p id="gaLog" style="font-family:monospace;font-size:0.85rem;color:var(--muted);">Aguardando execução...</p>
      </div>
      <script>
      function runGA() {
        const pop = parseInt(document.getElementById('gaPop').value);
        const genMax = parseInt(document.getElementById('gaGen').value);
        document.getElementById('maxGen').innerText = genMax;
        let g = 0, currentBest = 14;
        const timer = setInterval(() => {
          g++;
          document.getElementById('curGen').innerText = g;
          document.getElementById('gaProgress').style.width = (g / genMax * 100) + '%';
          if (g > 5 && Math.random() > 0.4 && currentBest > 4) currentBest--;
          document.getElementById('bestFit').innerText = `${currentBest} PMUs (Observabilidade 100%)`;
          document.getElementById('gaLog').innerText = `[Geração ${g}] População: ${pop} | Mutação aplicada | Melhor Solução: ${currentBest} PMUs instaladas nas barras [2, 6, 9, 14]`;
          if (g >= genMax) { clearInterval(timer); document.getElementById('gaLog').innerText = `✅ Convergência concluída! Solução ótima com ${currentBest} PMUs!`; }
        }, 40);
      }
      </script>
    ''',
    3: '''
      <div class="sim-controls">
        <div class="control-box"><label>Fator de Escala (F):</label><input type="number" id="deF" value="0.7" step="0.1" min="0.1" max="2.0"></div>
        <div class="control-box"><label>Taxa de Crossover (CR):</label><input type="number" id="deCR" value="0.9" step="0.05" min="0.1" max="1.0"></div>
        <div class="control-box"><label>População (Np):</label><input type="number" id="deNp" value="25" min="10" max="100"></div>
      </div>
      <button class="btn-run" onclick="runDE()">⚡ Calcular Mutação Vetorial & Iterar ED</button>
      <div class="sim-display" style="margin-top:20px;">
        <h4 style="color:var(--accent);margin-bottom:8px;">Vetor Mutante Gerado (v_i):</h4>
        <div id="deVectorOut" style="font-family:monospace;font-size:1rem;color:#fff;background:var(--surface2);padding:12px;border-radius:8px;">v_i = [12.4, 0.85, 4.12, 118.6]</div>
        <div style="margin-top:14px;display:flex;justify-content:space-around;color:var(--muted);font-size:0.88rem;">
          <span>Perdas Iniciais: <b style="color:#ef4444" id="deInitLoss">450 kW</b></span>
          <span>Perdas Otimizadas: <b style="color:var(--success)" id="deOptLoss">210 kW</b></span>
        </div>
      </div>
      <script>
      function runDE() {
        const F = parseFloat(document.getElementById('deF').value);
        const CR = parseFloat(document.getElementById('deCR').value);
        const v1 = (10 + F * 3.4).toFixed(2);
        const v2 = (0.8 + F * 0.12).toFixed(2);
        const v3 = (4.0 + F * 1.1).toFixed(2);
        const v4 = (115 + F * 6.5).toFixed(1);
        document.getElementById('deVectorOut').innerText = `v_i = [${v1}, ${v2}, ${v3}, ${v4}] (CR=${CR})`;
        document.getElementById('deOptLoss').innerText = `${Math.round(450 * (1 - (F * 0.25 + CR * 0.3)))} kW`;
      }
      </script>
    ''',
    4: '''
      <div class="sim-controls">
        <div class="control-box"><label>Algoritmo:</label><select id="swarmAlg"><option value="pso">PSO (Particle Swarm Optimization)</option><option value="aco">ACO (Ant Colony Optimization)</option></select></div>
        <div class="control-box"><label>Coeficiente Cognitivo (c1):</label><input type="number" id="swC1" value="2.0" step="0.1"></div>
        <div class="control-box"><label>Coeficiente Social (c2):</label><input type="number" id="swC2" value="2.0" step="0.1"></div>
      </div>
      <button class="btn-run" onclick="runSwarm()">⚡ Simular Roteamento em Tempo Real</button>
      <div class="sim-display" style="margin-top:20px;">
        <h4 style="color:var(--gold);margin-bottom:8px;" id="swarmStatus">Status do Roteamento: Pronto</h4>
        <div style="display:flex;justify-content:space-around;margin-top:14px;">
          <div><div style="font-size:1.6rem;font-weight:800;color:var(--accent)" id="swLatency">12 ms</div><div style="font-size:0.78rem;color:var(--muted)">Latência de Rede</div></div>
          <div><div style="font-size:1.6rem;font-weight:800;color:var(--success)" id="swLoss">0.01%</div><div style="font-size:0.78rem;color:var(--muted)">Perda de Pacotes</div></div>
        </div>
      </div>
      <script>
      function runSwarm() {
        const alg = document.getElementById('swarmAlg').value;
        const c1 = parseFloat(document.getElementById('swC1').value);
        const c2 = parseFloat(document.getElementById('swC2').value);
        const lat = Math.max(5, Math.round(25 / (c1 + c2)));
        document.getElementById('swarmStatus').innerText = `⚡ Roteamento Convergido via ${alg.toUpperCase()}!`;
        document.getElementById('swLatency').innerText = `${lat} ms`;
        document.getElementById('swLoss').innerText = `${(0.05 / (c1 * 0.5 + c2 * 0.5)).toFixed(3)}%`;
      }
      </script>
    ''',
    5: '''
      <div class="sim-controls">
        <div class="control-box"><label>Tensão Medida z1 (kV):</label><input type="number" id="wlsZ1" value="13.8" step="0.1"></div>
        <div class="control-box"><label>Tensão Medida z2 (kV):</label><input type="number" id="wlsZ2" value="13.7" step="0.1"></div>
        <div class="control-box"><label>Injetar Mau Dado (Bad Data):</label><select id="wlsBadData"><option value="none">Nenhum (Ruído Normal)</option><option value="spike">Erro na Medição 2 (+3.0 kV)</option></select></div>
      </div>
      <button class="btn-run" onclick="runWLS()">⚡ Executar Estimação de Estado WLS</button>
      <div class="sim-display" style="margin-top:20px;">
        <h4 style="color:var(--accent);margin-bottom:8px;">Resultado da Estimação do Estado (V_estimado):</h4>
        <div style="font-family:monospace;font-size:1.2rem;color:#fff;background:var(--surface2);padding:14px;border-radius:8px;text-align:center;">
          V_est = <span id="wlsResVal" style="color:var(--success);font-weight:800;">13.78 kV</span> (Ângulo θ = -2.14°)
        </div>
        <div style="margin-top:14px;display:flex;justify-content:space-between;color:var(--muted);font-size:0.88rem;">
          <span>Resíduo Ponderado J(x): <b style="color:var(--accent)" id="wlsJval">0.14</b></span>
          <span>Teste de Mau Dado (χ²): <b style="color:var(--success)" id="wlsBadRes">APROVADO (Sem mau dado)</b></span>
        </div>
      </div>
      <script>
      function runWLS() {
        const z1 = parseFloat(document.getElementById('wlsZ1').value);
        let z2 = parseFloat(document.getElementById('wlsZ2').value);
        const bad = document.getElementById('wlsBadData').value;
        if (bad === 'spike') z2 += 3.0;
        const wlsEst = ((z1 + z2) / 2).toFixed(2);
        document.getElementById('wlsResVal').innerText = `${wlsEst} kV`;
        document.getElementById('wlsJval').innerText = (Math.abs(z1 - z2) * 1.8).toFixed(2);
        if (bad === 'spike') document.getElementById('wlsBadRes').innerHTML = '<span style="color:#ef4444">⚠️ REJEITADO (Mau dado detectado no canal 2!)</span>';
        else document.getElementById('wlsBadRes').innerHTML = '<span style="color:var(--success)">✅ APROVADO (Sem mau dado)</span>';
      }
      </script>
    ''',
    6: '''
      <div class="sim-controls">
        <div class="control-box"><label>Chave Tie-Switch (S1):</label><select id="rsS1"><option value="open">Aberta (NO - Padrão)</option><option value="closed">Fechada (NC)</option></select></div>
        <div class="control-box"><label>Chave Seccionadora A (S2):</label><select id="rsS2"><option value="closed">Fechada (NC)</option><option value="open">Aberta (NO)</option></select></div>
        <div class="control-box"><label>Chave Seccionadora B (S3):</label><select id="rsS3"><option value="closed">Fechada (NC)</option><option value="open">Aberta (NO)</option></select></div>
      </div>
      <button class="btn-run" onclick="runRS()">⚡ Reconfigurar Topologia & Calcular Perdas</button>
      <div class="sim-display" style="margin-top:20px;">
        <h4 style="color:var(--accent-pink);margin-bottom:8px;" id="rsStatus">Status da Topologia: Radial Válida</h4>
        <div style="display:flex;justify-content:space-around;margin-top:14px;">
          <div><div style="font-size:1.6rem;font-weight:800;color:var(--gold)" id="rsLoss">320 kW</div><div style="font-size:0.78rem;color:var(--muted)">Perdas Elétricas (I²R)</div></div>
          <div><div style="font-size:1.6rem;font-weight:800;color:var(--success)" id="rsRadial">VÁLIDA</div><div style="font-size:0.78rem;color:var(--muted)">Radialidade da Rede</div></div>
        </div>
      </div>
      <script>
      function runRS() {
        const s1 = document.getElementById('rsS1').value;
        const s2 = document.getElementById('rsS2').value;
        const s3 = document.getElementById('rsS3').value;
        if (s1 === 'closed' && s2 === 'closed' && s3 === 'closed') {
          document.getElementById('rsStatus').innerText = '⚠️ VIOLAÇÃO: LAÇO FECHADO DE CORRENTE!';
          document.getElementById('rsRadial').innerHTML = '<span style="color:#ef4444">INVÁLIDA (MALHA)</span>';
          document.getElementById('rsLoss').innerText = '0 kW (Disjuntor Atuado)';
          return;
        }
        if (s1 === 'closed' && s2 === 'open' && s3 === 'closed') {
          document.getElementById('rsStatus').innerText = '⚡ Topologia Otimizada Encontrada!';
          document.getElementById('rsRadial').innerHTML = '<span style="color:var(--success)">VÁLIDA</span>';
          document.getElementById('rsLoss').innerText = '210 kW (-34% de Perdas)';
          return;
        }
        document.getElementById('rsStatus').innerText = 'Topologia Radial Convencional Mantida';
        document.getElementById('rsRadial').innerHTML = '<span style="color:var(--success)">VÁLIDA</span>';
        document.getElementById('rsLoss').innerText = '320 kW';
      }
      </script>
    ''',
    7: '''
      <div class="sim-controls">
        <div class="control-box"><label>Geração Solar PV (kW):</label><input type="number" id="mgSolar" value="50" min="0" max="100" onchange="runMicrogrid()"></div>
        <div class="control-box"><label>Demanda de Carga (kW):</label><input type="number" id="mgLoad" value="35" min="5" max="100" onchange="runMicrogrid()"></div>
        <div class="control-box"><label>Modo da Microgrid:</label><select id="mgMode" onchange="runMicrogrid()"><option value="grid">Conectado à Rede</option><option value="island">Modo Ilhado (Islanded)</option></select></div>
      </div>
      <button class="btn-run" onclick="runMicrogrid()">⚡ Simular Balanço de Potência</button>
      <div class="sim-display" style="margin-top:20px;">
        <h4 style="color:var(--gold);margin-bottom:8px;" id="mgStatus">Status do Despacho: Equilibrado</h4>
        <div style="display:flex;justify-content:space-around;margin-top:14px;">
          <div><div style="font-size:1.6rem;font-weight:800;color:var(--success)" id="mgBessAction">Carga (+15 kW)</div><div style="font-size:0.78rem;color:var(--muted)">Ação da Bateria BESS</div></div>
          <div><div style="font-size:1.6rem;font-weight:800;color:var(--accent)" id="mgGridFlow">Exportação (0 kW)</div><div style="font-size:0.78rem;color:var(--muted)">Fluxo com a Rede Principal</div></div>
        </div>
      </div>
      <script>
      function runMicrogrid() {
        const solar = parseFloat(document.getElementById('mgSolar').value);
        const load = parseFloat(document.getElementById('mgLoad').value);
        const mode = document.getElementById('mgMode').value;
        const diff = solar - load;
        if (diff > 0) {
          document.getElementById('mgBessAction').innerText = `Carregando (+${diff} kW)`;
          document.getElementById('mgGridFlow').innerText = mode === 'grid' ? `Exportando (${(diff*0.4).toFixed(1)} kW)` : 'Isolado (0 kW)';
          document.getElementById('mgStatus').innerText = '☀️ Excedente Solar Armazenado no BESS';
        } else {
          const def = Math.abs(diff);
          document.getElementById('mgBessAction').innerText = `Descarregando (-${def} kW)`;
          document.getElementById('mgGridFlow').innerText = mode === 'grid' ? `Importando (${(def*0.5).toFixed(1)} kW)` : 'Isolado (0 kW)';
          document.getElementById('mgStatus').innerText = '🔋 Suporte da Bateria para Carga';
        }
      }
      runMicrogrid();
      </script>
    ''',
    8: '''
      <div class="sim-controls">
        <div class="control-box"><label>Perfil de Preferência:</label><select id="hemsPref" onchange="runHems()"><option value="bal">Equilibrado (Custo Médio / Conforto Médio)</option><option value="eco">Economia Máxima (Tarifa Branca Baixa)</option><option value="comf">Conforto Máximo</option></select></div>
      </div>
      <button class="btn-run" onclick="runHems()">⚡ Gerar Soluções da Fronteira de Pareto</button>
      <div class="sim-display" style="margin-top:20px;">
        <h4 style="color:var(--accent-pink);margin-bottom:8px;">Ponto Selecionado na Fronteira de Pareto:</h4>
        <div style="display:flex;justify-content:space-around;margin-top:14px;">
          <div><div style="font-size:1.6rem;font-weight:800;color:var(--success)" id="hemsCost">R$ 145,00/mês</div><div style="font-size:0.78rem;color:var(--muted)">Custo Estimado de Energia</div></div>
          <div><div style="font-size:1.6rem;font-weight:800;color:var(--gold)" id="hemsDiscomfort">12%</div><div style="font-size:0.78rem;color:var(--muted)">Índice de Desconforto</div></div>
        </div>
      </div>
      <script>
      function runHems() {
        const pref = document.getElementById('hemsPref').value;
        if (pref === 'eco') {
          document.getElementById('hemsCost').innerText = 'R$ 98,50/mês (-35%)';
          document.getElementById('hemsDiscomfort').innerText = '28% (Horário flexível)';
        } else if (pref === 'comf') {
          document.getElementById('hemsCost').innerText = 'R$ 210,00/mês';
          document.getElementById('hemsDiscomfort').innerText = '2% (Conforto Máximo)';
        } else {
          document.getElementById('hemsCost').innerText = 'R$ 145,00/mês (-18%)';
          document.getElementById('hemsDiscomfort').innerText = '12% (Equilibrado)';
        }
      }
      </script>
    ''',
    9: '''
      <div class="sim-controls">
        <div class="control-box"><label>Arquitetura da Rede:</label><select id="dlArch"><option value="lstm">LSTM Profunda (2 Camadas 128 Unidades)</option><option value="cnn_lstm">Híbrida CNN-LSTM</option></select></div>
        <div class="control-box"><label>Número de Épocas:</label><input type="number" id="dlEpochs" value="30" min="5" max="100"></div>
      </div>
      <button class="btn-run" onclick="runDL()">⚡ Treinar Rede Neural Profunda</button>
      <div class="sim-display" style="margin-top:20px;">
        <h4 style="color:var(--accent);margin-bottom:8px;" id="dlStatus">Status do Treinamento: Não Iniciado</h4>
        <div style="display:flex;justify-content:space-around;margin-top:14px;">
          <div><div style="font-size:1.6rem;font-weight:800;color:var(--success)" id="dlMse">0.0024</div><div style="font-size:0.78rem;color:var(--muted)">Erro Quadrático Médio (MSE)</div></div>
          <div><div style="font-size:1.6rem;font-weight:800;color:var(--gold)" id="dlAcc">98.6%</div><div style="font-size:0.78rem;color:var(--muted)">Precisão da Previsão</div></div>
        </div>
      </div>
      <script>
      function runDL() {
        const epochs = parseInt(document.getElementById('dlEpochs').value);
        document.getElementById('dlStatus').innerText = `⏳ Treinando em ${epochs} épocas...`;
        setTimeout(() => {
          document.getElementById('dlStatus').innerText = `✅ Treinamento Concluído!`;
          document.getElementById('dlMse').innerText = (0.01 / (epochs * 0.1)).toFixed(4);
          document.getElementById('dlAcc').innerText = `${(94 + (epochs * 0.08)).toFixed(1)}%`;
        }, 500);
      }
      </script>
    ''',
    10: '''
      <div class="sim-controls">
        <div class="control-box"><label>Taxa de Ingestão (Medidores/s):</label><input type="number" id="bdRate" value="5000" step="1000"></div>
      </div>
      <button class="btn-run" onclick="runBigData()">⚡ Iniciar Processamento de Stream Big Data</button>
      <div class="sim-display" style="margin-top:20px;">
        <h4 style="color:var(--accent);margin-bottom:8px;" id="bdStatus">Status do Cluster Spark/Hadoop: Pronto</h4>
        <div style="display:flex;justify-content:space-around;margin-top:14px;">
          <div><div style="font-size:1.6rem;font-weight:800;color:var(--accent)" id="bdProcessed">0 leituras</div><div style="font-size:0.78rem;color:var(--muted)">Processados em Tempo Real</div></div>
          <div><div style="font-size:1.6rem;font-weight:800;color:var(--gold)" id="bdFrauds">0 alarme(s)</div><div style="font-size:0.78rem;color:var(--muted)">Anomalias Detectadas</div></div>
        </div>
      </div>
      <script>
      let count = 0;
      function runBigData() {
        const rate = parseInt(document.getElementById('bdRate').value);
        document.getElementById('bdStatus').innerText = `⚡ Processando ${rate} eventos/seg via Spark Streaming...`;
        let i = 0;
        const timer = setInterval(() => {
          i += rate; count += rate;
          document.getElementById('bdProcessed').innerText = `${(count / 1000).toFixed(0)}k leituras`;
          document.getElementById('bdFrauds').innerText = `${Math.round(count * 0.0003)} alarme(s)`;
          if (i > rate * 10) { clearInterval(timer); document.getElementById('bdStatus').innerText = `✅ Stream finalizado!`; }
        }, 300);
      }
      </script>
    '''
}

mapping = {
    '1-AulaDeIntroducaoDaDisciplina_Labtel.pptx': (1, 'Introdução a Smart Grids & Conceitos Fundamentais', '#00f3ff'),
    '2-AulaAG_Labtel.pptx': (2, 'Algoritmos Genéticos (AG) em Smart Grids', '#c77dff'),
    '3-AulaEvoluçãoDiferencial_Labtel.pptx': (3, 'Evolução Diferencial (ED) em Smart Grids', '#00ff66'),
    '4-AulaOTITelecPSOeACO_Labtel.pptx': (4, 'Otimização em Telecomunicações, PSO e ACO', '#ffb700'),
    '5-AulaEstimaçãoDeEstado_Labtel.pptx': (5, 'Estimação de Estado em Sistemas Elétricos (EE)', '#00f3ff'),
    '6-AulaPlanejOperacaoBTeRS_Labtel.pptx': (6, 'Operação BT & Reconfiguração de Redes (RS)', '#ff0055'),
    '7-GdMicrogridVPPeVNS_Labtel.pptx': (7, 'Geração Distribuída, Microgrids & VPP', '#ffb700'),
    '8-AulaSmartHomeRNAeNSGA_Labtel.pptx': (8, 'Smart Home, Redes Neurais & NSGA-II', '#ff0055'),
    '9-RedesNeuraisProfundas_Labtel.pptx': (9, 'Redes Neurais Profundas (Deep Learning)', '#00f3ff'),
    '10-BigDataScienceSG_Labtel.pptx': (10, 'Big Data & Data Science em Smart Grids', '#00ff66')
}

import re

for file_key, (num, title, color) in mapping.items():
    slides = slides_data.get(file_key, [])
    script_text = podcasts_scripts.get(num, "")
    svg_diagram = svg_figures.get(num, "")
    
    # Continuous Text Compilation (100% CLEAN OF "Slide X:" prefixes!)
    continuous_blocks = []
    for s_idx, s_text in enumerate(slides, 1):
        # 1. Strip all "Slide \d+:" or "Slide \d+" prefixes completely
        cleaned = re.sub(r'Slide\s+\d+:\s*', '', s_text.strip(), flags=re.IGNORECASE)
        cleaned = re.sub(r'Slide\s+\d+\b', '', cleaned, flags=re.IGNORECASE).strip()
        cleaned = re.sub(r'^\s*:\s*', '', cleaned) # Remove leading colon if left
        
        if not cleaned: continue
        
        lines = [l.strip() for l in cleaned.split('\n') if l.strip()]
        if not lines: lines = [cleaned]
        
        items = [it.strip() for it in lines[0].split(';') if it.strip()]
        
        block_html = '<div class="content-block">'
        if len(items) > 1:
            block_html += f'<h3 class="block-heading">{html.escape(items[0])}</h3>'
            bullet_items = items[1:]
            for extra_line in lines[1:]:
                sub_items = [it.strip() for it in extra_line.split(';') if it.strip()]
                bullet_items.extend(sub_items)
            if bullet_items:
                block_html += '<ul class="block-list">' + ''.join([f'<li>{html.escape(it)}</li>' for it in bullet_items]) + '</ul>'
        else:
            block_html += f'<h3 class="block-heading">{html.escape(lines[0])}</h3>'
            bullet_items = []
            for extra_line in lines[1:]:
                sub_items = [it.strip() for it in extra_line.split(';') if it.strip()]
                bullet_items.extend(sub_items)
            if bullet_items:
                block_html += '<ul class="block-list">' + ''.join([f'<li>{html.escape(it)}</li>' for it in bullet_items]) + '</ul>'
        
        block_html += '</div>'
        continuous_blocks.append(block_html)
    
    full_continuous_html = '\n'.join(continuous_blocks)
    
    html_content = f'''<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Aula {num}: {title}</title>
<script>
(function() {{
  const t = localStorage.getItem('sg_theme');
  if (t && t !== 'default') {{
    document.documentElement.setAttribute('data-theme', t);
  }}
}})();
</script>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700;800;900&family=Rajdhani:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root {{
  --bg: #03050d; --surface: rgba(10, 14, 28, 0.9); --surface2: rgba(18, 24, 48, 0.95);
  --border: rgba(0, 243, 255, 0.2); --accent: {color}; --gold: #ffb700; --success: #00ff66;
  --text: #f1f5f9; --muted: #8a99ad; --accent-pink: #ff0055;
}}

[data-theme="light"] {{
  --bg: #f8fafc;
  --surface: #ffffff;
  --surface2: #f1f5f9;
  --border: rgba(2, 132, 199, 0.25);
  --accent: #0284c7;
  --gold: #d97706;
  --success: #059669;
  --text: #0f172a;
  --muted: #475569;
  --accent-pink: #e11d48;
}}

* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: 'Rajdhani', 'Inter', sans-serif; background: var(--bg); color: var(--text); padding: 24px; transition: all 0.3s; }}
.container {{ max-width: 1050px; margin: 0 auto; }}

.hero-card {{ background: var(--surface); border: 1px solid var(--border); border-radius: 20px; padding: 28px; margin-bottom: 24px; position: relative; overflow: hidden; backdrop-filter: blur(20px); box-shadow: 0 0 30px rgba(0, 243, 255, 0.1); }}
.hero-card::before {{ content: ''; position: absolute; top:0; left:0; right:0; height:4px; background: linear-gradient(90deg, var(--accent), var(--accent-pink)); }}
.title {{ font-family: 'Orbitron', sans-serif; font-size: 1.8rem; font-weight: 800; color: var(--accent); margin-bottom: 8px; letter-spacing: 1px; }}
.subtitle {{ color: var(--muted); font-size: 0.98rem; margin-bottom: 16px; font-weight: 500; }}
.badge-group {{ display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 16px; }}
.badge {{ background: var(--surface2); border: 1px solid var(--border); border-radius: 8px; padding: 4px 10px; font-size: 0.78rem; font-weight: 700; color: var(--gold); font-family: 'Orbitron', sans-serif; }}

/* PODCAST CARD STYLING */
.podcast-card {{
  background: linear-gradient(135deg, var(--surface), var(--surface2));
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 22px;
  margin-bottom: 24px;
  box-shadow: 0 0 30px rgba(0, 243, 255, 0.15);
  position: relative;
  overflow: hidden;
}}
.podcast-card::before {{
  content: ''; position: absolute; top:0; left:0; right:0; height:3px;
  background: linear-gradient(90deg, var(--accent), var(--gold), var(--success));
}}
.podcast-header {{ display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 14px; margin-bottom: 14px; }}
.podcast-title {{ font-family: 'Orbitron', sans-serif; font-weight: 800; font-size: 1.1rem; color: var(--text); display: flex; align-items: center; gap: 10px; }}
.podcast-controls {{ display: flex; align-items: center; gap: 10px; }}

.btn-podcast {{
  background: linear-gradient(135deg, var(--accent), var(--accent-pink));
  color: #ffffff; padding: 10px 20px; border-radius: 12px; border: none;
  font-family: 'Orbitron', sans-serif; font-weight: 800; font-size: 0.88rem;
  cursor: pointer; display: flex; align-items: center; gap: 8px; box-shadow: 0 0 15px var(--accent); transition: all 0.2s;
}}
.btn-podcast:hover {{ transform: scale(1.04); }}

.podcast-speed {{ background: var(--surface); border: 1px solid var(--border); color: var(--text); padding: 8px 12px; border-radius: 10px; font-family: inherit; font-size: 0.85rem; cursor: pointer; outline: none; }}

.eq-bars {{ display: inline-flex; align-items: flex-end; gap: 3px; height: 16px; margin-left: 8px; }}
.eq-bar {{ width: 3px; background: var(--accent); border-radius: 2px; height: 4px; transition: height 0.2s; }}
.eq-bar.playing {{ animation: eqBounce 0.4s infinite alternate; }}
.eq-bar:nth-child(1) {{ animation-delay: 0.0s; }}
.eq-bar:nth-child(2) {{ animation-delay: 0.2s; }}
.eq-bar:nth-child(3) {{ animation-delay: 0.1s; }}
.eq-bar:nth-child(4) {{ animation-delay: 0.3s; }}
@keyframes eqBounce {{ 0% {{ height: 4px; }} 100% {{ height: 16px; }} }}

.podcast-transcript {{
  background: var(--surface2); border: 1px solid var(--border); border-radius: 12px; padding: 14px;
  font-size: 0.92rem; line-height: 1.6; color: var(--text); max-height: 120px; overflow-y: auto; white-space: pre-wrap; margin-top: 10px;
}}

/* TABS */
.tab-btns {{ display: flex; gap: 8px; margin-bottom: 20px; border-bottom: 1px solid var(--border); padding-bottom: 10px; overflow-x: auto; }}
.tab-btn {{ background: var(--surface2); border: 1px solid var(--border); color: var(--muted); padding: 10px 18px; border-radius: 12px; font-family: 'Orbitron', sans-serif; font-size: 0.8rem; font-weight: 700; cursor: pointer; transition: all 0.2s; flex-shrink: 0; }}
.tab-btn:hover {{ color: var(--text); border-color: var(--accent); }}
.tab-btn.active {{ background: var(--accent); color: #ffffff; border-color: var(--accent); box-shadow: 0 0 20px var(--accent); }}
.tab-content {{ display: none; }}
.tab-content.active {{ display: block; animation: fadeIn 0.3s ease; }}
@keyframes fadeIn {{ from {{ opacity:0; transform:translateY(8px); }} to {{ opacity:1; transform:translateY(0); }} }}

/* CONTINUOUS READING CONTENT */
.card {{ background: var(--surface); border: 1px solid var(--border); border-radius: 18px; padding: 26px; margin-bottom: 20px; backdrop-filter: blur(15px); }}
.card-title {{ font-family: 'Orbitron', sans-serif; font-size: 1.2rem; font-weight: 700; margin-bottom: 16px; color: var(--text); display: flex; align-items: center; gap: 8px; }}

.content-block {{ background: var(--surface2); border: 1px solid var(--border); border-radius: 14px; padding: 18px 22px; margin-bottom: 14px; transition: border-color 0.2s; }}
.content-block:hover {{ border-color: var(--accent); }}
.block-heading {{ font-family: 'Orbitron', sans-serif; font-size: 1.05rem; font-weight: 700; color: var(--accent); margin-bottom: 10px; }}
.block-list {{ margin-left: 20px; line-height: 1.7; font-size: 0.95rem; font-weight: 500; color: var(--text); }}
.block-list li {{ margin-bottom: 6px; }}

.sim-controls {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 14px; margin-bottom: 20px; background: var(--surface2); padding: 16px; border-radius: 12px; border: 1px solid var(--border); }}
.control-box {{ display: flex; flex-direction: column; gap: 6px; }}
.control-box label {{ font-size: 0.8rem; font-weight: 700; color: var(--muted); font-family: 'Orbitron', sans-serif; }}
.control-box input, .control-box select {{ padding: 8px 12px; background: var(--surface); border: 1px solid var(--border); color: var(--text); border-radius: 8px; outline: none; font-family: inherit; }}
.btn-run {{ padding: 12px 20px; background: linear-gradient(135deg, var(--accent), var(--accent-pink)); color: #ffffff; border: none; border-radius: 10px; font-family: 'Orbitron', sans-serif; font-weight: 800; cursor: pointer; margin-top: 10px; width: 100%; letter-spacing: 1px; box-shadow: 0 0 20px var(--accent); }}

.sim-display {{ background: var(--surface2); border-radius: 12px; padding: 20px; border: 1px solid var(--border); color: var(--text); }}
.quiz-opt {{ display: block; width: 100%; text-align: left; padding: 14px 18px; background: var(--surface2); border: 1px solid var(--border); color: var(--text); border-radius: 12px; margin-bottom: 10px; cursor: pointer; font-size: 0.95rem; font-family: 'Rajdhani', sans-serif; font-weight: 600; transition: all 0.2s; }}
.quiz-opt:hover {{ border-color: var(--accent); box-shadow: 0 0 15px var(--accent); }}
.quiz-opt.correct {{ background: rgba(0, 255, 102, 0.2); border-color: var(--success); }}
.quiz-opt.wrong {{ background: rgba(255, 0, 85, 0.2); border-color: var(--accent-pink); }}

.flashcard-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; }}
.flashcard {{ background: var(--surface2); border: 1px solid var(--border); border-radius: 14px; padding: 20px; height: 140px; display: flex; align-items: center; justify-content: center; text-align: center; cursor: pointer; transition: transform 0.4s; font-family: 'Rajdhani', sans-serif; font-size: 1rem; font-weight: 700; }}
.flashcard.flipped {{ background: var(--accent); color: #ffffff; font-weight: 800; }}

/* EXPLICIT LIGHT MODE OVERRIDES FOR LESSONS */
[data-theme="light"] body {{
  background-color: #f8fafc !important;
  color: #0f172a !important;
}}

[data-theme="light"] .card, 
[data-theme="light"] .hero-card, 
[data-theme="light"] .podcast-card {{
  background: #ffffff !important;
  box-shadow: 0 4px 20px rgba(2, 132, 199, 0.1) !important;
  border-color: rgba(2, 132, 199, 0.25) !important;
}}

[data-theme="light"] .content-block, 
[data-theme="light"] .sim-controls, 
[data-theme="light"] .sim-display, 
[data-theme="light"] .quiz-opt, 
[data-theme="light"] .flashcard, 
[data-theme="light"] .podcast-transcript {{
  background: #f1f5f9 !important;
  color: #0f172a !important;
  border-color: rgba(2, 132, 199, 0.25) !important;
}}

[data-theme="light"] .tab-btn {{
  background: #ffffff !important;
  color: #475569 !important;
  border-color: rgba(2, 132, 199, 0.25) !important;
}}

[data-theme="light"] .tab-btn.active {{
  color: #ffffff !important;
  background: #0284c7 !important;
  border-color: #0284c7 !important;
  box-shadow: 0 4px 15px rgba(2, 132, 199, 0.3) !important;
}}

[data-theme="light"] .btn-podcast, 
[data-theme="light"] .btn-run {{
  color: #ffffff !important;
  background: linear-gradient(135deg, #0284c7, #e11d48) !important;
}}
</style>
</head>
<body>

<div class="container">
  <!-- Hero Banner -->
  <div class="hero-card">
    <div class="badge-group">
      <span class="badge">AULA {num:02d}</span>
      <span class="badge">{len(slides)} TÓPICOS DA AULA</span>
      <span class="badge">PROF. HELDER / LABTEL</span>
    </div>
    <div class="title">{title}</div>
    <div class="subtitle">Texto teórico em leitura contínua, diagramas vetoriais SVG, podcast guiado com voz e ferramentas interativas.</div>
  </div>

  <!-- 🎙️ PODCAST CARD DA PROFESSORA BIA -->
  <div class="podcast-card">
    <div class="podcast-header">
      <div class="podcast-title">
        🎙️ PODCAST DA AULA {num} — PROFESSORA BIA
        <div class="eq-bars">
          <div class="eq-bar" id="eq1"></div>
          <div class="eq-bar" id="eq2"></div>
          <div class="eq-bar" id="eq3"></div>
          <div class="eq-bar" id="eq4"></div>
        </div>
      </div>
      <div class="podcast-controls">
        <button class="btn-podcast" onclick="togglePodcastPlay()">
          <span id="podIcon">▶️</span> <span id="podBtnTxt">Ouvir Podcast</span>
        </button>
        <select class="podcast-speed" id="podSpeed" onchange="changePodcastSpeed(this.value)">
          <option value="1.0">1.0x</option>
          <option value="1.15" selected>1.15x</option>
          <option value="1.3">1.3x</option>
          <option value="1.5">1.5x</option>
        </select>
      </div>
    </div>
    <div class="podcast-transcript" id="podTranscript">
{script_text}
    </div>
  </div>

  <!-- TABS -->
  <div class="tab-btns">
    <button class="tab-btn active" onclick="showSubTab('teoria')">📖 Conteúdo Teórico</button>
    <button class="tab-btn" onclick="showSubTab('diagrama')">🎨 Diagrama Ilustrativo</button>
    <button class="tab-btn" onclick="showSubTab('simulador')">⚡ Simulador Interativo</button>
    <button class="tab-btn" onclick="showSubTab('quiz')">📝 Quiz</button>
    <button class="tab-btn" onclick="showSubTab('flashcards')">🎴 Flashcards</button>
  </div>

  <!-- TAB 1: TEORIA CONTINUA -->
  <div id="teoria" class="tab-content active">
    <div class="card">
      <div class="card-title">📖 Texto Acadêmico de Leitura Contínua</div>
      {full_continuous_html}
    </div>
  </div>

  <!-- TAB 2: DIAGRAMA SVG -->
  <div id="diagrama" class="tab-content">
    <div class="card">
      <div class="card-title">🎨 Diagrama Vetorial Explicativo (Aula {num})</div>
      {svg_diagram}
    </div>
  </div>

  <!-- TAB 3: SIMULADOR -->
  <div id="simulador" class="tab-content">
    <div class="card">
      <div class="card-title">⚡ Simulador Interativo — Aula {num}</div>
      {simulators[num]}
    </div>
  </div>

  <!-- TAB 4: QUIZ -->
  <div id="quiz" class="tab-content">
    <div class="card">
      <div class="card-title">📝 Quiz de Fixação (Aula {num})</div>
      <p><b>1. Qual o objetivo central da Aula {num}?</b></p>
      <button class="quiz-opt" onclick="checkQuiz(this, true)">A) Aplicação de conceitos avançados de inteligência e automação em Smart Grids.</button>
      <button class="quiz-opt" onclick="checkQuiz(this, false)">B) Desligamento manual sem supervisão.</button>

      <br>
      <p><b>2. Como este método contribui para a operação do sistema de potência?</b></p>
      <button class="quiz-opt" onclick="checkQuiz(this, true)">A) Minimizando perdas, acelerando a restauração e garantindo alta confiabilidade.</button>
      <button class="quiz-opt" onclick="checkQuiz(this, false)">B) Aumentando os custos operacionais.</button>
    </div>
  </div>

  <!-- TAB 5: FLASHCARDS -->
  <div id="flashcards" class="tab-content">
    <div class="card">
      <div class="card-title">🎴 Flashcards da Aula {num} (Clique para virar)</div>
      <div class="flashcard-grid">
        <div class="flashcard" onclick="flipCard(this)" data-back="Integração de sensores, automação e inteligência em redes elétricas.">
          <b>Smart Grid</b>
        </div>
        <div class="flashcard" onclick="flipCard(this)" data-back="Técnica de otimização estocástica para resolução de problemas complexos.">
          <b>Metaheurística</b>
        </div>
        <div class="flashcard" onclick="flipCard(this)" data-back="Capacidade de adaptação e tomada de decisão automatizada no sistema.">
          <b>Automação Digital</b>
        </div>
      </div>
    </div>
  </div>
</div>

<script>
function setThemeFromParent(theme) {{
  if (theme === 'light') document.documentElement.setAttribute('data-theme', 'light');
  else document.documentElement.removeAttribute('data-theme');
}}

function showSubTab(id) {{
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
  event.target.classList.add('active');
  document.getElementById(id).classList.add('active');
}}

let isPodcastPlaying = false;
let podSpeedRate = 1.15;

function togglePodcastPlay() {{
  if (!('speechSynthesis' in window)) {{
    alert("Seu navegador não suporta a síntese de voz do Podcast.");
    return;
  }}

  if (isPodcastPlaying) {{
    window.speechSynthesis.cancel();
    stopPodcastUI();
  }} else {{
    startPodcastSpeech();
  }}
}}

function startPodcastSpeech() {{
  window.speechSynthesis.cancel();
  const text = document.getElementById('podTranscript').innerText;
  const u = new SpeechSynthesisUtterance(text);
  u.lang = 'pt-BR';
  u.rate = podSpeedRate;
  u.pitch = 1.25;

  u.onstart = () => {{
    isPodcastPlaying = true;
    document.getElementById('podIcon').innerText = '⏸️';
    document.getElementById('podBtnTxt').innerText = 'Pausar Podcast';
    document.querySelectorAll('.eq-bar').forEach(b => b.classList.add('playing'));
  }};

  u.onend = () => {{ stopPodcastUI(); }};
  u.onerror = () => {{ stopPodcastUI(); }};

  window.speechSynthesis.speak(u);
}}

function stopPodcastUI() {{
  isPodcastPlaying = false;
  document.getElementById('podIcon').innerText = '▶️';
  document.getElementById('podBtnTxt').innerText = 'Ouvir Podcast';
  document.querySelectorAll('.eq-bar').forEach(b => b.classList.remove('playing'));
}}

function changePodcastSpeed(val) {{
  podSpeedRate = parseFloat(val);
  if (isPodcastPlaying) startPodcastSpeech();
}}

function checkQuiz(btn, isCorrect) {{
  if (isCorrect) {{
    btn.classList.add('correct');
    alert('✨ Resposta Correta!');
  }} else {{
    btn.classList.add('wrong');
    alert('❌ Tente novamente!');
  }}
}}

function flipCard(card) {{
  if (card.classList.contains('flipped')) {{
    card.classList.remove('flipped');
    card.innerHTML = `<b>${{card.dataset.front || card.innerText}}</b>`;
  }} else {{
    card.dataset.front = card.innerText;
    card.classList.add('flipped');
    card.innerText = card.dataset.back;
  }}
}}

// ☀️/🌙 LIGHT & DARK THEME SYNC
function setThemeFromParent(theme) {{
  if (theme === 'default' || !theme) {{
    document.documentElement.removeAttribute('data-theme');
  }} else {{
    document.documentElement.setAttribute('data-theme', theme);
  }}
}}
const savedTheme = localStorage.getItem('sg_theme');
if (savedTheme) setThemeFromParent(savedTheme);
</script>
</body>
</html>
'''
    target_path = f'aula{num}.html'
    with open(target_path, 'w', encoding='utf-8') as out:
        out.write(html_content)
    print(f'Generated {target_path} with Podcast, Continuous Text and SVG Figures!')

