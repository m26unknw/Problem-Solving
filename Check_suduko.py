def suduko_check(squares):
    for row in squares:
        check_list = list(range(1, len(squares[0])+1))

        for i in row:
            if i not in check_list:
                return False
            check_list.remove(i)
    for col in range(len(squares[0])):
        check_list = list(range(1, len(squares[0])+1))

        for row in squares:
            if row[col] not in check_list:
                return False
            check_list.remove(row[col])
    return True

suduko=[[1, 2 , 3],
        [2, 3 ,  1],
        [3, 1, 2]]
print(suduko_check(suduko))
