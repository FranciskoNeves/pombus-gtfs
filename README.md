# Pombus — Linha 1 Azul (site + feed GTFS)

Site estático (index.html) com o mapa da Linha 1 do Pombus (Pombal, Portugal), horários e exportação do feed GTFS. Feed também disponível em gtfs/ (empacotar os 9 .txt num zip para validar/submeter).

## Estado (26/10/2026)
- 54 paragens com coordenadas reais fornecidas pelo utilizador.
- 10 viagens oficiais (07:10–18:40), tempos ao minuto (HH:MM:00); paragens intermédias interpoladas por distância.
- Dois percursos na Charneca: A (via Lar Rainha Sta. Isabel) e B (via Centro Recreativo); Casarelo (ida) só nas viagens 08:10 e 15:42; Escola M. de Pombal (volta) só nas primeiras 6 viagens (07:32, 08:40, 09:22, 11:22, 12:22, 13:52); Casarelo (volta) só nas viagens 08:10, 16:45 e 18:40 (08:45, 17:07, 19:03); Estrada da Charneca (volta) em todas as viagens (2 min antes da Rot. da Cooperativa volta).
- Calendário: ano inteiro de 2026, exceto sábados, domingos e feriados (nacionais + municipal de Pombal a 11/11) — calendar.txt + calendar_dates.txt.
- shapes.txt: traçados L1-A (base), L1-A-desvio, L1-B, L1-B-desvio, L1-A-casvolt e L1-B-casvolt desenhados no mapa pelo utilizador (KML, 24-25/10/2026; L1-A redesenhado com correções a 29/10/2026, KML 1.1; L1-B-desvio redesenhado a 29/10/2026, KML 1.2; L1-A-desvio redesenhado a 29/10/2026, KML 1.3, e retoque no mesmo dia, KML 1.3 v2; L1-B redesenhado a 29/10/2026, KML 1.4); L1-A atribuído às viagens 07:10, 09:00, 12:00 e 13:30; L1-A-desvio (ida via Casarelo, Charneca via Lar Rainha Sta. Isabel) atribuído à viagem 15:42; L1-A-casvolt (ida normal; volta pelo Casarelo, sem passar na Escola) atribuído à viagem 16:45; L1-B (Charneca via Centro Recreativo) atribuído às viagens 11:00 e 17:42; L1-B-desvio (ida via Casarelo, Charneca via Centro Recreativo) atribuído à viagem 08:10; L1-B-casvolt (ida normal; volta pelo Casarelo, sem passar na Escola; Charneca via Centro Recreativo) atribuído à viagem 18:40; distâncias acumuladas em metros.
- mapa.html: visualizador do feed GTFS num mapa real (Leaflet + OpenStreetMap).

## Como testar
1. Abrir index.html no browser (funciona offline, sem servidor).
2. Validar o feed: zipar o conteúdo de gtfs/ e enviar a gtfs-validator.mobilitydata.org.

## Visualizar no mapa (mapa.html)
- Mostra o feed GTFS lido diretamente da pasta gtfs/: traçado da viagem selecionada, paragens com horários de passagem (popup com todas as viagens que servem cada paragem), camada com todos os traçados e todas as paragens, horário da viagem.
- Requer um servidor local (o browser bloqueia a leitura de ficheiros em file://):
  1. Na raiz do repositório: `python3 -m http.server 8000`
  2. Abrir http://localhost:8000/mapa.html (requer internet para os tiles do mapa). Tiles: OSM Deutschland (tile.openstreetmap.de — dados OpenStreetMap servidos pelo servidor comunitário alemão, gratuito, sem chave; ao contrário do tile.openstreetmap.org, que bloqueia com imagens «Access blocked», e da CARTO, que passou a exigir API key). Leaflet em si é livre e não requer chave nenhuma; só o fundo de mapa vem de um servidor de tiles terceiro.
- Alternativa sem servidor: abrir mapa.html e, no diálogo que aparece, selecionar manualmente os 9 ficheiros .txt da pasta gtfs/.
- Nota: nas viagens com traçado L1-A, o site avisa que Governos 2 (~104 m) e o R. do Lagar (~261 m, vaivém do traçado) ficam longe do traçado desenhado — são avisos de ordem do percurso, não erros do visualizador: a ordem oficial das paragens é Governos 1 → 2, mas o traçado passa primeiro na rua de Governos 2, e o R. do Lagar é servido no vaivém da R. das Maiorcas. As distâncias de projeção mais próximas são agora ~12 m (Governos 2) e ~7 m (R. do Lagar); o validador GTFS já não acusa nenhuma paragem como longe do traçado L1-A.

## Próximos passos
- Outras 8 linhas do Pombus.
