#!/bin/bash

# Tor 실행
service tor start

# 크롤링 스크립트 실행
python main.py
