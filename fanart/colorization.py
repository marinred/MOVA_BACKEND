import cv2
from .utils import process
from .utils import models
import numpy as np
import torch
from PIL import Image
from uuid import uuid4

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

def colorization(resize_id,hint_id):

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
    hint = cv2.imread(hint_id, cv2.IMREAD_COLOR) # img = cv2.resize(img, dsize=(512, 512), interpolation=cv2.INTER_AREA)
    hint = cv2.cvtColor(hint, cv2.COLOR_BGR2RGB)
    hint = cv2.resize(hint, dsize=(512,512),interpolation=cv2.INTER_AREA)


    resize = cv2.imread(resize_id, cv2.IMREAD_GRAYSCALE).reshape(512, 512, 1)
    input_array = np.concatenate([resize, hint], axis=2)
    with torch.no_grad():
        result = process.ForwardNet(input_array, netS2C, device)
    result = result * 255
    result = result.astype(np.uint8)

    # Save result
    uuid = uuid4().hex +'.png'
    img_media = 'media/'
    result_dir = "fanart/result/"+uuid
    result = Image.fromarray(result)
    result.save(img_media+result_dir)

    return result_dir