# Master_Thesis
Topic: Modification of YOLOv3(Keras) for object distance estimation  
(original model: https://github.com/qqwweee/keras-yolo3)  

Methods:  
1.Modify the output of YOLOv3 by adding a predicted distance variable at each prediction layer.   
2.Meanwhile, modify the original YOLOv3 loss function by adding a distance loss function (here I tried MAE,MSE,RMSE. MAE is the best among them).  
3.Retrain the modified model by main using processed public KITTI dataset and inhouse SMART dataset. (Transfer Learning, Finetune...)  
4.Evaluation: judge the performance of object detection (metrics of TP, PR curve, mAP) and distance estimation separately.  

Some test examples are shown here:  
![testimage_kitti1](https://github.com/Jichen66/Master_Thesis/blob/master/result_images/result_007022.png)
![testimage_kitti2](https://github.com/Jichen66/Master_Thesis/blob/master/result_images/result_007395.png)
![testimage_kitti3](https://github.com/Jichen66/Master_Thesis/blob/master/result_images/result_007476.png)
![testimage_smart1](https://github.com/Jichen66/Master_Thesis/blob/master/result_images/result_frame000409.JPEG)
