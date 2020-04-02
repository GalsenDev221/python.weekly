from PIL import Image

def black_and_white(input_image_path,
                    output_image_path):
    color_image = Image.open(input_image_path)

    bw = color_image.convert('L')

    bw.save(output_image_path)

if __name__ == '__name__':
    black_and_white('python-weekly.png',
                    'b_python-weekly.png')


# PROG
# Ce script Python permet de transformer
# une copie d'une image en couleur en une image en noir et blanc. 👇🏾