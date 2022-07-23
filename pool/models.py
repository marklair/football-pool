from django.conf import settings
from django.db import models
from django.utils import timezone


class Season(models.Model):
	year = models.IntegerField()


class Week(models.Model):
	season_id = models.ForeignKey(Season, on_delete=models.CASCADE)
	winner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	is_post_season = models.BooleanField(default=False)
	week_start = models.DateField(auto_now=False, auto_now_add=False)
	week_end = models.DateField(auto_now=False, auto_now_add=False)
	value = models.DecimalField(max_digits=5, decimal_places=2)


class Team(models.Model):
	location = models.CharField(max_length=200)
	mascot = models.CharField(max_length=200)
	logo = models.CharField(max_length=200)


class Game(models.Model):
	week_id = models.ForeignKey(Week, on_delete=models.CASCADE)
	home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team')
	away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_team')
	kickoff_time = models.DateTimeField(blank=True, null=True)
	home_team_score = models.IntegerField()
	away_team_score = models.IntegerField()
	winning_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='winning_team')
	is_monday_night = models.BooleanField(default=False)
	is_playoff = models.BooleanField(default=False)
	is_superbowl = models.BooleanField(default=False)


class Pick(models.Model):
    player = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
#    published_date = models.DateTimeField(blank=True, null=True)
    total_points = models.IntegerField()

    def submit(self):
#        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.team_id