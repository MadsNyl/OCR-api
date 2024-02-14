

build:
	docker build -t ocr-api .


run:
	docker run -d --name ocr -p 8001:8001 ocr-api


stop:
	docker stop ocr


clean:
	docker rm ocr
	docker rmi ocr-api