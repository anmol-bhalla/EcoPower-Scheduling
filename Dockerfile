FROM python:3-alpine

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt
EXPOSE 9000
ENV DATABASE_URL='postgresql://bqafdzmwdkhjrn:07623061f89a9b916aae8121938773b6e6020aae7688a93c875f301960aeb4bd@ec2-34-202-53-101.compute-1.amazonaws.com:5432/df70jf2v65kau1'
ENTRYPOINT ["python3", "app.py"]