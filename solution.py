import itertools

from bridges import*

import sys

class TrieNode:

    def __init__(self):
        self.children = dict()
        self.morse = []
        self.english = []

class Trie:

    def __init__(self, root:TrieNode):
        self.root = root

    def add_word(self, new_word:str, english):
        curr = self.root
        for letter in new_word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.morse.append(new_word)
        curr.english.append(english)

    def has_word(self, goal_word:str):
        curr = self.root
        for letter in goal_word:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return True

    def convert_morse_to_english(self, morse):
        if(self.has_word(morse)):
            curr = self.root
            for letter in morse:
                curr = curr.children[letter]
            return curr.english


    def backtracking_sentence(self, morse_code, tracker, new_root, old_root , possible):
        curr = new_root
        if morse_code == "" and curr.english:
            for word in curr.english:
                possible.append(tracker + word)
        elif morse_code and (morse_code[0] in curr.children or curr.english):
            if curr.english:
                new_tracker = tracker
                for word in curr.english:
                    new_tracker += word + " "
                    self.backtracking_sentence(morse_code, new_tracker, old_root, old_root, possible)
                    new_tracker = tracker
                if morse_code[0] in curr.children:
                    current = curr.children[morse_code[0]]
                    self.backtracking_sentence(morse_code[1:], tracker, current, old_root, possible)
            else:
                current = curr.children[morse_code[0]]
                self.backtracking_sentence(morse_code[1:], tracker, current, old_root, possible)
        return possible






def handle_spaced_letters(morse_code: str, conversion_dict):
    inp = morse_code.split(" ")

    out = ""

    for morse in inp:
        out += conversion_dict[morse]

    print(out)

    return conversion_dict

def get_choices(morse_code, reversed_dict):
    letters = {}
    for letter in reversed_dict.keys():
        tmp = len(reversed_dict[letter])
        if reversed_dict[letter] == morse_code[:tmp]:
            letters[letter] = morse_code[tmp:]
    return letters


def handle_word(reversed_dict, morse_code, dictionary, english):
    if len(morse_code) == 0 and str("".join(english)) in dictionary:
        solution = "".join(english)
        print(solution)
        return [solution]
    else:
        next_choices = get_choices(morse_code, reversed_dict)
        end = []
        for next in next_choices:
            english.append(next)
            intermediate = handle_word(reversed_dict, next_choices[next],dictionary, english)
            end.extend(intermediate)
            english.pop()
        return end

def handle_spaced_words(morse_code: str,trie):
    arr = morse_code.split(" ")
    result = []
    for word in arr:
        result.append(trie.convert_morse_to_english(word))
    num_words = len(result)
    if num_words == 1:
        print(result[0][0])
    else:
        final = [" ".join(str(y) for y in x) for x in itertools.product(*result)]
        for words in final:
            print(words)



def convert_english_to_morse(english, reversed_dict):
    result = ""
    for letter in english:
        result += reversed_dict[letter]
    return result






def handle_sentence(morse_code: str, candidate,trie, root: TrieNode, start: TrieNode):
    possibilities = trie.backtracking_sentence(morse_code,candidate,root,start, [])
    smallest_size = float("inf")
    final = []
    for option in possibilities:
        sentence = option.split(" ")
        if len(sentence) < smallest_size:
            smallest_size = len(sentence)
    for result in possibilities:
        sentence = result.split(" ")
        if len(sentence) == smallest_size:
            final.append(result)
    final.sort()
    for result in final:
        print(result)

def get_outgoing_edges(graph: GraphAdjList, vertex_id: str):
    """
    Retrieves all the edges associated with a specific vertex within the graph.
    """
    adj_list = graph.get_adjacency_list(vertex_id)
    if adj_list is None:
        return []
    return list(adj_list.list_helper())

def bridges_visualization_tree_couple(words_dict: dict):
    bridges = Bridges(1, "ankithe", "434778460587")

    t0 = BinTreeElement()
    t0.label = "root"
    #left is "-"
    #right is "."


    # title, description
    bridges.set_title("Trie")
    bridges.set_description(".")


    for english,word in words_dict.items():
        curr = t0
        count = 0
        for letter in word:
            count +=1
            if count == len(word):
                if letter == "-" and curr.left is not None:
                    curr = curr.left
                    curr.label = curr.label + ", " + english
                elif letter == "." and curr.right is not None:
                    curr = curr.right
                    curr.label = curr.label + ", " + english
                elif letter == "-" and curr.left is None:
                    curr.left = BinTreeElement()
                    curr.left.label = english
                    curr = curr.left
                elif letter == "." and curr.right is None:
                    curr.right = BinTreeElement()
                    curr.right.label = english
                    curr = curr.right
            else:
                if letter == "-" and curr.left is not None:
                    curr = curr.left
                elif letter == "." and curr.right is not None:
                    curr = curr.right
                elif letter == "-" and curr.left is None:
                    curr.left = BinTreeElement()
                    curr.left.label = ""
                    curr = curr.left
                elif letter == "." and curr.right is None:
                    curr.right = BinTreeElement()
                    curr.right.label = ""
                    curr = curr.right

    bridges.set_data_structure(t0)

    # visualize the tree
    bridges.visualize()


def bridges_visualization_tree_dict(words_dict: dict):
    bridges = Bridges(2, "ankithe", "434778460587")

    t0 = BinTreeElement()
    t0.label = "root"
    #left is "-"
    #right is "."


    # title, description
    bridges.set_title("Trie")
    bridges.set_description(".")


    for english,word in words_dict.items():
        curr = t0
        count = 0
        for letter in word:
            count +=1
            if count == len(word):
                if letter == "-" and curr.left is not None:
                    curr = curr.left
                    curr.label = curr.label + ", " + english
                elif letter == "." and curr.right is not None:
                    curr = curr.right
                    curr.label = curr.label + ", " + english
                elif letter == "-" and curr.left is None:
                    curr.left = BinTreeElement()
                    curr.left.label = english
                    curr = curr.left
                elif letter == "." and curr.right is None:
                    curr.right = BinTreeElement()
                    curr.right.label = english
                    curr = curr.right
            else:
                if letter == "-" and curr.left is not None:
                    curr = curr.left
                elif letter == "." and curr.right is not None:
                    curr = curr.right
                elif letter == "-" and curr.left is None:
                    curr.left = BinTreeElement()
                    curr.left.label = ""
                    curr = curr.left
                elif letter == "." and curr.right is None:
                    curr.right = BinTreeElement()
                    curr.right.label = ""
                    curr = curr.right

    bridges.set_data_structure(t0)

    # visualize the tree
    bridges.visualize()







def main():
    conversion_dict = {}
    words = []
    bridges_dict = dict()



    root_node = TrieNode()
    trie = Trie(root_node)


    with open("morse.txt","r" ) as conversion_chart:
        for line in conversion_chart:
            english = line[0:1]
            morse = line[2:].strip()
            conversion_dict[morse] = english
    reverse_dict = dict([(value,key) for key,value in conversion_dict.items()])

    with open("dictionary.txt", "r") as dictionary:
        for word in dictionary:
            cleaned = word.strip()
            words.append(cleaned)
            bridges_dict[cleaned] = convert_english_to_morse(cleaned, reverse_dict)
            trie.add_word(convert_english_to_morse(cleaned, reverse_dict), cleaned)

    # Bridges Visualization
    test_words = ["I", "A", "IT", "AT", "ME", "AN", "WE", "AM"]
    test_dict = dict()

    for word in test_words:
        test_dict[word] = convert_english_to_morse(word, reverse_dict)



    # Type in an input to try it out.
    style, morsed = input().split(":")
    morse_code = morsed.strip()
    # morse_code will be the string of morse coded text(e.g., '..--.-')

    if style == 'Spaced Letters':
        handle_spaced_letters(morse_code, conversion_dict)
    elif style == 'Word':
        handle_word(reverse_dict,morse_code, words, [])
    elif style == 'Spaced Words':
        handle_spaced_words(morse_code, trie)
    elif style == 'Sentence':
        handle_sentence(morse_code, "",trie,trie.root, root_node)
    elif style == 'Visualize':
        if morsed == "sample":
            bridges_visualization_tree_couple(test_dict)
        else:
            bridges_visualization_tree_dict(bridges_dict)


if __name__ == '__main__':
    main()
