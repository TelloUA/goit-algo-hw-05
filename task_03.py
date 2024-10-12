import os
import timeit
from bm_function import boyer_moore_search
from kmp_function import kmp_search
from rk_function import rabin_karp_search

file_pattern_map = {
    'article_1.txt': ["швидкий час пошуку", "random fsdfa"],
    'article_2.txt': ["BDD", "щось абсолютно невідоме"],
}

algos = [
    kmp_search, 
    boyer_moore_search,
    rabin_karp_search,
]

for path, patterns in file_pattern_map.items():
    with open(path, 'r') as file:
        file_content = file.read()
    
    for function in algos:
        for pattern in patterns:
            print(f"Run function {function.__name__}, search text: {pattern}")
            execution_time = timeit.timeit(lambda: function(file_content, pattern), number=1000)
            print(f"Result of execution {function(file_content, pattern)}")
            print(f"Execution time {execution_time:.3f}")
            print("----------------------")
