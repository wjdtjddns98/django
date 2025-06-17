from django.http import HttpResponse
from django.shortcuts import render

def show_feed(request):
    return HttpResponse("show feed")

def one_feeds(request, feed_id, feed_content):
    return HttpResponse(f"Feed ID: {feed_id}, Content: {feed_content}")

def all_feeds(request):
    return HttpResponse("All feeds")
