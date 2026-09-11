import asyncio
import httpx


BASE_URL = "https://jsonplaceholder.typicode.com"


async def get_post(post_id: int):

    async with httpx.AsyncClient() as client:

        response = await client.get(
            f"{BASE_URL}/posts/{post_id}"
        )

        response.raise_for_status()

        return response.json()


async def get_user(user_id: int):

    async with httpx.AsyncClient() as client:

        response = await client.get(
            f"{BASE_URL}/users/{user_id}"
        )

        response.raise_for_status()

        return response.json()


async def get_comments(post_id: int):

    async with httpx.AsyncClient() as client:

        response = await client.get(
            f"{BASE_URL}/posts/{post_id}/comments"
        )

        response.raise_for_status()

        return response.json()
async def sequential_requests():

    user = await get_user(1)

    post = await get_post(1)

    comments = await get_comments(1)

    return {
        "user": user,
        "post": post,
        "comments": comments
    }

async def concurrent_requests():

    user_task = get_user(1)

    post_task = get_post(1)

    comments_task = get_comments(1)

    user, post, comments = await asyncio.gather(
        user_task,
        post_task,
        comments_task
    )

    return {
        "user": user,
        "post": post,
        "comments": comments
    }