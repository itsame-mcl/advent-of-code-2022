from anytree import Node
import sys


def generate_tree(path):
    root = Node("root", type="dir", size=None)
    current_dir = root
    with open(path) as file:
        for line in file:
            command = line.replace('\n', '').split(' ')
            match command:
                case ["$", "cd", ".."]:
                    current_dir = current_dir.parent
                case ["$", "cd", "/"]:
                    current_dir = current_dir.root
                case ["$", "cd", directory]:
                    current_dir = [node for node in current_dir.children if node.name == directory][0]
                case ["$", "ls"]:
                    pass  # Ignore command, as the next lines of the input will be the output of ls
                case ["dir", directory]:
                    Node(directory, parent=current_dir, type="dir", size=None)
                case [filesize, filename] if filesize.isnumeric():
                    Node(filename, parent=current_dir, type="file", size=int(filesize))
    return root


def compute_dir_size(node):
    total_size = 0
    for child in node.children:
        if child.type == 'dir':
            child = compute_dir_size(child)
        total_size += child.size
    node.size = total_size
    return node


def find_little_dirs(path):
    tree = generate_tree(path)
    tree_with_sizes = compute_dir_size(tree)
    size_little_dirs = 0
    for node in tree_with_sizes.descendants:
        if node.type == 'dir' and node.size <= 100000:
            size_little_dirs += node.size
    return size_little_dirs


def free_space(path):
    tree = generate_tree(path)
    tree_with_sizes = compute_dir_size(tree)
    unused_space = 70000000 - tree_with_sizes.size
    smallest_dir_to_delete = sys.maxsize
    for node in tree_with_sizes.descendants:
        if node.type == 'dir' and node.size+unused_space > 30000000:
            if node.size < smallest_dir_to_delete:
                smallest_dir_to_delete = node.size
    return smallest_dir_to_delete
