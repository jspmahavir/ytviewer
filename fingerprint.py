import js2py

your_script = "const fpPromise = new Promise((resolve, reject) => { const script = document.createElement('script'); script.onload = resolve; script.onerror = reject; script.async = true; script.src = 'https://cdn.jsdelivr.net/npm/' + '@fingerprintjs/fingerprintjs-pro@3/dist/fp.min.js';document.head.appendChild(script); }).then(() => FingerprintJS.load({token:'RkgHmrIAZ2rtQtOtUh6X', egion: 'eu'}));"

js = """
var output;
document = {
    write: function(value){
        output = value;
    }
}
""" + your_script

context = js2py.EvalJs()
print(context)
# exit()
# context.execute(js)
print(context.output)