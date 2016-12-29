from moviepy.editor import *

video = VideoFileClip("We_Are_Number_One.mp4")

infile = raw_input("Give me some video file to replace every \"One\" with: ")

video2 = VideoFileClip(infile)

times = [(39.2, 39.8), (45.2, 45.7), (56.9, 57.5), ((1, 17.9), (1, 18.3)),
         ((1, 23.7), (1, 24.3)), ((1, 31.1), (1, 31.7)), ((2, 12.6), (2, 13.2)),
         ((2, 19.3), (2, 20.1)), ((2, 36.3), (2, 36.8)), ((2, 42.3), (2, 42.8)),
         ((2, 43.8), (2, 44.3)), ((2, 45.3), (2, 45.8))]

videoparts = []

oldt = 0
for t0, t1 in times:
    videoparts.append(video.subclip(oldt, t0))
    videoparts.append(video2)
    oldt = t1
videoparts.append(video.subclip(oldt))

result = concatenate_videoclips(videoparts)

result.write_videofile("output.mp4",fps=23) # Many options...
