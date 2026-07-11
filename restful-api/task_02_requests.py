#!/usr/bin/python3
"""
Module task_02_requests

Fetches posts from the JSONPlaceholder API and either prints their
titles or saves the data to a CSV file.
"""
import csv
import requests


def fetch_and_print_posts():
    """
    Fetch all posts from JSONPlaceholder, print the status code,
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    """
    Fetch all posts from JSONPlaceholder and, if successful, save.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        posts = response.json()

        data = [
            {
                'id': post.get('id'),
                'title': post.get('title'),
                'body': post.get('body')
            }
            for post in posts
        ]

        with open('posts.csv', mode='w', newline='', encoding='utf-8') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
