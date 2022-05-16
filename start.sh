#!/bin/bash

echo Starting App
exec gunicorn --reload src.app:app \--bind 0.0.0.0:4100