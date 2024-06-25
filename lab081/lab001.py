def lab001():
    from ultralytics import YOLO

    # Load a model
    model = YOLO("yolov8n.yaml")  # build a new model from scratch
    model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

    # Use the model
    model.train(data="coco8.yaml", epochs=3)  # train the model
    metrics = model.val()  # evaluate model performance on the validation set
    results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
    path = model.export(format="onnx")  # export the model to ONNX format


def lab002():
    from ultralytics import YOLO
    import os

    # Load a model
    model = YOLO("yolov8n.pt")  # pretrained YOLOv8n model

    root_dir = "/Users/li/Downloads/temp/yolo"
    # Find all jpg files in root_dir
    files = [os.path.join(root_dir,file) for file in os.listdir(root_dir) if file.endswith(".jpg")]

    # Print the list of jpg files

    # Run batched inference on a list of images
    results = model(files)  # return a list of Results objects

    # Process results list
    for index, result in enumerate(results):
        boxes = result.boxes  # Boxes object for bounding box outputs
        masks = result.masks  # Masks object for segmentation masks outputs
        keypoints = result.keypoints  # Keypoints object for pose outputs
        probs = result.probs  # Probs object for classification outputs
        obb = result.obb  # Oriented boxes object for OBB outputs
        result.show()  # display to screen
        result.save(filename=f"result_{index}.jpg")  # save to disk
        
def lab003():
    """
    视频
    """
    import cv2
    from ultralytics import YOLO

    # Load the YOLOv8 model
    model = YOLO("yolov8n.pt")

    # Open the video file
    video_path = "/Users/li/Downloads/temp/yolo/VIDEO_1719275734042.MP4"
    cap = cv2.VideoCapture(video_path)

    # Loop through the video frames
    while cap.isOpened():
        # Read a frame from the video
        success, frame = cap.read()

        if success:
            # Run YOLOv8 inference on the frame
            results = model(frame)

            # Visualize the results on the frame
            annotated_frame = results[0].plot()

            # Display the annotated frame
            cv2.imshow("YOLOv8 Inference", annotated_frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            # Break the loop if the end of the video is reached
            break

    # Release the video capture object and close the display window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    # lab001()
    # lab002()
    lab003()

    pass