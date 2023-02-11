input_sentence = input("Введіть речення: ")
sentence_to_compare = input("Введіть речення для порівняння: ")
new_word = input("Введіть нове слово, яке потрібно додати в кінець речення: ")
input_word_to_remove = input("Введіть слово яке потрібно вилучити: ")


class Sentence:
    # your code goes here
    sentence = input_sentence
    compare_sentence = sentence_to_compare

    def __init__(self, sentence):
        Sentence.sentence = sentence

    @classmethod
    def to_lower(cls):
        cls.sentence = Sentence.sentence.lower()
        return cls.sentence

    def is_similar(self, compare_sentence=compare_sentence):
        self.compare_sentence = compare_sentence
        if self.compare_sentence.lower() != self.sentence.lower():
            return False
        else:
            return True

    def add_word(self, new_word):
        Sentence.sentence = self.sentence + new_word

    def remove_word(self, word_to_remove):
        Sentence.sentence = self.sentence.replace(word_to_remove, "")


my_sentence = Sentence(input_sentence)
print(my_sentence.is_similar(sentence_to_compare))

my_sentence.add_word(new_word)
my_sentence.to_lower()
print(my_sentence.sentence)

my_sentence.remove_word(input_word_to_remove)
print(my_sentence.sentence)
