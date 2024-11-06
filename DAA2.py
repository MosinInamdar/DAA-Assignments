import heapq

class Node: 
    def __init__(self, freq, symbol, left=None, right=None): 
        self.freq = freq  # Frequency of symbol
        self.symbol = symbol  # Symbol name (character)
        self.left = left  # Left child
        self.right = right  # Right child
        self.huff = ''  # Tree direction (0/1)

    def __lt__(self, nxt): 
        return self.freq < nxt.freq 

# Utility function to print Huffman codes for all symbols
def printNodes(node, val=''): 
    newVal = val + str(node.huff)  # Huffman code for current node

    if node.left:
        printNodes(node.left, newVal) 
    if node.right:
        printNodes(node.right, newVal) 

    # Display Huffman code if node is a leaf node
    if not node.left and not node.right: 
        print(f"{node.symbol} -> {newVal}") 

# Main function to build the Huffman Tree and print codes
def huffmanCoding(chars, freq):
    nodes = []

    # Create nodes for each character and frequency pair
    for x in range(len(chars)):
        heapq.heappush(nodes, Node(freq[x], chars[x])) 

    while len(nodes) > 1: 
        # Get the two nodes with the lowest frequency
        left = heapq.heappop(nodes) 
        right = heapq.heappop(nodes) 

        # Assign directional values
        left.huff = 0
        right.huff = 1

        # Create a new parent node by combining two nodes
        newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right) 
        heapq.heappush(nodes, newNode) 

    # Print the Huffman codes
    printNodes(nodes[0]) 

# Taking user input
chars = list(input("Enter the characters (e.g., abcdef): "))
freq = list(map(int, input("Enter the frequencies separated by space: ").split()))

# Validate input
if len(chars) != len(freq):
    print("Error: The number of characters must match the number of frequencies.")
else:
    # Build Huffman Tree and print codes
    huffmanCoding(chars, freq)
