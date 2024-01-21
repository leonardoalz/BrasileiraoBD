# BrasileiraoDB

**I.**	O universo escolhido consiste nas informações dos jogos das temporadas do Campeonato Brasileiro de Futebol a partir de 2012, primeiro ano das classificações dos pontos corridos, até hoje (final da temporada de 2023). <br><br>
**II.**	Fonte dos dados utilizada:
https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2023<br><br>
**III.**	Método de obtenção dos dados: WebScraping com Python<br><br>
**IV.**	A estrutura da base de dados foi concebida para armazenar informações em sete tabelas distintas, representando dados estáticos e dinâmicos:

Clubes
          ID_Clube (PK)
          Nome
          Ano_Fundacao
          Apelido
          Mascote
          ID_Estadio (FK ) que referencia Estadios (ID_Estadio)

Estadios
          ID_Estadio (PK)
          Nome_Estadio
          Apelido
         ID_Localidade (FK) que referencia Localidades (ID_Localidade)
         Capacidade

InfoPartida
         ID_Partida (PK)
         ID_Rodada (FK) que referencia RodadaTemporada (ID_Rodada)
         ID_Estadio (FK) que referencia Estadios (ID_Estadio)

Localidades
         ID_Localidade (PK)
         Cidade
         Estadio

Pontos
         ID_Pontos (PK)
         Resultado_Pontos

ResultadoPartida
         ID_Partida (PK) e (FK) que referencia InfoPartida (ID_Partida)
         ID_Clube (PK) e (FK) que referencia Clubes (ID_Clube)
         Golos
         Pontos (FK) que referencia Pontos (ID_Pontos)
         CasaFora

RodadaTemporada
         ID_Rodada (PK)
         Rodada
         Temporada
