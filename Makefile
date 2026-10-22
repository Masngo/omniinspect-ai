.PHONY: install run test docker-build

install:
	pip install -r requirements.txt

run:
	streamlit run web_demo/app.py

test:
	pytest tests/

docker-build:
	docker build -f deploy/docker/Dockerfile.graviton -t omniinspect-graviton .
