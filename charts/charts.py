import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
    sizes = [15, 30, 45, 10]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.savefig('pie_chart.png')
    plt.close()