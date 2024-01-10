from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib import messages
from .models import ShortTermCourse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST


# Create your views here.

def view_courses(request):
    user = request.user
    if user.is_authenticated:
        try:
            all_courses = ShortTermCourse.objects.get(user = user)


            
            courses_per_page = 10 

            paginator = Paginator(all_courses, courses_per_page)
            page = request.GET.get('page')

            try:
                courses = paginator.page(page)
            except PageNotAnInteger:
            
                courses = paginator.page(1)
            except EmptyPage:
                
                courses = paginator.page(paginator.num_pages)

            context = {
                'courses': courses,
            }
            return render(request, 'dashboard/short-term-course.html', context)
        except ShortTermCourse.DoesNotExist:
            print("no data present")
    else:
        return redirect('handle_login')




from django.shortcuts import render, redirect
from .models import ShortTermCourse

def create_courses(request):
    user = request.user
    if request.method == "POST":
        
        image = request.FILES.get("image", None)

        
        title = request.POST.get('title')
        subtitle = request.POST.get('subtitle')
        amount = request.POST.get('amount')
        amount_text = request.POST.get('amount_text')
        status = request.POST.get('status')

        if not title:
            
            return render(request, 'dashboard/short-term-course-create.html', {'error_message': 'Title is required.'})
        if not amount:
            
            return render(request, 'dashboard/short-term-course-create.html', {'error_message': ' Amount is required.'})

        
        course = ShortTermCourse.objects.create(
            user = user, 
            title=title,
            subtitle=subtitle,
            amount=amount,
            amount_text=amount_text,
            status=status,
            images=image,
        )

        
        return redirect(view_courses) 

    return render(request, 'dashboard/short-term-course-create.html')






def delete_course(request, item_id):
    print("delete function calling >>>>>>>>>>>>>>>>>>")

    user = request.user
    if user.is_authenticated:
        try:
            course = ShortTermCourse.objects.get(id=item_id, user = user)
            course.delete()
            
            messages.success(request, 'Item deleted successfully!!')
            return redirect(view_courses)

        except ShortTermCourse.DoesNotExist:
            messages.error(request, 'Course does not exist.')
            return redirect(view_courses)

    else:
        return redirect('handle_login')
    

def edit_course(request, item_id):
    user =  request.user
    if user.is_authenticated :
        if request.method == "POST" : 
            image = request.FILES.get("image", None)

            
            title = request.POST.get('title')
            subtitle = request.POST.get('subtitle')
            amount = request.POST.get('amount')
            amount_text = request.POST.get('amount_text')
            status = request.POST.get('status')

            if title == "" or amount == '':
                    messages.error(request, "title and amount should not to be None")
                    return redirect(edit_course)
            try:
                course = ShortTermCourse.objects.filter(id=item_id).update(
                    title=title,
                    subtitle=subtitle,
                    amount=amount,
                    amount_text=amount_text,
                    status=status,
                    images=image,
                )
                messages.success(request, f'{title} updated successfully!')
                return redirect(view_courses)

            except ShortTermCourse.DoesNotExist:
                messages.error(request, "item not present in the list")
        try:
            course = ShortTermCourse.objects.get(id = item_id)
            print("data get")
            print("data get")
            print(course)
            print(course)
            context = {
                'course' : course
            }
            return render(request, 'dashboard/edit-course.html', context)
        except:
            messages.error(request, 'data not present in the list')
            return redirect(view_courses)
        

def update_status(reqeust, item_id):
    user = reqeust.user
