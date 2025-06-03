from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import CustomUser

def connection(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Corrigé: était 'email'
        password = request.POST.get('pwd')       # Corrigé: était 'password'
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Connexion réussie.")
            return redirect('image_recognize:index') 
        else:
            messages.error(request, "Identifiants invalides.")
            return render(request, 'connection.html', {'error': True})
    
    return render(request, 'connection.html')

def inscription(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')  # Corrigé: le champ email existe maintenant
        tel = request.POST.get('tel', '')
        password = request.POST.get('pwd')
        confirm_password = request.POST.get('confirm_pwd')  # Nouveau champ

        # Validation des champs
        if not username or not email or not password:
            messages.error(request, "Tous les champs obligatoires doivent être remplis.")
            return render(request, 'register.html', {'error': True})

        # Vérification de la confirmation du mot de passe
        if confirm_password and password != confirm_password:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return render(request, 'register.html', {'error': True})

        # Vérification si l'utilisateur existe déjà
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Cet email est déjà utilisé.")
            return render(request, 'register.html', {'error': True})
        
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Ce nom d'utilisateur est déjà utilisé.")
            return render(request, 'register.html', {'error': True})

        # Création de l'utilisateur
        try:
            user = CustomUser.objects.create_user(
                username=username,
                email=email,
                tel=tel,
                password=password
            )
            messages.success(request, "Compte créé avec succès. Vous pouvez maintenant vous connecter.")
            return redirect('connections:connection')
        except Exception as e:
            messages.error(request, "Erreur lors de la création du compte.")
            return render(request, 'register.html', {'error': True})

    return render(request, 'register.html')

def deconnection(request):
    logout(request)
    messages.success(request, "Vous avez été déconnecté avec succès.")
    return redirect('connection')