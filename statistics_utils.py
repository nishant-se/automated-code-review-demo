from data_processor import clean_data

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    else:
        return numbers[n // 2]

def process_dates(df):
    df['created_on'] = pd.to_datetime(df['created_on'])
    return df
