#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app import create_app

app = create_app("development")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081,ssl_context=('localhost+2.pem', 'localhost+2-key.pem'))