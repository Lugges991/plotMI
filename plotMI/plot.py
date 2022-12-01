import tkinter as tk
import matplotlib
import numpy as np
import matplotlib.pyplot as plt


from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

class PlotMI:
    def __init__(self, img):
        # Create a container
        self.img = img.copy()
        self.max = img.shape[-1]-1
        self.master = tk.Tk()
        frame = tk.Frame(self.master)
        self. index = img.shape[-1]//2
        # Create 2 buttons

        fig = Figure(figsize=(16, 9))
        self.axs = fig.subplots(1, 3)
        [a.set_axis_off() for a in self.axs]
        self.axs[0].imshow(self.img[:, :, self.index])
        self.axs[1].imshow(self.img[:, self.index, :])
        self.axs[2].imshow(self.img[self.index, :, :])

        self.canvas = FigureCanvasTkAgg(fig, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side='top', fill='both', expand=1)
        self.canvas.mpl_connect("scroll_event", self._on_mousewheel)
        frame.pack()

    def _on_mousewheel(self, event):

        if event.button == "up":
            if self.index >= self.max:
                self.index  = self.index
            else:
                self.index += 1
        elif event.button == "down":
            if self.index == 0:
                self.index = 0
            else:
                self.index -= 1


        self.axs[0].imshow(self.img[:, :, self.index])
        self.axs[1].imshow(self.img[:, self.index, :])
        self.axs[2].imshow(self.img[self.index, :, :])
        self.canvas.draw()

    def __call__(self, ):
        self.master.mainloop()


if __name__ == "__main__":
    import nibabel as nib
    img = nib.load(
        "/mnt/DATA/datasets/ABIDEII/50002/baseline/anat_1/anat.nii.gz").get_fdata()
    app = PlotMI(img)
    app()
    # plot3D(img)
