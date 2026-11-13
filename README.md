# Pombus — site + feed GTFS (Linhas 1 Azul e 2 Vermelha)

Site estático (index.html) com o mapa da Linha 1 do Pombus (Pombal, Portugal), horários e exportação do feed GTFS. Feed também disponível em gtfs/ (empacotar os 9 .txt num zip para validar/submeter).

## Estado (13/11/2026)
- 54 paragens com coordenadas reais fornecidas pelo utilizador.
- 10 viagens oficiais (07:10–18:40), tempos ao minuto (HH:MM:00); paragens intermédias interpoladas por distância.
- Dois percursos na Charneca: A (via Lar Rainha Sta. Isabel) e B (via Centro Recreativo); Casarelo (ida) só nas viagens 08:10 e 15:42; Escola M. de Pombal (volta) só nas primeiras 6 viagens (07:32, 08:40, 09:22, 11:22, 12:22, 13:52); Casarelo (volta) só nas viagens 08:10, 16:45 e 18:40 (08:45, 17:07, 19:03); Estrada da Charneca (volta) em todas as viagens (2 min antes da Rot. da Cooperativa volta).
- Calendário: ano inteiro de 2026, exceto sábados, domingos e feriados (nacionais + municipal de Pombal a 11/11) — calendar.txt + calendar_dates.txt.
- shapes.txt: traçados L1-A (base), L1-A-desvio, L1-B, L1-B-desvio, L1-A-casvolt e L1-B-casvolt desenhados no mapa pelo utilizador (KML, 24-25/10/2026; L1-A redesenhado com correções a 29/10/2026, KML 1.1; L1-B-desvio redesenhado a 29/10/2026, KML 1.2; L1-A-desvio redesenhado a 29/10/2026, KML 1.3, e retoque no mesmo dia, KML 1.3 v2; L1-B redesenhado a 29/10/2026, KML 1.4; L1-B-casvolt redesenhado com correções a 29/10/2026, KML 1.6; L1-A-casvolt redesenhado com correções a 29/10/2026, KML 1.5); L1-A atribuído às viagens 07:10, 09:00, 12:00 e 13:30; L1-A-desvio (ida via Casarelo, Charneca via Lar Rainha Sta. Isabel) atribuído à viagem 15:42; L1-A-casvolt (ida normal; volta pelo Casarelo, sem passar na Escola) atribuído à viagem 16:45; L1-B (Charneca via Centro Recreativo) atribuído às viagens 11:00 e 17:42; L1-B-desvio (ida via Casarelo, Charneca via Centro Recreativo) atribuído à viagem 08:10; L1-B-casvolt (ida normal; volta pelo Casarelo, sem passar na Escola; Charneca via Centro Recreativo) atribuído à viagem 18:40; distâncias acumuladas em metros.
- mapa.html: visualizador do feed GTFS num mapa real (Leaflet + OpenStreetMap).

### Linha 2 – Vermelha (13/11/2026)
- 15 viagens oficiais (07:00–19:10), 59 paragens: 41 novas (P55–P95) + 18 partilhadas com a L1 (P01–P04, P06, P18–P22, P24–P27, P31, P32, P52, P53). A viagem das 07:00 parte do Barrocal (Covão da Silva) e a das 08:43 parte do Souto 2; as viagens das 17:10 e 18:10 fazem uma pausa de 8 minutos no Largo do Cardal; a das 18:50 termina na Fonte Nova e a das 19:10 termina no Covão da Silva.
- shapes L2-V1 a L2-V15: V1, V2 e V3 desenhados no My Maps (V3 com o desvio Fonte Nova → Souto 2 → R. Narciso); V4–V15 compostos por blocos das shapes desenhadas; distâncias acumuladas em metros.
- stop_times.txt: coluna shape_dist_traveled preenchida para todas as 577 linhas L2 (projeção das paragens no traçado, validada — pior caso 34,9 m na Rot. do Bombeiro volta); as linhas L1 ficam com o campo vazio (válido no GTFS) porque Governos 2 (~104 m) e o R. do Lagar (~261 m) ficam longe do traçado L1-A (ver nota em baixo).
- linha-2-vermelha.html: página estática com o horário completo (59 paragens × 15 viagens), gerada das tabelas de horários; sitemap.xml atualizado.
- routes.txt: L2,POMBUS,2,"Linha 2 - Vermelha",3,E30613,FFFFFF (cor E30613 provisória; substituir quando houver cor oficial).

## Como testar
1. Abrir index.html no browser (funciona offline, sem servidor).
2. Validar o feed: zipar o conteúdo de gtfs/ e enviar a gtfs-validator.mobilitydata.org.

## Visualizar no mapa (mapa.html)
- Mostra o feed GTFS lido diretamente da pasta gtfs/: traçado da viagem selecionada, paragens com horários de passagem (popup com todas as viagens que servem cada paragem), camada com todos os traçados e todas as paragens, horário da viagem.
- Seletor de linhas: lista as 9 linhas da rede Pombus; as que ainda não têm dados no feed (L3, L3.1, L4, L4.1, L5, L6, L7) aparecem como «(Brevemente)» e desativadas. Tornam-se selecionáveis automaticamente quando a respetiva rota for adicionada a gtfs/routes.txt (route_id: L3, L3.1, L4, L4.1, L5, L6, L7). Ao mudar de linha, o seletor de viagens, o traçado, as paragens, os horários e a cor da linha passam a mostrar apenas essa linha; os popups das paragens identificam a linha e o padrão de cada passagem (ex.: 1·A).
- Otimizado para telemóvel: alvos de toque maiores em ecrãs de toque (linhas do horário, seletores, opções de camadas), a linha do horário tocada fica destacada, área de notch respeitada em iPhone (safe-area) e tiles nítidos em ecrãs retina (detectRetina).
- Janela «Sobre este projeto»: apresentação do projeto, nota de que não tem ligação oficial com a Câmara Municipal de Pombal, e email de contacto para sugestões (kiko_afn@hotmail.com) com assunto pré-preenchido.
- SEO (2026-11-07): title/description/canonical/OG + JSON-LD no mapa.html, parágrafo de introdução indexável; linha-1-azul.html = página estática com o horário completo da Linha 1 (gerada dos gtfs/*.txt; quadro 54 paragens × 10 viagens) ligada ao mapa; robots.txt e sitemap.xml apontam a https://pombus.pt/.
- Requer um servidor local (o browser bloqueia a leitura de ficheiros em file://):
  1. Na raiz do repositório: `python3 -m http.server 8000`
  2. Abrir http://localhost:8000/mapa.html (requer internet para os tiles do mapa). Tiles: OSM Deutschland (tile.openstreetmap.de — dados OpenStreetMap servidos pelo servidor comunitário alemão, gratuito, sem chave; ao contrário do tile.openstreetmap.org, que bloqueia com imagens «Access blocked», e da CARTO, que passou a exigir API key). Leaflet em si é livre e não requer chave nenhuma; só o fundo de mapa vem de um servidor de tiles terceiro.
- Alternativa sem servidor: abrir mapa.html e, no diálogo que aparece, selecionar manualmente os 9 ficheiros .txt da pasta gtfs/.
- Nota (dados, sem efeito no UI): nas viagens com traçado L1-A, Governos 2 (~104 m) e o R. do Lagar (~261 m, vaivém do traçado) ficam longe do traçado desenhado — é uma particularidade da ordem oficial do percurso, não um erro do visualizador: a ordem oficial das paragens é Governos 1 → 2, mas o traçado passa primeiro na rua de Governos 2, e o R. do Lagar é servido no vaivém da R. das Maiorcas. As distâncias de projeção mais próximas são ~12 m (Governos 2) e ~7 m (R. do Lagar); o validador GTFS já não acusa nenhuma paragem como longe do traçado L1-A.

## Monetização (donativos + AdSense)
Ambas as opções estão implementadas no mapa.html e desativadas por predefinição — nada carrega e nada aparece enquanto os valores não estiverem preenchidos no topo do script (secção «MONETIZAÇÃO»).
- Donativos: cria uma conta num serviço de apoio (Buy Me a Coffee, Ko-fi ou PayPal.me) e cola o teu link em DONATE_URL. O botão «Apoiar este projeto» passa a aparecer no fundo da barra lateral; o texto edita-se em DONATE_LABEL.
- Google AdSense: requer o site publicado num domínio público (não funciona em file:// nem em localhost) e uma conta AdSense aprovada. Depois da aprovação, cria um bloco de anúncios Display no painel e cola o ID do publisher (ca-pub-…) em ADSENSE_CLIENT e o ID do bloco em ADSENSE_SLOT. O bloco de anúncios passa a aparecer no fundo da barra lateral.
- Nota: «Pombus» é um serviço/marca da Câmara Municipal de Pombal. Antes de ativar publicidade, o ideal é acordar o projeto com a Câmara (patrocínio/parceria em vez de anúncios genéricos).

## Próximos passos
- Site publicado em https://pombus.pt/ (alojamento estático da dominios.pt; index.html no servidor = mapa.html do repo).
- Submeter o sitemap (https://pombus.pt/sitemap.xml) no Google Search Console e pedir indexação de /, /linha-1-azul.html e /linha-2-vermelha.html.
- Adicionar as restantes linhas do Pombus aos poucos (L3, L3.1, L4, L4.1, L5, L6, L7); cada linha nova ganha também a sua página de horários estáticos (linha-X.html) e entrada no sitemap.
- Validar o feed (gtfs-validator) e submeter ao Google Maps.
