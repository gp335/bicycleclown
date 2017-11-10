import os

# Load some secrets
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# ---------------------------------------------
# ref: https://github.com/slackapi/python-slackclient
#

from slackclient import SlackClient

slack_token = os.environ["SLACK_API_TOKEN"]
sc = SlackClient(slack_token)

sc.api_call(
  "chat.postMessage",
  channel="#python",
  text="Hello from Python! :tada:",
  thread_ts="1476746830.000003"
)