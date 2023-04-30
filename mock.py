import argparse

def convertToMockingCase(charArray, startUpper):
    flop = startUpper
    for index,letter in enumerate(charArray):
        if letter != " ":
            if flop:
                charArray[index] = letter.upper()
            flop = not flop
        
    return "".join(charArray)

def main(phrase, startUpper):
    charArray = list(phrase)
    mocked = convertToMockingCase(charArray, startUpper)
    return mocked

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="SpongebobMocker", description="Program that turns text into mocking spongebob format")
    parser.add_argument("--phrase", required=True, help="phrase to convert to spongebob mock case")
    parser.add_argument("--startUpper", required=False, default=False, action=argparse.BooleanOptionalAction, help="set this flag if you want the phrase to start with a capital letter instead of lower case")
    args = parser.parse_args()
    
    output = main(args.phrase, args.startUpper)
    print("\n"+output+"\n")