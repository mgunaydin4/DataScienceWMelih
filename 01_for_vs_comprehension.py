import time

N = 100_000_000

# FOR DÖNGÜSÜ
start = time.time()

numbers = []
for i in range(N):
    numbers.append(i * 2)

end = time.time()
print(f"For loop süresi: {end - start:.5f} saniye")


# LIST COMPREHENSION
start = time.time()

numbers = [i * 2 for i in range(N)]

end = time.time()
print(f"List comprehension süresi: {end - start:.5f} saniye")

