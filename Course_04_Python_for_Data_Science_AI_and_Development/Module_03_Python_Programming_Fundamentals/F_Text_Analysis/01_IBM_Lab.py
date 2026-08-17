## Step 1: Define the String
givenstring = "Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

## Step 2: Define the Class
# Please do not run this code cell as it is incomplete and will produce an error.


# Let's create a class called TextAnalyzer to analyze text.
class TextAnalyzer(object):

    # The __init__ method initializes the class with a 'text' parameter.
    # You will store the provided 'text' as an instance variable.
    def __init__(self, text):
        self.text = text

    ## Step 3: Format the Text
    # class TextAnalyzer(object):

    def __init__(self, text):

        # remove punctuation
        formattedText = (
            text.replace(".", "").replace("!", "").replace(",", "").replace("?", "")
        )

        # make text lowercase
        self.fmtText = formattedText.lower()

    ## Step 4: Count the Frequency of All Unique Words
    # class TextAnalyzer(object):

    def __init__(self, text):

        # remove punctuation
        formattedText = (
            text.replace(".", "").replace("!", "").replace(",", "").replace("?", "")
        )

        # make text lowercase
        self.fmtText = formattedText.lower()

    def freqAll(self):

        # split text into words
        wordList = self.fmtText.split()

        # Create dictionary
        freqMap = {}

        for word in set(wordList):
            freqMap[word] = wordList.count(word)

        return freqMap

    ## Step 5: Count the Frequency of a Specific Word
    #   class TextAnalyzer(object):

    def __init__(self, text):

        # remove punctuation
        formattedText = (
            text.replace(".", "").replace("!", "").replace(",", "").replace("?", "")
        )

        # make text lowercase
        self.fmtText = formattedText.lower()

    def freqAll(self):

        # split text into words
        wordList = self.fmtText.split()

        # Create dictionary
        freqMap = {}

        for word in set(wordList):
            freqMap[word] = wordList.count(word)

        return freqMap

    def freqOf(self, word):

        freqDict = self.freqAll()

        if word in freqDict:
            return freqDict[word]
        else:
            return 0


## Part-B
# Step 1: Create the Object
# textAnalyzer = TextAnalyzer(givenstring)
# Step 2: Print the Frequency of All Words
# print(textAnalyzer.freqAll())
# Step 3: Print the Frequency of the Word "lorem"
# Step 3: Print the Frequency of the Word "lorem"
