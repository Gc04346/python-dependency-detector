import os

from output_gen import generate_html_output, generate_total_graphic, generate_double_graphic, \
    generate_different_components_called_graphic, generate_different_components_received_graphic

BASE_DIR = 'input_files'
METHOD_PREFIX = 'def '

components = sorted({directory for directory in next(os.walk(BASE_DIR))[1]})
methods = set()
method_components_relation = {}
for component in components:
    current_dir = os.path.join(BASE_DIR, component)
    for file in os.listdir(current_dir):
        filepath = os.path.join(current_dir, file)
        with open(filepath) as f:
            while line := f.readline():
                if METHOD_PREFIX in line:
                    method = line.strip(METHOD_PREFIX).split('(')[0] + '('
                    methods.add(method)
                    method_components_relation[method] = component

components_deps = {}
zeros_list = [0 for i in enumerate(components)]

for component in components:
    components_deps[component] = zeros_list.copy()
    component_deps = components_deps[component]
    current_dir = os.path.join(BASE_DIR, component)
    for file in os.listdir(current_dir):
        filepath = os.path.join(current_dir, file)
        with open(filepath) as f:
            while line := f.readline():
                for method in methods:
                    if method in line:
                        component_deps[components.index(method_components_relation.get(method))] += 1
dep_matrix = [deps for deps in components_deps.values()]

generate_html_output(components, dep_matrix)

dependency_sums = zeros_list.copy()
calls_made = zeros_list.copy()
calls_received = zeros_list.copy()
different_components_called = zeros_list.copy()
different_components_received = zeros_list.copy()

for i, row in enumerate(dep_matrix):  # Percorrendo as linhas da matriz
    calls_made[i] = sum(row)
    different_components_called[i] = sum(1 for val in row if val)
    for j, val in enumerate(row):  # Percorrendo cada linha
        if i == j:  # Não soma nos casos onde o componente chama a si mesmo
            calls_made[i] -= val
            continue
        dependency_sums[i] += val
        dependency_sums[j] += val
        calls_received[j] += val
        if val:
            different_components_received[j] += 1
components = [component.replace(' ', '\n') for component in components]
ordered_total_calls = sorted(list(zip(components, dependency_sums)), key=lambda x: x[1])
ordered_calls_by_received = sorted(list(zip(components, calls_made, calls_received)), key=lambda x: x[2])
ordered_different_components_called = sorted(list(zip(components, different_components_called)), key=lambda x: x[1])
ordered_different_components_received = sorted(list(zip(components, different_components_received)), key=lambda x: x[1])

generate_total_graphic(
    [component for component, total_calls in ordered_total_calls],
    [total_calls for component, total_calls in ordered_total_calls])
generate_double_graphic(
    [component for component, calls_made, calls_received in ordered_calls_by_received],
    [calls_made for component, calls_made, calls_received in ordered_calls_by_received],
    [calls_received for component, calls_made, calls_received in ordered_calls_by_received])
generate_different_components_called_graphic(
    [component for component, total_calls in ordered_different_components_called],
    [total_calls for component, total_calls in ordered_different_components_called])
generate_different_components_received_graphic(
    [component for component, total_calls in ordered_different_components_received],
    [total_calls for component, total_calls in ordered_different_components_received])
