def isValidNumber(num_candidate):
    return num_candidate.replace('.','',1).isdigit() and float(num_candidate) >= 0 and float(num_candidate) <= 10

def checkFormat(items):
    if len(items) == 2 and isValidNumber(items[1]):
        return True
    return False

def main():
    print("Digite suas notas no formato \"nota [ESPAÇO] n°.créditos\"")
    print("Ex.: 9.5 3")
    sum_points = 0
    sum_credits = 0
    string_in = ""
    while string_in != "fim":
        print("para finalizar, digite \"fim\"")
        string_in = input()
        items = string_in.split(" ")
        if not checkFormat(items):
            continue
        nota = float(items[0])
        creditos = int(items[1])
        if nota < 5:
            nota = 0
        elif nota < 7:
            nota = 1
        elif nota < 8.5:
            nota = 2
        elif nota <= 10:
            nota = 3
        print(nota)
        sum_points = sum_points + nota * creditos
        sum_credits = sum_credits + creditos

    print(sum_points)
    print(sum_credits)
    print(sum_points / sum_credits)

if __name__ == "__main__":
    main()
