corpus:
	./corpi/combine_all.sh
models:
	python3 generate_models.py
sentences:
	python3 main.py 20
