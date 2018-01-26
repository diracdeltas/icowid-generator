corpus:
	./corpi/combine_all.sh
models:
	python3 generate_models.py
tweets:
	python3 main.py 10
