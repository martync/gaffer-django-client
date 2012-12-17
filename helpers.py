from django.conf import settings
from django.http import Http404
import pyuv
from gaffer.httpclient import Server, GafferNotFound, ProcessId


def get_gaffer_server():
    loop = pyuv.Loop.default_loop()
    s = Server(settings.GAFFER_SERVER, loop=loop)
    return s


def get_process_or_404(proc_name, server=None):
    s = server
    if not s:
        s = get_gaffer_server()
    try:
        process = s.get_process(proc_name)
        return process
    except GafferNotFound:
        raise Http404


def get_process_list():
    s = get_gaffer_server()
    return s.processes()


def get_pid_or_404(pid, proc_name):
    s = get_gaffer_server()
    process = get_process_or_404(proc_name, s)
    pid_object = ProcessId(s, pid, process)
    return pid_object
