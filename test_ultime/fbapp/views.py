from flask import Flask, render_template, url_for, request

app = Flask(__name__)

from .utils import find_content

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

@app.route('/')
@app.route('/index/')
def index():
        description = """
                Toi, tu n'as pas peur d'être seul ! Les grands espaces et les aventures sont faits pour toi. D'ailleurs, Koh Lanta est ton émission préférée ! Bientôt tu partiras les cheveux au vent sur ton radeau. Tu es aussi un idéaliste chevronné. Quelle chance !
                """
        return render_template('index.html',
                        user_name='Julio',
                        user_image=url_for('static', filename='img/profile.png'),
                        description=description,
                        blur=True)

@app.route('/result/')
def result():
        gender =request.args.get('gender')
        user_name = request.args.get('first_name')
        uid = request.args.get('id')
        profile_pic = 'http://graph.facebook.com' + uid + '/picture?type=large'
        description = find_content(gender).description
        return render_template('result.html',
                        user_name=user_name,
                        user_image=profile_pic,
                        description=description)

#@app.route('/contents/<content_id>/')
#def content(content_id):
#        return content_id 

if __name__ == "__main__":
        app.run()