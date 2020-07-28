# Object Detection and Tracking with OpenCV and Python
In this repo, I created an object detector and tracker for both image and video captures. 

## How to Detect Objects in Images?
First, run the <code>detect.py</code> file on your terminal and pass the desired image path to the --image argument. Like this:
<pre>
<code>
  python3 detect.py --image <your-image-file-path-with-extension>
</code>
</pre> 

Then, use the provided trackbars to manipulate the H, S, and V parameters that match the object color and it gets tracked.

**Image Example** 
<img src='img-ex.png' width=800 height=600>


## How to Detect Objects in Videos?
That's even simpler. Run the <code>tracking.py</code> file. Your default webcam will be automatically opened and just like the above example, adjust HSV to detect any object around you.

**Video Example**
<img src='vid-ex.png' width=800 height=600>
