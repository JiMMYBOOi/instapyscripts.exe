import random
from instapy import InstaPy
from instapy import smart_run

insta_username = ''
insta_password = ''

session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False,
                  disable_image_load=True,
                  multi_logs=True)

with smart_run(session):
    session.set_simulation(enabled=True)
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=7500,
                                    max_following=5000,
                                    min_followers=300,
                                    min_following=100,
                                    min_posts=0)

    session.set_skip_users(skip_private=False,
                           skip_no_profile_pic=True,
                           skip_business=False)

    session.set_quota_supervisor(enabled=True, sleep_after=["follows","server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=False,
                                peak_follows_hourly=48,
                                  peak_server_calls_hourly=25)


    session.follow_user_following([''], amount=10, randomize=True, sleep_delay=600)
