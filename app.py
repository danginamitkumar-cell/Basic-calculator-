from flask import Flask, render_template_string
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1)

HTML = '''
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>FINAL CALC</title>
<script src="https://cdn.tailwindcss.com"></script>
<style>
body{background:#000; font-family: sans-serif;}
.btn{width:72px; height:72px; border-radius:50%; font-size:26px; font-weight:600; display:flex; align-items:center; justify-content:center;}
.btn:active{transform:scale(0.9);}
</style>
</head>
<body class="bg-black min-h-screen flex items-center justify-center p-4">

<div class="w-full max-w-[350px] bg-[#111] rounded-[2rem] p-6 border border-[#222]">

<div class="bg-black rounded-2xl p-4 border border-[#222]">
<div id="history" class="text-right text-gray-500 text-sm h-5">0</div>
<div id="display" class="text-right text-white text-4xl font-bold mt-2">0</div>
</div>

<div class="grid grid-cols-4 gap-4 mt-6 place-items-center">

<button onclick="clearAll()" class="btn bg-[#222] text-red-400">C</button>
<button onclick="back()" class="btn bg-[#222] text-white text-lg">⌫</button>
<button onclick="press('%')" class="btn bg-[#222] text-green-400">%</button>
<button onclick="press('/')" class="btn bg-[#222] text-green-400">÷</button>

<button onclick="press('7')" class="btn bg-[#1A1A1A] text-white">7</button>
<button onclick="press('8')" class="btn bg-[#1A1A1A] text-white">8</button>
<button onclick="press('9')" class="btn bg-[#1A1A1A] text-white">9</button>
<button onclick="press('*')" class="btn bg-[#222] text-green-400">×</button>

<button onclick="press('4')" class="btn bg-[#1A1A1A] text-white">4</button>
<button onclick="press('5')" class="btn bg-[#1A1A1A] text-white">5</button>
<button onclick="press('6')" class="btn bg-[#1A1A1A] text-white">6</button>
<button onclick="press('-')" class="btn bg-[#222] text-green-400">-</button>

<button onclick="press('1')" class="btn bg-[#1A1A1A] text-white">1</button>
<button onclick="press('2')" class="btn bg-[#1A1A1A] text-white">2</button>
<button onclick="press('3')" class="btn bg-[#1A1A1A] text-white">3</button>
<button onclick="press('+')" class="btn bg-[#222] text-green-400">+</button>

<button onclick="press('0')" class="btn bg-[#1A1A1A] text-white">0</button>
<button onclick="press('.')" class="btn bg-[#1A1A1A] text-white">.</button>
<button onclick="press('00')" class="btn bg-[#1A1A1A] text-white text-xl">00</button>
<button onclick="calculate()" class="btn bg-green-500 text-white font-black">=</button>

</div>
</div>

<script>
let expr = "";
let d = document.getElementById('display');
let h = document.getElementById('history');

function press(v){
    if(d.innerText=="0" && v!="." && v!="00") expr="";
    expr += v;
    d.innerText = expr;
    h.innerText = expr;
}
function clearAll(){
    expr = "";
    d.innerText = "0";
    h.innerText = "0";
}
function back(){
    expr = expr.slice(0, -1);
    d.innerText = expr || "0";
    h.innerText = expr || "0";
}
function calculate(){
    try{
        let finalExpr = expr.replace(/%/g, '/100');
        let result = eval(finalExpr);
        h.innerText = expr + " =";
        d.innerText = result;
        expr = result.toString();
    }catch(e){
        d.innerText = "ERROR";
        expr = "";
    }
}
</script>

</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
