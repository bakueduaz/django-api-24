from django.http import JsonResponse, HttpResponseForbidden
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

class News:
    def __init__(self, tit, des, img):
        self.tit = tit
        self.des = des
        self.img = img

# Create news objects
news1 = News("Iphone 14 Pro",
             "iPhone 14 Pro and iPhone 14 Pro Max are splash, water, and dust resistant and were tested under controlled laboratory conditions with a rating of IP68 under IEC standard 60529(maximum depth of 6 meters up to 30 minutes.",
             "https://picsum.photos/1000")
news2 = News("New iPadOS 17",
             "iPadOS 17 takes iPad even further. With new levels of personalization, beautiful and helpful custom Lock Screens, and features to help you get more done, iPad is more capable than ever.",
             "https://picsum.photos/1000")
news3 = News("New General AI",
             "The ultimate achievement to some in the AI industry is creating a system with artificial general intelligence (AGI), or the ability to understand and learn any task that a human can.",
             "https://picsum.photos/1000")
news4 = News("Samsung S22 Ultra",
             "The iconic S Pen fits right into S for the first time. Eject it from the bottom to take notes, sketch, edit content with precision or control your phone.",
             "https://picsum.photos/1000")
news5 = News("Redmi Note 12 Pro 5G",
             "Powerful AI algorithms greatly improve image quality and speed. Every priceless moment in your life comes to life, waiting for you to seize.",
             "https://picsum.photos/1000")
news6 = News("iPhone 12 Pro Max",
             "The iPhone 12 Pro Max display has rounded corners that follow a beautiful curved design, and these corners are within a standard rectangle. When measured as a standard rectangular shape, the screen is 6.68 inches diagonally (actual viewable area is less).",
             "https://picsum.photos/1000")
news7 = News("Iphone 14 Pro",
             "iPhone 14 Pro and iPhone 14 Pro Max are splash, water, and dust resistant and were tested under controlled laboratory conditions with a rating of IP68 under IEC standard 60529(maximum depth of 6 meters up to 30 minutes.",
             "https://picsum.photos/1000")
news8 = News("New iPadOS 17",
             "iPadOS 17 takes iPad even further. With new levels of personalization, beautiful and helpful custom Lock Screens, and features to help you get more done, iPad is more capable than ever.",
             "https://picsum.photos/1000")
news9 = News("New General AI",
             "The ultimate achievement to some in the AI industry is creating a system with artificial general intelligence (AGI), or the ability to understand and learn any task that a human can.",
             "https://picsum.photos/1000")
news10 = News("Samsung S22 Ultra",
             "The iconic S Pen fits right into S for the first time. Eject it from the bottom to take notes, sketch, edit content with precision or control your phone.",
             "https://picsum.photos/1000")
news11 = News("Redmi Note 12 Pro 5G",
             "Powerful AI algorithms greatly improve image quality and speed. Every priceless moment in your life comes to life, waiting for you to seize.",
             "https://picsum.photos/1000")
news12 = News("iPhone 12 Pro Max",
             "The iPhone 12 Pro Max display has rounded corners that follow a beautiful curved design, and these corners are within a standard rectangle. When measured as a standard rectangular shape, the screen is 6.68 inches diagonally (actual viewable area is less).",
             "https://picsum.photos/1000")
news13 = News("Iphone 14 Pro",
             "iPhone 14 Pro and iPhone 14 Pro Max are splash, water, and dust resistant and were tested under controlled laboratory conditions with a rating of IP68 under IEC standard 60529(maximum depth of 6 meters up to 30 minutes.",
             "https://picsum.photos/1000")
news14 = News("New iPadOS 17",
             "iPadOS 17 takes iPad even further. With new levels of personalization, beautiful and helpful custom Lock Screens, and features to help you get more done, iPad is more capable than ever.",
             "https://picsum.photos/1000")
news15 = News("New General AI",
             "The ultimate achievement to some in the AI industry is creating a system with artificial general intelligence (AGI), or the ability to understand and learn any task that a human can.",
             "https://picsum.photos/1000")
news16 = News("Samsung S22 Ultra",
             "The iconic S Pen fits right into S for the first time. Eject it from the bottom to take notes, sketch, edit content with precision or control your phone.",
             "https://picsum.photos/1000")
news17 = News("Redmi Note 12 Pro 5G",
             "Powerful AI algorithms greatly improve image quality and speed. Every priceless moment in your life comes to life, waiting for you to seize.",
             "https://picsum.photos/1000")
news18 = News("iPhone 12 Pro Max",
             "The iPhone 12 Pro Max display has rounded corners that follow a beautiful curved design, and these corners are within a standard rectangle. When measured as a standard rectangular shape, the screen is 6.68 inches diagonally (actual viewable area is less).",
             "https://picsum.photos/1000")
news19 = News("Iphone 14 Pro",
             "iPhone 14 Pro and iPhone 14 Pro Max are splash, water, and dust resistant and were tested under controlled laboratory conditions with a rating of IP68 under IEC standard 60529(maximum depth of 6 meters up to 30 minutes.",
             "https://picsum.photos/1000")
news20 = News("New iPadOS 17",
             "iPadOS 17 takes iPad even further. With new levels of personalization, beautiful and helpful custom Lock Screens, and features to help you get more done, iPad is more capable than ever.",
             "https://picsum.photos/1000")
news21 = News("New General AI",
             "The ultimate achievement to some in the AI industry is creating a system with artificial general intelligence (AGI), or the ability to understand and learn any task that a human can.",
             "https://picsum.photos/1000")
news22 = News("Samsung S22 Ultra",
             "The iconic S Pen fits right into S for the first time. Eject it from the bottom to take notes, sketch, edit content with precision or control your phone.",
             "https://picsum.photos/1000")
news23 = News("Redmi Note 12 Pro 5G",
             "Powerful AI algorithms greatly improve image quality and speed. Every priceless moment in your life comes to life, waiting for you to seize.",
             "https://picsum.photos/1000")
news24 = News("iPhone 12 Pro Max",
             "The iPhone 12 Pro Max display has rounded corners that follow a beautiful curved design, and these corners are within a standard rectangle. When measured as a standard rectangular shape, the screen is 6.68 inches diagonally (actual viewable area is less).",
             "https://picsum.photos/1000")

# Store news objects in a list
news_list = [news1, news2, news3, news4, news5, news6, news7, news8, news9, news10, news11, news12, news13, news14, news15, news16, news17, news18, news19, news20, news21, news22, news23, news24]

@method_decorator(csrf_exempt, name='dispatch')
class NewsView(View):
    def get(self, request):
        # Check for the API key
        api_key = request.GET.get('api_key')
        if api_key != settings.API_KEY:
            return HttpResponseForbidden("Invalid API key")

        # Prepare the news data
        news_data = [{'tit': news.tit, 'des': news.des, 'img': news.img} for news in news_list]
        
        # Return the response
        return JsonResponse({'news': news_data})
