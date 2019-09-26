# filename: tree.py

import random

names = ['virginia', 'christine', 'carl', 'lillian']


def generate_tree(depth):
    n_children =  int(random.random()*10/depth)
    if n_children == 0:
        x = {'type': 'leaf', 'name': random.choice(names)} # for test purposes
        print(x) # test print
        return x
    branch = {'type': 'branch', 'children': []}
    for i in range(n_children):
        child = generate_tree(depth+1)
        branch['children'].append(child)
    print(branch) # test print
    return branch


def print_node(node, indentation):
    if node['type'] == 'leaf':
        print(indentation + node['name'])
    else:
        print(indentation + '-')
        for i in range(len(node['children'])):
            print_node(node['children'][i], indentation + '\t')


# count all trees and branches
def count_nodes(node):
    if node['type'] == 'leaf':
        return 1
    r = 1
    for i in range(len(node['children'])):
        r += count_nodes(node['children'][i])
    return r

# count all leaves
def count_leaves(node):
    r = 0
    for i in range(len(node['children'])):
        if node['type'][i] =='leaf':
            r += 1
    return r
    


root = generate_tree(1)
print_node(root, '')
print(count_nodes(root))
print(count_leaves(root))