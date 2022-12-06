import cv2
from .utils import process
from .utils import models
import numpy as np
import torch
from PIL import Image

def sketchProcess(image_name):

    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    with torch.no_grad():
        netC2S = models.Color2Sketch(input_nc=3,
                                        output_nc=1,
                                        norm='IN',
                                        SN=True,
                                        activation='relu',
                                        residual=False,
                                        ckpt_path='fanart/utils/checkpoint/color2sketch.pth').to(device)
        netS2C = models.Colorizenet(input_nc=4,
                                    output_nc=3,
                                    norm='IN',
                                    SN=True,
                                    activation='relu',
                                    residual=True,
                                    ckpt_path='fanart/utils/checkpoint/sketch2color.pth').to(device)

        netC2S.eval()
        netS2C.eval()

    # Iamge process
    img = cv2.imread('media/fanart/origin/'+image_name, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, dsize=(512, 512), interpolation=cv2.INTER_AREA)
    with torch.no_grad():
        img_ = process.ForwardNet(img, netC2S, device)
    img_ = img_ * 255
    img_ = img_.astype(np.uint8)
    img_ = np.broadcast_to(img_, img.shape)

    # Save sketch
    img_name_ = image_name
    img_media = 'media/'
    img_dir_ = 'fanart/resize/' + img_name_
    img_ = Image.fromarray(img_)
    img_.save(img_media + img_dir_)

    return img_dir_