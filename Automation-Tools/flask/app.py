from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    render_template_string,
)
import feedparser, sqlite3
import pandas as pd

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/rss", methods=["GET", "POST"])
def rss():
    rss_url = request.form["rss_url"]
    feed = feedparser.parse(rss_url)
    return render_template("rss.html", feed=feed)


@app.route("/convert", methods=["POST"])
def convert():
    file = request.files["file"]
    df = pd.read_excel(file)
    conn = sqlite3.connect("database.db")
    df.to_sql("data", conn, if_exists="replace")
    conn.close()

    return render_template_string(
        """
        <h1>Conversion completed!</h1>
        <p>Redirect to view the result!!</p>
        <script>
        setTimeout(() => {
            window.location.href="{{ url_for('inquiry') }}";
        }, 3000);
        </script>
        """
    )


@app.route("/inquiry")
def inquiry():
    conn = sqlite3.connect("database.db")
    df = pd.read_sql_query("select * from data", conn)
    conn.close()
    return render_template(
        "sql_inquiry.html", tables=[df.to_html(classes="data")], titles=["Data"]
    )


if __name__ == "__main__":
    app.run(debug=True)
