# coding: utf-8

from __future__ import print_function
import matplotlib.pyplot as plt
# get_ipython().run_line_magic('matplotlib', 'inline')

import argparse
import os
# os.environ['CUDA_VISIBLE_DEVICES'] = '1'
import numpy as np
from models import *
from models.skipfc import skipfc
from models.skip import skip
import cv2
import torch
import torch.optim
import glob
from skimage.io import imread
from skimage.io import imsave
from skimage.measure import compare_psnr
from models.downsampler import Blurconv2
from torch.optim.lr_scheduler import MultiStepLR
from util.sr_utils import *
import re
import urllib.request
import scipy.misc

def parse_args():

    parser=argparse.ArgumentParser()
    parser.add_argument("--preprocess", type=bool, default=False, help='run prepare_data or not')
    parser.add_argument('--num_iter', type=int, default=1000, help='number of epochs of training')
    parser.add_argument('--img_size', type=int, default=[256, 256], help='size of each image dimension')
    parser.add_argument('--kernel_size', type=int, default=[21, 21], help='size of blur kernel [height, width]')
    parser.add_argument('--data_path', type=str, default="DataSet/Levin/blurry/", help='path to blurry image')
    parser.add_argument('--save_path', type=str, default="res/", help='path to blurry image')
    parser.add_argument('--lam_fidelity', type=float, default=10000, help='lamda value for fidelity term')
    parser.add_argument('--lam_reg_img', type=float, default=50000, help='lamda value for reg term on image')
    parser.add_argument('--lam_reg_ker', type=float, default=100, help='lamda value for reg term on kernel')
    parser.add_argument('--save_frequency', type=int, default=1000, help='lfrequency to save results')
    opt=parser.parse_args()
    # print(opt)
    return opt

class TVLoss(nn.Module):
    def __init__(self, tv_loss_weight=1):
        super(TVLoss, self).__init__()
        self.tv_loss_weight=tv_loss_weight

    def forward(self, x):
        batch_size=x.size() [0]
        h_x=x.size() [2]
        w_x=x.size() [3]
        count_h=self.tensor_size(x [:, :, 1:, :])
        count_w=self.tensor_size(x [:, :, :, 1:])
        h_tv=torch.pow((x [:, :, 1:, :] - x [:, :, :h_x - 1, :]), 2).sum()
        w_tv=torch.pow((x [:, :, :, 1:] - x [:, :, :, :w_x - 1]), 2).sum()
        return self.tv_loss_weight * 2 * (h_tv / count_h + w_tv / count_w) / batch_size

    @staticmethod
    def tensor_size(t):
        return t.size() [1] * t.size() [2] * t.size() [3]

def manage2(input_path):
    opt = parse_args()
    imsize=-1
    enforse_div32='noCROP'  # we usually need the dimensions to be divisible by a power of two (32 in this case)
    PLOT=True
    torch.backends.cudnn.enabled=True
    torch.backends.cudnn.benchmark=True
    dtype=torch.cuda.FloatTensor

    end="i"
    f=input_path [input_path.rfind(end):]
    print(f) # im1_kernel6.png
    # files_source=glob.glob(os.path.join(opt.data_path, '*.png'))
    # files_source.sort()
    save_path=opt.save_path
    os.makedirs(save_path, exist_ok=True)

    # process data
    # for f in files_source:
    INPUT='noise'
    pad='reflection'
    LR=0.01
    tv_weight=0.0
    num_iter=opt.num_iter
    reg_noise_std=0.001

    path_to_image=f
    imgname=os.path.basename(f)
    imgname=os.path.splitext(imgname) [0]

    if imgname.find('kernel1') != -1:
        opt.kernel_size=[17, 17]
    if imgname.find('kernel2') != -1:
        opt.kernel_size=[15, 15]
    if imgname.find('kernel3') != -1:
        opt.kernel_size=[13, 13]
    if imgname.find('kernel4') != -1:
        opt.kernel_size=[27, 27]
    if imgname.find('kernel5') != -1:
        opt.kernel_size=[11, 11]
    if imgname.find('kernel6') != -1:
        opt.kernel_size=[19, 19]
    if imgname.find('kernel7') != -1:
        opt.kernel_size=[21, 21]
    if imgname.find('kernel8') != -1:
        opt.kernel_size=[21, 21]

    imgs=load_imgs_deblur(input_path, imsize, enforse_div32)
    # imgs = scipy.misc.imread(input_path)
    img_size=imgs.shape
    print(img_size)
    # ######################################################################
    padh, padw=opt.kernel_size [0] - 1, opt.kernel_size [1] - 1
    opt.img_size [0], opt.img_size [1]=img_size [1] + padh, img_size [2] + padw
    '''
    x_subnet:
    '''
    # x_subnet:
    input_depth=8

    net_input=get_noise(input_depth, INPUT, (opt.img_size [0], opt.img_size [1])).type(dtype).detach()
    # TODO:
    print('net_input: ', net_input.shape)

    NET_TYPE='texture_nets'  # UNet, ResNet
    net=skip(input_depth, 1,
             num_channels_down=[128, 128, 128, 128, 128],
             num_channels_up=[128, 128, 128, 128, 128],
             num_channels_skip=[16, 16, 16, 16, 16],
             upsample_mode='bilinear',
             need_sigmoid=True, need_bias=True, pad=pad, act_fun='LeakyReLU')
    if os.path.exists(os.path.join(opt.save_path, "%s_xnet.pth" % imgname)):
        net=torch.load(os.path.join(opt.save_path, "%s_xnet.pth" % imgname))

    net=net.type(dtype)

    '''
    k_subnet:
    '''
    # k_subnet:
    n_k=200
    net_input_kernel=get_noise(n_k, INPUT, (1, 1)).type(dtype).detach()
    net_input_kernel.squeeze_()

    net_kernel=skipfc(
        n_k, opt.kernel_size [0] * opt.kernel_size [1],
        num_channels_down=[1000, 64, 64, 64, 64],
        num_channels_up=[64, 64, 64, 64, 64],
        num_channels_skip=[16, 16, 16, 16, 16],
        upsample_mode='bilinear',
        need_sigmoid=True, need_bias=True, pad=pad, act_fun='LeakyReLU')
    if os.path.exists(os.path.join(opt.save_path, "%s_knet.pth" % imgname)):
        net_kernel=torch.load(os.path.join(opt.save_path, "%s_knet.pth" % imgname))

    net_kernel=net_kernel.type(dtype)

    # ######################################################################

    # Losses
    mse=torch.nn.MSELoss().type(dtype)
    L1=torch.nn.L1Loss(reduction='sum').type(dtype)
    tv_loss2=TVLoss(tv_loss_weight=0e-6)

    img_LR_var=np_to_torch(imgs).type(dtype)

    optimizer=torch.optim.Adam([{'params': net.parameters()}, {'params': net_kernel.parameters(), 'lr': 1e-4}], lr=LR)

    scheduler=MultiStepLR(optimizer, milestones=[800, 1200, 1600], gamma=0.5)  # learning rates

    net_input_saved=net_input.detach().clone()
    net_input_kernel_saved=net_input_kernel.detach().clone()

    for step in range(num_iter):

        # input regularization
        net_input=net_input_saved + reg_noise_std * torch.zeros(net_input_saved.shape).type_as(
            net_input_saved.data).normal_()
        # net_input_kernel = net_input_kernel_saved + reg_noise_std*torch.zeros(net_input_kernel_saved.shape).type_as(net_input_kernel_saved.data).normal_()

        # change the learning rate
        scheduler.step(step)
        optimizer.zero_grad()

        # get the network output
        out_x=net(net_input)
        # TODO:
        # print("out_x: ", out_x.shape)

        out_k=net_kernel(net_input_kernel)
        out_k_m=out_k.view(-1, 1, opt.kernel_size [0], opt.kernel_size [1])
        #    print(out_k_m)
        out_y=nn.functional.conv2d(out_x, out_k_m, padding=0, bias=None)

        # calculate the loss and take an optimizer step
        total_loss=mse(out_y, img_LR_var) + tv_loss2(out_x)  # + tv_loss2(out_k_m)
        total_loss.backward()
        optimizer.step()
        # print loss index parameter
        print("[step %d] loss: %.4f, mseloss: %.4f, tvloss: %.4f" %
              (step + 1, total_loss, mse(out_y, img_LR_var), tv_loss2(out_x)))

        if PLOT and (step + 1) % opt.save_frequency == 0:
            print('Iteration %05d' % (step + 1))

            save_path=os.path.join(opt.save_path, '%s.png' % imgname)
            # save_path=os.path.join(opt.save_path, imgname)
            out_x_np=torch_to_np(out_x)
            out_x_np=out_x_np.squeeze()
            out_x_np=out_x_np [padh // 2:padh // 2 + img_size [1], padw // 2:padw // 2 + img_size [2]]
            imsave(save_path, out_x_np)
            if step == opt.num_iter:
                print("step: ", step)

# blurryImage = 'E:/PyQt5/Openimg/DataSet/Levin/blurry/im1_kernel1.png'
# manage2(blurryImage)








