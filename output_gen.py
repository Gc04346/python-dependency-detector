def generate_html_output(modules, dep_matrix):
    output_file = open("output/output.html", "w")
    prefix = """
    <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Relações de Dependências entre os módulos</title>
        </head>
        <body>
        <h3>Módulos identificados: {}</h3>
        <table>
            <tr style="text-align: center">
                <th>\/Chama/É Chamado ></th>
    """.format(', '.join(modules))
    output_file.write(prefix)
    for module in modules:
        output_file.write(f'<th>{module}</th>')
    output_file.write('</tr>')
    for i, module in enumerate(modules):
        output_file.write('<tr style="text-align: center">')
        output_file.write(f'<td>{module}</td>')
        for val in dep_matrix[i]:
            output_file.write(f'<td>{val}</td>')
        output_file.write('</tr>')
    output_file.write("""
            </table>
        </body>
    </html>
    """)
    output_file.close()

def generate_total_graphic(xAxis, yAxis):
    import matplotlib.pyplot as plt
    bc = plt.bar(xAxis, yAxis)
    plt.bar_label(bc, yAxis)
    plt.title('Nível de Acoplamento dos Componentes')
    plt.xlabel('Componente')
    plt.ylabel('Chamadas totais (feitas e recebidas)')
    plt.show()
    plt.savefig('output/chamadas_totais.png')


def generate_different_components_called_graphic(xAxis, yAxis):
    import matplotlib.pyplot as plt
    bc = plt.bar(xAxis, yAxis, label=yAxis)
    plt.bar_label(bc, yAxis)
    plt.title('Quantidade de componentes invocados')
    plt.xlabel('Componente')
    plt.ylabel('Quantidade de componentes invocados')
    plt.show()
    plt.savefig('output/comp_diferentes_chamados.png')


def generate_different_components_received_graphic(xAxis, yAxis):
    import matplotlib.pyplot as plt
    bc = plt.bar(xAxis, yAxis)
    plt.bar_label(bc, yAxis)
    plt.title('Número de componentes dependentes')
    plt.xlabel('Componente')
    plt.ylabel('Chamadas recebidas')
    plt.show()
    plt.savefig('output/comp_diferentes_atendidos.png')

def generate_double_graphic(xAxis, calls_made, calls_received):
    import matplotlib.pyplot as plt
    import numpy as np
    width = 0.35  # the width of the bars
    x = np.arange(len(xAxis))
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, calls_made, width, label='Chamadas Feitas')
    rects2 = ax.bar(x + width / 2, calls_received, width, label='Chamadas Recebidas')
    ax.set_xlabel('Componente')
    ax.set_ylabel('Chamadas')
    ax.set_title('Chamadas Feitas e Recebidas Por Cada Componente')
    ax.set_xticks(x, xAxis)
    ax.legend()
    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()
    plt.show()
    plt.savefig('output/feitas_x_recebidas.png')
