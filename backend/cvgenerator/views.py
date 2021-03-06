from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader


class CVGenerator(APIView):
    def post(self, request):
        name = request.data.get("name", "")
        email = request.data.get("email", "")
        phone = request.data.get("phone", "")
        summary = request.data.get("summary", "")
        degree = request.data.get("degree", "")
        school = request.data.get("school", "")
        university = request.data.get("university", "")
        previous_work = request.data.get("previous_work", "")
        skills = request.data.get("skills", "")

        profile = Profile(name=name, email=email, phone=phone, summary=summary, degree=degree, school=school,
                          university=university, previous_work=previous_work, skills=skills)

        template = loader.get_template('pdf/resume.html')

        html = template.render({"profile": profile})
        options = {
            'page-size': 'Letter',
            'encoding': "UTF-8",
        }

        # use these commands to download
        # cd ~
        # wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.3/wkhtmltox-0.12.3_linux-generic-amd64.tar.xz
        # tar vxf wkhtmltox-0.12.3_linux-generic-amd64.tar.xz
        # cp wkhtmltox/bin/wk* /usr/local/bin/

        pdf = pdfkit.from_string(html, 'resume.pdf', options)

        response = Response(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment'
        profile.save()

        return response


# def resume(request, id):
#     user_profile = Profile.objects.get(pk=id)
#     template = loader.get_template('pdf/resume.html')
#     html = template.render({'user_profile': user_profile})
#     options = {
#         'page-size': 'Letter',
#         'encoding': "UTF-8",
#     }
#     pdf = pdfkit.from_string(html, False, options)
#     response = HttpResponse(pdf, content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment'
#     filename = "resume.pdf"
#     return response
#
#

class ProfileList(APIView):
    def list(self, request):
        profiles = Profile.objects.all()
        return render(request, 'pdf/list.html', {'profiles': profiles})
