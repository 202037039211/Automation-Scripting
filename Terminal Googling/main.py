from googlesearch import search

def terminal_googling():
    """Perform Google search from the terminal and display the results."""
    query = input("Enter search query: ")  # Take input query from the user
    num_results = 10  # Number of search results to fetch
    lang = 'fr'  # Language for the search results (French)

    try:
        print(f"\nSearching for '{query}'...\n")
        # Perform the search and print the top 10 results
        for j in search(query, num_results=num_results, lang=lang):
            print(j)
    except Exception as e:
        # Handle any errors during the search process
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    terminal_googling()  # Run the terminal googling function
