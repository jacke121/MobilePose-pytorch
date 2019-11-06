from dataloader import Rescale, Wrap, PoseDataset, ToTensor, Augmentation, Expansion
from torchvision import datasets, transforms, utils, models
import os

ROOT_DIR = "./pose_dataset/mpii"  # root dir to the dataset

DEBUG_MODE = False

def get_transform(modeltype, input_size):
    """
    :param modeltype: "resnet" / "mobilenet"
    :param input_size:
    :return:
    """
    # if "resnet" in modeltype:
    #     return Rescale((input_size, input_size))
    # elif "mobilenet" in modeltype:
    #     return Wrap((input_size, input_size))
    # else:
    #     raise ValueError("modeltype is not wrong")
    return Rescale((input_size, input_size))
    # return Wrap((input_size, input_size))


class DatasetFactory:
    def __init__(self):
        pass

    @staticmethod
    def get_train_dataset(modeltype, input_size, debug=DEBUG_MODE):
        """
        :param modeltype: "resnet" / "mobilenet"
        :return: type: PoseDataset
        Example:
        DataFactory.get_train_dataset("resnet", 224)
        In debug mode, it will return a small dataset
        """
        csv_name = "train_joints.csv"
        if debug:
            csv_name = "train_joints-500.csv"

        return PoseDataset(csv_file=os.path.join(ROOT_DIR, csv_name),
                           transform=transforms.Compose([
                               Augmentation(),
                               get_transform(modeltype, input_size),
                            #    Expansion(),
                               ToTensor()
                           ]))

    @staticmethod
    def get_test_dataset(modeltype, input_size, debug=DEBUG_MODE):
        """
        :param modeltype: resnet / mobilenet
        :return: type: PoseDataset
        Example:
        DataFactory.get_test_dataset("resnet", 224)
        In debug mode, it will return a small dataset
        """
        csv_name = "test_joints.csv"
        if debug:
            csv_name = "test_joints-500.csv"
        return PoseDataset(
            csv_file=os.path.join(ROOT_DIR, csv_name),
            transform=transforms.Compose([
                get_transform(modeltype, input_size),
                # Expansion(),
                ToTensor()
            ]))
