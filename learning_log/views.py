# Views for Learning Log application
# 学习日志应用的视图函数

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.http import Http404


def index(request):
    """
    The home page for Learning Log.
    学习日志的主页。
    """
    return render(request, 'learning_log/index.html')

@login_required
def topics(request):
    """
    Show all topics owned by the current user.
    显示当前用户拥有的所有主题。
    """
    # Get all topics for current user, ordered by creation date
    # 获取当前用户的所有主题，按创建日期排序
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_log/topics.html', context)

@login_required
def topic(request, topic_id):
    """
    Show a single topic and all its entries.
    显示单个主题及其所有条目。
    
    Args:
        request: HTTP request object / HTTP请求对象
        topic_id: ID of the topic to display / 要显示的主题ID
    """
    # Get the topic / 获取主题
    topic = Topic.objects.get(id=topic_id)
    
    # Verify the topic belongs to the current user / 验证主题属于当前用户
    if topic.owner != request.user:
        raise Http404

    # Get all entries for this topic, newest first / 获取此主题的所有条目，最新的在前
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_log/topic.html', context)

@login_required
def new_topic(request):
    """
    Add a new topic for the current user.
    为当前用户添加新主题。
    """
    if request.method != 'POST':
        # No data submitted; create a blank form / 未提交数据；创建空表单
        form = TopicForm()
    else:
        # POST data submitted; process data / 提交了POST数据；处理数据
        form = TopicForm(data=request.POST)
        if form.is_valid():
            # Create topic but don't save to database yet / 创建主题但先不保存到数据库
            new_topic = form.save(commit=False)
            # Set the owner to current user / 将所有者设置为当前用户
            new_topic.owner = request.user
            # Now save to database / 现在保存到数据库
            new_topic.save()
            # Redirect to the new topic page / 重定向到新主题页面
            return redirect('learning_log:topic', topic_id=new_topic.id)

    # Display a blank or invalid form / 显示空白或无效的表单
    context = {'form': form}
    return render(request, 'learning_log/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """
    Add a new entry for a particular topic.
    为特定主题添加新条目。
    
    Args:
        request: HTTP request object / HTTP请求对象
        topic_id: ID of the topic to add entry to / 要添加条目的主题ID
    """
    # Get the topic / 获取主题
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data submitted; create a blank form / 未提交数据；创建空表单
        form = EntryForm()
    else:
        # POST data submitted; process data / 提交了POST数据；处理数据
        form = EntryForm(data=request.POST)
        if form.is_valid():
            # Create entry but don't save yet / 创建条目但先不保存
            new_entry = form.save(commit=False)
            # Associate entry with topic / 将条目与主题关联
            new_entry.topic = topic
            # Save to database / 保存到数据库
            new_entry.save()
            # Redirect back to topic page / 重定向回主题页面
            return redirect('learning_log:topic', topic_id=topic_id)

    # Display a blank or invalid form / 显示空白或无效的表单
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_log/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """
    Edit an existing entry.
    编辑现有条目。
    
    Args:
        request: HTTP request object / HTTP请求对象
        entry_id: ID of the entry to edit / 要编辑的条目ID
    """
    # Get the entry and its topic / 获取条目及其主题
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    
    # Verify the topic belongs to the current user / 验证主题属于当前用户
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with current entry / 初始请求；用当前条目预填表单
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data / 提交了POST数据；处理数据
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            # Save the updated entry / 保存更新后的条目
            form.save()
            # Redirect back to topic page / 重定向回主题页面
            return redirect('learning_log:topic', topic_id=topic.id)

    # Display form with current or invalid data / 显示当前或无效数据的表单
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_log/edit_entry.html', context)