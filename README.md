🛵 Monitoramento Inteligente de Pátio de Motos — Mottu Challenge

Solução de monitoramento inteligente para pátios de motos da Mottu, permitindo localização precisa e gestão em tempo real da frota por meio de tecnologias IoT, comunicação MQTT e dashboard interativo.

👥 Integrantes
Nome	RM	Funções no Projeto
Celso Canaveze Teixeira Pinto	RM556118	IoT, Dashboard, Integração
Thiago Moreno Matheus	RM554507	API, Banco de Dados, DevOps
🎯 Objetivo do Projeto

Garantir visibilidade total das motos dentro do pátio Mottu, acompanhando:

✅ Localização
✅ Status operacional (pronta / pendente / manutenção)
✅ Monitoramento em tempo real
✅ Histórico de movimentação e alertas

📌 O projeto está alinhado ao desafio real da Mottu para otimizar operações e reduzir perdas.

🏛️ Arquitetura da Solução

Fluxo completo dos dados (ponta a ponta):

ESP32 (simulado) → MQTT Broker → Node-RED
→ Processamento e classificação
→ Dashboard e Persistência dos dados (CSV/JSON)


✅ Captura IoT
✅ Processamento e automação
✅ Visualização final
✅ Persistência e histórico

📡 IoT com ESP32 (Simulado no Wokwi)

Cada moto possui:

ID único

Placa

Modelo

Status operacional

Localização (coordenadas simuladas)

Os dados são enviados periodicamente ao MQTT em:

📌 mottu/patio/motos

O ESP32 também recebe comandos do sistema:

📌 mottu/patio/comandos

Status indicados no LED RGB e buzzer como feedback local.

🚦 Status das Motos
Status	Indicador	Significado
PRONTA_PARA_ALUGAR	🟢 LED Verde	Moto liberada
PENDENTE_REGULARIZACAO	🟡 LED Amarelo	Requer análise
EM_MANUTENCAO	🔴 LED Vermelho	Bloqueada para uso

Mudança de status pode ocorrer:

🖱️ por comando via MQTT
🔘 por botão físico (simulado)

🧠 Lógica do Dispositivo

1️⃣ Recebe status e dados via MQTT ou botão
2️⃣ Atualiza indicadores visuais (LED + buzzer)
3️⃣ Publica a nova situação da moto
4️⃣ Simula movimentação pela área do pátio

📌 Uma nova moto entra a cada 10s durante a simulação

🖥️ Node-RED — Processamento + Dashboard

O Node-RED:

✔ Recebe dados via MQTT
✔ Classifica motos por status
✔ Exibe localização e estado em tempo real
✔ Salva histórico da frota

Arquivos gerados automaticamente:

Arquivo	Conteúdo	Atualização
motos.json	Situação atual do pátio	Em tempo real
historico.csv	Movimentações e alertas	Sempre que houver alteração

Dashboard inclui:

✅ Lista de motos divididas por status
✅ Mapa interativo com suas localizações
✅ Atualizações sem recarregar página

URL padrão: http://localhost:1880/ui

(inserir prints do dashboard no repositório)

🛠️ Tecnologias Utilizadas
Categoria	Tecnologias
IoT & Simulação	ESP32, Wokwi
Comunicação	MQTT — Broker HiveMQ
Processamento e UI	Node-RED Dashboard
Armazenamento	JSON & CSV
Versão e Deploy	GitHub — Controle e documentação
▶️ Como Executar

1️⃣ Instale e rode o Node-RED:

node-red


2️⃣ Importe o fluxo da pasta /node-red

3️⃣ Abra a interface na Web:
🔗 http://localhost:1880/ui

4️⃣ Inicie o ESP32 no Wokwi
👉 Ele começa a enviar automaticamente

5️⃣ Observe as motos surgindo e mudando de status ✅
