from flask import Flask, request

app = Flask(__name__)

app.config['DEBUG'] = True
signup_screen = """
<!DOCTYPE html>
<html>
<head>
    <style>
        .sign{
            display:inline;
        }
    </style>
</head>
<body>
    <h1>Signup</h1>
    <form action= "/" method="post">
        <table>
            <tr>
                <td><label for="username">Username  </label></td>

                <td><input type="text" name="username"></td>
            </tr>
            <tr>
                <td><label for="password">Password</label></td>

                <td><input type="text" name="password"></td>
            </tr>
            <tr>
                <td><label for="verifypassword">Verify Password</label></td>

                <td><input type="text" name="verifypassword"></td>
            </tr>
            <tr>
                <td><label for="email">Email (optional)</label></td>
                
                <td><input type="text" name="email"></td>    
            </tr>
        </table>
        <input type="submit">
    </div>

    </form>
</body>
</html>
"""


@app.route("/")
def index():
    return signup_screen


app.run()