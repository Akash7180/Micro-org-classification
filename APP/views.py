from django.shortcuts import render, redirect
from . models import UserPredictModel
from . forms import UserPredictForm, UserRegisterForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
import numpy as np

from tensorflow import keras
from PIL import Image, ImageOps
from . import forms



def Landing_1(request):
    return render(request, '1_Landing.html')

def Register_2(request):
    form = UserRegisterForm()
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created. ' + user)
            return redirect('Login_3')

    context = {'form':form}
    return render(request, '2_Register.html', context)


def Login_3(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Home_4')
        else:
            messages.info(request, 'Username OR Password incorrect')

    context = {}
    return render(request,'3_Login.html', context)

def Home_4(request):
    return render(request, '4_Home.html')

def Teamates_5(request):
    return render(request,'5_Teamates.html')

def Domain_Result_6(request):
    return render(request,'6_Domain_Result.html')

def Problem_Statement_7(request):
    return render(request,'7_Problem_Statement.html')
    
def Deploy_8(request): 
    print("HI")
    if request.method == "POST":
        form = forms.UserPredictForm(files=request.FILES)
        if form.is_valid():
            print('HIFORM')
            form.save()
        obj = form.instance

        result1 = UserPredictModel.objects.latest('id')
        models = keras.models.load_model('C:/Users/raghu/Downloads/ITPDL20-FINAL CODING NEW/ITPDL20-FINAL CODING/Deploy/PROJECT/APP/keras_model.h5')
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        image = Image.open("C:/Users/raghu/Downloads/ITPDL20-FINAL CODING NEW/ITPDL20-FINAL CODING/Deploy/PROJECT/media/" + str(result1)).convert("RGB")
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        data[0] = normalized_image_array
        classes = ['Amoeba','Euglena','Hydra','Paramecium','Rod_bacteria','Spherical_bacteria','Spiral_bacteria','Yeast']
        prediction = models.predict(data)
        idd = np.argmax(prediction)
        a = (classes[idd])
        print("This is the class name", a)
        confidence_score = prediction[0][idd]
        print(confidence_score)
        threshold = 0.98  
        if confidence_score >= threshold:
            predicted_class = classes[idd]
            print("This is predicted class", predicted_class)
            if predicted_class == 'Amoeba':
                a = 'FOUND THIS IMAGE IS AMOEBA'
                b = 'Amoeba is a unicellular organism that has the ability to change its shape. They are usually found in water bodies such as ponds, lakes and slow-moving rivers. Sometimes, these unicellular organisms can also make their way inside the human body and cause various illnesses.Human Health: While most amoebas are harmless to humans, some species can cause diseases. For example, the genus Entamoeba includes species like Entamoeba histolytica, which can cause amoebic dysentery, a severe gastrointestinal infection'
            elif predicted_class == 'Euglena':
                a = 'FOUND THIS IMAGE IS Euglena'
                b = 'Euglenoids are unicellular microorganisms, that have a flexible body. They possess the characteristic features of plants and animals. Euglena has plastids and performs photosynthesis in light, but moves around in search of food using its flagellum at night. There are around 1000 species of Euglena found'
            elif predicted_class == 'Hydra':
                a = 'FOUND THIS IMAGE IS Hydra'
                b = 'Hydra, genus of invertebrate freshwater animals of the class Hydrozoa (phylum Cnidaria).'
            elif predicted_class == 'Paramecium':
                a = 'FOUND THIS IMAGE IS Paramecium'
                b = 'Paramecium are widespread in freshwater, brackish, and marine environments and are often abundant in stagnant basins and ponds. Because some species are readily cultivated and easily induced to conjugate and divide, they have been widely used in classrooms and laboratories to study biological processes.'
            elif predicted_class == 'Rod_bacteria':
                a = 'FOUND THIS IMAGE IS Rod bacteria'
                b = 'Rod-shaped bacteria are termed bacilli. These bacilliform bacteria are found in several taxonomic groups of bacteria. The term Bacillus (genus) includes rod-shaped gram-positive bacteria. Bacilli also comprise several other such genera.'
            elif predicted_class == 'Spherical_bacteria':
                a = 'FOUND THIS IMAGE IS Spherical bacteria'
                b = ''
            elif predicted_class == 'Spiral_bacteria':
                a = 'FOUND THIS IMAGE IS Spiral bacteria'
                b = 'spirillum) shapes are curved-shaped bacteria which can range from a gently curved shape to a corkscrew spiral. Many spirilla are rigid and able to move. The length of rod-shaped bacteria is over 2–100 μm. Spiral-shaped bacteria occur in one of three forms: vibrio, spirillum, and spirochete '
            elif predicted_class == 'Yeast':
                a = 'FOUND THIS IMAGE IS Yeast'
                b = 'Yeasts are eukaryotic, single-celled microorganisms classified as members of the fungus kingdom. The first yeast originated hundreds of millions of years ago, and at least 1,500 species are currently recognized. They are estimated to constitute 1 percentage of all described fungal species.'
            else:
                a = 'WRONG INPUT'
                b = 'WRONG INPUT'

            data = UserPredictModel.objects.latest('id')
            data.label = a
            data.save()

            
            return render(request, '8_Deploy.html',{'form':form,'obj':obj,'predict':a, 'output': b})
        else:
            predicted_class = 'Unknown'
            print("Unknown image class predicted!")
            data = UserPredictModel.objects.latest('id')
            data.label = a
            data.save()
            return render(request, '8_Deploy.html',{'form':form,'obj':obj,'predict':predicted_class})
    else:
        form = forms.UserPredictForm()
    return render(request, '8_Deploy.html',{'form':form})


def Out_Database_9(request):
    models = UserPredictModel.objects.all()
    return render(request, '9_Out_Database.html', {'models':models})

def Logout(request):
    logout(request)
    return redirect('Landing_1')
