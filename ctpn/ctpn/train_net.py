import pprint
import sys
import os.path

import tensorflow.compat.v1 as tf

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
this_dir = os.path.dirname(__file__)

from lib.fast_rcnn.train import get_training_roidb, train_net
from lib.fast_rcnn.config import cfg_from_file, get_output_dir, get_log_dir
from lib.datasets.factory import get_imdb
from lib.networks.factory import get_network
from lib.fast_rcnn.config import cfg

if __name__ == '__main__':
    cfg_from_file('../ctpn/text.yml')
    print('Using config:')
    pprint.pprint(cfg)
    imdb = get_imdb('voc_2007_trainval')

    print('Loaded dataset `{:s}` for training'.format(imdb.name))
    roidb = get_training_roidb(imdb)
    output_dir = get_output_dir(imdb, None)
    log_dir = get_log_dir(imdb)
    print('Output will be saved to `{:s}`'.format(output_dir))
    print('Logs will be saved to `{:s}`'.format(log_dir))

    device_name = '/gpu:0'
    print(device_name)

    network = get_network('VGGnet_train')
    ctpn_model_path = os.path.join(os.getcwd(), 'ctpn', 'models')
    print(ctpn_model_path)
    ckpt = tf.train.get_checkpoint_state(ctpn_model_path)

    # train_net(network, imdb, roidb, output_dir=output_dir, log_dir=log_dir,
    #           pretrained_model='../data/pretrain/VGG_imagenet.npy', max_iters=250, restore=bool(int(0)))
