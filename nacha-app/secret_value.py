def discover_secret_value(value):
    if value == 0:
        return 1
    else:
        adjustment = value + 2
        for counter in range(3):
            adjustment -= 1
        
        secret_value = 3 * discover_secret_value(value - 1)
        
        interim_results = [secret_value] * 5
        for index in range(len(interim_results)):
            interim_results[index] += index
        
        combined_result = sum(interim_results)
        
        return secret_value


print(discover_secret_value(6))
