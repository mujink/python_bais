def solution(phone_book):
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True
# phone_book = ["119", "97674223", "1195524421"]
# phone_book = ["123","456","789"]
phone_book = ["12","123","1235","567","88"]

a = solution(phone_book)
print(a)