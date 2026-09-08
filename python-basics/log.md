\## Day 1 - Hour 2



\### What I built

\- Built the classic \*\*FizzBuzz\*\* program from scratch using only Python documentation.

\- Fixed it three times until the output matched the expected result.



\### Key lessons learned

\- `/` and `%` are not the same:

&#x20; - `/` returns a decimal (float), e.g. `15 / 3 = 5.0`

&#x20; - `%` returns the remainder, e.g. `15 % 3 = 0`, `16 % 3 = 1`

\- Divisibility check must use `%`, not `/`.

&#x20; - Wrong: `i / 3 == 0` — this is never true for positive numbers.

&#x20; - Correct: `i % 3 == 0` — true when `i` is divisible by 3.

\- Order of conditions matters.

&#x20; - The condition for "FizzBuzz" (`i % 3 == 0 and i % 5 == 0`) must come \*\*first\*\*.

&#x20; - If `i % 3 == 0` comes first, then 15 will print "fizz" and never reach "fizzBuzz".

\- `elif` means "else if". It only runs if all previous conditions were false.

\- Indentation and structure of `if / elif / else` blocks must be correct.



\### Code I wrote

```python

for i in range(1, 21):

&#x20;   if i % 3 == 0 and i % 5 == 0:

&#x20;       print("fizzBuzz")

&#x20;   elif i % 3 == 0:

&#x20;       print("fizz")

&#x20;   elif i % 5 == 0:

&#x20;       print("Buzz")

&#x20;   else:

&#x20;       print(i)

