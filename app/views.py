from django.shortcuts import render
import math




def index(request):
    if request.method == 'POST':
        num1 = float(request.POST.get('num1', 0))
        num2 = float(request.POST.get('num2', 0))
        operation = request.POST.get('operation')

        if operation == 'add':
            result7 = num1 + num2, ("="), (num1), ("+"), (num2) 
        elif operation == 'subtract':
            result7 = num1 - num2, ("="), (num1), ("-"), (num2)
        elif operation == 'multiply':
            result7 = num1 * num2, ("="), (num1), ("x"), (num2)
        elif operation == 'divide':
            if num2 != 0:
                result7 = num1 / num2, ("="), (num1), ("/"), (num2)
            else:
                result7 = "Error: Division by zero"
        elif operation == 'sqrt':
            result7 = math.sqrt(num1), ("="), (num1), ("square root")
        elif operation == 'square':
            result7 = num1 ** 2, ("="), (num1), ("squared")
        elif operation == 'reciprocal':
            if num1 != 0:
                result7 = 1 / num1, ("="), (num1), ("reciprocal")
            else:
                result7 = "Error: Division by zero"
        elif operation == 'percentage':
            if num2 != 0:
                result7 = num1 / 100, ("="), (num1),  ("percent")
            else:
                result7 = "Error: Division by zero"
        else:
            result7 = "Invalid operation"

        modified_result7 = ' '.join(str(item) for item in result7)

        return render(request, 'index.html', {'result7': result7, 'result7': modified_result7, 'operation': operation})
    return render(request, 'index.html')
