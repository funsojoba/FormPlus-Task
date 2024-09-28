

def get_form_responses_count(form_id):
    count = mongo.db.responses.count_documents({"form_id": form_id})
    return count