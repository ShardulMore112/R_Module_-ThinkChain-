from tools import openalex_tool

if __name__ == "__main__":
    query = input("Enter research field or keyword: ").strip()
    result = openalex_tool.func(query)
    print("\n--- Results ---\n")
    print(result)
