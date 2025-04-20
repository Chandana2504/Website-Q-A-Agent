import argparse
from dotenv import load_dotenv
from web_crawler import crawl_website
from vector_store import create_vector_store
from query_handler import ask_question

def main():
    load_dotenv()  # Load GOOGLE_API_KEY from .env

    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True, help="Help center base URL to crawl")
    args = parser.parse_args()

    print("\n[+] Crawling website...")
    docs = crawl_website(args.url)
    print(f"[✓] Crawled {len(docs)} pages.")

    print("[+] Creating vector store...")
    vectorstore = create_vector_store(docs)
    print("[✓] Vector store is ready.")

    print("\nType your questions below (or type 'exit' to quit):")
    while True:
        query = input("\n> ")
        if query.lower() in ["exit", "quit"]:
            break
        ask_question(vectorstore, query)

if __name__ == "__main__":
    main()