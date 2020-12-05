array:
	mkdir -p images
	python makearray.py
images: array
	python makeimage.py
%.webm: images
	ffmpeg -r 15 -i images/mbsNp%03d.png $@
clean:
	rm images/*
