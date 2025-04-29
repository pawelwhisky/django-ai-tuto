from django.shortcuts import render
import joblib

# Load the trained model
model = joblib.load('model.pkl')

def predict(request):
    prediction = None
    if request.method == 'POST':
        input_value = float(request.POST.get('input_value'))
        prediction = model.predict([[input_value]])[0]
    return render(request, 'predict.html', {'prediction': prediction})
