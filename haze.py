import numpy as np
from PIL import Image
import png
import matplotlib.pyplot as plt


class Haze(object):

    def __init__(self):
        self.focal_length = 1
        self.baseline = 1
        self.beta = 2
        self.height = 0
        self.width = 0
        self.haze_intensity = 200
        self.noise_variance = 0.0001
        self.noise_mean = 0
        self.infinite_far = 1
        self.left0 = None
        self.left1 = None
        self.right0 = None
        self.right1 = None
        self.disp_left = None
        self.disp_right = None
        self.alpha_left = None
        self.alpha_right = None
        self.haze_map = None
        self.rendered_left = None
        self.rendered_right = None
        self.read_background_map()
        self.read_disparity_map()

    def set_alpha_param(self, focal_length, baseline):
        self.focal_length = focal_length
        self.baseline = baseline

    def set_haze_intensity(self, intensity):
        self.haze_intensity = intensity

    def set_noise_param(self, mean, variance):
        self.noise_mean = mean
        self.noise_variance = variance

    def set_beta(self, beta_value):
        self.beta = beta_value

    def set_depth_param(self, infinite_far):
        self.infinite_far = infinite_far

    def read_disparity_map(self):
        self.disp_left = self.read_disp_png('disp_left.png')
        self.disp_right = self.read_disp_png('disp_right.png')

    def read_background_map(self):
        self.left0 = self.read_image('left0.png')
        self.right0 = self.read_image('right0.png')
        self.left1 = self.read_image('left1.png')
        self.right1 = self.read_image('right1.png')
        # sanity check
        if self.left0.shape == self.right0.shape:
            (self.height, self.width) = self.left0.shape[0:2]
        else:
            raise AssertionError

    def read_haze(self):
        haze = np.ones((self.height, self.width), dtype=np.float32)
        self.haze_map = haze * self.haze_intensity

    def get_depth_map(self, disparity_map):
        mask = (disparity_map == 0)
        disparity_map[mask] = self.infinite_far
        depth_map = self.focal_length * self.baseline / disparity_map
        return depth_map

    def get_alpha_map(self):
        depth_left = self.get_depth_map(self.disp_left.astype(np.float32))
        depth_right = self.get_depth_map(self.disp_right.astype(np.float32))
        self.alpha_left = np.exp(-1 * self.beta * depth_left)
        self.alpha_right = np.exp(-1 * self.beta * depth_right)

    def synthesize(self):
        self.read_haze()
        self.get_alpha_map()
        left = self.render_haze(self.alpha_left, self.left0, self.haze_map)
        self.rendered_left = left.astype(np.uint8)
        right = self.render_haze(self.alpha_right, self.right0, self.haze_map)
        self.rendered_right = right.astype(np.uint8)

    @staticmethod
    def visualize(img):
        plt.imshow(img)
        plt.show()

    @staticmethod
    def read_image(image_file):
        img = Image.open(image_file)
        img_array = np.array(img, dtype=np.uint8)
        return img_array

    @staticmethod
    def render_haze(alpha_map, background_map, haze_map):
        render_map = np.zeros(background_map.shape)
        render_map[:, :, 0] = alpha_map * background_map[:, :, 0] + (1 - alpha_map) * haze_map
        render_map[:, :, 1] = alpha_map * background_map[:, :, 1] + (1 - alpha_map) * haze_map
        render_map[:, :, 2] = alpha_map * background_map[:, :, 2] + (1 - alpha_map) * haze_map
        return render_map

    @staticmethod
    def read_disp_png(disp_file):
        """
        Read kitti disp from .png file
        :param disp_file:
        :return:
        """
        image_object = png.Reader(filename=disp_file)
        image_direct = image_object.asDirect()
        image_data = list(image_direct[2])
        (w, h) = image_direct[3]['size']
        channel = len(image_data[0]) / w
        disp = np.zeros((h, w, channel), dtype=np.float64)
        for i in range(len(image_data)):
            for j in range(channel):
                disp[i, :, j] = image_data[i][j::channel]
        return disp[:, :, 0]
