# coding: utf-8
# 2010 Ilshad Khabibullin <astoon@spacta.com>

class View:

    def __call__(self):
        q = self.request.get("q")

        r = u"варианты\nвариации\nкоманда\nLinux\nсистемный"

        self.request.response.setHeader('Content-Type', 'text/plain')
        return r
