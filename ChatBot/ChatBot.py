from flask import Flask
from nltk.chat.util import Chat, reflections
import requests

pairs = [
    [
        r"my name is (.*)",
        ["\nHello %1, How are you today ?", ]
    ],
    [
        r"sorry (.*)",
        ["\nIts alright", "Its OK, never mind tha\nt", ]
    ],
    [
        r"i am (.*) doing good",
        ["\nNice to hear that", "Alright, great !\n", ]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["\nHello\n", "\nHey there\n", "\nhi\n"]
    ],
    [
        r"what (.*) want ?",
        ["\nMake me an offer I can't refuse\n", ]

    ],
    [
        r"(.*) created ?",
        ["\nSangeet created me using Python's NLTK library \n", "top secret ;)\n", ]
    ],
    [
        r"(.*) (location|city) ?",
        ['Tokyo, Japan', ]
    ],
    [
        r"how is the weather in (.*)?",
        ["\nWeather in %1 is amazing like always", "\nIt's soothibg here in %1",
            "\nIt's chilli here in %1", "\nIn %1 there is a 50% chance of rain", ]
    ],
    [
        r"i work (in|at) (.*)?",
        ["%1 is an amazing company, I have heard about it.\n", ]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2",
            "In %2 there is a 50% chance of rain\n", ]
    ],
    [
        r"is it (.*) in (.*)",
        ["No its not %1 in %2", "It could be", "Yes its %1 in %2\n"]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health \n", ]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Basketball\n", ]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy", "LeBron", "D-Wade"]
    ],


    [
        r"(who are you|who are u ?)",
        ["I am a ChatBot.\n"]
    ],

    [
        r"(what is a chatbot|tell me about chatbot|chatbot?)",
        ["\nA chatbot is a piece of software that conducts a conversation via auditory or textual methods. Such programs are often designed to convincingly simulate how a human would behave as a conversational partner, \nalthough as of 2019, they are far short of being able to pass the Turing test.   \n for more info visit: https://en.wikipedia.org/wiki/Chatbot\n"]
    ],


    [
        r"what is your favorite food",
        ["nanites\n"]
    ],
    [
        r"quit",
        ["\nBye for now. See you soon :) ",
            "It was nice talking to you. See you soon :)"]
    ],

    [
        r"(python|what is python|python info|tell me about python)",
        ["\n Python is an interpreted, high-level, general-purpose programming language.\nCreated by Guido van Rossum and first released in 1991,\nPython's design philosophy emphasizes code readability with its notable use of significant whitespace.\n\nFor more info you can refer to this link: https://en.wikipedia.org/wiki/Python_(programming_language)\n\n"]
    ],

    [
        r"fruit basket",
        ["\n A gift basket or fruit basket is typically a gift delivered to the recipient at their home or workplace.\n A variety of gift baskets exist: some contain fruit;\n while others might contain dry or canned foods such as tea,\n crackers and jam; or the basket might include a combination of fruit and dried good items.\n\n for more info visit this link: https://en.wikipedia.org/wiki/Gift_basket \n\n"]
    ]
]

chat = Chat(pairs, reflections)


def chatty(sentence):
    # print("                                            Hi, \n                                                  I'm J.A.R.V.I.S and I want to help and chat with you ! \n\n                                          Click on the --> PLAY Button -- on the left corner to start chating!\n\n                                  Please type lowercase English language to start a conversation. Type quit to leave\n\n")  # default message at the start
	return chat.respond(sentence)


# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


@app.route('/hello/<s>')
def hello_name(s):
	return chatty(s)
    

if __name__ == '__main__':
    app.run()
print("\n")
