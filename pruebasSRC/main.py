from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

from tmdb3 import Movie, set_key, searchMovie, searchPerson, searchStudio
set_key('8756c376f367fb966d3c0dec2c69e1c5')

@app.route("/")
def root():
  return render_template('base.html', title='Main', pageActive='home')

#@app.route("/noresults/")
#def noresults():
#  return render_template('no_results.html')

@app.route("/movies/", methods=['POST', 'GET'])
def movies():
  if request.method == 'POST':
    keyword = request.form['search field']
    res = searchMovie(keyword)
    if len(res) == 0:
      return redirect(url_for('noresults'))
    else:
      #return ',,,'.join(m.title for m in res)  
      return render_template('movies.html', title='Moviesss', pageActive='movies', movies=res)
  else:
    return render_template('movies.html', title='Moviesss', pageActive='movies')

@app.route("/people/", methods=['POST', 'GET'])
def people():
  if request.method == 'POST':
    keyword = request.form['keyword']
    res = searchPerson(keyword)
    if len(res) == 0:
      return redirect(url_for('noresults'))
    else:
      return res[0].name
  else:
    return render_template('people.html')

@app.route("/studios/", methods=['POST', 'GET'])
def studios():
  if request.method == 'POST':
    keyword = request.form['keyword']
    res = searchStudio(keyword)
    if len(res) == 0:
      return redirect(url_for('noresults'))
    else:
      return res[0].name
  else:
    return render_template('studios.html')

@app.route("/mostpopular/")
def mostpopular():
  movies = Movie.mostpopular()
  res = movies[0:10]
  nom = "ruben"
  ##res = ""
  ##for m in movies[0:10]:
  ##  res += m.title+'\n'
  ##return res
  return render_template('mostpopular.html', title='Most popular', pageActive='movies', movies=res)

@app.errorhandler(404)
def page_not_found(error):
  return render_template('not_found.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
