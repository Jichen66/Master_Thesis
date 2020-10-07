'''
evaluate the distance estimation performance for MAE and MSE version and plot it
'''

import os
import numpy as np
import matplotlib.pyplot as plt


#path_gt = "/media/smart/05F013960677C1A7/Jichen_Thesis/code/gt_dist_kitti_480/"  #ground truth
#path_dr = "/media/smart/05F013960677C1A7/Jichen_Thesis/code/jichen_l1_dist_kitti_/"  #detection results
#path_eval = "/media/smart/05F013960677C1A7/Jichen_Thesis/code/jichen_l1_dist_eval/"  # writting results
#path_dr = "/media/smart/05F013960677C1A7/Jichen_Thesis/code/dist_eval_mse/jichen_mse_dist_kitti_/"  #detection results
#path_eval = "/media/smart/05F013960677C1A7/Jichen_Thesis/code/dist_eval_mse/jichen_mse_dist_eval/"  # writting results


## smart dataset mae
#path_gt = "/media/smart/05F013960677C1A7/Jichen_Thesis/code/dist_eval_l1/smart_gt/"  # ground truth
#path_dr = "/media/smart/05F013960677C1A7/Jichen_Thesis/code/dist_eval_l1/jichen_l1_dist_smart_/"  #dr_KITTI
#path_eval = "/media/smart/05F013960677C1A7/Jichen_Thesis/code/dist_eval_l1/jichen_l1_smart_eval/"  #output

## smart dataset mse
path_gt = "/media/smart/05F013960677C1A7/Jichen_Thesis/code/dist_eval_l1/smart_gt/"  # ground truth
path_dr = "/media/smart/05F013960677C1A7/Jichen_Thesis/code/dist_eval_mse/jichen_mse_dist_smart_/"  #dr_KITTI
##path_eval = "/media/smart/05F013960677C1A7/Jichen_Thesis/code/dist_eval_mse/jichen_mse_smart_eval/"  #output

#if not os.path.exists(path_eval):
#    os.makedirs(path_eval)

path_gt_list=os.listdir(path_gt)
path_gt_list.sort() #sort

ff = 0
n_sum = 0
pp = 0
error_sum = 0
xvalue = []
yvalue = []

for file_name in path_gt_list:
    full_path_gt = os.path.join(path_gt, file_name)
    full_path_dr = os.path.join(path_dr, file_name)
    #full_path_eval = os.path.join(path_eval, file_name)


    txt_gt = open(full_path_gt)
    txt_dr = open(full_path_dr)
    #txt_eval = open(full_path_eval,'w')

    split_lines_gt = txt_gt.readlines()
    split_lines_dr = txt_dr.readlines()

    for split_line_gt in split_lines_gt:
        line_gt=split_line_gt.strip().split()
        for split_line_dr in split_lines_dr:
            line_dr = split_line_dr.strip().split()
            if line_dr[0] == line_gt[0]:
                bi=[max(int(line_gt[1]),int(line_dr[2])),max(int(line_gt[2]),int(line_dr[3])),min(int(line_gt[3]),int(line_dr[4])),min(int(line_gt[4]),int(line_dr[5]))]
                iw = bi[2] - bi[0] + 1
                ih = bi[3] - bi[1] + 1
                if iw > 0 and ih > 0:
                    # compute overlap (IoU) = area of intersection / area of union
                    ua = (int(line_dr[4]) - int(line_dr[2]) + 1) * (int(line_dr[5]) - int(line_dr[3]) + 1) + (int(line_gt[3]) - int(line_gt[1])+ 1) * (int(line_gt[4]) - int(line_gt[2]) + 1) - iw * ih
                    ov = iw * ih / ua
                    if ov >= 0.3:
                        n_sum = n_sum+1
                        val = np.abs(float(line_gt[-1])-float(line_dr[-1]))
                        error_sum = error_sum + val
                        xvalue.append(float(line_gt[-1]))
                        yvalue.append(float(line_dr[-1]))
                        if val >= 15:   # 15 meters
                            ff = ff + 1
                        if val >= 5:   # 5 meters
                            pp = pp+1
                        #txt_eval.write(str(val))
                        #txt_eval.write('\n')
                        break
#txt_eval.close()
print('pp: ', pp)
print('ff: ', ff)
print('n_sum: ',n_sum)
acc = 1-pp/n_sum
print('accuracy: ',acc)
print('error_sum:',error_sum)
avg_error = error_sum/n_sum
print('avg_error:', avg_error)

#plt.figure(1)

# plt.scatter(xvalue,yvalue)
# plt.xlabel('Actual Distance(m)')
# plt.ylabel('Predicted Distance(m)')
# plt.plot([0,1000],[0,1000],ls='--',c='.3')
# plt.xlim((0,1000))
# plt.ylim((0,1000))
# x_tick=np.arange(0,1000,100)
# y_tick=np.arange(0,1000,100)
# plt.xticks(x_tick)
# plt.yticks(y_tick)
# plt.title('Distance between Ground Truth and Prediction (MAE)')
# plt.savefig('mae_smart')
# plt.show()

plt.figure(2)

plt.scatter(xvalue,yvalue)
plt.xlabel('Actual Distance(m)')
plt.ylabel('Predicted Distance(m)')
plt.plot([0,1000],[0,1000],ls='--',c='.3')
plt.xlim((0,1000))
plt.ylim((0,1000))
x_tick=np.arange(0,1000,100)
y_tick=np.arange(0,1000,100)
plt.xticks(x_tick)
plt.yticks(y_tick)
plt.title('Distance between Ground Truth and Prediction (MSE)')
plt.savefig('mse_smart')
plt.show()













