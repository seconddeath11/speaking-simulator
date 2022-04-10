def set_info(num, name=""):
    return {
        1: "Imagine that you are preparing a project with your friend. You have found some interesting material for the presentation and you want to read this text to your friend. You have 1.5 minutes to read the text silently, then be ready to read it out aloud. You will not have more than 1.5 minutes to read it.",
        2: "Study the advertisement.",
        3: "You are going to give an interview. You have to answer five questions. Give full answers to the questions (2–3 sentences). Remember that you have 40 seconds to answer each question.",
        4: "Imagine that you are doing a project " + name + " together with your friend. You have found some illustrations and want to share the news. Leave a voice message to your friend. In 2.5 minutes be ready to tell the friend about the photos:"
    }.get(num, 1)


def set_outro(num):
    return {
        1: "",
        2: "You have 20 seconds to ask each question.",
        3: "",
        4: "You will speak for not more than 3 minutes (2–3 sentences for every item of the plan, 12–15 sentences total). You have to talk continuously."
    }.get(num, 1)


class Task(object):
    def __init__(self, num, prep_time, answer_time, text="", audio="", picture1="", picture2="", project_name=""):
        self.num = num
        self.prep_time = prep_time
        self.answer_time = answer_time
        self.info = set_info(num, project_name)
        self.text = text
        self.outro = set_outro(num)
        self.audio = audio
        self.picture1 = picture1
        self.picture2 = picture2
