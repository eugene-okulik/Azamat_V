def repeat_me(func):
    def wrapper(*args, **kwargs):
        quantity = kwargs.pop("quantity", 1)
        for _ in range(quantity):
            func(*args, **kwargs)
    return wrapper


@repeat_me
def example(text):
    print(text)


example("print me", quantity=2)

# Option 2
# def repeat_me(**kwargs):
#     def decorator(func):
#         def wrapper(*args):
#             quantity = kwargs.pop("quantity", 1)
#             for i in range(quantity):
#                 func(*args)
#         return wrapper
#     return decorator
#
#
# @repeat_me(quantity=5)
# def example(text):
#     print(text)
#
#
# example("print me")
