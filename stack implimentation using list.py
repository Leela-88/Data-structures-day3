#stack using list
stack=[]
def push():
    element=int(input("enter the element"))
    stack.append(element)
    print(stack)

def pop():
    if stack is None:  # or not stack
        print("stack is empty")
    else:
        e=stack.pop()
        print(stack)
                     
while True:
    print("select operation 1.push 2.pop 3.quit")
    choice=int(input("enter the choice"))
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print("enter the correct operation")
               
                   
               
