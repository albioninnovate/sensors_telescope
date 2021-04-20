import module_b


def function():
    print( 'I am in module a')

if __name__ == "__main__":
    function()
    module_b.function()