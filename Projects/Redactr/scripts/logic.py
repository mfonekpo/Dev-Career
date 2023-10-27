import time

def user_string():
    text = input("Type a message: ")
    return text


# def message_scan(text):
#     word_count = len(text.split())
#     return word_count

def get_redact_word():
    rtext = input("Type the words to redact, multiple words should be seperated by space: ")
    return rtext

def scan_redact(text, rtext, replacement="replacement"):
    start_time = time.time()
    texts_to_scan = rtext.split()
    matches = []
    scrambled_words = text
    for wrd in texts_to_scan:
        if wrd in scrambled_words:
            scrambled_words = scrambled_words.replace(wrd, replacement)
            matches.append(wrd)
    end_time = time.time()
    duration = end_time - start_time
    return scrambled_words, matches, duration


def scan_stats(text, rtext):
    stats = scan_redact(text, rtext)
    return stats





def main():
    text = user_string() #Get users input
    print(text)

    # word_count = message_scan(text) #Get word count
    # print(f"word count: {word_count}")

    rtext = get_redact_word() #Get redact words from user

    scrambledWords = scan_redact(text, rtext) #Scrambling the words
    print(scrambledWords[0])

    stats = scan_stats(text, rtext) #Getting word statistics
    print(f"Words Scanned: {len(text.split())}") #Get word count
    print(f"Matches found: {len(stats[1])}") #Get matches
    print(f"Words Scrambled: {', '.join(stats[1])}") #Get scrambled words
    print(f"Scan Duration: {round(stats[2], 2)} seconds") #Get scan duration





if __name__ == "__main__":
    main()
