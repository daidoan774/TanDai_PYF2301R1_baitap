dictionary = {
    "hello": "xin chào",
    "goodbye": "tạm biệt",
    "book": "sách",
    "computer": "máy tính"
}

word = input("Nhập từ cần tra cứu: ")
meaning = dictionary.get(word)

if meaning is not None:
    print(f"Nghĩa của từ {word} là: {meaning}")
else:
    print(f"Không tìm thấy từ {word} trong từ điển.")
