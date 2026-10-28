.PHONY: test demo refresh report charts dashboard docker
test:
	python -m unittest discover -s tests -v
demo:
	python -m src.pipeline.run --demo
refresh:
	python -m scripts.refresh --demo
report:
	python -m scripts.build_report
charts:
	python -m src.analytics.charts
dashboard:
	streamlit run dashboard/app.py
docker:
	docker compose up --build -d
