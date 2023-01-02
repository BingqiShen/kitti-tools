import time
import eval as kitti_eval
import pickle

def evaluation(eval_gt_annos, eval_det_annos, class_names):

    print("type(eval_gt_annos): ", type(eval_gt_annos))
    print("type(eval_det_annos): ", type(eval_det_annos))
    # ap_result_str, ap_dict = kitti_eval.get_official_eval_result(eval_gt_annos, eval_det_annos, class_names)
    ap_result_str, ap_dict = kitti_eval.get_official_eval_result_sbq(eval_gt_annos, eval_det_annos, class_names)

    return ap_result_str, ap_dict


if __name__ == '__main__':
    gt_path = '../pkl/gt.pkl'
    # det_path = '../pkl/det.pkl'
    det_path = '../pkl/3D-Fusion.pkl'
    with open(gt_path, 'rb') as f1:
        eval_gt_annos = pickle.load(f1)
    with open(det_path, 'rb') as f2:
        eval_det_annos = pickle.load(f2)
    
    class_names = ['Car', 'Pedestrian', 'Cyclist']
    ap_result_str, ap_dict = evaluation(eval_gt_annos, eval_det_annos, class_names)

    print(ap_result_str)
