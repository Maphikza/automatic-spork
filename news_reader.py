from newspaper import Article


def extract_text(url):
    article = Article(url)
    article.download()
    article.parse()

    return article.text


if __name__ == "__main__":
    url = input("Enter the article URL: ")
    text = extract_text(url)
    print(text)
