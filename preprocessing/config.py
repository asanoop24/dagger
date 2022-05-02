dependencies = {
    "a": None,
    "b": None,
    "c": ["a","b"],
    "d": "c"
}


in_args = {
    "a": {},
    "b": {},
    "c": {
        "x1": ("a","x1"),
        "x2": ("a","x2"),
        "start": ("b")
    },
    "d": {
        "x5": ("c","x4")
    }
}


out_args = {
    "a": ["x1", "x2"],
    "b": ["result"],
    "c": ["x4","x5"],
    "d": ["x6"]
}