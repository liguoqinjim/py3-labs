import cv2
from ultralytics import YOLO

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
    # model = YOLO("yolov8n.pt")
    model = YOLO("yolov10n.pt")

    # Open the video file
    video_path = "/Users/li/Downloads/temp/yolo/VIDEO_1719275734042.MP4"
    # video_path = "/Users/li/Movies/Mac Video Library/VIDEO_1719275734042.mp4"
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

def lab004():
    """
    视频
    """
    import cv2
    from ultralytics import YOLO

    # Load the YOLO model
    model = YOLO("yolov10n.pt")

    # Open the video file
    # video_path = "/Users/li/Downloads/temp/yolo/VIDEO_1719275734042.MP4"
    video_path = '/Users/li/Downloads/temp/yolo/002.MP4'
    # video_path = '/Users/li/Downloads/temp/yolo/003.MP4'
    cap = cv2.VideoCapture(video_path)

    # Define the region of interest (ROI) coordinates
    # x1, y1, x2, y2 = 100, 100, 500, 500  # 示例坐标，按实际需求修改
    # (813,1032,253,172)
    # x1, y1, x2, y2 = 837, 142, 214, 92
    x1, y1, w, h = 837, 142, 214, 92
    x2, y2 = x1 + w, y1 + h

    # Loop through the video frames
    while cap.isOpened():
        # Read a frame from the video
        success, frame = cap.read()

        if success:
            # Crop the frame to the region of interest (ROI)
            roi_frame = frame[y1:y2, x1:x2]

            # Run YOLO inference on the ROI frame
            results = model(roi_frame)

            # Visualize the results on the ROI frame
            annotated_roi_frame = results[0].plot()

            # Replace the original ROI in the frame with the annotated ROI
            frame[y1:y2, x1:x2] = annotated_roi_frame

            # Display the annotated frame
            # cv2.imshow("YOLO Inference", frame)
            cv2.imshow("YOLO Inference", roi_frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            # Break the loop if the end of the video is reached
            break

    # Release the video capture object and close the display window
    cap.release()
    cv2.destroyAllWindows()

def lab005():
    """
    视频
    """
    # Load the YOLO model
    model = YOLO("yolov10n.pt")

    # Open the video file
    # video_path = '/Users/li/Downloads/temp/yolo/002.MP4'
    video_path = '/Users/li/Downloads/temp/yolo/003.MP4'
    cap = cv2.VideoCapture(video_path)

    # Get ROI coordinates from the video
    roi_coordinates = get_roi_coordinates(video_path)
    if not roi_coordinates:
        print("No ROI selected. Exiting.")
        return

    x1, y1, w, h = roi_coordinates
    x2, y2 = x1 + w, y1 + h

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('/Users/li/Downloads/temp/yolo/output.mp4', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

    # Loop through the video frames
    while cap.isOpened():
        # Read a frame from the video
        success, frame = cap.read()

        if success:
            # Crop the frame to the region of interest (ROI)
            roi_frame = frame[y1:y2, x1:x2]

            # Run YOLO inference on the ROI frame
            results = model(roi_frame)

            # Visualize the results on the ROI frame
            annotated_roi_frame = results[0].plot()

            # Replace the original ROI in the frame with the annotated ROI
            frame[y1:y2, x1:x2] = annotated_roi_frame

            # Write the frame to the output video file
            out.write(frame)

            # Display the annotated frame
            # cv2.imshow("YOLO Inference", frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            # Break the loop if the end of the video is reached
            break

    # Release the video capture and writer objects, and close the display window
    cap.release()
    out.release()
    cv2.destroyAllWindows()


# Function to get ROI coordinates from a video frame
def get_roi_coordinates(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return None

    success, frame = cap.read()

    if not success:
        print("Error: Could not read frame from video.")
        return None

    roi = cv2.selectROI("Select ROI", frame, fromCenter=False, showCrosshair=True)
    cv2.destroyAllWindows()

    print(roi)
    return roi

if __name__ == '__main__':
    # lab001()
    # lab002()
    # lab003()
    # lab004()
    lab005()
    # get_roi_coordinates("/Users/li/Downloads/temp/yolo/VIDEO_1719275734042.MP4")

    pass