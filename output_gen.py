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
                <th></th>
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
