from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Quiz, Question, Choice, Attempt
from .forms import QuizForm

# @login_required
def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz_list.html', {'quizzes': quizzes})

# @login_required
def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()

    if request.method == 'POST':
        form = QuizForm(request.POST, questions=questions)
        if form.is_valid():
            score = 0
            for question in questions:
                selected_choice_id = form.cleaned_data[f'question_{question.id}']
                choice = Choice.objects.get(id=selected_choice_id)
                if choice.is_correct:
                    score += 1
            attempt = Attempt.objects.create(user=request.user, quiz=quiz, score=score)
            return redirect('quiz_result', attempt_id=attempt.id)
    else:
        form = QuizForm(questions=questions)

    return render(request, 'take_quiz.html', {'quiz': quiz, 'form': form})

# @login_required
def quiz_result(request, attempt_id):
    attempt = get_object_or_404(Attempt, id=attempt_id, user=request.user)
    return render(request, 'quiz_result.html', {'attempt': attempt})
