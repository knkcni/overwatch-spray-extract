run:
	docker run -v $PWD/extract_output:/usr/src/spray/extract_output knkcni/overwatch_spray_extract

launch:
	python sprayExtract.py