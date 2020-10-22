import cv2
import sys
import argparse
from edgetpu.detection.engine import DetectionEngine
import numpy as np

filelist = open(sys.argv[1],'r')
PARSER = argparse.ArgumentParser(description='Run detection on trains.')
PARSER.add_argument('-m', '--model', action='store', default='/Users/dhawal/Desktop/aqi/tflite/ssd_mobilenet_v2_coco_quant_postprocess_edgetpu.tflite', help="Path to detection model.")
PARSER.add_argument('-l', '--label', action='store', default='/Users/dhawal/Desktop/aqi/tflite/coco_labels.txt', help="Path to labels text file.")

ARGS = PARSER.parse_args()
ENGINE = DetectionEngine(ARGS.model)
if not ENGINE:
	print("Failed to load detection engine.")
	exit()

