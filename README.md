# Base de dados do Campeonato Brasileiro de Futebol

``` A base de dados (BD_Brasileirao.db) pode ser visualizada inteiramente em um software adequado para tal (utilizamos durante o processo de desenvolvimento o SQLite). Para que consiga executar a aplicação, leia o final da página e siga as instruções. ```
<br><br>
**I.**	O universo escolhido consiste nas informações dos jogos das temporadas do Campeonato Brasileiro de Futebol a partir de 2012, primeiro ano das classificações dos pontos corridos, até hoje (final da temporada de 2023). <br><br>
**II.**	Fonte dos dados utilizada:
https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2023<br><br>
**III.**	Método de obtenção dos dados: WebScraping com Python<br><br>
**IV.**	A estrutura da base de dados foi concebida para armazenar informações em sete tabelas distintas, representando dados estáticos e dinâmicos.

## Tabelas e colunas (atributos): <br>

Clubes<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ID_Clube (PK)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nome<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ano_Fundacao<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Apelido<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mascote<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ID_Estadio (FK ) que referencia Estadios (ID_Estadio)<br>
<br>
Estadios<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ID_Estadio (PK)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nome_Estadio<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Apelido<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ID_Localidade (FK) que referencia Localidades (ID_Localidade)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Capacidade<br>
<br>
InfoPartida<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ID_Partida (PK)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ID_Rodada (FK) que referencia RodadaTemporada (ID_Rodada)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ID_Estadio (FK) que referencia Estadios (ID_Estadio)<br>
<br>
Localidades<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ID_Localidade (PK)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Cidade<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Estadio<br>
<br>
Pontos<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ID_Pontos (PK)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Resultado_Pontos<br>
<br>
ResultadoPartida<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ID_Partida (PK) e (FK) que referencia InfoPartida (ID_Partida)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ID_Clube (PK) e (FK) que referencia Clubes (ID_Clube)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Golos<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pontos (FK) que referencia Pontos (ID_Pontos)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CasaFora<br>
<br>
RodadaTemporada<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ID_Rodada (PK)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Rodada<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Temporada
<br><br>
## Modelo relacional:<br>
![Relacional](https://github.com/leonardoalz/BrasileiraoDB/assets/90292319/1685367c-5a99-4e0e-9f4d-00f3cd8cc9f1)
<br><br>
## Modelo UML:<br>
![UML](https://github.com/leonardoalz/BrasileiraoDB/assets/90292319/df2226df-b069-4ac3-852f-9affe1eebc86)
<br><br>
## Como executar a aplicação:<br>
**I.** Abra o CMD e digite "pip install flask".<br>
**II.** Execute o "server.py" e entre no endereço gerado pelo servidor local.<br><br>
### Deverá ser exibida a seguinte página:<br>
![Captura da Web_21-1-2024_192511_127 0 0 1](https://github.com/leonardoalz/BrasileiraoDB/assets/90292319/26eeb2dd-688c-4d01-a5da-a8353710848c)


