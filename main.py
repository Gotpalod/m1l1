meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "РОФЛ": "ШУТКА",
            "ПОН": "ПОНЯТНО"
            
            }
word = input("Введите непонятное слово (большими буквами!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("токого словечка нету")
