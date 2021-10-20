FROM python:3.6.1-alpine
WORKDIR /cocktail-recipe
ADD . /cocktail-recipe
COPY . .
RUN pip install -r requirements.txt
CMD ["python","app.py"]