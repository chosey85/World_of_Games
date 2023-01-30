from flask import Flask
import Utils

app = Flask(__name__)


@app.route('/')
def hello_world():
    try:
        score_file = open(Utils.scores_file_name(), "r")
        score_value = score_file.read()
        print(score_value)
        data = f'''<html>
                  <head>
                    <title>Scores Game</title>
                  </head>
                  <body>
                    <h1>The score is <div id="score">{score_value}</div></h1>
                  </body>
                </html>'''
        score_file.close()
        return data
    except FileNotFoundError:
        error = '''<html>
                             <head>
                               <title>Scores Game</title>
                             </head>
                             <body>
                               <h1><div id="score" style="color:red">{ERROR}</div></h1>
                             </body>
                            </html>'''
        return error


if __name__ == '__main__':
    app.run(host='0.0.0.0')
