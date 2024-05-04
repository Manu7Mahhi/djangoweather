from django.shortcuts import render

def home(request):
	import json
	import requests

	if request.method=="POST":
		zipcode=request.POST["zipcode"]
		api_request=requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=BF5B4369-94E9-46A8-A824-FAF1E744B629")
		
		try:
			api=json.loads(api_request.content)
		except Exception as e:
			api="Error..."

		if api[0]['Category']['Name'] =="Good":
		  	category_description="(0-50) Air quality is considered satisfactory, and air pollution poses little or no risk"
		  	category_color="good"

		elif api[0]['Category']['Name'] =="Moderate":
		  	category_description="(51-100) Air quality is acceptable;however,for some pollutants there may be a moderate health conceern for a very small number of people who are usually sensitive to air pollution"
		  	category_color="moderate"

		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
		  	category_description="(101-150) Altough general public is not likelt to be affected at this AQI range, people with lung dieaases,older adults and children are at a greater risk from exposure to ozone, where as persons with heart and lung dieases, older adults and children are at agreater risk from the presence of particles in the air."
		  	category_color="unhealthy for Sensitive Groups"

		elif api[0]['Category']['Name'] == "Unhealthy":
		  	category_description="(151-200)Everone may begin to experience health effects; number of sensitive groups may experience more serious health effects."
		  	category_color="Unhealthy"

		elif api[0]['Category']['Name'] == "Very Unhealthy":
		  	category_description="(201-300)Health alert: everyone may experience more serious health effects"
		  	category_color="verunhealthy"

		elif api[0]['Category']['Name'] == "Hazardous":
		  	category_description="(301-500)Health Warning of emergency conditions. The population is more likelyy to be affected"
		  	category_color="Hazardous"


		return render(request,'home.html',{'api':api,
			'category_description':category_description,
			'category_color':category_color
			})

	else:
		api_request=requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=BF5B4369-94E9-46A8-A824-FAF1E744B629")
		
		try:
			api=json.loads(api_request.content)

		except Exception as e:
			api="Error..."

		if api[0]['Category']['Name'] == "Good":
		  	category_description="(0-50) Air quality is considered satisfactory, and air pollution poses little or no risk"
		  	category_color="good"

		elif api[0]['Category']['Name'] == "Moderate":
		  	category_description="(51-100) Air quality is acceptable;however,for some pollutants there may be a moderate health conceern for a very small number of people who are usually sensitive to air pollution"
		  	category_color="moderate"

		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
		  	category_description="(101-150) Altough general public is not likelt to be affected at this AQI range, people with lung dieaases,older adults and children are at a greater risk from exposure to ozone, where as persons with heart and lung dieases, older adults and children are at agreater risk from the presence of particles in the air."
		  	category_color="unhealthy for Sensitive Groups"

		elif api[0]['Category']['Name'] == "Unhealthy":
		  	category_description="(151-200)Everone may begin to experience health effects; number of sensitive groups may experience more serious health effects."
		  	category_color="Unhealthy"

		elif api[0]['Category']['Name'] == "Very Unhealthy":
		  	category_description="(201-300)Health alert: everyone may experience more serious health effects"
		  	category_color="verunhealthy"

		elif api[0]['Category']['Name'] == "Hazardous":
		  	category_description="(301-500)Health Warning of emergency conditions. The population is more likelyy to be affected"
		  	category_color="Hazardous"


		return render(request,'home.html',{'api':api,
			'category_description':category_description,
			'category_color':category_color
			})


def about(request):
	return render(request,'about.html',{})