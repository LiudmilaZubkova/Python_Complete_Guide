def example_fun():
    local_var = 'I am local var'
    print(f"Inside example_fun {local_var}")

example_fun()

global_var = 'I am global var'
def example_fun_2():
    global global_var
    global_var = 'I am modified'
    print(f"Inside example_fun_2 {global_var}")

example_fun_2()
print(f"outside example_fun_2 {global_var}")