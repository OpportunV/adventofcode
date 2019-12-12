def part_one(data):
    layers = []
    for i in range(len(data) // width // height):
        layers.append(data[width * height * i:width * height * (i + 1)])

    target_layer = layers[0]
    for i in range(1, len(layers)):
        if layers[i].count('0') < target_layer.count('0'):
            target_layer = layers[i]
    
    ans = target_layer.count('1') * target_layer.count('2')
    print(ans)
    return layers
    

def part_two(layers):
    img = []
    
    def get_pixel(pos, layers, start=0):
        for layer in layers[start:]:
            if layer[pos] == '0':
                return ' '
            if layer[pos] == '1':
                return '\u25A0'
            if layer[pos] == '2':
                return get_pixel(pos, layers, start + 1)
            
    for i in range(len(layers[0])):
        img.append(get_pixel(i, layers))
    
    for i in range(0, 126, 25):
        print(''.join(img[i: i + 25]))


with open('d8_input.txt') as fin:
    width = 25
    height = 6
    pic_flat = fin.readline()

part_two(part_one(pic_flat))
