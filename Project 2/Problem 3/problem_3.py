'''
--------------------------------------------------------------------------------------------------------------------------
Huffman Coding
A Huffman code is a type of optimal prefix code that is used for compressing data. The Huffman encoding and decoding schema is also lossless, meaning that when compressing the data to make it smaller, there is no loss of information.

The Huffman algorithm works by assigning codes that correspond to the relative frequency of each character for each character. The Huffman code can be of any length and does not require a prefix; therefore, this binary code can be visualized on a binary tree with each encoded character being stored on leafs.

There are many types of pseudocode for this algorithm. At the basic core, it is comprised of building a Huffman tree, encoding the data, and, lastly, decoding the data.

Here is one type of pseudocode for this coding schema:

Take a string and determine the relevant frequencies of the characters.
Build and sort a list of tuples from lowest to highest frequencies.
Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters. (This is the heart of the Huffman algorithm.)
Trim the Huffman Tree (remove the frequencies from the previously built tree).
Encode the text into its compressed form.
Decode the text from its compressed form.
You then will need to create encoding, decoding, and sizing schemas.
----------------------------------------------------------------------------------------------------------------------------
'''
import sys
import collections

class Node(object):

    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    @staticmethod
    def nodes(node_1, node_2):
        node = Node()

        if node_1.freq <= node_2.freq:
            node.left = node_1
            node.right = node_2
        else:
            node.left = node_1
            node.right = node_2

        node.freq = node_1.freq + node_2.freq

        return node

    def __repr__(self):
        return "Character: {} | frequency: {}".format(self.char, self.freq)


class Queue(object):
    def __init__(self, string):
        val= collections.Counter(string)
        self.arr = [Node(char=letter, freq=val[letter]) for letter in val]
        self.sort()

    def sort(self):
        self.arr = sorted(self.arr, key=lambda x: x.freq, reverse=True)

    def step(self):
        low_node_1 = self.arr.pop()
        low_node_2 = self.arr.pop()

        self.arr.append(Node.nodes(node_1=low_node_1, node_2=low_node_2))
        self.sort()


class Tree(object):
    def __init__(self, queue):
        while len(queue.arr) > 1:
            queue.step()

        self.root = queue.arr[0]

    def binary_generator(self):
        self.root = self._add_binary_code(self.root)
        self.root.freq = 0

    @staticmethod
    def _add_binary_code(node):
        if (node.left is None) and (node.right is None):
            return node

        if node.left is not None:
            node.left.freq = 1
            node.left = Tree._add_binary_code(node.left)

        if node.right is not None:
            node.right.freq = 0
            node.right = Tree._add_binary_code(node.right)

        return node


class HuffmanEncoder(object):
    def __init__(self, tree):
        self.table = self._create_encoding_table('',tree.root)
        self.encode_dict = None
        self.decode_dict = None

        self._create_encoder()
        self._create_decoder()

    def _create_encoder(self):
        encoder_dict = dict()

        for i,element in enumerate(self.table):
            encoder_dict[element[0]] = element[1]

        self.encode_dict = encoder_dict

    def _create_decoder(self):
        decoder_dict = dict()

        for i,element in enumerate(self.table):
            decoder_dict[element[1]] = element[0]

        self.decode_dict = decoder_dict

    def encode(self, text):
        coded_text = ''
        for char in text:
            coded_text += self.encode_dict[char]

        return coded_text

    def decode(self, encoded_text):
        decoded_text = ''

        while len(encoded_text) > 0:
            i_decoder = 1
            while True:
                if encoded_text[:i_decoder] in self.decode_dict.keys():
                    decoded_text += self.decode_dict[encoded_text[:i_decoder]]
                    encoded_text = encoded_text[i_decoder:]
                    break
                i_decoder += 1

        return decoded_text

    @staticmethod
    def _create_encoding_table(base_code, node):
        if (node.left is None) and (node.right is None):
            return [(node.char, base_code + str(node.freq))]

        if node.freq == -1:
            current_code = ''
        else:
            current_code = base_code + str(node.freq)

        coding_dict = []

        if node.char is not None:
            coding_dict.append((node.char, current_code + str(node.freq)))

        if node.left is not None:
            coding_dict.extend(HuffmanEncoder._create_encoding_table(current_code, node.left))

        if node.right is not None:
            coding_dict.extend(HuffmanEncoder._create_encoding_table(current_code, node.right))

        return coding_dict


def huffman_encoding(data):
    if len(data) == 0:
        print("Null String cannot be encoded")
        return

    else:
        temp_queue = Queue(data)
        temp_tree = Tree(temp_queue)
        temp_tree.binary_generator()
        temp_encoder = HuffmanEncoder(temp_tree)

        return temp_encoder.encode(data), temp_encoder


def huffman_decoding(data, encoder):
    return encoder.decode(data)

if __name__ == "__main__":
    val = "Bhavana Gopal"

    print(f"Size of plain text : {sys.getsizeof(val)}")
    print(f"Content of plain text:{val}")
    encoded_data, tree = huffman_encoding(val)

    print(f"Size of encoded data : {sys.getsizeof(int(encoded_data, base=2))}")
    print(f"Content of the encoded data : {encoded_data}")
    

    decoded_data = huffman_decoding(encoded_data, tree)
    print(f"Size of decoded data : {sys.getsizeof(decoded_data)}")
    print(f"Content of decoded data : {decoded_data}")

    print("-------------------------------------------------------------------------------------------------------")

    val = "Data Structures and Algorithm Nanodegree"

    print(f"Size of plain text : {sys.getsizeof(val)}")
    print(f"Content of plain text:{val}")
    encoded_data, tree = huffman_encoding(val)

    print(f"Size of encoded data : {sys.getsizeof(int(encoded_data, base=2))}")
    print(f"Content of the encoded data : {encoded_data}")
    

    decoded_data = huffman_decoding(encoded_data, tree)
    print(f"Size of decoded data : {sys.getsizeof(decoded_data)}")
    print(f"Content of decoded data : {decoded_data}")

    print("-------------------------------------------------------------------------------------------------------")

    #EDGE CASE
    val= "aaa"

    print(f"Size of plain text : {sys.getsizeof(val)}")
    print(f"Content of plain text:{val}")
    encoded_data, tree = huffman_encoding(val)

    print(f"Size of encoded data : {sys.getsizeof(int(encoded_data, base=2))}")
    print(f"Content of the encoded data : {encoded_data}")
    

    decoded_data = huffman_decoding(encoded_data, tree)
    print(f"Size of decoded data : {sys.getsizeof(decoded_data)}")
    print(f"Content of decoded data : {decoded_data}")

    print("-------------------------------------------------------------------------------------------------------")

    #EDGE CASE

    #empty string
    val= ""

    print(f"Size of plain text : {sys.getsizeof(val)}")
    print(f"Content of plain text:{val}")
    huffman_encoding(val)
    print("-------------------------------------------------------------------------------------------------------")