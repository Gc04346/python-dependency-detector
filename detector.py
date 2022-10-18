import os

BASE_DIR = 'input_files'
METHOD_PREFIX = 'def '

components = sorted({directory for directory in os.listdir(BASE_DIR)})
methods = set()
method_components_relation = {}
for component in components:
    # print(component.upper())
    current_dir = os.path.join(BASE_DIR, component)
    for file in os.listdir(current_dir):
        filepath = os.path.join(current_dir, file)
        # print(file)
        with open(filepath) as f:
            while line := f.readline():
                if METHOD_PREFIX in line:
                    method = line.strip(METHOD_PREFIX).split('(')[0]+'('
                    methods.add(method)
                    method_components_relation[method] = component
    #     print('\n')
    # print('\n')

# print(method_components_relation)
components_deps = {}

for component in components:
    components_deps[component] = [0 for i in enumerate(components)]
    component_deps = components_deps[component]
    # print(component.upper())
    current_dir = os.path.join(BASE_DIR, component)
    for file in os.listdir(current_dir):
        filepath = os.path.join(current_dir, file)
        # print(file)
        with open(filepath) as f:
            while line := f.readline():
                for method in methods:
                    if method in line:
                        component_deps[components.index(method_components_relation.get(method))] += 1
final = [deps for deps in components_deps.values()]

print(final)
