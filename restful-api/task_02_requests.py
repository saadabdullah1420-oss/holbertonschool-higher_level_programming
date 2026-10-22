#!/usr/bin/python3
"""Fetch posts from an API and print or save them."""

import csv

import requests


def fetch_and_print_posts():
    """Fetch posts and print the response status and post titles."""
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    )
    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Fetch posts and save their IDs, titles, and bodies to CSV."""
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    )

    if response.status_code == 200:
        posts = response.json()
        data = [
            {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            for post in posts
        ]

        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file, fieldnames=["id", "title", "body"]
            )
            writer.writeheader()
            writer.writerows(data)
