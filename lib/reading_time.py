def read_time_estimate(text, wpm):
    if isinstance(text, str):
        result = text.split(" ")
        wpm = int(len(result)/wpm)
        response = f"This will take approx {wpm} minutes to read"
        return response
    else: 
        return "You have not entered any text"