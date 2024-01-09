from flask import Flask, render_template, jsonify
app = Flask(__name__)

JOBS=[
{
  'id': '1',
  'title':'keyboardist',
  'location': 'Kikuyu, Kenya',
  'salary': 'ksh 20000'
},
{
  'id': '2',
  'title':'saxophonist',
  'location': 'Kimbu, Kenya',
  'salary': 'ksh 19000'
},
{
  'id': '3',
  'title':'bassist',
  'location': 'Kisumu, Kenya',
  'salary': 'ksh 25000'
},
{
  'id': '4',
  'title':'drummer',
  'location': 'Nairobi, Kenya',
  'salary': 'ksh 20000'
}
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name="CyrusMusic")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run('0.0.0.0', debug = True)