a = "I am global variable!"


def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():
        a = "I am local variable!"
        print(a)
    return inner_function  # 1.1 return the function to be called later


a = enclosing_funcion()()
