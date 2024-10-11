from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from .models import GameTracking
import json

# Create your views here.
from django.views.generic import TemplateView


class MathFactsView(TemplateView):
    template_name = "math-facts.html"


class AnagramHuntView(TemplateView):
    template_name = "anagram-hunt.html"


# View to start the game
@csrf_exempt
def start_game(request):
    if request.method == "POST":
        user = request.user  # The logged-in user (or AnonymousUser).
        data = json.loads(request.body)  # Data from JavaScript.

        game_type = data.get("game_type")
        game_settings = data.get("game_settings")

        # Create a new GameTracking object
        game_tracking = GameTracking.objects.create(
            user=request.user,
            game_type=game_type,
            game_settings=game_settings,
            start_time=timezone.now(),
        )

        return JsonResponse({"status": "started", "game_id": game_tracking.id})


# View to update the game
@csrf_exempt
def update_game(request):
    if request.method == "POST":
        data = json.loads(request.body)  # Data from JavaScript.
        tries = data.get("tries")
        game_id = data.get("gameId")

        try:
            game_tracking = GameTracking.objects.get(id=game_id, user=request.user)
            game_tracking.tries = tries
            game_tracking.end_time = timezone.now()
            game_tracking.save()
            return JsonResponse({"status": "updated", "game_id": game_tracking.id})
        except GameTracking.DoesNotExist:
            return JsonResponse(
                {"status": "error", "message": "Game not found"}, status=404
            )


# View to end the game
@csrf_exempt
def end_game(request):
    if request.method == "POST":
        data = json.loads(request.body)
        score = data.get("score")
        game_id = data.get("gameId")

        try:
            game_tracking = GameTracking.objects.get(id=game_id, user=request.user)
            game_tracking.score = score
            game_tracking.end_time = timezone.now()
            game_tracking.save()
            return JsonResponse(
                {
                    "status": "ended",
                    "game_id": game_tracking.id,
                    "score": game_tracking.score,
                }
            )
        except GameTracking.DoesNotExist:
            return JsonResponse(
                {"status": "error", "message": "Game not found"}, status=404
            )
