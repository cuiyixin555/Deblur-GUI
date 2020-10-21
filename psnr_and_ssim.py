import numpy as np
import scipy.misc

def PSNRLossnp(y_true, y_pred):
    return 10 * np.log(255 * 2 / (np.mean(np.square(y_pred - y_true))))

def SSIMnp(y_true, y_pred):
    u_true=np.mean(y_true)
    u_pred=np.mean(y_pred)
    var_true=np.var(y_true)
    var_pred=np.var(y_pred)
    std_true=np.sqrt(var_true)
    std_pred=np.sqrt(var_pred)
    c1=np.square(0.01 * 7)
    c2=np.square(0.03 * 7)
    ssim=(2 * u_true * u_pred + c1) * (2 * std_pred * std_true + c2)
    denom=(u_true ** 2 + u_pred ** 2 + c1) * (var_pred + var_true + c2)
    return ssim / denom

def calculate_psnr_and_ssim(groundtruth, sharp, list):
    # groundtruth and sharp is picture numpy
    list[0] = str(round(PSNRLossnp(groundtruth, sharp), 4))
    list[1] = str(round(SSIMnp(groundtruth, sharp), 4))
    # return psnr, ssim

# sharp_path='E:/PyQt5/Openimg/res/k014.png'
# groundtruth_path='E:/PyQt5/Openimg/DataSet/gopro_blur/groundtruth/k014.png'
#
# sharp=scipy.misc.imread(sharp_path)
# groundtruth=scipy.misc.imread(groundtruth_path)
#
# psnr, ssim=calculate_psnr_and_ssim(groundtruth, sharp)
#
# print('psnr: %.4f' % psnr)
# print('ssim: %.4f' % ssim)




