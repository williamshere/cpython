with open("Lib/xml/dom/minicompat.py", "r") as f:
    content = f.read()

old_text = """#   defproperty   -- function used in conjunction with GetattrMagic;
#                    using these together is needed to make them work
#                    as efficiently as possible in both Python 2.2+
#                    and older versions.  For example:
#
#                        class MyClass(GetattrMagic):
#                            def _get_myattr(self):
#                                return something
#
#                        defproperty(MyClass, "myattr",
#                                    "return some value")
#
#                    For Python 2.2 and newer, this will construct a
#                    property object on the class, which avoids
#                    needing to override __getattr__().  It will only
#                    work for read-only attributes.
#
#                    For older versions of Python, inheriting from
#                    GetattrMagic will use the traditional
#                    __getattr__() hackery to achieve the same effect,
#                    but less efficiently.
#
#                    defproperty() should be used for each version of
#                    the relevant _get_<property>() function."""

new_text = """#   defproperty   -- function used to construct a read-only property
#                    object on a class.  For example:
#
#                        class MyClass:
#                            def _get_myattr(self):
#                                return something
#
#                        defproperty(MyClass, "myattr",
#                                    "return some value")
#
#                    It will only work for read-only attributes.
#
#                    defproperty() should be used for each version of
#                    the relevant _get_<property>() function."""

content = content.replace(old_text, new_text)
with open("Lib/xml/dom/minicompat.py", "w") as f:
    f.write(content)
