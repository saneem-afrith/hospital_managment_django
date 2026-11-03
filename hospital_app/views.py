from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
# Create your views here.
class GoodMorningView(View):
    def get(self, request):
        data = {"message": "Welcome to Viyoor Hospital!"}
        return JsonResponse(data)

class HospitalView(View):
    def get(self, request):
        data = {
            'Hospital': 'viyoor Hospital',
            'Contact': '9838492093',
            'Owner': 'Dr. Suresh',
            'Location': 'Thiruvananthapuram',
            'Status': 'Open',
        }
        return JsonResponse(data)
class DoctorView(View):
    def get(self, request):
        data = {
            'Name': 'Dr. suresh',
            'Specialization': 'Cardiology',
            'Experience': 12,
            'Fees': 500,
            'Available_days': 'Mon - Fri',
        }
        return JsonResponse(data)
class PatientView(View):
    def get(self, request):
        data = {
            'Name': 'Arun',
            'Age': 35,
            'Gender': 'Male',
            'Blood_group': 'B+',
            'Location': 'Kollam',
            'Mobile': 9876543210,
            'Admitted_date': '10/10/2026',
        }
        return JsonResponse(data)
class DepartmentsView(View):
    def get(self, request):
        data = {
            'Departments': [
                'Cardiology',
                'Neurology',
                'Orthopedics',
                'Pediatrics',
                'Dermatology',
            ]
        }
        return JsonResponse(data)
class NurseView(View):
    def get(self, request):
        data = {
            'id': "",
            'name': "",
            'place': "",
            'shift': "",
            'contact': "",
            'experience': "",
            'qualification': "",
        }
        return JsonResponse(data)
