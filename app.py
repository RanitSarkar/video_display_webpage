from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Define the videos directory where uploaded videos will be stored
app.config['VIDEOS_DIR'] = os.path.join(app.root_path, 'static/videos')

# Define a route to display the video player and a list of videos
@app.route('/')
def index():
    videos = os.listdir(app.config['VIDEOS_DIR'])
    return render_template('index.html', videos=videos)

# Define a route to add a video
@app.route('/add_video', methods=['GET', 'POST'])
def add_video():
    if request.method == 'POST':
        # Get the title and video file from the form
        title = request.form['title']
        video_file = request.files['video']

        # Save the video file to the videos directory
        filename = video_file.filename
        video_file.save(os.path.join(app.config['VIDEOS_DIR'], filename))

        # Redirect to the home page
        return redirect(url_for('index'))

    # Render the add_video template for GET requests
    return render_template('add_video.html')

if __name__ == '__main__':
    app.run(debug=True)