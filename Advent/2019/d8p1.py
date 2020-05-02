with open('d8p1.txt', 'r') as f:
    pixels = f.readline()

pixels = pixels[:-1]  # Drop the newline char at the end
pixels = list(pixels)
pixels = [int(pixel) for pixel in pixels]

width = 25
height = 6
layers = int(len(pixels) / width / height)
idx = 0
full = []
for _ in range(layers):
    cur_layer = []
    for _ in range(height):
        cur_row = []
        for _ in range(width):
            cur_row.append(pixels[idx])
            idx += 1
        cur_layer.append(cur_row)
    full.append(cur_layer)

min_zeros = 100
# Find the layer with the maximum numer
for layer in full:
    num_zeros = sum(row.count(0) for row in layer)
    if num_zeros < min_zeros:
        min_zeros = num_zeros
        min_layer = layer

num_ones = sum(row.count(1) for row in min_layer)
num_twos = sum(row.count(2) for row in min_layer)

ans = num_ones * num_twos
ans
