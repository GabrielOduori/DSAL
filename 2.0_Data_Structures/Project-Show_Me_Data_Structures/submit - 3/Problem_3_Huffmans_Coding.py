
import sys
import collections


class Node(object):

    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # @staticmethod
    def combine_node(node_1, node_2):
        """
        Combines two nodes together, by using them as the leafs of a new node
        :param node_1: one of the nodes to fuse
        :param node_2: another node to fuse
        :return: combined nodes, being the leaves of a third parent node
        """
        combined_node = Node()

        if node_1.freq <= node_2.freq:
            combined_node.left = node_1
            combined_node.right = node_2
        else:
            combined_node.left = node_1
            combined_node.right = node_2

        combined_node.freq = node_1.freq + node_2.freq

        return combined_node

    def __repr__(self):
        return "Node of character: {} | frequency: {}".format(self.char, self.freq)


class Queue(object):
    def __init__(self, string):
        _ = collections.Counter(string)
        self.arr = [Node(char=letter, freq=_[letter]) for letter in _]
        self.sort()

    def sort(self) -> None:
        """
        Sorts the queue by frequency
        :return: None
        """
        self.arr = sorted(self.arr, key=lambda x: x.freq, reverse=True)

    def fuse_step(self) -> None:
        """
        Applies fusion of two nodes present on the queue;
        :return: None
        """
        low_node_1 = self.arr.pop()
        low_node_2 = self.arr.pop()

        self.arr.append(Node.combine_node(node_1=low_node_1, node_2=low_node_2))
        self.sort()


class Tree(object):
    def __init__(self, queue: Queue):
        while len(queue.arr) > 1:
            queue.fuse_step()

        self.root = queue.arr[0]

    def binaryze(self) -> None:
        """
        Binarizes a Tree, by changing Node.char information for a 1/0 value;  recursive launcher
        :return: None
        """

        self.root = self._add_binary_code(self.root)
        self.root.freq = 0

    @staticmethod
    def _add_binary_code(node: Node) -> Node:
        """
        Binarizes a Tree, by changing Node.char information for a 1/0 value
        :param node: node to modify
        :return: node binarized
        """
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
    def __init__(self, tree: Tree):
        self.table = self._create_encoding_table(base_code='', node=tree.root)
        self.encode_dict = None
        self.decode_dict = None

        self._create_encoder()
        self._create_decoder()

    def _create_encoder(self) -> None:
        """
        Encoder dictionary constructor
        :return: None
        """
        encoder_dict = dict()

        for i, element in enumerate(self.table):
            encoder_dict[element[0]] = element[1]

        self.encode_dict = encoder_dict

    def _create_decoder(self) -> None:
        """
        Decoder dictionary constructor
        :return: None
        """
        decoder_dict = dict()

        for i, element in enumerate(self.table):
            decoder_dict[element[1]] = element[0]

        self.decode_dict = decoder_dict

    def encode(self, text: str) -> str:
        """
        Text encoding method, specific for each encoder which takes in text to encode, 
        and returns text encoded with Huffman algorithm
        """
        coded_text = ''
        for char in text:
            coded_text += self.encode_dict[char]

        return coded_text

    def decode(self, encoded_text: str) -> str:
        """
        Text decoding method takes it text to decode and returns a 
        decoded text with Huffman algorithm
        """
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
    def _create_encoding_table(base_code: str, node: Node) -> list:
        """
        Traverses a binary tree and creates the basic encoding table and returns a list of 
        of the characters and their binary encoding
        """
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


def huffman_encoding(data: str) -> (str, HuffmanEncoder):
    """
    Huffman encoding method which takes a text and returns encoded text and 
    a relevant corresponding text encoder.
    """
    if len(data) == 0:
        print("No string to encode!")
        return

    else:
        temp_queue = Queue(string=data)
        temp_tree = Tree(queue=temp_queue)
        temp_tree.binaryze()
        temp_encoder = HuffmanEncoder(temp_tree)

        return temp_encoder.encode(data), temp_encoder


def huffman_decoding(data: str, encoder: HuffmanEncoder) -> str:
    """
    Huffman decoding method takes a text to decode and returns a decorded text using 
    Huffman encoder used to initially encode the text
    """

    return encoder.decode(data)


# TEST CASES

if __name__ == "__main__":

    # TEST 1
    print('TEST 1:')

    a_great_sentence = "Data is the new Gold!!!"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    
    print("The content of the data is: {}\n".format(a_great_sentence))
    

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))

    print("The content of the encoded data is: {}\n".format(encoded_data))
    

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))

    print("The content of the encoded data is: {}\n".format(decoded_data))


    # TEST 2
    print("TEST 2")


    a_great_sentence = "To be or not to be, that is the question"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
   
    print("The content of the data is: {}\n".format(a_great_sentence))
    

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
  
    print("The content of the encoded data is: {}\n".format(encoded_data))


    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))

    print("The content of the encoded data is: {}\n".format(decoded_data))


    # TEST 3
    print("TEST 3: Testing edge case")


    a_great_sentence = '  '

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
   
    print("The content of the data is: {}\n".format(a_great_sentence))
    

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
  
    print("The content of the encoded data is: {}\n".format(encoded_data))


    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))

    print("The content of the encoded data is: {}\n".format(decoded_data))
 

    
    
    # TEST 4
    print("TEST 3: Testing edge case")


    a_great_sentence = 'AAAAAAAA'

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
   
    print("The content of the data is: {}\n".format(a_great_sentence))
    

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
  
    print("The content of the encoded data is: {}\n".format(encoded_data))


    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))

    print("The content of the encoded data is: {}\n".format(decoded_data))