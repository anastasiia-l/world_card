from rake_nltk import Rake
from server.models import Complaint, Medic
import math
from ast import literal_eval

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

def find_by_location(coordinates, medics):
    tuple_coord = literal_eval(coordinates)
    dirst = dict()
    for medic in medics:
        m_coord = literal_eval(medic["coordinates"])
        dirst[medic["medic_id"]] = math.fabs(tuple_coord[0]-m_coord[0]) + math.fabs(tuple_coord[1]-m_coord[1])
    return min(dirst, key=dirst.get)



