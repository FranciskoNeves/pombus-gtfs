# Pombus — Linha 1 Azul (site + feed GTFS)

Site estático (index.html) com o mapa da Linha 1 do Pombus (Pombal, Portugal), horários e exportação do feed GTFS. Feed também disponível em gtfs/ (empacotar os 7 .txt num zip para validar/submeter).

## Estado (16/10/2026)
- 53 paragens com coordenadas reais fornecidas pelo utilizador.
- Viagem 1 (07:10-08:05): horário oficial nas paragens-chave; intermédias interpoladas por distância.
- Viagens 2-8: DRAFT (a substituir pelos tempos oficiais).
- calendar.txt: suposição (14/09/2026-15/06/2027, dias úteis letivos).

## Como testar
1. Abrir index.html no browser (funciona offline, sem servidor).
2. Validar o feed: zipar o conteúdo de gtfs/ e enviar a gtfs-validator.mobilitydata.org.

## Próximos passos
- Tempos oficiais das viagens 2-8.
- shapes.txt (rota ao longo das ruas).
- Outras 8 linhas do Pombus.
