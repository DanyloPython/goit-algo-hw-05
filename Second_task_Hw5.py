import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    
    
    for number in re.finditer(r'\b\d+(\.\d+)?\b', text):
        yield float(number.group())

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
  
   
    return sum(func(text))


text_example = "Ми заробили 2012.5 доларів в січні, 1500 у лютому та 2500.75 у березні."
total_profit = sum_profit(text_example, generator_numbers)
print(f"Загальний прибуток: {total_profit}")
