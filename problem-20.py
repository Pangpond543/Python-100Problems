def transpose_matrix(matrix: list[list[int]]) -> list[list[int]]:
    transposed =[]
    for i in range(len(matrix)):        #หาแต่ละ row
        for j in range(len(matrix[i])): #หาแต่ละ column
            if len(transposed) <= j:    #หาว่า transposed มี row ที่ j หรือยัง ถ้ายังไม่มีให้สร้าง row ใหม่
                row = []
                transposed.append(row)  #เพิ่ม row ใหม่เข้าไปใน transposed
            transposed[j].append(matrix[i][j]) #เพิ่ม element ลงใน row ที่เหมาะสม / เปลื่ยน column เป็น row ในแต่ละ column แรก ของแต่ละ row
    return transposed

print(transpose_matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

#---------------------------------------------------------------------

def transpose_matrix_2(matrix: list[list[int]]) -> list[list[int]]:
    transposed = []
    
    for j in range(len(matrix[0])): #หาแต่ละ column
        row = []
        
        for i in range(len(matrix)): #วน row จนได้แต่ละ column ของ row นั้น
            row.append(matrix[i][j]) #เพิ่ม row แรก ของแต่ละ column เก่า ที่ได้มา
            
        transposed.append(row)  #เพิ่ม row ใหม่เข้าไปใน transposed
    return transposed

print(transpose_matrix_2([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))