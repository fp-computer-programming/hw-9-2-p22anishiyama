# Author: ATN 1/12/22

def row_initials(last_initials, rows):
    for i, v in enumerate(rows):
        if i < len(i):
            rows[i] = "{0}, {1}.".format(rows, last_initials)
        else:
            return rows

print(row_initials[["B", "D", "H", "E", "G", "G", "H", "R", "M", "L", "I", "I", "N", "N", "O", "P", "P", "X", "T", "S", "S", "P"]
], [["Mateo", "Jason", "Jordan", "Mohamed", "Michael", "Charlie", "Declan"], ["Sean", "Luis", "Ryan", "James", "Jack"], ["Aiden", "Ian", "Colin" "Tim", "Cam"], ["Larry", "Spencer", "Chris", "Ryan", "Nolan"]])
