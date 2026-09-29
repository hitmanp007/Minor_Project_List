import os
import requests
import webbrowser
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")

BASE_URL = "https://newsapi.org/v2"


# --------------------------------
# Fetch top headlines
# --------------------------------
def get_headlines(category=None):
    url = f"{BASE_URL}/top-headlines"

    params = {
        "country": "in",
        "pageSize": 10
    }

    if category:
        params["category"] = category

    headers = {
        "X-Api-Key": API_KEY
    }

    try:
        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=10
        )

        data = response.json()

        if response.status_code != 200:
            print("\n❌ Error:", data.get("message", "Something went wrong"))
            return []

        return data.get("articles", [])

    except requests.exceptions.RequestException as e:
        print("\n❌ Network error:", e)
        return []


# --------------------------------
# Search news
# --------------------------------
def search_news(keyword):
    url = f"{BASE_URL}/everything"

    params = {
        "q": keyword,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 10
    }

    headers = {
        "X-Api-Key": API_KEY
    }

    try:
        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=10
        )

        data = response.json()

        if response.status_code != 200:
            print("\n❌ Error:", data.get("message", "Something went wrong"))
            return []

        return data.get("articles", [])

    except requests.exceptions.RequestException as e:
        print("\n❌ Network error:", e)
        return []


# --------------------------------
# Display articles
# --------------------------------
def display_articles(articles):
    if not articles:
        print("\n⚠️ No articles found.")
        return

    print("\n" + "=" * 60)
    print("                    📰 NEWS")
    print("=" * 60)

    for i, article in enumerate(articles, start=1):

        title = article.get("title", "No title")
        source = article.get("source", {}).get("name", "Unknown")
        published = article.get("publishedAt", "Unknown")

        print(f"\n[{i}] {title}")
        print(f"    Source    : {source}")
        print(f"    Published : {published}")

    print("\n" + "=" * 60)


# --------------------------------
# Show article details
# --------------------------------
def show_article(articles):

    if not articles:
        return

    while True:

        choice = input(
            "\nEnter article number to open "
            "(0 to return): "
        )

        if choice == "0":
            return

        if not choice.isdigit():
            print("❌ Please enter a valid number.")
            continue

        choice = int(choice)

        if choice < 1 or choice > len(articles):
            print("❌ Invalid article number.")
            continue

        article = articles[choice - 1]

        print("\n" + "=" * 60)
        print("ARTICLE DETAILS")
        print("=" * 60)

        print("\nTitle:")
        print(article.get("title", "No title"))

        print("\nDescription:")
        print(article.get("description", "No description available."))

        print("\nSource:")
        print(
            article.get("source", {}).get(
                "name",
                "Unknown"
            )
        )

        print("\nAuthor:")
        print(article.get("author", "Unknown"))

        print("\nPublished:")
        print(article.get("publishedAt", "Unknown"))

        print("\nURL:")
        print(article.get("url", "No URL"))

        open_article = input(
            "\nOpen this article in browser? (y/n): "
        ).lower()

        if open_article == "y":
            webbrowser.open(article.get("url", ""))

        return


# --------------------------------
# Main menu
# --------------------------------
def main():

    if not API_KEY:
        print("❌ API key not found.")
        print("Please create a .env file and add:")
        print("NEWS_API_KEY=YOUR_API_KEY")
        return

    while True:

        print("\n")
        print("=" * 45)
        print("             📰 NEWS CLI")
        print("=" * 45)

        print("\n1. Top Headlines")
        print("2. Technology News")
        print("3. Sports News")
        print("4. Business News")
        print("5. Science News")
        print("6. Health News")
        print("7. Search News")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            print("\nFetching top headlines...")
            articles = get_headlines()
            display_articles(articles)
            show_article(articles)

        elif choice == "2":

            print("\nFetching technology news...")
            articles = get_headlines("technology")
            display_articles(articles)
            show_article(articles)

        elif choice == "3":

            print("\nFetching sports news...")
            articles = get_headlines("sports")
            display_articles(articles)
            show_article(articles)

        elif choice == "4":

            print("\nFetching business news...")
            articles = get_headlines("business")
            display_articles(articles)
            show_article(articles)

        elif choice == "5":

            print("\nFetching science news...")
            articles = get_headlines("science")
            display_articles(articles)
            show_article(articles)

        elif choice == "6":

            print("\nFetching health news...")
            articles = get_headlines("health")
            display_articles(articles)
            show_article(articles)

        elif choice == "7":

            keyword = input("\nEnter topic to search: ")

            if not keyword.strip():
                print("❌ Search cannot be empty.")
                continue

            print(f"\nSearching news about '{keyword}'...")

            articles = search_news(keyword)

            display_articles(articles)
            show_article(articles)

        elif choice == "8":

            print("\n👋 Thanks for using News CLI!")
            break

        else:

            print("\n❌ Invalid choice. Please select 1-8.")


# --------------------------------
# Program starts here
# --------------------------------
if __name__ == "__main__":
    main()