single_parameter_user = """
class User(Generic[T]):
    pass
"""
single_parameter_user_expected = """
class User[T]():
    pass
"""

multiple_parameter_user = """
class User(Generic[T], BaseUser, Generic[B]):
    pass
"""

multiple_parameter_user_expected = """
class User[T,B](BaseUser):
    pass
"""

multiple_parameter_user_2 = """
class User[C](Generic[T], Generic[B]):
    pass
"""

multiple_parameter_user_2_expected = """
class User[C,T,B]():
    pass
"""

multiple_parameter_user_v2 = """
class User(Generic[B,T,C]):
    pass
"""

multiple_parameter_user_v2_expected = """
class User[B,T,C]():
    pass
"""

no_generic_user = """
class User:
    pass
"""
no_generic_user_expected = """
class User:
    pass
"""

