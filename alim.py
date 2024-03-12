import tkinter as tk
import requests
from bs4 import BeautifulSoup
import time
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

url = 'http://192.168.0.2/Home.cgi'
i = 0
max_value = 0

root = tk.Tk()
root.title("Graph")

# Create a Matplotlib figure and axis
fig, ax = plt.subplots()

# Create a Tkinter canvas for the figure
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Create a button to reset the graph and the maximum value
reset_button = tk.Button(root, text="Reset", command=lambda: reset_graph(ax, max_value))
reset_button.pack(side=tk.BOTTOM)

def reset_graph(ax, max_value):
    global i
    ax.clear()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 0)
    max_value = 0
    i = 0

# Set the x-axis tick labels to display time in minutes and seconds
def format_x(x, pos):
    minutes = int(x / 60)
    seconds = int(x % 60)
    if seconds == 0:
        return f'{minutes} m'
    else:
        return f'{minutes} m {seconds} s'

formatter = ticker.FuncFormatter(format_x)
ax.xaxis.set_major_formatter(formatter)

# Turn on the interactive mode of Matplotlib
plt.ion()

while True:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        input_element = soup.find('input', {'id':'actcur'})
        value = input_element['value']
        max_value = max(max_value, float(value.replace(' A', '')))
        ax.plot(i, float(value.replace(' A', '')), 'bo')
        ax.set_xlim(left=0, right=i+1)
        ax.set_ylim(bottom=0, top=max_value)
        ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.01))
        ax.text(0.05, 0.9, f'Max: {max_value:.2f} A', transform=ax.transAxes)
        fig.canvas.draw()
        fig.canvas.flush_events()
        print(i, value)
        i += 1
    else:
        print(f"Error {response.status_code} while retrieving the power supply web page")

    time.sleep(1)
