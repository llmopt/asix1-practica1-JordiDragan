from transformers import AutoModelForCausalLM, AutoTokenizer
import re

# Load the model and token  izer from Hugging Face
model_name = "mistral-7b-instruct"  # Replace with an equivalent model if not available
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def parse_apache_logs(log_file):
    """
    Reads and processes Apache logs.
    """
    with open(log_file, 'r') as file:
        logs = file.readlines()

    # Example regex to process Apache logs
    log_pattern = r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<date>.*?)\] "(?P<request>.*?)" (?P<status>\d+) (?P<size>\d+|-)'
    parsed_logs = [re.match(log_pattern, log).groupdict() for log in logs if re.match(log_pattern, log)]
    return parsed_logs

def interpret_logs_with_model(parsed_logs):
    """
    Uses the model to interpret the processed logs.
    """
    interpretations = []
    for log in parsed_logs:
        input_text = f"Interpret this Apache log entry: {log}"
        inputs = tokenizer(input_text, return_tensors="pt")
        outputs = model.generate(**inputs, max_length=100)
        interpretation = tokenizer.decode(outputs[0], skip_special_tokens=True)
        interpretations.append(interpretation)
    return interpretations

if __name__ == "__main__":
    # Path to the Apache log file
    log_file = "apache_logs.txt"  # Replace with the correct path

    # Process and interpret the logs
    parsed_logs = parse_apache_logs(log_file)
    interpretations = interpret_logs_with_model(parsed_logs)

    # Display the results
    for log, interpretation in zip(parsed_logs, interpretations):
        print(f"Log: {log}")
        print(f"Interpretation: {interpretation}")
        print("-" * 50)