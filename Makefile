

build:
	docker build -t ocr-api .


run:
	docker run -d --name ocr-container -p 8080:8080 ocr-api


stop:
	docker stop ocr-container


clean:
	docker rm ocr-container
	docker rmi ocr-api