import tkinter as tk


BITMAP = """
#define im_width 32
#define im_height 32
static char im_bits[] = {
0xaf,0x6d,0xeb,0xd6,0x55,0xdb,0xb6,0x2f,
0xaf,0xaa,0x6a,0x6d,0x55,0x7b,0xd7,0x1b,
0xad,0xd6,0xb5,0xae,0xad,0x55,0x6f,0x05,
0xad,0xba,0xab,0xd6,0xaa,0xd5,0x5f,0x93,
0xad,0x76,0x7d,0x67,0x5a,0xd5,0xd7,0xa3,
0xad,0xbd,0xfe,0xea,0x5a,0xab,0x69,0xb3,
0xad,0x55,0xde,0xd8,0x2e,0x2b,0xb5,0x6a,
0x69,0x4b,0x3f,0xb4,0x9e,0x92,0xb5,0xed,
0xd5,0xca,0x9c,0xb4,0x5a,0xa1,0x2a,0x6d,
0xad,0x6c,0x5f,0xda,0x2c,0x91,0xbb,0xf6,
0xad,0xaa,0x96,0xaa,0x5a,0xca,0x9d,0xfe,
0x2c,0xa5,0x2a,0xd3,0x9a,0x8a,0x4f,0xfd,
0x2c,0x25,0x4a,0x6b,0x4d,0x45,0x9f,0xba,
0x1a,0xaa,0x7a,0xb5,0xaa,0x44,0x6b,0x5b,
0x1a,0x55,0xfd,0x5e,0x4e,0xa2,0x6b,0x59,
0x9a,0xa4,0xde,0x4a,0x4a,0xd2,0xf5,0xaa
};
"""

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('800x800')
        self.title('Mandelbrot Drawing Program')

        # self.mandelbrot_bitmap = self.create_mandelbrot_bitmap()

        # self.bitmap_image = tk.BitmapImage(data=BITMAP)
        self.bitmap_image = tk.BitmapImage(data=self.create_mandelbrot_bitmap(750, 750))
        print(self.bitmap_image, type(self.bitmap_image))
        self.fractal_label = tk.Label(self, image=self.bitmap_image)
        self.fractal_label.pack(fill=tk.BOTH, expand=True)


    def bitmapify(self, width, height, pixels):
        bmp_string = '#define im_width ' + str(width) + '\n'
        bmp_string += '#define im_height ' + str(height) + '\n'
        bmp_string += 'static char im_bits[] = {'
        bmp_string += ','.join([hex(pixel) for pixel in pixels])
        bmp_string += '};'
        return bmp_string

    def create_mandelbrot_bitmap(self, width, height):
        return tk.BitmapImage(data=self.bitmapify(width, height, self.compute_mandelbrot(width, height)))

    def compute_mandelbrot(self, width, height):
        x_origin = width // 2
        y_origin = height // 2
        mandelbrot = []

        for i in range(0, width):
            for j in range(0, height):
                c = complex((i - x_origin)/x_origin, (j - y_origin) / y_origin)
                if MainWindow.test_mandelbrot(c):
                    mandelbrot.append(255)
                else:
                    mandelbrot.append(0)

        return mandelbrot

    @staticmethod
    def test_mandelbrot(c):
        z = 0
        for i in range(100):
            z = z * z + c
            if (c.conjugate() * c).real > 100:
                return False

        return True

if __name__ == '__main__':
    main_window = MainWindow()
    main_window.mainloop()
