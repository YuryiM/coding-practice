# Checks if list of emails have duplicates
def solution(input):
    # Please write your code here.

    unique = set()

    for i in input:
        # email into user and domain
        i = i.replace("\"", "").strip().lower().split("@")

        # Simplify username (before @)

        # Removes periods
        if "." in i[0]:
            i[0] = i[0].replace(".", "")

        # Removes "+" and everything after
        if "+" in i[0]:
            plusPos = i[0].find("+")
            i[0] = i[0][0:plusPos]

        # Recombine user and domain and add to set if unique
        unique.add("@".join(i))

    return len(unique)

print(solution(["\" te.st@a.com \'", "\" test@a.com \'", "\" test@aa.com \'", "\" te.st+3@aa.com \'"]))
