with open("books/frankenstein.txt") as f:
    file_contents = f.read()

    words = file_contents.split()
    count = len(words)

    lower = file_contents.lower()
    
    item_counts = {}
    for item in lower:
        item_counts[item] = item_counts.get(item, 0) + 1
    # print(item_counts)    

    # for item in sorted(item_counts):
        # print(item, item_counts[item])

    # for item in sorted(item_counts, key=item_counts.get, reverse=False):
    #     print(item, item_counts[item])

    # alphanumeric_counts = [(item, item_counts[item]) for item in item_counts if item.isalnum()]
    # print(alphanumeric_counts)

    # alphanumeric_counts = [(item, item_counts[item]) for item in item_counts if item.isalnum()]
    # alphanumeric_counts.sort(key=lambda x: x[0])
    # print(alphanumeric_counts)

    alphanumeric_counts = [(item, item_counts[item]) for item in item_counts if item.isalnum()]
    alphanumeric_counts.sort(key=lambda x: x[1])

    item_list = ""
    for item in alphanumeric_counts:
        item_list += f"- {item}\n"

    report = f"""\
    This book has {count} words. Can you believe it?!!!

    {item_list}

    """

    print(report)
    
    


    # print(lower)