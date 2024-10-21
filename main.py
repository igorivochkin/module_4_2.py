#module_4_2.ru

def test_function():
    def  inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

test_function()
inner_function()    #Попытка вызова обречена на провал, так как за пределами test_function
                    #она не определена