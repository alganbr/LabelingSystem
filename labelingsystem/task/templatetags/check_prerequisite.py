from django import template
register = template.Library()

from response.models import QuizResponse

@register.simple_tag
def check_prerequisite(task, coder):
	# test if the prerequisite has been satisfied by the coder
	if QuizResponse.objects.filter(quiz=task.prerequisite, responder=coder, score__gte=task.prerequisite.pass_mark):
		return True
	return False