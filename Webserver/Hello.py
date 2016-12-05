from flask import Flask
from flask import render_template
app= Flask(__name__)
@app.route("/")

def mypysite(name=None):
    print("Shutdown")
    return render_template('main.html')

@app.route("/Reboot")
def Reboot( ):
    return render_template('Webseite.html')
    pass


@app.route("/Shutdown")
def Shutdown( ):
    print("Shutdown")
    pass
    
@app.route("/Delete_Messages")
def Delete_Messages():
    print("Delete")
    pass

if __name__=="__main__":
    app.run()
    
