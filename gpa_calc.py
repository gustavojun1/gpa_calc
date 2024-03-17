from pypdf import PdfReader 

# verifica se a string do número
# - é formado apenas por dígitos
# - é maior ou igual a zero
# - é menor ou igual a 10
def isValidNumber(num_candidate):
    return num_candidate.replace('.','',1).isdigit() and float(num_candidate) >= 0 and float(num_candidate) <= 10

# verifica se a string recebida
# - possui dois números (nota e créditos)
# - se a nota é válida
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
        sum_points = sum_points + nota * creditos
        sum_credits = sum_credits + creditos
    gpa = 0.4 * sum_points / sum_credits
    print("GPA BR = " + str(gpa))
if __name__ == "__main__":
    main()