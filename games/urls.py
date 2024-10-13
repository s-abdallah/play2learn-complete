from django.urls import path

from games.views import (
    MathFactsView,
    AnagramHuntView,
    start_game,
    update_game,
    end_game,
    LeaderboardView,
)

app_name = "games"
urlpatterns = [
    path("math-facts/", MathFactsView.as_view(), name="math-facts"),
    path("anagram-hunt/", AnagramHuntView.as_view(), name="anagram-hunt"),
    path("leaderboard/", LeaderboardView.as_view(), name="leaderboard"),
    path("start/", start_game, name="ajax-start-game"),
    path("update/", update_game, name="ajax-update-game"),
    path("end/", end_game, name="ajax-end-game"),
]
