from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")

# views.py

# import joblib
import os
# Load model once (at module level)
# model_path = os.path.join(settings.BASE_DIR, 'model', 'model.pkl')
# model = joblib.load(model_path)
# # print("Model loaded successfully.")

# def predict_price(sqft, bedrooms, location):
#     input_data = [[sqft, bedrooms, location]]
#     return model.predict(input_data)[0]

def home(request):
    # if request.method == 'POST':
    #     sqft = float(request.POST.get('sqft'))
    #     bedrooms = int(request.POST.get('bedrooms'))
    #     location = int(request.POST.get('location'))

    #     price = predict_price(sqft, bedrooms, location)
    #     return HttpResponse(f'Predicted Price: ₹{round(price):,}')

    return render(request, 'home.html')

