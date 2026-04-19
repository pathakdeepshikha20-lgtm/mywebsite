from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Find Odd Number Game</title>
        <style>
            body {
                background: black;
                color: white;
                text-align: center;
                font-family: Arial;
            }
            h1 {
                margin-top: 40px;
            }
            .grid {
                display: grid;
                grid-template-columns: repeat(3, 100px);
                gap: 15px;
                justify-content: center;
                margin-top: 40px;
            }
            button {
                height: 100px;
                font-size: 20px;
                background: lime;
                border: none;
                cursor: pointer;
            }
        </style>
        <script>
            function check(num) {
                if (num % 2 !== 0) {
                    alert("You Win 🎉");
                } else {
                    alert("You Lose ❌");
                }
            }
        </script>
    </head>
    <body>
        <h1>🔥 Find the Odd Number 🔥</h1>

        <div class="grid">
            <button onclick="check(2)">2</button>
            <button onclick="check(4)">4</button>
            <button onclick="check(6)">6</button>
            <button onclick="check(8)">8</button>
            <button onclick="check(10)">10</button>
            <button onclick="check(12)">12</button>
            <button onclick="check(14)">14</button>
            <button onclick="check(16)">16</button>
            <button onclick="check(9)">9</button>
        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)