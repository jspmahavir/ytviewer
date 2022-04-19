from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

class ytDetails:
    def getName(self):
        return "First Name"

    def getLastName(self, data):
        print(data)
        return "Last Name"
    

if __name__ == '__main__':
    @app.route('/check', methods=['GET'])

    def check():
        yt = ytDetails()
        data = ['test']
        yt.getLastName(data)
        return {"status":"True"}

    app.run()