from addsimple.adding import add
import requests
from apitest.api import focus


def test_add():
    given_value=1
    expected=2
    assert add(given_value)==expected

def test_add2():
    given_value=-1
    expected=0
    assert add(given_value)==expected


def test_focus():
 full_name={ "full_name": "Idris Shabanli", id:	int,"created_at":"($date-time)","updated_at": "($date-time)"}
 request = requests.post("http://35.225.243.133/bloggers/", full_name)
 assert request.status_code == 201

def test_focus1():
  full_name = {"full_name": "abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd "}
  request = requests.post("http://35.225.243.133/bloggers/", full_name)
  assert request.status_code == 400

def test_focus2():
    full_name = {"full_name": ""}
    request = requests.post("http://35.225.243.133/bloggers/", full_name)
    assert request.status_code == 400

def test_focus3():
    full_name = {"id": 1223}
    request = requests.post("http://35.225.243.133/bloggers/", full_name)
    assert request.status_code == 400


