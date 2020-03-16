"""[String] caesarCipher"""
def main():
    """Write an encoder/decoder program based on the idea of shifting each character
    to the right hand side (for encoder) with a fixed number or key value where the
    order of characters is upper case, space and lower case characters. The program
     will do the shifting in circular fashion: meaning, the next character after
    the last one 'z' is the first character 'A' as '...xyzABC...XYZ abc...'

    For example, with the input message 'ABCDabcd' and key = 5, we will get the
    encoded message as 'FGHIfghi'.Moreover, for decoding, we will use the negative
    of the key such as the input message 'SAAplXGow' and key = -12, we will get the
    encoded message as 'Good Luck'."""

    circulartext = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz"
    text = input()
    key = int(input())
    true_key = 0
    for text_index in range(0, len(text), 1):
        for circular_index in range(0, len(circulartext), 1):
            if text[text_index] == circulartext[circular_index]:
                true_key = (circular_index+key)%53
                print(circulartext[true_key], end='')

main()
