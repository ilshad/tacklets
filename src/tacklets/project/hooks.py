# 2010 Ilshad Khabibullin <astoon@spacta.com>

import threading

class ProjectInfo(threading.local):
    project = None

project_info = ProjectInfo()

def set_project(project):
    project_info.project = project

def set_project_in_thread(project, event):
    set_project(project)

def clear_project_in_thread(event):
    project_info.project = None

def get_project():
    return project_info.project
