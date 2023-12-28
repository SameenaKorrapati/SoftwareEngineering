def predict_weather(temp, humidity, windspeed):
    weather = 0.5 * (temp ** 2) - 0.2 * humidity + 0.1 * windspeed - 15
    if weather > 300:
        return "Weather is Sunny"
    elif 200 < weather <= 300:
        return "Weather is Cloudy"
    elif 100 < weather <= 200:
        return "Weather is Rainy"
    else:
        return "Weather is Stormy"

inputs = []
n = int(input("Enter the number of values: "))
for i in range(n):
    temp, humidity, windspeed = map(int, input("Enter temperature, humidity and windspeed: ").split())
    inputs.append([temp, humidity, windspeed])
for each in inputs:
    temp, humidity, windspeed = each
    print(predict_weather(temp, humidity, windspeed))