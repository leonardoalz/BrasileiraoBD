import warnings
from flask import render_template, Flask
import db

warnings.filterwarnings('ignore', category=FutureWarning)

APP = Flask(__name__)

@APP.route('/')
def index():
    stats = db.execute("SELECT * FROM (SELECT count(*) as total_clubes from Clubes), (SELECT count(*) as total_estadios from Estadios), (SELECT count(DISTINCT ID_Partida) as total_partidas from InfoPartida), (SELECT count(Rodada) as total_rodadas from RodadaTemporada), (SELECT count(DISTINCT Temporada) as total_temporadas from RodadaTemporada ), (select min(Ano_Fundacao) as ano_fundacao_antigo from Clubes), (select max(Golos) as max_gols_clube_partida from ResultadoPartida), (select max(data) as max_gols_partida from (select sum(Golos) as data from ResultadoPartida group by ID_Partida))").fetchone()
    return render_template('index.html', stats=stats)

@APP.route('/clubes/')
def clubes():
    clube = db.execute("SELECT ID_Clube, Nome, Ano_Fundacao FROM Clubes").fetchall()
    return render_template('clubes.html', clubes=clube)

@APP.route('/clubes/<int:id>/')
def clubes_unico(id):
    clube = db.execute("SELECT c.ID_Clube, c.Nome, c.Ano_Fundacao, c.Apelido, c.Mascote, e.Nome_Estadio FROM Clubes c JOIN Estadios e ON e.ID_Estadio=c.ID_Estadio WHERE ID_Clube = ?", [id]).fetchone()
    return render_template('clubesUnico.html', clubes=clube)

@APP.route('/estadios/')
def estadios():
    estadio = db.execute("SELECT e.ID_Estadio, e.Nome_Estadio, e.Apelido, l.cidade as ID_Localidade, e.Capacidade FROM Estadios e JOIN Localidades l ON l.ID_Localidade=e.ID_Localidade").fetchall()
    return render_template('estadios.html', estadios=estadio)

@APP.route('/estadios/<int:id>/')
def estadios_unico(id):
    estadio = db.execute("SELECT s.ID_Estadio, s.Nome_Estadio, s.Apelido, l.cidade as ID_Localidade, s.Capacidade FROM Estadios s JOIN Localidades l ON l.ID_Localidade=s.ID_Localidade WHERE s.ID_Estadio = ?", [id]).fetchone()
    return render_template('estadiosUnico.html', estadios=estadio)

@APP.route('/localidades/')
def localidades():
    localidade = db.execute("SELECT ID_Localidade, Cidade, Estado FROM Localidades").fetchall()
    return render_template('localidades.html', localidades=localidade)

@APP.route('/localidadesUnico/<int:id>/')
def localidades_unico(id):
    localidade = db.execute("SELECT ID_Localidade, Cidade, Estado FROM Localidades WHERE ID_Localidade = ?", [id]).fetchone()
    return render_template('localidadesUnico.html', localidades=localidade)

@APP.route('/resultadoPartida/')
def resultados():
    resultado = db.execute("SELECT rp.ID_Partida, rp.ID_Clube, c.Nome AS Clube, rp.Golos, p.ID_Pontos, p.Resultado_Pontos FROM ResultadoPartida rp JOIN Clubes c ON rp.ID_Clube = c.ID_Clube JOIN Pontos p ON rp.Pontos = p.ID_Pontos JOIN InfoPartida ip ON rp.ID_Partida = ip.ID_Partida JOIN RodadaTemporada rt ON ip.ID_Rodada = rt.ID_Rodada").fetchall()
    return render_template('resultadoPartida.html', resultados=resultado)

@APP.route('/resultadoPartida')
def resultado_partida():
    resultados = db.execute("SELECT rp.ID_Partida, rp.ID_Clube, c.Nome AS Clube, rp.Golos, p.ID_Pontos, p.Resultado_Pontos, rt.Rodada, rt.Temporada FROM ResultadoPartida rp JOIN Clubes c ON rp.ID_Clube = c.ID_Clube JOIN Pontos p ON rp.Pontos = p.ID_Pontos JOIN InfoPartida ip ON rp.ID_Partida = ip.ID_Partida JOIN RodadaTemporada rt ON ip.ID_Rodada = rt.ID_Rodada").fetchall()
    return render_template('resultadoPartida.html', resultados=resultados)

@APP.route('/derrotasTemporada/<string:NomeClube>/<int:Temporada>/<string:Criterio>/')
def derrotas_temp(NomeClube, Temporada, Criterio):
    resultado = db.execute("SELECT c.Nome, COUNT(*) as num FROM Clubes c JOIN ResultadoPartida rp ON rp.ID_Clube = c.ID_Clube JOIN Pontos p ON p.ID_Pontos = rp.Pontos JOIN InfoPartida ip ON ip.ID_Partida = rp.ID_Partida JOIN RodadaTemporada rt ON rt.ID_Rodada = ip.ID_Rodada WHERE c.Nome = ? AND rt.Temporada = ? AND p.Resultado_Pontos = ?", (NomeClube, Temporada, Criterio)).fetchone()
    return render_template('derrotasTemporada.html', nome_clube=NomeClube, temporada=Temporada, criterio=Criterio, resultado=resultado)