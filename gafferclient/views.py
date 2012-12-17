from django.shortcuts import render, redirect
from .helpers import get_gaffer_server, get_process_or_404, get_pid_or_404


def process_list(request):
    s = get_gaffer_server()
    return render(
        request,
        'process_list.html',
        {'server': s, },
    )


def process_detail(request, proc_name):
    process = get_process_or_404(proc_name)
    return render(
        request,
        'process_detail.html',
        {"process": process},
    )


def process_set(request, proc_name, action='add'):
    process = get_process_or_404(proc_name)
    getattr(process, action)()
    return redirect("process_detail", proc_name)


def pid_list(request):
    s = get_gaffer_server()
    object_list = [s.get_process(pid) for pid in s.running()]
    return render(
        request,
        'pid_list.html',
        {"object_list": object_list},
    )


def pid_detail(request, proc_name, pid):
    pid_object = get_pid_or_404(pid, proc_name)
    return render(
        request,
        'pid_detail.html',
        {"pid": pid_object},
    )


def pid_stop(request, proc_name, pid):
    pid_object = get_pid_or_404(pid, proc_name)
    pid_object.stop()
    next = request.GET.get('next')
    if next:
        next = redirect(next)
    else:
        next = redirect("process_detail", proc_name)
    return next
