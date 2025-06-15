# 1.

import threading
import math
from queue import Queue

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def prime_checker(start: int, end: int, result_queue: Queue) -> None:
    """Check for primes in a sub-range and put results in a queue."""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    result_queue.put(primes)

def parallel_prime_finder(start: int, end: int, thread_count: int = 4) -> list[int]:
    """Divide range among threads to find primes in parallel."""
    if start > end:
        raise ValueError("Start must be less than or equal to end")
    
    range_size = end - start + 1
    chunk_size = max(1, range_size // thread_count)
    threads = []
    result_queue = Queue()
    
    # Create and start threads
    for i in range(thread_count):
        chunk_start = start + i * chunk_size
        chunk_end = start + (i + 1) * chunk_size - 1 if i < thread_count - 1 else end
        thread = threading.Thread(
            target=prime_checker,
            args=(chunk_start, chunk_end, result_queue)
        )
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    # Collect results
    primes = []
    while not result_queue.empty():
        primes.extend(result_queue.get())
    
    return sorted(primes)

if __name__ == "__main__":
    try:
        start = int(input("Enter start of range: "))
        end = int(input("Enter end of range: "))
        thread_count = int(input("Enter number of threads (default 4): ") or 4)
        
        print(f"\nChecking primes between {start} and {end} using {thread_count} threads...")
        
        primes = parallel_prime_finder(start, end, thread_count)
        
        print(f"\nFound {len(primes)} prime numbers:")
        print(primes)
    
    except ValueError as e:
        print(f"Error: {e}")


# 2.

import threading
from collections import defaultdict
from queue import Queue
import time

def process_chunk(lines: list[str], result_queue: Queue) -> None:
    """Process a chunk of lines and count words in it."""
    local_count = defaultdict(int)
    for line in lines:
        words = line.strip().lower().split()
        for word in words:
            # Remove punctuation (basic cleanup)
            word = ''.join(c for c in word if c.isalnum())
            if word:
                local_count[word] += 1
    result_queue.put(local_count)

def threaded_word_count(file_path: str, num_threads: int = 4) -> dict[str, int]:
    """Count words in a file using multiple threads."""
    # Read the file and split into chunks
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    chunk_size = len(lines) // num_threads
    threads = []
    result_queue = Queue()
    
    # Create and start threads
    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_threads - 1 else len(lines)
        chunk = lines[start:end]
        thread = threading.Thread(
            target=process_chunk,
            args=(chunk, result_queue)
        )
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    
    # Merge results from all threads
    global_count = defaultdict(int)
    while not result_queue.empty():
        chunk_result = result_queue.get()
        for word, count in chunk_result.items():
            global_count[word] += count
    
    return dict(global_count)

if __name__ == "__main__":
    file_path = input("Enter file path: ").strip()
    num_threads = int(input("Number of threads (default 4): ") or 4)
    
    print(f"\nProcessing {file_path} with {num_threads} threads...")
    start_time = time.time()
    
    try:
        word_counts = threaded_word_count(file_path, num_threads)
        print(f"\nCompleted in {time.time() - start_time:.2f} seconds")
        
        # Display top 20 words by frequency
        sorted_words = sorted(word_counts.items(), key=lambda x: -x[1])
        print("\nTop 20 words:")
        for word, count in sorted_words[:20]:
            print(f"{word}: {count}")
            
        # Save full results to a file
        with open("word_counts.txt", 'w', encoding='utf-8') as f:
            for word, count in sorted_words:
                f.write(f"{word}: {count}\n")
        print("\nFull results saved to 'word_counts.txt'")
    
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
    except Exception as e:
        print(f"Error: {str(e)}")
