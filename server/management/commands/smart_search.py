from rake_nltk import Rake
from server.models import Complaint
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'The Zen of Python'

    def handle(self, *args, **options):
        test = "болит голова, жар, повышенная температура, воспаленные гланды и першит горло"
        res = find_specialty(test, 'Терапевт', 'russian')
        return res


def count_references(references_list, key):
    references_counts = dict()
    if references_list:
        for keyword_references in references_list:
            for reference in keyword_references:
                specialty = reference[key]
                if reference[key] in references_counts:
                    references_counts[specialty] += 1
                else:
                    references_counts[specialty] = 1
    return references_counts


def find_specialty(complaint, default_specialty, language):
    rake = Rake(language=language)
    rake.extract_keywords_from_text(complaint)
    complaint_keywords = rake.get_ranked_phrases()
    references_list = [Complaint.objects.filter(name__icontains=keyword).values()
                       for keyword in complaint_keywords]
    references_counts = count_references(references_list, 'medic_specialty')
    result_specialty = max(references_counts, key=references_counts.get) \
        if references_counts else default_specialty

    print(references_list)
    print(complaint_keywords)

    return result_specialty
