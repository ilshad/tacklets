from zope.browserpage import ViewPageTemplateFile

class ManageDocumentTopics:

    template = ViewPageTemplateFile("topics.pt")

    def __call__(self):
        if self.request.get("submit"):
            topics = self.request.get("topics")
            if topics:
                topics = [x.strip() for x in topics.split(",")]
                self.context.update_topics(topics)
                self.request.response.redirect(".")
        self.titles = ", ".join([x.title for x
                                 in self.context.get_topics()])
        return self.template()
