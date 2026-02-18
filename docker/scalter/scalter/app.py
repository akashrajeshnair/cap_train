from flask import Flask, Response
import matplotlib.pyplot as plt
import io
import random

app = Flask(__name__)

@app.route("/")
def scatter_plot():
    # Generate random data
    x = [random.randint(1, 100) for _ in range(50)]
    y = [random.randint(1, 100) for _ in range(50)]

    # Create scatter plot
    plt.figure()
    plt.scatter(x, y)
    plt.title("Random Scatter Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")

    # Save image to memory
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()

    return Response(img.getvalue(), mimetype='image/png')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
