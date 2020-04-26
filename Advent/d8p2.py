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

# Need to dive deep through each pixel
final_layer = []
for row in range(height):
    cur_row = []
    for column in range(width):
        layer = 0
        while True:
            cur_pixel = full[layer][row][column]
            if cur_pixel != 2:
                if cur_pixel == 1:
                    cur_row.append('|||')
                else:
                    cur_row.append('   ')
                break
            layer += 1
    final_layer.append(cur_row)

for x in final_layer:
    print(*x, sep='')
