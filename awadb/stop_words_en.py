#!/bin/python3

stop_words = {
    "third",
    "yes",
    "her",
    "want",
    "at",
    "once",
    "willing",
    "sub",
    "sufficiently",
    "via",
    "others",
    "cry",
    "with",
    "maybe",
    "edu",
    "became",
    "quickly",
    "am",
    "why's",
    "que",
    "hi",
    "sent",
    "these",
    "or",
    "amount",
    "needs",
    "sec",
    "somewhere",
    "ref",
    "significantly",
    "consequently",
    "everything",
    "along",
    "shan't",
    "et-al",
    "whereafter",
    "himse",
    "necessarily",
    "she'll",
    "okay",
    "opposite",
    "around",
    "how",
    "theirs",
    "we've",
    "himself",
    "bill",
    "ran",
    "top",
    "keeps",
    "pages",
    "primarily",
    "weren't",
    "said",
    "shes",
    "knows",
    "recent",
    "fewer",
    "later",
    "does",
    "somehow",
    "previously",
    "detail",
    "given",
    "he's",
    "id",
    "i'm",
    "mainly",
    "besides",
    "k",
    "mayn't",
    "right",
    "results",
    "sorry",
    "an",
    "happens",
    "per",
    "seemed",
    "gave",
    "g",
    "away",
    "first",
    "least",
    "especially",
    "new",
    "then",
    "noone",
    "thanks",
    "whereupon",
    "ml",
    "non",
    "thereto",
    "inner",
    "both",
    "them",
    "lets",
    "she's",
    "appear",
    "name",
    "anyways",
    "whod",
    "outside",
    "provided",
    "gotten",
    "backward",
    "describe",
    "c'mon",
    "changes",
    "next",
    "look",
    "give",
    "theyre",
    "when",
    "someone",
    "somebody",
    "isn't",
    "anywhere",
    "greetings",
    "following",
    "noted",
    "ord",
    "forty",
    "need",
    "way",
    "inc.",
    "mostly",
    "ts",
    "gone",
    "that've",
    "downwards",
    "you're",
    "same",
    "move",
    "invention",
    "index",
    "arent",
    "didn't",
    "mine",
    "sometime",
    "of",
    "definitely",
    "perhaps",
    "someday",
    "came",
    "de",
    "affecting",
    "nd",
    "brief",
    "did",
    "followed",
    "added",
    "thank",
    "where",
    "ups",
    "he'll",
    "shows",
    "ex",
    "you'll",
    "who's",
    "act",
    "showed",
    "anymore",
    "forth",
    "nos",
    "without",
    "wasn't",
    "nowhere",
    "could",
    "forward",
    "owing",
    "mill",
    "specifying",
    "she'd",
    "seriously",
    "nobody",
    "u",
    "beginnings",
    "qv",
    "make",
    "unto",
    "show",
    "never",
    "say",
    "exactly",
    "daren't",
    "ignored",
    "rather",
    "'ll",
    "now",
    "actually",
    "yourselves",
    "aren",
    "whats",
    "youre",
    "thin",
    "ending",
    "thousand",
    "they'd",
    "couldn't",
    "showns",
    "they'll",
    "substantially",
    "adj",
    "three",
    "whether",
    "more",
    "course",
    "proud",
    "will",
    "ok",
    "us",
    "whomever",
    "its",
    "strongly",
    "certain",
    "j",
    "whichever",
    "again",
    "as",
    "get",
    "also",
    "ah",
    "may",
    "a",
    "lower",
    "another",
    "our",
    "able",
    "hardly",
    "likely",
    "inasmuch",
    "theyd",
    "anything",
    "significant",
    "regardless",
    "quite",
    "yourself",
    "neither",
    "using",
    "and",
    "backwards",
    "part",
    "six",
    "what's",
    "thick",
    "tip",
    "becomes",
    "upwards",
    "thou",
    "farther",
    "on",
    "what'll",
    "poorly",
    "d",
    "looks",
    "already",
    "contain",
    "i",
    "to",
    "just",
    "took",
    "why",
    "do",
    "their",
    "some",
    "back",
    "use",
    "section",
    "overall",
    "versus",
    "try",
    "serious",
    "affected",
    "found",
    "fix",
    "www",
    "im",
    "whose",
    "that's",
    "ask",
    "went",
    "tried",
    "currently",
    "so",
    "that",
    "latter",
    "near",
    "mustn't",
    "means",
    "oughtn't",
    "that'll",
    "unfortunately",
    "s",
    "herself",
    "sixty",
    "regarding",
    "readily",
    "hundred",
    "better",
    "tends",
    "please",
    "possibly",
    "z",
    "herein",
    "latterly",
    "containing",
    "ten",
    "whos",
    "system",
    "necessary",
    "ninety",
    "q",
    "km",
    "less",
    "for",
    "obtained",
    "liked",
    "we",
    "him",
    "thoughh",
    "be",
    "ain't",
    "obtain",
    "vols",
    "hers",
    "mean",
    "concerning",
    "full",
    "dare",
    "thence",
    "off",
    "undoing",
    "merely",
    "almost",
    "through",
    "accordance",
    "every",
    "can",
    "y",
    "meanwhile",
    "o",
    "thereby",
    "until",
    "apart",
    "would",
    "thereupon",
    "the",
    "most",
    "onto",
    "take",
    "predominantly",
    "from",
    "immediately",
    "kg",
    "side",
    "heres",
    "except",
    "it'd",
    "stop",
    "itd",
    "howbeit",
    "m",
    "he'd",
    "might",
    "there's",
    "neverf",
    "gives",
    "nearly",
    "best",
    "whence",
    "go",
    "ours",
    "going",
    "things",
    "although",
    "each",
    "sup",
    "indicates",
    "let",
    "it",
    "how's",
    "mr",
    "five",
    "used",
    "everywhere",
    "while",
    "wherein",
    "approximately",
    "gets",
    "they",
    "throughout",
    "are",
    "shouldn't",
    "trying",
    "a's",
    "if",
    "co.",
    "wish",
    "is",
    "about",
    "over",
    "youd",
    "eight",
    "ahead",
    "re",
    "twelve",
    "mug",
    "believe",
    "getting",
    "promptly",
    "but",
    "such",
    "whereas",
    "thered",
    "fairly",
    "t",
    "plus",
    "cause",
    "com",
    "across",
    "several",
    "well",
    "there",
    "directly",
    "evermore",
    "shown",
    "nothing",
    "selves",
    "couldnt",
    "wheres",
    "corresponding",
    "seen",
    "sincere",
    "much",
    "i'd",
    "briefly",
    "slightly",
    "hello",
    "specified",
    "unless",
    "ltd",
    "l",
    "amidst",
    "aside",
    "beside",
    "has",
    "hither",
    "seems",
    "thirty",
    "considering",
    "mightn't",
    "eg",
    "wonder",
    "second",
    "ca",
    "had",
    "indeed",
    "ought",
    "yours",
    "ie",
    "many",
    "placed",
    "t's",
    "usefulness",
    "behind",
    "doesn't",
    "fill",
    "hereafter",
    "got",
    "seem",
    "associated",
    "we're",
    "been",
    "keep",
    "which",
    "resulted",
    "similar",
    "having",
    "half",
    "enough",
    "moreover",
    "home",
    "always",
    "c",
    "whereby",
    "twenty",
    "needn't",
    "whom",
    "x",
    "comes",
    "together",
    "relatively",
    "information",
    "everyone",
    "begins",
    "i've",
    "asking",
    "often",
    "become",
    "research",
    "provides",
    "don't",
    "none",
    "too",
    "reasonably",
    "beyond",
    "awfully",
    "elsewhere",
    "far",
    "w",
    "by",
    "insofar",
    "therein",
    "p",
    "cannot",
    "two",
    "uucp",
    "no-one",
    "effect",
    "particular",
    "allows",
    "refs",
    "resulting",
    "call",
    "page",
    "saw",
    "other",
    "towards",
    "soon",
    "who",
    "before",
    "little",
    "one",
    "whim",
    "unlikely",
    "appreciate",
    "here's",
    "eleven",
    "myself",
    "underneath",
    "computer",
    "r",
    "taking",
    "alone",
    "anyway",
    "thorough",
    "inside",
    "can't",
    "says",
    "n",
    "nine",
    "twice",
    "during",
    "under",
    "ed",
    "have",
    "four",
    "namely",
    "think",
    "various",
    "front",
    "unlike",
    "date",
    "largely",
    "suggest",
    "were",
    "accordingly",
    "itse”",
    "furthermore",
    "he",
    "possible",
    "somewhat",
    "viz",
    "I",
    "co",
    "let's",
    "former",
    "available",
    "self",
    "successfully",
    "specifically",
    "states",
    "end",
    "entirely",
    "amid",
    "when's",
    "up",
    "you've",
    "na",
    "value",
    "state",
    "we'll",
    "caption",
    "than",
    "round",
    "few",
    "last",
    "lest",
    "your",
    "et",
    "similarly",
    "whilst",
    "auth",
    "etc",
    "contains",
    "into",
    "here",
    "ff",
    "f",
    "till",
    "particularly",
    "against",
    "cant",
    "this",
    "any",
    "lately",
    "probably",
    "hereupon",
    "ones",
    "shed",
    "thereof",
    "thanx",
    "nor",
    "b",
    "itself",
    "usually",
    "miss",
    "sure",
    "i'll",
    "even",
    "ourselves",
    "out",
    "described",
    "otherwise",
    "bottom",
    "begin",
    "know",
    "thus",
    "regards",
    "seven",
    "omitted",
    "mrs",
    "wants",
    "certainly",
    "eighty",
    "whatever",
    "important",
    "run",
    "those",
    "vs",
    "because",
    "usefully",
    "hes",
    "looking",
    "causes",
    "though",
    "specify",
    "related",
    "therefore",
    "you",
    "nevertheless",
    "me",
    "different",
    "uses",
    "giving",
    "must",
    "likewise",
    "seeing",
    "very",
    "appropriate",
    "instead",
    "present",
    "wherever",
    "she",
    "themselves",
    "indicated",
    "sensible",
    "con",
    "there're",
    "potentially",
    "allow",
    "who'll",
    "truly",
    "yet",
    "find",
    "upon",
    "world",
    "there'll",
    "they've",
    "thru",
    "announce",
    "thing",
    "'ve",
    "own",
    "rd",
    "vol",
    "it's",
    "help",
    "forever",
    "fifty",
    "done",
    "formerly",
    "hereby",
    "taken",
    "whenever",
    "throug",
    "consider",
    "there've",
    "theres",
    "somethan",
    "hence",
    "won't",
    "either",
    "wouldn't",
    "line",
    "anyone",
    "aren't",
    "doing",
    "being",
    "c's",
    "wed",
    "made",
    "anyhow",
    "v",
    "becoming",
    "oh",
    "tries",
    "however",
    "hadn't",
    "fifteen",
    "who'd",
    "inc",
    "alongside",
    "where's",
    "abroad",
    "within",
    "respectively",
    "fire",
    "hasnt",
    "whole",
    "no",
    "due",
    "seeming",
    "beforehand",
    "til",
    "follows",
    "neverless",
    "one's",
    "tell",
    "biol",
    "zero",
    "importance",
    "sometimes",
    "anybody",
    "was",
    "whoever",
    "interest",
    "see",
    "kept",
    "nay",
    "whither",
    "immediate",
    "therere",
    "afterwards",
    "despite",
    "old",
    "down",
    "according",
    "meantime",
    "h",
    "thoroughly",
    "recently",
    "beginning",
    "mg",
    "notwithstanding",
    "haven't",
    "really",
    "indicate",
    "hid",
    "everybody",
    "we'd",
    "e",
    "there'd",
    "saying",
    "un",
    "million",
    "else",
    "obviously",
    "toward",
    "widely",
    "still",
    "known",
    "since",
    "all",
    "fifth",
    "ever",
    "makes",
    "myse”",
    "between",
    "welcome",
    "empty",
    "pp",
    "novel",
    "apparently",
    "example",
    "goes",
    "not",
    "after",
    "secondly",
    "abst",
    "nonetheless",
    "something",
    "what've",
    "amongst",
    "come",
    "useful",
    "normally",
    "what",
    "low",
    "affects",
    "inward",
    "like",
    "it'll",
    "should",
    "th",
    "thats",
    "herse",
    "they're",
    "words",
    "thereafter",
    "hasn't",
    "my",
    "ago",
    "put",
    "you'd",
    "among",
    "above",
    "below",
    "arise",
    "past",
    "presumably",
    "his",
    "minus",
    "in",
    "only",
    "hopefully",
    "keys",
    "clearly",
    "adopted",
    "shall",
    "further",
}