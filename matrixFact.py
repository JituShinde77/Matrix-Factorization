## Import library to generate random number
import random
import sys

def create_MAT(rows, cols):
    '''
        Create a matrix with random number.
        It takes input as number of rows and columns
        and return random number generator matrix.
    '''
    
    m = []
    for i in range(rows):
        r = []
        for j in range(cols):
            r.append(random.random())
            
        m.append(r)
    return m

def mat_mul(a, b):
    '''
        Perform matrix multiplication
        To check the generated and original matrix.
    '''
    
    user_mat = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            val = 0
            for k in range(len(b)):
                val +=a[i][k] * b[k][j]
            row.append(val)
        user_mat.append(row)
    return user_mat

def mat_diff(X, user_mat):
    '''
        This function is for calculating the difference in the original matrix and
        generated new 2 matrix product.
    '''
    diff_sum = []
    for i in range(len(X)):
        for j in range(len(X[0])):
            diff_sum.append((X[i][j] - user_mat[i][j])**2)
    sum(diff_sum)
    return sum(diff_sum)

def gradient(X, a, b, row, col, wrt_row=False, wrt_col=False):
    
    '''
        This function give us the actual and predicted value difference.
        
    '''
    actual = X[row][col]
    pred = 0
    
    for i in range(len(a[0])):
            pred += a[row][i]* b[i][col]
    if wrt_row:
        grad = 2*(actual - pred)*b[col][row]
    elif wrt_col:
        for i in range(len(a[0])):
            pred += a[row][i]* b[i][col]
        grad = 2*(actual - pred)*a[row][col]
    
    return grad

def total_gradient(X, a, b, row, col, wrt_row=False, wrt_col=False):
    
    '''
        This function function returns the how much rows are get affected due
        to the change in one value.
        It takes X, a, b, row, col as input and calculate total rate of change w.r.t 
        that value.
    '''
    total_grad = 0
    if wrt_row:
        for i in range(len(a)):
            total_grad += gradient(X, a, b, row, i, wrt_row=True)/len(a)
            
    elif wrt_col:
        for i in range(len(b[0])):
            total_grad += gradient(X, a, b, i, col, wrt_row=True)/len(b[0])
    return total_grad

def update_val(X, a, b, learning_rate=0.1):
    '''
        This function update the predicted values.
        
    '''
    
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] += learning_rate * total_gradient(X, a, b, i, j, wrt_row= True)
            
    for i in range(len(b)):
        for j in range(len(b[0])):
            b[i][j] += learning_rate * total_gradient(X, a, b, i, j, wrt_col= True)
    return a, b

def get_AB(X, k):
    r = len(X[0])
    a = create_MAT(r, k)
    b = create_MAT(k, r) 
  
    print ("**********")
    for i in range(1000):
        a, b = update_val(X, a, b, 0.2)
        if (i%50 == 0):
            print ("MSE:", mat_diff(X, mat_mul(a,b)))
            #print (a, b)
    return a, b

if __name__ == '__main__':
    str1 = sys.argv[1]
    rows = 0
    for i in range(len(str1)):
        if str1[i] == '[':
            rows += 1
   
                    
    col = 0                               
    for i in range(len(str1)):
        if str1[i] == ']':
           break                        
        if str1[i] == ',':
            col += 1
     
    str1 = str1.replace('[','')
    str1 = str1.replace(' ','')
    str1 = str1.replace(']','')
 
    arr = []
    cnt = 0
    row = []  
    for i in range(0, len(str1), 2):
        row.append(int(str1[i]))
        cnt += 1
        if cnt == col+1:
            arr.append(row)
            row = []
            cnt = 0
        
    print (arr)
    
    
    
    print (sys.argv[2])

           
    a, b = get_AB(arr, int(sys.argv[2]))
    print ("Matrix A:",a)
    print ("Matrix B",b)

    