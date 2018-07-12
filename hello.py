
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name = name)
