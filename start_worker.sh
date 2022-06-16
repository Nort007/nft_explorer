#!/bin/bash
python3 -m celery -A api.celery_worker worker -l debug -Q main_queue -c 1