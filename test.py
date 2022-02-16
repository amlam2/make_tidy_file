# test.py
from typing import cast


a = cast(int, 1)
b = cast(Mapping[str, Any], a)
c = cast("Type", a)
d = cast("P,", a)
e = cast(func(1, 2), a)
f = cast(str, "abc)")
g = cast(str, func(1, 2))
h = cast(   str,   a )
i = cast(Mapping[str, str  ], {"p": "s"})
j = cast(Sequence[int],  [1, 2, func(1, 2)])
k, l = cast(bool, 1 == 1), cast(Tuple[int, …], (1,))
m =  cast("abc\"", p)
