class Book:
    def __init__(self, title, author, review):
        self.title = title
        self.author = author
        self.reviews = []
        self.reviews.append(review)

    def add_review(self, review):
        self.reviews.append(review)

    def count_reviews(self):
        count = len(self.reviews)
        print(f"No of reviews: {count}")

    def see_reviews(self):
        for review in self.reviews:
            print(review)

book1 = Book("The Alchemist", "Paulo Coelho", "Amazing book!")
book1.add_review("A must read for everyone.")
book1.count_reviews()
book1.see_reviews()
