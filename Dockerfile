# Step 1: Specify a minimal, official Python environment 
FROM python:3.11-slim 
 
# Step 2: Establish the working directory within the container 
WORKDIR /app 
 
# Step 3: Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Transfer the algorithm script into the container
COPY generate_data.py . 
 
# Step 5: Define the default execution command
CMD ["python", "generate_data.py"] 
 