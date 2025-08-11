passage_1 = ["the", "singapore", "river", "once", 
             "the", "lifeline", "of", "singapore", 
             "trade", "and", "commerce", "was", 
             "notoriously", "polluted", "in", "the", ""
             "past", "singapore", "faced", "significant", 
             "challenges", "as", "waste", "from", 
             "industries", "and", "homes", "flowed", 
             "into", "the", "singapore", "river", 
             "however", "singapore", "initiated", "an", 
             "ambitious", "cleanup", "transforming", 
             "the", "singapore", "river", "into", "a", 
             "symbol", "of", "singapore", "commitment", 
             "to", "urban", "sustainability", "and", "progress"]
word = "singapore"
while True:
    if word in passage_1:
        passage_1.remove("singapore")
    else:
        break

# print(passage_1)