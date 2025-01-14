# # # # # # #Pattern Matching using *

# # # # # # # row = int(input("row: "))
# # # # # # # col = int(input("col: "))
# # # # # # # for i in range(row):
# # # # # # #     for j in range(col):
# # # # # # #         print("*" ,end=" ")
# # # # # # #     print()
# # # # # # # col = int(input("col: "))
# # # # # # # val=1

# # # # # # # Pattern Matching using values

# # # # # # # row = int(input("row: "))
# # # # # # # col = int(input("col: "))
# # # # # # # val = 1
# # # # # # # for i in range(row):
# # # # # # #     for j in range(col):
# # # # # # #         print(val,end=" ")
# # # # # # #         val+=1
# # # # # # #         if val>9:
# # # # # # #             val=1
# # # # # # #     print()

# # # # # # row = int(input("row: "))
# # # # # # col = int(input("col: "))
# # # # # # for i in range(row):
# # # # # #         print("*" ,end=" ")
    
# # # # # # 888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888

# # # # # #n=5
# # # # # #  1 1 1 1 1
# # # # # #  1 1 1 1 1
# # # # # #  1 1 1 1 1
# # # # # #  1 1 1 1 1
# # # # # #  1 1 1 1 1

# # # # # # n=5
# # # # # # val=1
# # # # # # for i in range(n):
# # # # # #         for j in range(n):
# # # # # #                 print(val, end=" ")
# # # # # #         print()


# # # # # #n=5
# # # # # # 1 2 3 4 5
# # # # # # 1 2 3 4 5
# # # # # # 1 2 3 4 5
# # # # # # 1 2 3 4 5
# # # # # # 1 2 3 4 5

# # # # # # n=5
# # # # # # for i in range(n):
# # # # # #         val=1
# # # # # #         for j in range(n):
# # # # # #                 print(val,end=" ")
# # # # # #                 val+=1
# # # # # #         print()

# # # # # #n=5
# # # # # # 1 1 1 1 1
# # # # # # 2 2 2 2 2
# # # # # # 3 3 3 3 3
# # # # # # 4 4 4 4 4
# # # # # # 5 5 5 5 5

# # # # # # n=5
# # # # # # val=1
# # # # # # for i in range(n):
# # # # # #         for j in range(n):
# # # # # #                 print(val,end=" ")
# # # # # #         val+=1
# # # # # #         print()

# # # # # #n=5
# # # # # # 1 2 3 4 5
# # # # # # 6 7 8 9 1
# # # # # # 2 3 4 5 6
# # # # # # 7 8 9 1 2
# # # # # # 3 4 5 6 7

# # # # # # n=5
# # # # # # val=1
# # # # # # for i in range(n):
# # # # # #         for j in range(n):
# # # # # #                 print(val,end=" ")
# # # # # #                 val+=1
# # # # # #                 if val>9:
# # # # # #                         val=1
# # # # # #         print()

# # # # # #n=5
# # # # # # * * * * *
# # # # # # * * * * * 
# # # # # # * * * * *
# # # # # # * * * * *
# # # # # # * * * * *

# # # # # # n=5
# # # # # # for i in range(n):
# # # # # #         for j in range(n):
# # # # # #                 print("*",end=" ")
# # # # # #         print()

        
# # # # # # n=5
# # # # # # A B C D E
# # # # # # A B C D E
# # # # # # A B C D E
# # # # # # A B C D E
# # # # # # A B C D E

# # # # # # n=5
# # # # # # for i in range(n):
# # # # # #         val=0
# # # # # #         for j in range(n):
# # # # # #                 print(chr(65+val),end=" ")
# # # # # #                 val+=1
# # # # # #         print()

# # # # # # n=5
# # # # # # A A A A A
# # # # # # B B B B B
# # # # # # C C C C C
# # # # # # D D D D D
# # # # # # E E E E E

# # # # # # n=5
# # # # # # val=0
# # # # # # for i in range(n):
# # # # # #         for j in range(n):
# # # # # #                 print(chr(65+val),end=" ")
# # # # # #         val+=1
# # # # # #         print()


# # # # # # 1 
# # # # # # 2 2 
# # # # # # 3 3 3 
# # # # # # 4 4 4 4 
# # # # # # 5 5 5 5 5 
# # # # # # 6 6 6 6 6 6 
# # # # # # 7 7 7 7 7 7 7 
# # # # # # 8 8 8 8 8 8 8 8 
# # # # # # 9 9 9 9 9 9 9 9 9 
# # # # # # 1 1 1 1 1 1 1 1 1 1 

# # # # # # n=10
# # # # # # val=1
# # # # # # for i in range(n):
# # # # # #         for j in range(i+1):
# # # # # #                 print(val,end=" ")
# # # # # #         val+=1
# # # # # #         if val>9:
# # # # # #                 val=1
# # # # # #         print()
      
# # # # # # 1 
# # # # # # 1 2 
# # # # # # 1 2 3 
# # # # # # 1 2 3 4 
# # # # # # 1 2 3 4 5 
# # # # # # 1 2 3 4 5 6 
# # # # # # 1 2 3 4 5 6 7 
# # # # # # 1 2 3 4 5 6 7 8 
# # # # # # 1 2 3 4 5 6 7 8 9 
# # # # # # 1 2 3 4 5 6 7 8 9 1 

# # # # # # n=10
# # # # # # for i in range(n):
# # # # # #         val=1
# # # # # #         for j in range(i+1):
                
# # # # # #                 print(val,end=" ")
# # # # # #                 val+=1
# # # # # #                 if val>9:
# # # # # #                         val=1
# # # # # #         print()
      
# # # # # # 1 
# # # # # # 2 3 
# # # # # # 4 5 6 
# # # # # # 7 8 9 1 
# # # # # # 2 3 4 5 6 
# # # # # # 7 8 9 1 2 3 
# # # # # # 4 5 6 7 8 9 1 
# # # # # # 2 3 4 5 6 7 8 9 
# # # # # # 1 2 3 4 5 6 7 8 9 
# # # # # # 1 2 3 4 5 6 7 8 9 1 

# # # # # # n=10
# # # # # # val=1
# # # # # # for i in range(1,n+1):
# # # # # #         for j in range(1,n-i+1):
# # # # # #                 print(val,end=" ")
# # # # # #                 val+=1
# # # # # #                 if val>9:
# # # # # #                         val=1
# # # # # #         print()




# # # # # # 1
# # # # # # 2 2
# # # # # # 3 3 3 
# # # # # # 4 4 4 4

# # # # # n=int(input("n: "))
# # # # # val=1
# # # # # for i in range(n):
# # # # #         for j in range(n):
# # # # #                 if i>=j:
# # # # #                         print(val,end=" ")
# # # # #                 else:
# # # # #                         print(" ",end=" ")
# # # # #         print()
# # # # #         val+=1
# # # # #         if val>9:
# # # # #                 val=1


# # # # #3
# # # # #2 2 
# # # # #1 1 1

# # # # # n=int(input("n: "))
# # # # # val=n
# # # # # if val>9:
# # # # #         val=9
# # # # # for i in range(n):
# # # # #         for j in range(n):
# # # # #                 if i>=j:
# # # # #                         print(val,end=" ")
# # # # #                 else:
# # # # #                         print(" ",end=" ")
# # # # #         print()
# # # # #         val-=1
# # # # #         if val<1:
# # # # #                 val=9


# # # # #3
# # # # # 2
# # # # #  1

# # # # # n=int(input("n: "))
# # # # # val=n
# # # # # if val>9:
# # # # #         val=9
# # # # # for i in range(n):
# # # # #         for j in range(n):
# # # # #                 if i==j:
# # # # #                         print(val,end=" ")
# # # # #                 else:
# # # # #                         print(" ",end=" ")
# # # # #         print()
# # # # #         val-=1
# # # # #         if val<1:
# # # # #                 val=9

# # # # # 1
# # # # #   2
# # # # #     3

# # # # # n=int(input("n: "))
# # # # # val=1
# # # # # for i in range(n):
# # # # #         for j in range(n):
# # # # #                 if i==j:
# # # # #                         print(val,end=" ")
# # # # #                 else:
# # # # #                         print(" ",end=" ")
# # # # #         print()
# # # # #         val+=1
# # # # #         if val>9:
# # # # #                 val=1


# # # # A
# # # #   B 
# # # #     C 
# # # #       D

# # # # n=int(input("n: "))
# # # # val=0
# # # # for i in range(n):
# # # #         for j in range(n):
# # # #                 if i==j:
# # # #                         print(chr(65+val),end=" ")
# # # #                 else:
# # # #                         print(" ",end=" ")
# # # #         print()
# # # #         val+=1
# # # #         if val>25:
# # # #                 val=0

# # # # Z
# # # #   Y 
# # # #     X

# # # # n=int(input("n: "))
# # # # val=0
# # # # for i in range(n):
# # # #         for j in range(n):
# # # #                 if i==j:
# # # #                         print(chr(90-val),end=" ")
# # # #                 else:
# # # #                         print(" ",end=" ")
# # # #         print()
# # # #         val+=1
# # # #         if val>25:
# # # #                 val=0

# # # # print(chr(90))
# # # # print(chr(65+25))

# # # # 1 
# # # # 2 2 
# # # # 3 3 3 

# # # # n=int(input("n: "))
# # # # val=1
# # # # for i in range(n):
# # # #         for j in range(n):
# # # #                 if i+j>=n-1:
# # # #                         print(val,end=" ")
# # # #                 else:
# # # #                         print(" ",end=" ")
# # # #         print()
# # # #         val+=1
# # # #         if val>9:
# # # #                 val=1

# # # #     9 
# # # #   8 8 
# # # # 7 7 7

# # # # n=int(input("n: "))
# # # # val=n
# # # # if val>9:
# # # #         val=9
# # # # for i in range(n):
# # # #         for j in range(n):
# # # #                 if i+j>=n-1:
# # # #                         print(val,end=" ")
# # # #                 else:
# # # #                         print(" ",end=" ")
# # # #         print()
# # # #         val-=1
# # # #         if val<0:
# # # #                 val=9



# # # # n=int(input("n: "))

# # # # for i in range(n):
# # # #         val=1
# # # #         for j in range(n):
                
# # # #                 if i<=j:
# # # #                         print(val,end=" ")
# # # #                 else:
# # # #                         print(" ",end=" ")
# # # #                 val+=1
# # # #         print()
        
# # # #         if val>n:
# # # #                 val=1


# # # n=int(input("n: "))
# # # val=n
# # # if val>9:
# # #         val=9
# # # for i in range(n):
# # #         for j in range(n):
# # #                 if i<=j:
# # #                         print(val,end=" ")
# # #                 else:
# # #                         print(" ",end=" ")
# # #         print()
# # #         val-=1
# # #         if val<1:
# # #                 val=9


# # #  A B C D 
# # #    A B C 
# # #      A B 
# # #        A 

# # # n=int(input("n: "))
# # # for i in range(n):
# # #         val=0
# # #         for j in range(n):
# # #                 if i<=j:
# # #                         print(chr(65+val),end=" ")
# # #                         val+=1
# # #                         if val>25:
# # #                                 val=0
# # #                 else:
# # #                         print(" ",end=" ")
                
# # #         print()






# # # n=int(input("n: "))
# # # val=1
# # # if val>9:
# # #         val=9
# # # for i in range(n):
        
# # #         for j in range(n):
# # #                 if i<=j:
# # #                         print(val,end=" ")
# # #                         val+=1
# # #                         if val<1:
# # #                                 val=9
# # #                 else:
# # #                         print(" ",end=" ")
                
# # #         print()




# # # n=int(input("n: "))
# # # for i in range(n):
# # #         val=1
# # #         for j in range(n):
# # #                 if i<=j:
# # #                         print(val,end=" ")
# # #                         val+=1
# # #                         if val>9:
# # #                                 val=1
# # #                 else:
# # #                         print(" ",end=" ")
# # #         print()



# # # ***
# # # ***
# # # ***
# # # *******
# # # *******

# # # E D C B A 
# # #   E D C B 
# # #     E D C 
# # #       E D 
# # #         E

# # # n=int(input("n: "))
# # # for i in range(n):
# # #         val=n-1
# # #         for j in range(n):
# # #                 if i<=j:
# # #                         print(chr(65+val),end=" ")
# # #                         val-=1
# # #                         if val<0:
# # #                                 val=25
# # #                 else:
# # #                         print(" ",end=" ")
# # #         print()

# # # # 13
# # # A                                                       
# # # A B                                                     
# # # A B C                                                   
# # # A B C D


# # # n=int(input("n: "))
# # # for i in range(n):
# # #         val=0
# # #         for j in range(n):
# # #                 if i>=j:
# # #                         print(chr(65+val),end=" ")
# # #                         val+=1
# # #                         if val>25:
# # #                                 val=0
# # #                 else:
# # #                         print(" ",end=" ")
# # #         print()
                

# # # # 14
# # # D       
# # # C C     
# # # B B B   
# # # A A A A

# # # n=int(input("n: "))
# # # val=n-1
# # # if val>25:
# # #         val=25
# # # for i in range(n):
        
# # #         for j in range(n):
# # #                 if i>=j:
# # #                         print(chr(65+val),end=" ")        
# # #                 else:
# # #                         print(" ",end=" ")
# # #         print()
# # #         val-=1
# # #         if val<0:
# # #                 val=25

# # # #15
# # #       A 
# # #     B   
# # #   C     
# # # D  
# # # n=int(input("n: "))
# # # val=0
# # # for i in range(n):
# # #         for j in range(n):
# # #                 if i+j==n-1:
# # #                         print(chr(65+val),end=" ")
# # #                 else:
# # #                         print(" ",end=" ")
# # #         print()
# # #         val+=1
# # #         if val>25:
# # #                 val=0

# # # #16
# # # A B C D 
# # # A B C   
# # # A B     
# # # A 

# # # n=int(input("n: "))
# # # for i in range(n):
# # #         val=0
# # #         for j in range(n):
# # #                 if i+j<=n-1:
# # #                         print(chr(65+val),end=" ")
# # #                 else:
# # #                         print(" ",end=" ")
# # #                 val+=1
# # #                 if val>25:
# # #                         val=0
# # #         print()

# # # #17      
# # #       Z 
# # #     Y   
# # #   X     
# # # W 

# # # n=int(input("n: "))
# # # val=0
# # # for i in range(n):
# # #         for j in range(n):
# # #                 if i+j==n-1:
# # #                         print(chr(90-val),end=" ")
# # #                 else:
# # #                         print(" ",end=" ")
# # #         print()
# # #         val+=1
# # #         if val>25:
# # #                 val=0


# # # #18
# # #       4 
# # #     3   
# # #   2     
# # # 1 

# # # n=int(input("n: "))
# # # val=n
# # # if val>9:
# # #         val=9
# # # for i in range(n):
# # #         for j in range(n):
# # #                 if i+j==n-1:
# # #                         print(val,end=" ")
# # #                 else:
# # #                         print(" ",end=" ")
# # #         print()
# # #         val-=1
# # #         if val<1:
# # #                 val=9

# # # #19
# # #       D 
# # #     C   
# # #   B     
# # # A

# # # n=int(input("n: "))
# # # val=n-1
# # # if val>25:
# # #         val=25
# # # for i in range(n):
# # #         for j in range(n):
# # #                 if i+j==n-1:
# # #                         print(chr(65+val),end=" ")
# # #                 else:
# # #                         print(" ",end=" ")
# # #         print()
# # #         val-=1
# # #         if val<0:
# # #                 val=25

# # #20
# # #       A 
# # #     B C 
# # #   D E F 
# # # G H I J 

# # # n=int(input("n: "))
# # # val=0
# # # for i in range(n):
# # #         for j in range(n):
# # #                 if i+j>=n-1:
# # #                         print(chr(65+val),end=" ")
# # #                         val+=1
# # #                         if val>25:
# # #                                 val=0
# # #                 else:
# # #                         print(" ",end=" ")
# # #         print()
        
# # #1
# # # 1 * * * 
# # # 2 3 * * 
# # # 4 5 6 * 
# # # 7 8 9 1 


# # # n=int(input("n: "))
# # # val=1
# # # for i in range(n):
# # #         for j in range(n):
# # #                 if i>=j:
# # #                         print(val,end=" ")
# # #                         val+=1
# # #                         if val>9:
# # #                                 val=1
# # #                 else:
# # #                         print("*",end=" ")
# # #         print()



# # # n=int(input("n: "))
# # # for i in range(n):
# # #         val=1
# # #         for j in range(n):
# # #                 if i<j or i>j:
# # #                         print(val,end=" ")
# # #                 else:
# # #                         print("*",end=" ")
# # #                 val+=1
# # #                 if val>9:
# # #                         val=1
# # #         print()


# # # n=int(input("n: "))
# # # for i in range(n):
# # #         val=1
# # #         for j in range(n):
                
# # #                 if i<j:
                        
# # #                         print(val,end=" ")
                        
# # #                 elif i>j:
# # #                         print(val,end=" ")
# # #                 else:
# # #                         print("*",end=" ")
# # #                 val+=1
# # #                 if val>9:
# # #                         val=1
# # #         print()


# # n=int(input("n: "))
# # for i in range(n):
# #         val=1
# #         for j in range(n):
# #                 if i==j:
# #                         print("*",end=" ")
# #                 else:
# #                         print(val,end=" ")
# #                         val+=1
# #                         if val>9:
# #                                 val=1
# #         print()

# # *           * 
# #   *       *   
# #     *   *     
# #       *       
# #     *   *     
# #   *       *   
# # *           * 


# # n=int(input("n: "))
# # val=1
# # # p=True
# # for i in range(n):
# #         for j in range(n):
# #                 if i==j or i+j==n+1:
# #                         print("*",end=" ")
# #                 else:
# #                         print(" ",end=" ")
# #         print()



# n=int(input("n: "))
# for i in range(n):
#         for j in range(n):
#                 if i==0 or j==0 or i==n-1 or j==n-1:
#                         print("*",end=" ")
#                 else:
#                         print(" ",end=" ")
#         print()

# n: 4
#       *       
#     *         
#   *           
# * * * * * * * 

# n=int(input("n: "))
# for i in range(n):
#         for j in range(2*n-1):
#                 if i+j==n-1 or i==n-1:
#                         print("*",end=" ")
#                 else:
#                         print(" ",end=" ")
#         print()

# n: 4
#       *       
#         *     
#           *   
# * * * * * * * 

# n=int(input("n: "))
# for i in range(n):
#         for j in range(2*n-1):
#                 if i==n-1 or i+j==2*i+3:
#                         print("*",end=" ")
#                 else:
#                         print(" ",end=" ")
#         print()

# n=int(input("n: "))
# for i in range(n):                                        Pending    ******
#         for j in range(2*n-1):
#                 if i+j==n-1 or i==n-1 :
#                         print("*",end=" ")
#                 else:
#                         print(" ",end=" ")
#         print()

# n: 4
# *           * 
#   *       *   
#     *   *     
#       *  

# n=int(input("n: "))
# for i in range(n):
#         for j in range(2*n-1):
#                 if i==j or i+j==2*n-2:
#                         print("*",end=" ")
#                 else:
#                         print(" ",end=" ")
#         print()

# n: 4
# * * * * * * * 
#   *       *   
#     *   *     
#       *  

# n=int(input("n: "))
# for i in range(n):
#         for j in range(2*n-1):
#                 if i==j or i==0 or i+j==2*n-2:
#                         print("*",end=" ")
#                 else:
#                         print(" ",end=" ")
#         print()

# n: 4
#       * 
#     * * * 
#   * * * * * 
# * * * * * * * 

# n=int(input("n: "))
# for i in range(n):
#         for j in range(n-i-1):
#                 print(" ",end=" ")
#         for k in range(2*i+1):
#                 print("*",end=" ")
#         print()

# n: 3
#     * 
#   * * 
# *   * 
#   * * 
#     * 

# n=int(input("n: "))
# for i in range(2*n-1):
#         for j in range(n):
#                 if i-j==n-1 or i+j==n-1 or j==n-1:
#                         print("*",end=" ")
#                 else:
#                         print(" ",end=" ")
#         print()

# n: 3
#  *      
#  *   *    
#  *     *  
#  *   *    
#  * 

# n=int(input("n: "))
# for i in range(2*n-1):
#         for j in range(n):
#                 if i==j or i+j==2*n-2 or j==0:
#                         print("*",end=" ")
#                 else:
#                         print(" ",end=" ")
#         print()

# n: 3
#     A 
#   B B B 
# C C C C C 

# n=int(input("n: "))
# val=0
# for i in range(n):
#         for j in range(n-i-1):
#                 print(" ",end=" ")
#         for k in range(2*i+1):
#                 print(chr(65+val),end=" ")
#         print()
#         val+=1
#         if val>25:
#                 val=0

# n: 3
#     3 
#   2 2 2 
# 1 1 1 1 1 

# n=int(input("n: "))
# val=n
# if val>9:
#         val=9
# for i in range(n):
#         for j in range(n-i-1):
#                 print(" ",end=" ")
#         for k in range(2*i+1):
#                 print(val,end=" ")
#         print()
#         val-=1
#         if val<1:
#                 val=9

# n: 3
#     1 
#   2 3 4 
# 5 6 7 8 9 

# n=int(input("n: "))
# val=1
# if val>9:
#         val=9
# for i in range(n):
#         for j in range(n-i-1):
#                 print(" ",end=" ")
#         for k in range(2*i+1):
#                 print(val,end=" ")
#                 val+=1
#                 if val>9:
#                         val=1
#         print()

# n: 4
#       D 
#     C C C 
#   B B B B B 
# A A A A A A A 

# n=int(input("n: "))
# val=n-1
# if val>25:
#         val=25
# for i in range(n):
#         for j in range(n-i-1):
#                 print(" ",end=" ")
#         for k in range(2*i+1):
#                 print(chr(65+val),end=" ")
#         print()
#         val-=1
#         if val<0:
#                 val=25

# n: 4
# 1 2 3 4 5 6 7 
#   8 9 1 2 3 
#     4 5 6 
#       7 

# n=int(input("n: "))
# val=1
# if val<1:
#         val=9
# for i in range(n):
#         for j in range(i):
#                 print(" ",end=" ")
#         for k in range(2*n-2*i-1):
#                 print(val,end=" ")
#                 val+=1
#                 if val>9:
#                         val=1
#         print()

# n: 4
# * * * * * * * 
#   * * * * * 
#     * * * 
#       * 

# n=int(input("n: "))
# for i in range(n):
#         for j in range(i):
#                 print(" ",end=" ")
#         for k in range(2*n-2*i-1):
#                 print("*",end=" ")
#         print()

# n=int(input("n: "))
# val=1
# for i in range(n):
#         for j in range(n):
#                 if i==j or i+j==n-1:
#                         print(val,end=" ")
#                 else:
#                         print(" ",end=" ")
#         print()
#         val+=1
#         if val>9:
#                 val=1

# n=int(input("n: "))
# val=1
# # p=True
# for i in range(n):
#         for j in range(n):
#                 if i==j or i+j==n-1:
#                         print("*",end=" ")
#                 else:
#                         print(" ",end=" ")
#         print()


# n=int(input("n: "))
# val=1
# for i in range(n):
#         for j in range(2*n-1):
#                 if i==j or i+j==2*n-2 or i==0:
#                         print(val,end=" ")
#                         val+=1
#                 else:
#                         print(" ",end=" ")
#         print()

n=int(input("n: "))
val=0
if val<0:
        val=25
for i in range(n):
        
        for j in range(n):
                if i+j>=n-1:
                        if i%2==0:
                                print(chr(65+val),end=" ")
                                
                        else:
                                print("$",end=" ")
                
                                
                else:
                        print(" ",end=" ")
        val+=1        
        print()
        
        if val>25:
                val=0

# n=int(input("n: "))
# val=0
# if val<0:
#         val=25
# for i in range(n):
#         for j in range(n):
#                 if i+j>=n-1:
#                         print(chr(65+val),end=" ")
#                         print("$",end=" ")
#                 else:
#                         print(" ",end=" ")
                
#         print()
#         val+=1
#         if val>25:
#                 val=0