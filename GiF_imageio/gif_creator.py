import imageio
imageio.plugins.ffmpeg.download()
reader = imageio.get_reader('1.mp4')
fps = reader.get_meta_data(['fps'])
with imageio.get_writer('movie.gif') as writer:
    for file in reader:
        writer.append_data(file)

writer.close()
